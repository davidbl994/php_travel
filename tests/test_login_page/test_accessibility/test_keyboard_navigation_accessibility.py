from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from axe_selenium_python import Axe

def test_keyboard_navigation_accessibility(driver, login_page):
    # Initialize Axe for accessibility testing
    axe = Axe(driver)
    axe.inject()

    # Verify keyboard navigation
    action = ActionChains(driver)
    body = driver.find_element(By.TAG_NAME, "body")

    # Focus on the body and start tabbing through elements
    body.send_keys(Keys.TAB)
    for _ in range(10):  # Adjust the range as needed to cover all interactive elements
        action.send_keys(Keys.TAB).perform()

    # Optionally, add specific checks for interactive elements
    # e.g., assert driver.switch_to.active_element == login_page.get_username_input()

    # Run Axe accessibility checks
    results = axe.run()

    # Save results to a file (optional)
    axe.write_results(results, 'axe-results-keyboard-navigation.json')

    # Check for keyboard accessibility related violations
    keyboard_violations = []
    for violation in results['violations']:
        for node in violation['nodes']:
            if 'keyboard' in violation['id']:
                keyboard_violations.append(violation)
                break

    # Print keyboard accessibility violations
    if keyboard_violations:
        print("Keyboard navigation accessibility violations found:")
        for violation in keyboard_violations:
            print(f"\n{violation['id']}: {violation['description']}")
            for node in violation['nodes']:
                print(f"  Target: {node['target']}")
                print(f"  Failure Summary: {node['failureSummary']}")
    else:
        print("No keyboard navigation accessibility violations found.")

    # Assert no keyboard navigation related violations were found
    assert len(keyboard_violations) == 0, "Keyboard navigation accessibility violations found on the login page."