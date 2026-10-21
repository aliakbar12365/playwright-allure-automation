from pathlib import Path

import allure
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    # Attach the completed video file after fixture teardown.
    if report.when == "teardown":
        output_dir = Path("test-results")

        if output_dir.exists():
            video_files = list(output_dir.rglob("*.webm"))

            if video_files:
                video_path = max(
                    video_files,
                    key=lambda path: path.stat().st_mtime,
                )

                try:
                    allure.attach.file(
                        str(video_path),
                        name="Test Execution Video",
                        attachment_type=allure.attachment_type.WEBM,
                    )
                    print(f"\nVideo attached to Allure: {video_path}")

                except Exception as error:
                    print(f"\nVideo attachment failed: {error}")
            else:
                print("\nNo .webm video found in test-results.")
