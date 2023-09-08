import pytest

# testcase code must be written inside method
# method name must start with test_
actual_result = 'Testing'


# pytest.mark.skipif (a>100, reason="skipping as this functionality is not accepting, developer will fix it in the next build")
@pytest.mark.toppriority
def test_tc_001_login_logout_testing():
    print("this is our top priority testcase code")
    assert actual_result == "Testing", "these two values must not be same"


@pytest.mark.Sanity
def test_TC_003_login_logout_invalid_credentials():
    print("this is my sanity testcase code")
    print("this is end of testcase")
