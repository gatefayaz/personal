Feature: Validate cc&b leanlist variables

    Scenario: Test if ContactClass column has null values in Customer_Contacts table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate ContactClass column has null values in Customer_Contacts table

    Scenario: Test if ContactClassCode column has null values in Customer_Contacts table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate ContactClassCode column has null values in Customer_Contacts table

    Scenario: Test if AccountID column values has ED_ as prefix in Customer_Contacts table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate AccountID column values has ED_ as prefix in Customer_Contacts table

    Scenario: Test to validate data between staging and ucdm for ContactClassCode in Customer_Contacts table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data between staging and ucdm for ContactClassCode in Customer_Contacts table
    
    Scenario: Test to validate data between staging and ucdm for contactmethod in Customer_Contacts table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data between staging and ucdm for contactmethod in Customer_Contacts table

    Scenario: Test to validate data between staging and ucdm for ContactClass in Customer_Contacts table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data between staging and ucdm for ContactClass in Customer_Contacts table

    Scenario: Test to validate data between staging and ucdm for accountid in Customer_Contacts table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data between staging and ucdm for accountid in Customer_Contacts table

    Scenario: Test to validate account table incremental
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate account table incremental

    Scenario: Test to validate serviceagreement table incremental
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate serviceagreement table incremental

    Scenario: Test to validate person table incremental
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate person table incremental

    Scenario: Test to validate bill table incremental
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate bill table incremental

    Scenario: Test to validate bill segment table incremental
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate bill segment table incremental

    Scenario: Test to validate SAStatusDesc column in serviceagreement table incremental
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate SAStatusDesc column in serviceagreement table incremental

    Scenario: Test to validate SA_TYPE column in serviceagreement table incremental
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate SA_TYPE column in serviceagreement table incremental