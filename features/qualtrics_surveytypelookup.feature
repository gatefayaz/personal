Feature: Validate SurveyTypeLookup Table

    Scenario: Test(surveytype) to validate the table structure of external tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate table structure of external tables for surveytype

    Scenario: Test(surveytype) to validate the table structure of staging tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate table structure of staging tables for surveytype

    Scenario: Test(surveytype) to validate the table structure of UCDM tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate table structure of UCDM tables for surveytype

    Scenario: Test(surveytype) to validate count of records between External and staging table are matching
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate count of records and data are matching between External and staging table for surveytype
    
    Scenario: Test(surveytype) to validate count of records between staging table and UCDM table are matching
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate count of records are matching between staging table and UCDM table for surveytype

    Scenario: Test(surveytype) to validate the data between External and staging table are matching
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between External and staging table for surveytype

    Scenario: Test(surveytype) to check for duplicate records in UCDM table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate duplicate records in UCDM table for surveytype

    Scenario: Test(surveytype) to validate the data in Staging and UCDM tables are as per transformation logic
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate the primary key in Ucdm table for surveytype for surveytype
    
    Scenario: Test(surveytype) to validate the date fields in the UCDM tables for date format and correctness
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate surveyQuestions fields in the UCDM tables for date format and correctness for surveytype

    Scenario: Test(Incremental) to validate SurveyQuestions table incremental load for qualtrics
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate SurveyQuestions table incremental load for qualtrics
    
   