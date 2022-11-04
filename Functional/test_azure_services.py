import pytest
from python_settings import settings
from pytest_bdd import given, when, then, scenario, parsers

@pytest.fixture(scope="session")
def available_azure_resources(resources):
    return resources.get_resources()

@pytest.mark.integration
@pytest.mark.infrastructure
@pytest.mark.parametrize(
    "azure_resource",
    [
        settings.ADF_SERVICE.name,
        settings.KV_SERVICE.name,
        settings.ADLS_SERVICE.name,
    ],
)
@scenario(
    "../../features/infrastructure.feature",
    "Test if expected resources are provisioned in the Subscription",
)
def test_if_expected_resources_are_provisioned(azure_resource):
    pass

@given('I have access to Azure')
def have_access_to_azure(resources):
    pass

@when('I list available resources')
def list_available_resources(available_azure_resources):
    pass

@then('I can find expected resources')
def expected_pipeline_exist(available_azure_resources, azure_resource):
    resources = [resource.name for resource in available_azure_resources]
    assert (
        azure_resource in resources
    ), f"Resource: {azure_resource} not found. \
        Available resources: {resources}"
