import pytest

# testcase code must be written inside method
# method name must start with test_
a = 103


# pytest.mark.skipif (a>100, reason="skipping as this functionality is not accepting, developer will fix it in the next build")
@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_001_login_logout_testing():
    print("this is third smoke as well as regression testcase code")


@pytest.mark.Sanity
@pytest.mark.Regression
def test_TC_003_login_logout_invalid_credentials():
    print("this is my third sanity as well as regression testcase")
    print("this is end of testcase")
