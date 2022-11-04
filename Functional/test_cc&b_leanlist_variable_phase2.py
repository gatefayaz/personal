from asyncio.windows_events import NULL
import pytest
import pytest
import pyodbc
from pytest_bdd import given, when, then, scenario, parsers
from functools import partial
from python_settings import settings
import pytest_bdd

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test if ContactClass column has null values in Customer_Contacts table",
)
def test_ContactClass_column_has_null_values_in_Customer_Contacts_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate ContactClass column has null values in Customer_Contacts table')
def validate_ContactClass_column_has_null_values_in_Customer_Contacts_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Customer_Contacts")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [ucdm].[Customer_Contacts]  where currentflag=1 and ContactClass is NULL'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test if ContactClassCode column has null values in Customer_Contacts table",
)
def test_ContactClassCode_column_has_null_values_in_Customer_Contacts_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate ContactClassCode column has null values in Customer_Contacts table')
def validate_ContactClassCode_column_has_null_values_in_Customer_Contacts_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Customer_Contacts")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [ucdm].[Customer_Contacts] where currentflag=1 and ContactClassCode is NULL'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test if AccountID column values has ED_ as prefix in Customer_Contacts table",
)
def test_AccountID_column_values_has_ED_as_prefix_in_Customer_Contacts_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate AccountID column values has ED_ as prefix in Customer_Contacts table')
def validate_AccountID_column_values_has_ED_as_prefix_in_Customer_Contacts_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Customer_Contacts")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT AccountID
        FROM ucdm.Customer_Contacts
        WHERE AccountID NOT LIKE '%ED_%' and AccountID is NULL'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        elif row[0]==0 or row[0] is None:
            assert True
        else: 
            assert False
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate data between staging and ucdm for ContactClassCode in Customer_Contacts table",
)
def test_data_between_staging_and_ucdm_for_ContactClassCode_in_Customer_Contacts_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data between staging and ucdm for ContactClassCode in Customer_Contacts table')
def validate_data_between_staging_and_ucdm_for_ContactClassCode_in_Customer_Contacts_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Customer_Contacts")
    ucdm_data = cursor.fetchone()
    cursor.execute("select count(*) from stg.ci_cc_cl_l")
    stg_data = cursor.fetchone()
    if ucdm_data[0] != 0 and stg_data[0] !=0 :
        query = '''select ContactClassCode from [ucdm].[Customer_Contacts]  where currentflag=1
        except
        select distinct(cc_cl_cd) from stg.ci_cc_cl_l'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        elif row[0]==0 or row[0] is None:
            assert True
        else: 
            assert False
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate data between staging and ucdm for contactmethod in Customer_Contacts table",
)
def test_data_between_staging_and_ucdm_for_contactmethod_in_Customer_Contacts_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data between staging and ucdm for contactmethod in Customer_Contacts table')
def validate_data_between_staging_and_ucdm_for_contactmethod_in_Customer_Contacts_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Customer_Contacts")
    ucdm_data = cursor.fetchone()
    cursor.execute("select count(*) from stg.ci_cc")
    stg_data = cursor.fetchone()
    if ucdm_data[0] != 0 and stg_data[0] !=0:
        query = '''select contactmethod from [ucdm].[Customer_Contacts] where currentflag = 1
        except
        select distinct(contact_method) from [stg].[ci_cc]'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        elif row[0]==0 or row[0] is None:
            assert True
        else: 
            assert False
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate data between staging and ucdm for ContactClass in Customer_Contacts table",
)
def test_data_between_staging_and_ucdm_for_ContactClass_in_Customer_Contacts_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data between staging and ucdm for ContactClass in Customer_Contacts table')
def validate_data_between_staging_and_ucdm_for_ContactClass_in_Customer_Contacts_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Customer_Contacts")
    ucdm_data = cursor.fetchone()
    cursor.execute("select count(*) from stg.ci_cc_cl_l")
    stg_data = cursor.fetchone()
    cursor.execute("select count(*) from stg.ci_cc")
    stg2_data = cursor.fetchone()
    if ucdm_data[0] != 0 and stg_data[0] !=0 and stg2_data[0] !=0:
        query = '''select ContactClass from ucdm.Customer_Contacts where currentflag=1
        except
        SELECT DISTINCT cl.[ContactClass] AS [ContactClass] FROM [stg].[ci_cc] c 
        LEFT JOIN (SELECT descr AS [ContactClass], cc_cl_cd
        FROM stg.[ci_cc_cl_l]) cl
        ON cl.cc_cl_cd = c.cc_cl_cd'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        elif row[0]==0 or row[0] is None:
            assert True
        else: 
            assert False
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate data between staging and ucdm for accountid in Customer_Contacts table",
)
def test_data_between_staging_and_ucdm_for_accountid_in_Customer_Contacts_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data between staging and ucdm for accountid in Customer_Contacts table')
def validate_data_between_staging_and_ucdm_for_accountid_in_Customer_Contacts_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Customer_Contacts")
    ucdm_data = cursor.fetchone()
    cursor.execute("select count(*) from stg.ci_cc")
    stg_data = cursor.fetchone()
    if ucdm_data[0] != 0 and stg_data[0] !=0:
        query = '''select accountid from ucdm.Customer_Contacts where currentflag=1
        except
        select distinct('ED_' + acct_id) from [stg].[ci_cc]'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        elif row[0]==0 or row[0] is None:
            assert True
        else: 
            assert False
    else: 
        assert False    
    cursor.close()



