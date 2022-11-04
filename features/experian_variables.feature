Feature: Validate Mosaic Experian leanlist variables

    Scenario: Test(Mosaic) to validate data between external and staging table are matching for TypeLookUp table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between external and staging table for TypeLookUp table

    Scenario: Test(Mosaic) to validate data between staging and UCDM table are matching for TypeLookUp table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between staging and UCDM table for TypeLookUp table

    Scenario: Test(Mosaic) to validate data between external and staging table are matching for GroupLookUp table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between external and staging table for GroupLookUp table

    Scenario: Test(Mosaic) to validate data between staging and UCDM table are matching for GroupLookUp table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between staging and UCDM table for GroupLookUp table

    Scenario: Test(Mosaic) to validate data between external and staging table are matching for Mosaic table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between external and staging table for Mosaic table

    Scenario: Test(Mosaic) to validate data between staging and UCDM table are matching for Mosaic table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data are matching between staging and UCDM table for Mosaic table
    
    Scenario: Test(Mosaic) to validate primary key is not null in Mosaic table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate primary key is not null in Mosaic table
    
    Scenario: Test(Mosaic) to validate primary key is not null in GroupLookUp table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate primary key is not null in GroupLookUp table

    Scenario: Test(Mosaic) to validate primary key is not null in TypeLookUp table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate primary key is not null in TypeLookUp table

