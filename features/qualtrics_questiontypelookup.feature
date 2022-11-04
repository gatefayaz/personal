Feature: Validate QuestionTypeLookup Table

    Scenario: Test(questiontype) to validate the table structure of external tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can able to access external table

    Scenario: Test(questiontype) to validate the table structure of staging tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can able to access staging  table

    Scenario: Test(questiontype) to validate the table structure of UCDM tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can able to access ucdm table

    Scenario: Test(questiontype) to validate count of records between External and staging table are matching
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate count of records and data are matching between External and staging table
    
    Scenario: Test(questiontype) to validate count of records between staging table and UCDM table are matching
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate count of records are matching between staging table and UCDM table

    Scenario: Test(questiontype) to validate the data between External and staging table are matching
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between External and staging table

    Scenario: Test(questiontype) to check duplicate records in ucdm table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate duplicate records in UCDM table

    Scenario: Test(questiontype) to validate the data in Staging and UCDM tables are as per transformation logic
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate the primary key in Ucdm table for questiontype
    
    Scenario: Test(questiontype) to validate the date fields in the UCDM tables for date format and correctness 
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate question type  in the UCDM tables for date format and correctness

    Scenario: Test(Incremental) to validate responses table incremental load for qualtrics
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate responses table incremental load for qualtrics
