# Verify the visual appearance of the login page on different screen sizes and resolutions.
import os
import pytest

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

        # Take a screenshot of the current state
        login_page.take_screenshot(current_screenshot_path)

        # Compare with the baseline image
        if os.path.exists(screenshot_path):
            is_equal = login_page.compare_images(screenshot_path, current_screenshot_path, diff_path)
            assert is_equal, f"Visual regression detected for size {size[0]}x{size[1]}. Check {diff_path} for differences."
        else:
            # Save the current screenshot as the baseline if it doesn't exist
            os.rename(current_screenshot_path, screenshot_path)
            print(f"Baseline screenshot saved for size {size}: {screenshot_path}")

