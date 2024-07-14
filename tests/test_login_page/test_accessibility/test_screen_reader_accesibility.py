import pytest

@pytest.mark.xfail
def test_login_page_screen_reader_friendly(login_page):
    results = login_page.run_axe_accessibility_checks()

    # Check for screen reader related violations
    screen_reader_violations = []
    for violation in results['violations']:
        for node in violation['nodes']:
            if 'aria-' in violation['id'] or 'label' in violation['id']:
                screen_reader_violations.append(violation)
                break

    # Print screen reader violations
    if screen_reader_violations:
        print("Screen reader accessibility violations found:")
        for violation in screen_reader_violations:
            print(f"\n{violation['id']}: {violation['description']}")
            for node in violation['nodes']:
                print(f"  Target: {node['target']}")
                print(f"  Failure Summary: {node['failureSummary']}")
    else:
        print("No screen reader accessibility violations found.")

    # Assert no screen reader related violations were found
    assert len(screen_reader_violations) == 0, "Screen reader accessibility violations found on the login page."