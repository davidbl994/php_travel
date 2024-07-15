# Verify the visual appearance of the login page on different screen sizes and resolutions.
import os
import pytest
from pages.login_page import logger

# Test for visual appearance
@pytest.mark.xfail
def test_login_page_appearance(driver, login_page):

    # List of screen sizes to test (width, height)
    screen_sizes = [
        (1920, 1080),  # Desktop Full HD
        (1366, 768),  # Laptop
        (768, 1024),  # Tablet portrait
        (1024, 768),  # Tablet landscape
        (375, 812),  # Mobile portrait
        (812, 375)  # Mobile landscape
    ]

    for size in screen_sizes:
        driver.set_window_size(size[0], size[1])
        screenshot_path = f"{login_page.baseline_dir}login_page_{size[0]}x{size[1]}.png"
        current_screenshot_path = f"{login_page.diff_dir}current_login_page_{size[0]}x{size[1]}.png"
        diff_path = f"{login_page.diff_dir}diff_{size[0]}x{size[1]}.png"

        login_page.take_screenshot(current_screenshot_path)

        if os.path.exists(screenshot_path):
            is_equal = login_page.compare_images(screenshot_path, current_screenshot_path, diff_path)
            assert is_equal, f"Visual regression detected for size {size[0]}x{size[1]}. Check {diff_path} for differences."
        else:
            os.rename(current_screenshot_path, screenshot_path)
            logger.info(f"Baseline screenshot saved for size {size}: {screenshot_path}")

