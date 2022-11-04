Feature: Smoke_Tests

    Examples:
    | pipeline                      |
    | DB_DataValidator_CI_ACCT      |
    | DB_DataValidator_CI_ACCT_APAY |
    | DB_DataValidator_CI_ACCT_PER  |

    Scenario: Test if each pipeline work successfully
        Given I have DataFactory provisioned
        And Pipeline <pipeline> exists
        When I trigger pipeline <pipeline>
        Then It finishes with status succeeded
