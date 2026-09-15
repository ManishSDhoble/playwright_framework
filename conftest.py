recordings_by_test = {}


from html import escape
from pathlib import Path
import re
import shutil

import pytest
from playwright.sync_api import sync_playwright

try:
    import pytest_html
except ImportError:
    pytest_html = None

from config import BASE_URL


@pytest.fixture
def page(request):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    recordings_dir = Path("recordings")
    recordings_dir.mkdir(exist_ok=True)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(recordings_dir),
    )
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")
    yield page
    video = page.video
    context.close()

    if video:
        safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", request.node.nodeid)
        recording_path = recordings_dir / f"{safe_name}.webm"
        shutil.move(video.path(), recording_path)
        recordings_by_test[request.node.nodeid] = recording_path

    browser.close()
    playwright.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", getattr(report, "extra", []))

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            file_name = screenshots_dir / f"{item.name}.png"
            page.screenshot(path=str(file_name))
            if pytest_html is not None:
                extras.append(pytest_html.extras.image(str(file_name)))
            report.extras = extras


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.append("<th>Recording</th>")


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    recording_path = recordings_by_test.get(report.nodeid)
    if not recording_path or not recording_path.exists():
        cells.append("<td>No recording</td>")
        return

    report_path = escape(recording_path.as_posix())
    cells.append(
        "<td>"
        "<video controls width='640' style='max-width: 100%;'>"
        f"<source src='{report_path}' type='video/webm'>"
        "Your browser does not support video playback."
        "</video>"
        "</td>"
    )
