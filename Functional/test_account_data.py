import pytest
import pyodbc
from pytest_bdd import given, when, then, scenario, parsers
from functools import partial
from python_settings import settings
import pytest_bdd


@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "To Enter into the Synapse External tables",
)
def test_synapse_external_tables():
    pass

@given('User login into database write the query to retrieve the data of external tables')
def login_to_database(kv):
    pass

@when('I Will execute the query')
def query_execution(sql_connection):
    pass

@then('I will get the data retrieved of external table')
def get_data_from_external_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.ci_acct")
    data = cursor.fetchone()
    #print(data)
    if data[0] != 0:
        cursor.execute("select count(*) from ext.ci_acct;")
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "To Enter into the Synapse External tables of ext_ci_acct",
)
def test_ext_ci_acct_table():
    pass

@given('A valid connection to the ext_ci_acct is established, and table information retrieved from source')
def database_connection_ext_ci_acct(kv):
    pass

@when('I will write query to get details on ext_ci_acct table')
def execute_query_ext_ci_acct_table(sql_connection):
    pass

@then('Check if data exists in ext_ci_acct table')
def validate_if_data_exist_in_ext_ci_acct_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.ci_acct")
    data = cursor.fetchone()
    cursor.execute("select count(*) from stg.ci_acct")
    stg_data = cursor.fetchone()
    #print(data)
    if data[0] != 0 and stg_data[0] != 0:
        sql_query = '''SELECT [acct_id],[bill_cyc_cd],[setup_dt],[currency_cd],[acct_mgmt_grp_cd],[alert_info],[bill_after_dt],[protect_cyc_sw],[cis_division],[mailing_prem_id]
                    ,[protect_prem_sw],[coll_cl_cd],[cr_review_dt],[postpone_cr_rvw_dt],[int_cr_review_sw],[cust_cl_cd],[bill_prt_intercept],[no_dep_rvw_sw],[bud_plan_cd]
                    ,[version],[protect_div_sw],[access_grp_cd],[hvr_seq],[hvr_target_integrate_time],[source_operation],[src_commit_time]
                    FROM [ext].[ci_acct]
                    Except
                    SELECT [acct_id],[bill_cyc_cd],[setup_dt],[currency_cd],[acct_mgmt_grp_cd],[alert_info],[bill_after_dt],[protect_cyc_sw],[cis_division],[mailing_prem_id]
                    ,[protect_prem_sw],[coll_cl_cd],[cr_review_dt],[postpone_cr_rvw_dt],[int_cr_review_sw],[cust_cl_cd],[bill_prt_intercept],[no_dep_rvw_sw],[bud_plan_cd]
                    ,[version],[protect_div_sw],[access_grp_cd],[hvr_seq],[hvr_target_integrate_time],[source_operation],[src_commit_time]     
                    FROM [stg].[ci_acct]'''
        cursor.execute(sql_query)
        row = cursor.fetchone()
        #list = [0,'None']
        #assert row[0] is None
        assert isinstance(row, type(None))
    else: 
        assert False    
    cursor.close()
@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "To Enter into the Synapse Staging tables of stg.ci_acct",
)
def test_stg_ci_acct_table():
    pass

@given('A valid connection to the stg.ci_acct is established, and table information retrieved from source')
def database_connection_stg_ci_acct_table(kv):
    pass

@when('I will write query to get details on stg.ci_acct table')
def execute_query_stg_ci_acct_table(sql_connection):
    pass