@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate account table incremental",
)
def test_account_table_incremental():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate account table incremental')
def validate_account_table_incremental(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.account")
    ucdm_data = cursor.fetchone()
    if ucdm_data[0] != 0:
        query = '''select 1 where  
        (select count(distinct accountid) from ucdm.account  where load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.account'   
        AND InsertedRows>0    AND    Status= 'SUCCESS')) 
        = 
        (select count(accountid) from ucdm.account where currentflag=1 and 
        load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.account'   
        AND InsertedRows>0    AND    Status= 'SUCCESS'))'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert False
        else: 
            assert row[0]==1
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate serviceagreement table incremental",
)
def test_serviceagreement_table_incremental():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate serviceagreement table incremental')
def validate_serviceagreement_table_incremental(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.serviceagreement")
    ucdm_data = cursor.fetchone()
    if ucdm_data[0] != 0:
        query = '''select 1 where  
        (select count(distinct serviceagreementid) from ucdm.serviceagreement  where load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.serviceagreement'   
        AND InsertedRows>0    AND    Status= 'SUCCESS')) 
        = 
        (select count(serviceagreementid) from ucdm.serviceagreement where currentflag=1 and 
        load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.serviceagreement'   
        AND InsertedRows>0    AND    Status= 'SUCCESS'))'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert False
        else: 
            assert row[0]==1
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate person table incremental",
)
def test_person_table_incremental():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate person table incremental')
def validate_person_table_incremental(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.person")
    ucdm_data = cursor.fetchone()
    if ucdm_data[0] != 0:
        query = '''select 1 where  
        (select count(distinct personid) from ucdm.person  where load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.person'   
        AND InsertedRows>0    AND    Status= 'SUCCESS')) 
        = 
        (select count(personid) from ucdm.person where currentflag=1 and 
        load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.person'   
        AND InsertedRows>0    AND    Status= 'SUCCESS')) '''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert False
        else: 
            assert row[0]==1
    else: 
        assert False    
    cursor.close()


@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate bill table incremental",
)
def test_bill_table_incremental():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate bill table incremental')
def validate_bill_table_incremental(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.bill")
    ucdm_data = cursor.fetchone()
    if ucdm_data[0] != 0:
        query = '''select 1 where  
        (select count(distinct billid) from ucdm.bill  where load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.bill'   
        AND InsertedRows>0    AND    Status= 'SUCCESS')) 
        = 
        (select count(billid) from ucdm.bill where currentflag=1 and 
        load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.bill'   
        AND InsertedRows>0    AND    Status= 'SUCCESS'))'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert False
        else: 
            assert row[0]==1
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate bill segment table incremental",
)
def test_bill_segment_table_incremental():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate bill segment table incremental')
def validate_bill_segment_table_incremental(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.BillSegment")
    ucdm_data = cursor.fetchone()
    if ucdm_data[0] != 0:
        query = '''select 1 where  
        (select count(distinct BillSegmentid) from ucdm.BillSegment  where load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.BillSegment'   
        AND InsertedRows>0    AND    Status= 'SUCCESS')) 
        = 
        (select count(BillSegmentid) from ucdm.BillSegment where currentflag=1 and 
        load_date_time >=  
        (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
        FROM   ctl.LoadLog WHERE        TableName = 'ucdm.BillSegment'   
        AND InsertedRows>0    AND    Status= 'SUCCESS'))'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert False
        else: 
            assert row[0]==1
    else: 
        assert False    
    cursor.close()


