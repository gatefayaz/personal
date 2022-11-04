import pytest
from datetime import timedelta, datetime
from python_settings import settings
from pytest_bdd import given, when, then, scenario, parsers

@pytest.fixture(scope="session")
def available_pipelines(adf):
    return list(adf.list_pipelines())

@pytest.fixture(scope="session")
def available_linked_services(adf):
    return list(adf.get_linked_services())

@pytest.mark.integration
@pytest.mark.infrastructure
@scenario(
    "../../features/account_information_part2.feature",
    "Test if each table has corresponding pipeline",
)
def test_if_each_table_has_pipeline():
    pass

@given('I have DataFactory provisioned')
def datafactory_is_provisioned(adf):
    pass

@when('I list available pipelines')
def list_available_pipelines(available_pipelines):
    pass

@then(parsers.parse('I can find expected pipeline {expected_pipeline_name}'))
def expected_pipeline_exist(available_pipelines, expected_pipeline_name):
    pipelines = [pipeline.name for pipeline in available_pipelines]
    assert (
        expected_pipeline_name in pipelines
    ), f"Expected pipeline: {expected_pipeline_name}, \
         but available are: {pipelines}"

@pytest.mark.integration
@pytest.mark.infrastructure
@pytest.mark.parametrize(
    "linked_service",
    []
)
@scenario(
    "../../features/infrastructure.feature",
    "Test if DataFactory has right linked services",
)
def test_available_linked_services(linked_service):
    pass

@given('I have DataFactory provisioned')
def datafactory_is_provisioned(adf):
    pass

@when('I list available linked services')
def list_available_linked_services(available_pipelines):
    pass

@then('I can find expected linked services')
def expected_linked_service_exist(available_linked_services, linked_service):
    services = [service.name for service in available_linked_services]
    assert (
        linked_service in services
    ), f"Expected linked services: {linked_service}, \
         but available are: {services}"

@pytest.mark.smoke
@scenario(
    "../../features/smoke_tests.feature",
    "Test if each pipeline work successfully",
)
def test_if_pipeline_finishes_successfully():
    pass

@given('I have DataFactory provisioned')
def datafactory_is_provisioned(adf):
    pass

@given(parsers.parse('Pipeline {expected_pipeline_name} exists'))
def expect_pipeline_exists(available_pipelines, expected_pipeline_name):
    pipelines = [pipeline.name.lower() for pipeline in available_pipelines]
    assert (
        expected_pipeline_name.lower() in pipelines
    ), f"Expected pipeline: {expected_pipeline_name}, \
         but available are: {pipelines}"

@when(parsers.parse('I trigger pipeline {expected_pipeline_name}'), target_fixture="pipeline_result")
def trigger_test_pipeline(expected_pipeline_name, adf):
    currentDt = datetime.now()
    timeFmt = '%Y-%m-%d %H:%M:%S'
    pipeline_parameters = {
        'startDt': (currentDt + timedelta(minutes=-1)).strftime(timeFmt),
        'endDt': (currentDt + timedelta(minutes=1)).strftime(timeFmt)
    }
    return adf.run_pipeline_and_wait_for_status(pipeline_name = expected_pipeline_name, parameters = pipeline_parameters)

@then('It finishes with status succeeded')
def pipeline_status_succeeded(pipeline_result):
    assert (pipeline_result.status == 'Succeeded')