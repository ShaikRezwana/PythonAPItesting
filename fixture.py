import pytest


# we have to define a function to use fixture
@pytest.fixture(scope="module")
def fixture_code():
    print("This is a fixture code will execute before testcase")
    print("-----------------------------------------------------")
    yield
    print("close db connection executing testcase")
    print("------------------------------------------------------")

@pytest.mark.smoke
@pytest.mark.regression
def test_tc_001_login_logout_testing(fixture_code):
    print("this is third smoke as well as regression testcase code")


@pytest.mark.sanity
@pytest.mark.regression
def test_TC_003_login_logout_invalid_credentials(fixture_code):
    print("this is my third sanity as well as regression testcase")
    print("this is end of testcase")
