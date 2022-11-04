Feature: Validate Adobe Campaign leanlist variables

    Scenario: Test(adobe) to validate the table structure of CampaignTracking table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate the table structure of CampaignTracking table

    Scenario: Test(adobe) to validate the DeliveryDescription column is not null in CampaignTracking table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate the DeliveryDescription column is not null in CampaignTracking table
    
    Scenario: Test(adobe) to validate primary key is not null in CampaignTracking table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate primary key is not null in CampaignTracking table

    Scenario: Test(adobe) to validate AccountID is not null in CampaignTracking table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate AccountID is not null in CampaignTracking table

    Scenario: Test(adobe) to check for duplicate records in CampaignTracking table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate for duplicate records in CampaignTracking table

    Scenario: Test(adobe) to validate the data between External and UCDM table are matching for CampaignTracking
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between External and UCDM table for CampaignTracking

    Scenario: Test(adobe) to validate the data between External and UCDM table are matching for CampaignDelivery
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between External and UCDM table for CampaignDelivery

    Scenario: Test(adobe) to validate primary key is not null in CampaignDelivery table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate primary key is not null in CampaignDelivery table

    Scenario: Test(adobe) to validate the table structure of CampaignDelivery table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate the table structure of CampaignDelivery table

    Scenario: Test(adobe) to check for duplicate records in CampaignDelivery table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate for duplicate records in CampaignDelivery table

    Scenario: Test(adobe) to validate the data between External and UCDM table are matching for CampaignMeta
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between External and UCDM table for CampaignMeta

    Scenario: Test(adobe) to validate the table structure of CampaignMeta table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate the table structure of CampaignMeta table

    Scenario: Test(adobe) to validate the primary key is not null in CampaignMeta table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate primary key is not null in CampaignMeta table

    Scenario: Test(adobe) to check for duplicate records in CampaignMeta table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate for duplicate records in CampaignMeta table

    Scenario: Test(adobe) to validate the data between External and UCDM table are matching for CampaignSummary
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between External and UCDM table for CampaignSummary

    Scenario: Test(adobe) to check for duplicate records in CampaignSummary table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate for duplicate records in CampaignSummary table