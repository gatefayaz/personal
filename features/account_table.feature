Feature : validate account table data

    Scenario: To Enter into the Synapse External tables 
        Given User login into database write the query to retrieve the data of external tables
        When I Will execute the query 
        Then I will get the data retrieved of external table

    Scenario: To Enter into the Synapse External tables of ext_ci_acct
        Given A valid connection to the ext_ci_acct is established, and table information retrieved from source
        When I will write query to get details on ext_ci_acct table
        Then Check if data exists in ext_ci_acct table
        

    Scenario: To Enter into the Synapse Staging tables of stg.ci_acct
        Given A valid connection to the stg.ci_acct is established, and table information retrieved from source
        When I will write query to get details on stg.ci_acct table
        Then check if data exists in stg.ci_acct 

    Scenario: To Enter into the Synapse Data warehouse
        Given A valid connection to the data warehouse is established and table information retrieved from UCDM.account
        When I will write query to get details on data warehouse 
        Then I will validate number of rows from data warehouse with UCDM.account
        

    Scenario: Check number of records inserted or updated in the Synapse Data Warehouse
        Given User establishes a successful connection with Data Warehouse
        When user executes the query with start date and end date 
        Then user validate the rows in Data Warehouse from that specified dates

        
    Scenario: Check Null values inserted or updated in the Synapse Data Warehouse for AccountID
        Given User establishes a successful connection with Data Warehouse
        When user executes the query to retrieve all account ID 
        Then user validate the AccountID column has any null values
        
    Scenario: Check Null values inserted or updated in the Synapse Data Warehouse for PersonID
        Given User establishes a successful connection with Data Warehouse
        When user executes the query to retrieve all Person ID 
        Then user validate the PersonID column has any null values
        
    Scenario: Check Null value for start Date in External table
        Given User establishes a successful connection with External table
        When user executes the query to retrieve all records 
        Then user validate the EXT.CI_ACCT_APAY column has any null values
        
    Scenario: Check Null value for start Date in staging table
        Given User establishes a successful connection with staging table
        When user executes the query to retrieve all records 
        Then user validate the STG.CI_ACCT_APAY column has any null values
        
    Scenario: Check accepted values for Payment type in UCDM Account table
        Given User establishes a successful connection with UCDM account table
        When user executes the query to retrieve all records 
        Then user validate the Payment type column has any one of these values Fixed,Variable,Other values
        
    Scenario: Check accepted values for AutopayStartDate in UCDM Account table
        Given User establishes a successful connection with UCDM account table
        When user executes the query to retrieve all records 
        Then user validate the AutopayStartDate type column has valid date values

    Scenario: Check accepted values for FirstBillDate in UCDM Account table
        Given User establishes a successful connection with UCDM account table
        When user executes the query to retrieve all records 
        Then user validate the FirstBillDate type column has valid date values
        
    Scenario: Check duplicate records in external table
        Given User establishes a successful connection with external table
        When user executes the query to retrieve all records with ACCT_ID
        Then user checks for any duplicate records with ACCT_ID field

    Scenario: Check duplicate records in UCDM Account table
        Given User establishes a successful connection with UCDM Account table
        When user executes the query to retrieve all records with ACCT_ID
        Then user checks for any duplicate records with ACCT_ID field
