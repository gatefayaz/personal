Feature: Validate brandfire activity details 

    Scenario: Test(brandfire_activity) to validate the table structure of external tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can able to access external table for brandfire activity

    Scenario: Test(brandfire_activity) to validate the table structure of staging tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can able to access staging table for brandfire activity

    Scenario: Test(brandfire_activity) to validate the table structure of target tables
        Given I have Database connection details
        When I was able to connect to database
        Then I can able to access target table for brandfire activity

    Scenario: Test(brandfire_activity) to validate count of records between External and staging table are matching
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate count of records and data are matching between External and staging table for brandfire activity
    
    Scenario: Test(brandfire_activity) to validate count of records between staging table and target table are matching
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between staging table and target table for brandfire activity

    Scenario: Test(brandfire_activity) to check duplicate records in target table
        Given I have Database connection details 
        When I was able to connect to database 
        Then I can validate duplicate records in rewards_energia_res table for brandfire activity

    Scenario: Test(brandfire_activity) to validate the data in external and staging tables are as per transformation logic 
        Given I have Database connection details 
        When I was able to connect to database 
        Then I can validate the data between external and staging tables for brandfire activity

    Scenario: Test(brandfire_activity) to validate the data in staging and target tables are as per transformation logic 
        Given I have Database connection details 
        When I was able to connect to database 
        Then I can validate the data between staging and target tables for brandfire activity