@then('check if data exists in stg.ci_acct')
def validate_if_data_exist_in_stg_ci_acct_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.ci_acct")
    data = cursor.fetchone()
    cursor.execute("select count(*) from stg.ci_acct")
    stg_data = cursor.fetchone()
    if data[0] != 0 and stg_data[0] != 0:
        sql_query2 = '''SELECT [acct_id],[bill_cyc_cd],[setup_dt],[currency_cd],[acct_mgmt_grp_cd],[alert_info],[bill_after_dt],[protect_cyc_sw],[cis_division],[mailing_prem_id]
                    ,[protect_prem_sw],[coll_cl_cd],[cr_review_dt],[postpone_cr_rvw_dt],[int_cr_review_sw],[cust_cl_cd],[bill_prt_intercept],[no_dep_rvw_sw],[bud_plan_cd]
                    ,[version],[protect_div_sw],[access_grp_cd],[hvr_seq],[hvr_target_integrate_time],[source_operation],[src_commit_time]     
                    FROM [stg].[ci_acct]
                    Except
                    SELECT [acct_id],[bill_cyc_cd],[setup_dt],[currency_cd],[acct_mgmt_grp_cd],[alert_info],[bill_after_dt],[protect_cyc_sw],[cis_division]
                    ,[mailing_prem_id],[protect_prem_sw],[coll_cl_cd],[cr_review_dt],[postpone_cr_rvw_dt],[int_cr_review_sw],[cust_cl_cd],[bill_prt_intercept],[no_dep_rvw_sw]
                    ,[bud_plan_cd],[version],[protect_div_sw],[access_grp_cd],[hvr_seq],[hvr_target_integrate_time],[source_operation],[src_commit_time]
                    FROM [ext].[ci_acct]'''
        cursor.execute(sql_query2)
        row = cursor.fetchone()
        #list = [0,'None']
        #assert row[0] is None
        assert isinstance(row, type(None))
    else: 
        assert False    
    cursor.close()

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "To Enter into the Synapse Data warehouse",
)
def test_connect_to_synapse_data_warehouse():
    pass

@given('A valid connection to the data warehouse is established and table information retrieved from UCDM.account')
def database_connection_ucdm_acct_table(kv):
    pass

@when('I will write query to get details on data warehouse')
def execute_query_ucdm_acct_table(sql_connection):
    pass

@then('I will validate number of rows from data warehouse with UCDM.account')
def validate_number_of_rows_in_ucdm_acct_table(sql_connection):
    cursor = sql_connection.cursor()

    cursor.execute("select count(*) from ucdm.account")
    data = cursor.fetchone()
    if data[0] != 0:
        cursor.execute("select count(*) from ucdm.account") 
        row = cursor.fetchone()
        assert row[0] > 0
    else: 
        assert False    
    cursor.close()

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check number of records inserted or updated in the Synapse Data Warehouse",
)
def test_check_number_of_records_inserted_in_ucdm():
    pass

@given('User establishes a successful connection with Data Warehouse')
def database_connection_details(kv):
    pass

@when('user executes the query with start date and end date')
def query_execution(sql_connection):
    pass

@then('user validate the rows in Data Warehouse from that specified dates')
def validate_rows_in_ucdm_for_specific_dates(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.account")
    data = cursor.fetchone()
    if data[0] != 0:    
        cursor.execute("select count(*) from UCDM.Account where createddate >=(Select max(enddatetime) from [ctl].[LoadLog] where tablename='ucdm.account' and ID = 52) Except select count(*) from stg.ci_acct")
        row = cursor.fetchone()
        assert row[0] == 0
    else: 
        assert False    
    cursor.close()



@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check Null values inserted or updated in the Synapse Data Warehouse for AccountID",
)
def test_if_ucdm_account_id_is_null():
    pass

@given('User establishes a successful connection with Data Warehouse')
def database_connection_details(kv):
    pass

@when('user executes the query to retrieve all account ID')
def connection_to_execute_query(sql_connection):
    pass

@then('user validate the AccountID column has any null values')
def validate_account_id_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.account")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        cursor.execute("select count(*) from UCDM.account where Accountid is null")
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check Null values inserted or updated in the Synapse Data Warehouse for PersonID",
)
def test_if_person_id_is_null_ucdm():
    pass

@given('User establishes a successful connection with Data Warehouse')
def database_connection_details(kv):
    pass

@when('user executes the query to retrieve all Person ID')
def connection_to_execute_query(sql_connection):
    pass

@then('user validate the PersonID column has any null values')
def validate_person_id_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.account")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        cursor.execute("select count(*) from UCDM.account where PersonID is null")
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check Null value for start Date in External table",
)
def test_if_start_date_is_null_ext():
    pass

@given('User establishes a successful connection with External table')
def database_connection_details(kv):
    pass

