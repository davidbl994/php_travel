import pytest

@pytest.mark.xfail
def test_login_page_accessibility(login_page):
    results = login_page.run_axe_accessibility_checks()

    violations = results['violations']
    if violations:
        print('Accessibility violations found')
        for violation in violations:
            print(f"\n{violation['id']}: {violation['description']}")
            for node in violation['nodes']:
                print(f" Target: {node['target']}")
                print(f" Failure Summary: {node['failureSummary']}")
    else:
        print("No accessibility violations found.")

    assert len(violations) == 0, "Accessibility violations found on the login page"