@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate SAStatusDesc column in serviceagreement table incremental",
)
def test_SAStatusDesc_column_in_serviceagreement_table_incremental():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate SAStatusDesc column in serviceagreement table incremental')
def validate_SAStatusDesc_column_in_serviceagreement_table_incremental(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.ServiceAgreement")
    ucdm_data = cursor.fetchone()
    if ucdm_data[0] != 0:
        query = '''select count(*) from  ucdm.ServiceAgreement sa  
        where currentflag=1 and  not exists (  
        select 1   
        FROM stg.ci_sa ci_sa  
        LEFT JOIN [stg].[CI_SA_TYPE_L] STL ON ci_sa.[SA_TYPE_CD] = STL.[SA_TYPE_CD] 
        LEFT JOIN stg.ci_sa_rs_hist rsh   
        ON ci_sa.sa_id = rsh.sa_id   
        AND rsh.effdt = ( SELECT MAX(effdt)  FROM stg.ci_sa_rs_hist rsha   
        WHERE ci_sa.sa_id = rsha.sa_id)  
        JOIN stg.ci_rs_l rsl  ON rsh.rs_cd = rsl.rs_cd    
        where  sa.ServiceAgreementID = 'ED_' + ci_sa.sa_id   
        and sa.satype = STL.[DESCR]  
        and CASE ci_sa.[SA_STATUS_FLG]  
        WHEN '10' THEN 'Pending Start' 
        WHEN '20' THEN 'Active' 
        WHEN '30' THEN 'Pending Stop' 
        WHEN '40' THEN 'Stopped' 
        WHEN '50' THEN 'Reactivated' 
        WHEN '60' THEN 'Closed' 
        WHEN '70' THEN 'Canceled' 
        ELSE 'undefined' 
        END = sa.SAStatusDesc 
        and  ci_sa.[cis_division] IN ('ROI'))'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert False
        else: 
            assert row[0]==0
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_phase2
@scenario(
    "../../features/cc&b_variables_phase2.feature",
    "Test to validate SA_TYPE column in serviceagreement table incremental",
)
def test_SA_TYPE_column_in_serviceagreement_table_incremental():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate SA_TYPE column in serviceagreement table incremental')
def validate_SA_TYPE_column_in_serviceagreement_table_incremental(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.ServiceAgreement")
    ucdm_data = cursor.fetchone()
    if ucdm_data[0] != 0:
        query = '''select count(*) from  ucdm.ServiceAgreement sa
        where currentflag=1 and  not exists (
        select 1  
        FROM stg.ci_sa ci_sa
        LEFT JOIN [stg].[CI_SA_TYPE_L] STL ON ci_sa.[SA_TYPE_CD] = STL.[SA_TYPE_CD]
        LEFT JOIN stg.ci_sa_rs_hist rsh  
        ON ci_sa.sa_id = rsh.sa_id  
        AND rsh.effdt = ( SELECT MAX(effdt)  FROM stg.ci_sa_rs_hist rsha  
        WHERE ci_sa.sa_id = rsha.sa_id)
        JOIN stg.ci_rs_l rsl  ON rsh.rs_cd = rsl.rs_cd  
        where  sa.ServiceAgreementID = 'ED_' + ci_sa.sa_id  
        and isnull(sa.accountid, '') = isnull(CASE
        WHEN ci_sa.[sa_type_cd] IN ('DOMESTIC', 'DOMESTIG', 'RI-S-NHH', 'RI-S-HH','PREPAYRE','PREPAYRG') THEN 'ED_' + ci_sa.acct_id
        ELSE NULL
        END, '')
        and CASE ci_sa.[CHAR_PREM_ID]
        WHEN '' THEN NULL
        ELSE 'ED_' + ci_sa.[CHAR_PREM_ID]
        END = sa.premiseid
        and  ci_sa.[cis_division] IN ('ROI'))'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert False
        else: 
            assert row[0]==0
    else: 
        assert False    
    cursor.close()