@when('user executes the query to retrieve all records')
def database_connection_to_execute_query(sql_connection):
    pass

@then('user validate the EXT.CI_ACCT_APAY column has any null values')
def validate_start_date_ext(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.ci_acct_apay")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        cursor.execute("Select count(*) from ext.ci_acct_apay where acct_apay_id  is null")
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check Null value for start Date in staging table",
)
def test_if_start_date_is_null_stg():
    pass

@given('User establishes a successful connection with staging table')
def database_connection_details(kv):
    pass

@when('user executes the query to retrieve all records')
def database_connection_to_execute_query(sql_connection):
    pass

@then('user validate the STG.CI_ACCT_APAY column has any null values')
def validate_start_date_stg(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_acct_apay")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        cursor.execute("Select count(*) from stg.ci_acct_apay where acct_apay_id  is null")
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check accepted values for Payment type in UCDM Account table",
)
def test_check_accepted_values_for_payment_type_ucdm():
    pass

@given('User establishes a successful connection with UCDM account table')
def database_connection_details(kv):
    pass

@when('user executes the query to retrieve all records')
def database_connection_to_execute_query(sql_connection):
    pass

@then('user validate the Payment type column has any one of these values Fixed,Variable,Other values')
def validate_payment_type_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.account")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        cursor.execute("select count(*) from UCDM.account  where PaymentType not in ('Fixed', 'Variable', 'Other')")
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check accepted values for AutopayStartDate in UCDM Account table",
)
def test_check_autopay_start_date_ucdm():
    pass

@given('User establishes a successful connection with UCDM account table')
def database_connection_details(kv):
    pass

@when('user executes the query to retrieve all records ')
def database_connection_to_execute_query_ucdm(sql_connection):
    pass

@then('user validate the AutopayStartDate type column has valid date values')
def validate_autopay_start_date_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.account")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        cursor.execute("select count(*) from UCDM.account where AutopayStartDate is null")
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check accepted values for FirstBillDate in UCDM Account table",
)
def test_check_firstbilldate_ucdm():
    pass

@given('User establishes a successful connection with UCDM account table')
def database_connection_details(kv):
    pass

@when('user executes the query to retrieve all records')
def database_connection_to_execute_query(sql_connection):
    pass

@then('user validate the FirstBillDate type column has valid date values')
def validate_firstbilldate_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.account")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        cursor.execute("select count(*) from UCDM.account where FirstBillDate is null")
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check duplicate records in external table",
)
def test_check_for_duplicate_records_ext_table():
    pass

@given('User establishes a successful connection with external table')
def database_connection_details(kv):
    pass

@when('user executes the query to retrieve all records with ACCT_ID')
def database_connection_to_execute_query(sql_connection):
    pass

@then('user checks for any duplicate records with ACCT_ID field')
def validate_for_duplicate_records_ext_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.account")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        cursor.execute("select count(*) as count from UCDM.Account where createddate >=(Select max(enddatetime) from [ctl].[LoadLog] where tablename='ucdm.account' and ID = 52) Except select count(*) from stg.ci_acct")
        row = cursor.fetchone()
        #list = [0,'None']
        assert row[0] == 0
        #assert isinstance(row, type(None))
    else: 
        assert False    
    cursor.close() 

@pytest.mark.account
@scenario(
    "../../features/account_table.feature",
    "Check duplicate records in UCDM Account table",
)
def test_check_for_duplicate_records_ucdm():
    pass

@given('User establishes a successful connection with UCDM Account table')
def database_connection_details(kv):
    pass

@when('user executes the query to retrieve all records with ACCT_ID')
def database_connection_to_execute_query(sql_connection):
    pass

@then('user checks for any duplicate records with ACCT_ID field')
def validate_for_duplicate_records_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.account")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        cursor.execute("select count(*) as count from UCDM.Account where createddate >=(Select max(enddatetime) from [ctl].[LoadLog] where tablename='ucdm.account' and ID = 52) Except select count(*) from stg.ci_acct")
        row = cursor.fetchone()
        #list =[0,'None']
        assert row[0] == 0
        #assert isinstance(row, type(None))
    else: 
        assert False    
    cursor.close()                        