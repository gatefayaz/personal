Feature: Validate Qualtrics ResponseMetaData Table

    Scenario: Test to validate the SurveyID column is not null in ucdm table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate SurveyId column is not null in ucdm table

    Scenario: Test to validate the SurveyName column is not null in ucdm table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate SurveyName column is not null in ucdm table

    Scenario: Test to check duplicates for ResponseID
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate if there were any duplicates for ResponseID

    Scenario: Test to validate qualtrics relationship response metadata
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics relationship response metadata

    Scenario: Test to validate qualtrics pcw response metadata
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics pcw response metadata

    Scenario: Test to validate qualtrics onesurvey response metadata
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics onesurvey response metadata

    Scenario: Test to validate qualtrics complaints response metadata
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics complaints response metadata

    Scenario: Test to validate qualtrics registrations response metadata
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics registrations response metadata

    Scenario: Test to validate Missing Responses
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate Missing Responses

    Scenario: Test to validate qualtrics complaints between External and Staging tables 
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics complaints between External and Staging tables

    Scenario: Test to validate qualtrics onesurvey between External and Staging tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics onesurvey between External and Staging tables

    Scenario: Test to validate qualtrics pcw between External and Staging tables 
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics pcw between External and Staging tables

    Scenario: Test to validate qualtrics registrations between External and Staging tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics registrations between External and Staging tables

    Scenario: Test to validate qualtrics relationship between External and Staging tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate qualtrics relationship between External and Staging tables
    
    Scenario: Test(Incremental) to validate ResponseMetaData table incremental load for qualtrics
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate ResponseMetaData table incremental load for qualtrics

