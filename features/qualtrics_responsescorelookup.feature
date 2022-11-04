Feature: Validate ResponseScoreLookup Table

    Scenario: Test(ResponseScoreLookup) to validate the table structure of UCDM ResponseScoreLookup table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate UCDM ResponseScoreLookup table

    Scenario: Test(ResponseScoreLookup) to validate the primary key is not null in UCDM table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate primary key is not null in UCDM table

    Scenario: Test(ResponseScoreLookup) to check duplicate responseid
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate duplicate responseid in UCDM table

    Scenario: Test(ResponseScoreLookup) to validate the CreatedDate column is not null in ucdm table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate CreatedDate column is not null in ucdm table

    Scenario: Test(ResponseScoreLookup) to validate the responses between the Responses table and ResponseScoreLookup table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate the responses between the Responses table and ResponseScoreLookup table

    Scenario: Test(ResponseScoreLookup) to validate the recordId column is not null in staging qualtrics registrations table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate recordId column is not null in staging qualtrics registrations table

    Scenario: Test(ResponseScoreLookup) to validate the recordId column is not null in staging qualtrics pcw table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate recordId column is not null in staging qualtrics pcw table

    Scenario: Test(ResponseScoreLookup) to validate the recordId column is not null in staging qualtrics complaints table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate recordId column is not null in staging qualtrics complaints table

    Scenario: Test(ResponseScoreLookup) to validate the table structure of UCDM Responses table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate UCDM Responses table

    Scenario: Test(ResponseScoreLookup) to validate the unique SurveyName count in UCDM table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate unique SurveyName count in UCDM table

    Scenario: Test(Incremental) to validate ResponseScoreLookup table incremental load for qualtrics
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate ResponseScoreLookup table incremental load for qualtrics
