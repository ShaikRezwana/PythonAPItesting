import pytest

# testcase code must be written inside method
# name must start with test_
a = 103


# pytest.mark.skip (a>100, reason="skipping as this functionality is not accepting,
# developer will fix it in the next build")

@pytest.mark.smoke
def test_tc_001_login_logout_testing():
    print("this is fourth smoke testcase code")


@pytest.mark.sanity
def test_tc_003_login_logout_invalid_credentials():
    print("this is fourth sanity testcase 3")
    print("this is end of testcase")
