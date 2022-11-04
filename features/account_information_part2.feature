Feature: Surface_CC&B_Account_Information_270_view_Part2

    Examples:
    | source_table |
    | CI_ACCT      |
    | CI_ACCT_APAY |
    | CI_ACCT_PER  |

    Scenario: Test if each table has corresponding pipeline
        Given I have DataFactory provisioned
        When I list available pipelines
        Then I can find expected pipeline DB_DataValidator_<source_table>
