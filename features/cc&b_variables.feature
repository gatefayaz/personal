Feature: Validate cc&b leanlist variables

    Scenario: Test if latest execution records are available in ucdm Accountperson table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm AccountPerson table

    Scenario: Test if latest execution records are available in ucdm Bill table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm Bill table
    
    Scenario: Test if latest execution records are available in ucdm BillSegment table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm BillSegment table
    
    Scenario: Test if latest execution records are available in ucdm complaints table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm complaints table
    
    Scenario: Test if latest execution records are available in ucdm contract table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm contract table

    Scenario: Test if latest execution records are available in ucdm Customer_Contacts table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm Customer_Contacts table


    Scenario: Test if latest execution records are available in ucdm CustomerContactsComplaintsSummary table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm CustomerContactsComplaintsSummary table
    
    Scenario: Test if latest execution records are available in ucdm Debt table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm Debt table
    
    Scenario: Test if latest execution records are available in ucdm MarketingPreferences table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm MarketingPreferences table
    
    Scenario: Test if latest execution records are available in ucdm Person table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm Person table

    Scenario: Test if latest execution records are available in ucdm Premise table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm Premise table

    Scenario: Test if latest execution records are available in ucdm SATransactions table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm SATransactions table

    Scenario: Test if latest execution records are available in ucdm Service Agreement table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm Service Agreement table

    Scenario: Test to validate payment type in ucdm account table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate payment type in ucdm account table

    Scenario: Test to validate contract type in ucdm contract table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate contract type in ucdm contract table

    Scenario: Test to validate SeasonOfSignUp in ucdm contract table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate SeasonOfSignUp in ucdm contract table

    Scenario: Test to validate cash back amount in ucdm contract table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate cash back amount in ucdm contract table

    Scenario: Test to validate billing type in  ucdm Accountperson table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate billing type in  ucdm Accountperson table

    Scenario: Test to check If EnergyOnline Available
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate If EnergyOnline Available

    Scenario: Test to check If EnergyOnlineID Available
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate If EnergyOnlineID Available

    Scenario: Test to validate data in stg.ci_sa table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data in stg.ci_sa table

    Scenario: Test to validate data in ucdm person table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in ucdm person table

    Scenario: Test to validate data in stg.ci_per table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data in stg.ci_per table

    Scenario: Test to validate data in stg.ci_bseg table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate  data in stg.ci_bseg table

    Scenario: Test to validate data in ucdm contract table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data in ucdm contract table

    Scenario: Test to validate data in stg.ci_cc table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data in stg.ci_cc table

    Scenario: Test to validate data in stg ci_per table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data in stg.ci_per table

    Scenario: Test to validate data in stg.ci_prem table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data in stg.ci_prem table

    Scenario: Test to validate data in stg.ci_case table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data in stg.ci_case table

    Scenario: Test to validate data in stg.ci_bill table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data in stg.ci_bill table

    Scenario: Test to validate data in stg.ci_acct_per table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate records in stg.ci_acct_per table

    Scenario: Test to validate data in stg.ci_acct table
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data in stg.ci_acct table

    Scenario: Test to validate Level Pay Query
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate Level Pay Query

    Scenario: Test to validate meter read inquiry
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate meter read inquiry

    Scenario: Test to validate meter read dispute
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate meter read dispute

    Scenario: Test to validate open complaints variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate open complaints variable

    Scenario: Test to validate average consumption electricity variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate average consumption electricity variable

    Scenario: Test to validate last bill amount variance variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate last bill amount variance variable

    Scenario: Test to validate tariff(only for electricity) variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate tariff(only for electricity) variable

    Scenario: Test to validate Have you hit threshold/Cap ( Day/Night and Night Storage) variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate Have you hit threshold/Cap ( Day/Night and Night Storage) variable

    Scenario: Test to validate Is Discount offered is equal to discount availed variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate Is Discount offered is equal to discount availed variable

    Scenario: Test to validate Average consumption for gas variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate Average consumption for gas variable

    Scenario: Test to validate Average consumption for gas variable in ucdm
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate Average consumption for gas variable in ucdm

    Scenario: Test to validate Level Pay (NBB) Amount Increase variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate Level Pay (NBB) Amount Increase variable

    Scenario: Test to validate NBBPCChange variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate NBBPCChange variable

    Scenario: Test to validate NBBIncrease variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate NBBIncrease variable

    Scenario: Test to validate NBBDecrease variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate NBBDecrease variable

    Scenario: Test to validate DidNBBChangeAtReview variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate DidNBBChangeAtReview variable

    Scenario: Test to validate ElecMeterRead(MeterReadType) variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate ElecMeterRead(MeterReadType) variable

    Scenario: Test to validate GasMeterRead(MeterReadType) variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate GasMeterRead(MeterReadType) variable

    Scenario: Test to validate ElecMeterRead(MeterReadType values check) variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate ElecMeterRead(MeterReadType values check) variable

    Scenario: Test to validate GasMeterRead(MeterReadType values check) variable in ucdm
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate GasMeterRead(MeterReadType values check) variable in ucdm

    Scenario: Test to validate active bad debt variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate active bad debt variable

    Scenario: Test to validate active bad debt amount variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate active bad debt amount variable

    Scenario: Test to validate total number of times bad debt in ucdm variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate total number of times bad debt in ucdm variable

    Scenario: Test to validate total bad debt amount variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate total bad debt amount variable

    Scenario: Test to validate active bad debt variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate active bad debt variable

    Scenario: Test to validate active bad debt amount stage variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate active bad debt amount stage variable

    Scenario: Test to validate total number of times bad debt in stg 
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate total number of times bad debt in stg

    Scenario: Test to validate total bad debt amount in stg
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate total bad debt amount in stg

    Scenario: Test to validate price increase source
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate price increase source

    Scenario: Test to validate price decrease source
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate price decrease source

    Scenario: Test to validate discount applied  variable in stg
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate discount applied variable in stg

    Scenario: Test to validate initial signup channel in ucdm
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate initial signup channel in ucdm

    Scenario: Test to validate initial signup channel in stg
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate initial signup channel in stg  

    Scenario: Test to validate eoc contract notifications variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate eoc contract notifications variable

    Scenario: Test to validate complaints ever total variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate complaints ever total variable 

    Scenario: Test to validate complaints ever L3 variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate complaints ever L3 variable 

    Scenario: Test to validate complaints ever L2 variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate complaints ever L2 variable 

    Scenario: Test to validate complaints ever L1 variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate complaints ever L1 variable

    Scenario: Test to validate complaints ever one and done variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate complaints ever one and done variable 

    Scenario: Test to validate Any DD Auto rejection in last 30 days prior to Prediction Window (Day 335)  variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate Any DD Auto rejection in last 30 days prior to Prediction Window (Day 335)  variable 

    Scenario: Test to validate Did they cancel DD prior to Prediction Window (Day 335) variable
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate Did they cancel DD prior to Prediction Window (Day 335) variable   

    Scenario: Test to validate external table CI_ACCT_APAY does not contain the ext_acct_id column
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate external table CI_ACCT_APAY does not contain the ext_acct_id column

    Scenario: Test to validate staging table CI_ACCT_APAY does not contain the ext_acct_id column
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate staging table CI_ACCT_APAY does not contain the ext_acct_id column

    Scenario: Test to validate data between external and staging table are matching for CI_ACCT_APAY
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate data between external and staging table are matching for CI_ACCT_APAY

    Scenario: Test to validate count of records between external and staging table are matching for CI_ACCT_APAY
        Given I have Database connection details
        When I was able to connect to database
        Then I can validate count of records between external and staging table are matching for CI_ACCT_APAY

    