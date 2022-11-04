import pytest
import pytest
import pyodbc
from pytest_bdd import given, when, then, scenario, parsers
from functools import partial
from python_settings import settings
import pytest_bdd


@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm Accountperson table",
)
def test_record_count_in_ucdm_accountperson_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm AccountPerson table')
def validate_records_in_ucdm_accountperson_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.AccountPerson")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.AccountPerson where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.AccountPerson' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm Bill table",
)
def test_record_count_in_ucdm_bill_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm Bill table')
def validate_records_in_ucdm_bill_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Bill")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.Bill where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.Bill' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm BillSegment table",
)
def test_record_count_in_ucdm_billsegment_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm BillSegment table')
def validate_records_in_ucdm_billsegment_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.BillSegment")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.BillSegment where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.BillSegment' AND InsertedRows>0   AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm complaints table",
)
def test_record_count_in_ucdm_complaints_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm complaints table')
def validate_records_in_ucdm_complaints_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Complaints")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.Complaints where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.Complaints' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm contract table",
)
def test_record_count_in_ucdm_contract_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm contract table')
def validate_records_in_ucdm_contract_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Contract")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.Contract where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.Contract' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm Customer_Contacts table",
)
def test_record_count_in_ucdm_customer_contacts_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm Customer_Contacts table')
def validate_records_in_ucdm_customer_contacts_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Customer_Contacts")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.Customer_Contacts where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.Customer_Contacts' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm CustomerContactsComplaintsSummary table",
)
def test_record_count_in_ucdm_customercontacts_complaints_summarytable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm CustomerContactsComplaintsSummary table')
def validate_records_in_ucdm_customercontacts_complaints_summary_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.AccountPerson")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.CustomerContactsComplaintsSummary where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.CustomerContactsComplaintsSummary' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm Debt table",
)
def test_record_count_in_ucdm_debt_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm Debt table')
def validate_records_in_ucdm_debt_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Debt")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.Debt where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.Debt' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm MarketingPreferences table",
)
def test_record_count_in_ucdm_marketingpreferences_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm MarketingPreferences table')
def validate_records_in_ucdm_marketingpreferences_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.MarketingPreferences")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.MarketingPreferences where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.MarketingPreferences' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm Person table",
)
def test_record_count_in_ucdm_person_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm Person table')
def validate_records_in_ucdm_person_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Person")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.Person where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.Person' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm Premise table",
)
def test_record_count_in_ucdm_premise_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm Premise table')
def validate_records_in_ucdm_premise_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Premise")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.Premise where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.Premise' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm SATransactions table",
)
def test_record_count_in_ucdm_satransactions_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm SATransactions table')
def validate_records_in_ucdm_satransactions_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.SATransactions")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.SATransactions where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.SATransactions' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test if latest execution records are available in ucdm Service Agreement table",
)
def test_record_count_in_ucdm_serviceagreement_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm Service Agreement table')
def validate_records_in_ucdm_serviceagreement_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.ServiceAgreement")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.ServiceAgreement where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  
                   ctl.LoadLog WHERE TableName = 'ucdm.ServiceAgreement' AND InsertedRows>0  AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate payment type in ucdm account table",
)
def test_payment_type_in_ucdm_account_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate payment type in ucdm account table')
def validate_payment_type_in_ucdm_account_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Account")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.Account a where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM   ctl.LoadLog
                    WHERE TableName = 'ucdm.account' AND InsertedRows>0  AND Status= 'SUCCESS')
                   and not exists (SELECT 1 FROM stg.CI_ACCT CI_ACCT left join
                   (SELECT SA.[ACCT_ID], COUNT(*) AS MDDNBB FROM stg.[CI_SA] SA, stg.[CI_ACCT_APAY] AAP  WHERE [SA_TYPE_CD] = 'MDDNBB'
                   AND SA.[SA_STATUS_FLG] IN ('20','30') AND SA.[ACCT_ID] = AAP.[ACCT_ID] AND (AAP.[END_DT] IS NULL OR AAP.[END_DT] >= GETDATE())
                   GROUP BY SA.[ACCT_ID]) SA2 ON CI_ACCT.[ACCT_ID] = SA2.[ACCT_ID] where  'ED_' + CI_ACCT.acct_id = a.accountid and a.load_date_time=ci_acct.load_date_time);'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

# @pytest.mark.reconciliation_cc_and_b
# @scenario(
#     "../../features/cc&b_variables.feature",
#     "Test to validate contract type in ucdm contract table",
# )
# def test_contract_type_in_ucdm_contract_table():
#     pass

# @given('I have Database connection details')
# def database_connection_details(kv):
#     pass

# @when('I was able to connect to database')
# def database_connection(sql_connection):
#     pass

# @then('I can validate contract type in ucdm contract table')
# def validate_contract_type_in_ucdm_contract_table(sql_connection):
#     cursor = sql_connection.cursor()
#     cursor.execute("select count(*) from UCDM.Contract")
#     data = cursor.fetchone()
#     print(data)
#     if data[0] != 0:
#         query = '''select count(*) from UCDM.[Contract] c where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  ctl.LoadLog WHERE TableName = 'ucdm.Contract' AND InsertedRows>0  AND  Status= 'SUCCESS')  
#                     and not exists (select 1 from  
#                     (select SA_ID, contractType from ( 
#                     SELECT SA.SA_ID, CASE 
#                              WHEN SA.[end_dt] < DATEADD(D, 365, SC1.effdt) AND DATEDIFF(D,SA.start_dt,SC1.effdt) <= 365 OR 
#                                            SA.[end_dt] <= DATEADD(D, 365, SACON.[START_DT]) AND DATEDIFF(D,SA.start_dt,SACON.[START_DT]) < 365 OR 
#                                            SC1.effdt <= DATEADD(D, 30, SA.start_dt) AND SA.start_dt > DATEADD(D, -365, GETDATE()) OR 
#                                            SACON.[START_DT] <= DATEADD(D, 30, SA.start_dt) AND SA.start_dt > DATEADD(D, -365, GETDATE()) 
#                              THEN 'Acquisition' 
#                              WHEN (CAST(SA.end_dt AS DATE) < DATEADD(D, 365, SC1.effdt)) OR --Left Mid Contract 
#                                            (CAST(SC1.effdt AS DATE) > DATEADD(D, 30, SA.start_dt) AND DATEADD(D, 365, SC1.effdt) >= GETDATE() OR 
#                                            CAST(SACON.[START_DT] AS DATE) > DATEADD(D, 30, SA.start_dt) AND DATEADD(D, 365, SACON.[START_DT] ) >= GETDATE() OR 
#                                            CAST(SACON.[START_DT] AS DATE) > DATEADD(D, 30, SA.start_dt) AND SACON.[END_DT] >= GETDATE()) 
#                              THEN 'Retention' --365 Char Effdt before todays date 
#                              ELSE 'Standard' 
#                     END AS [contractType] 
#                     FROM  
#                     stg.[CI_SA] SA LEFT JOIN stg.[CI_SA_CHAR] SC1 ON SA.[SA_ID] = SC1.[SA_ID] AND SC1.[CHAR_TYPE_CD] = 'CONTPERD'  
#                     LEFT JOIN           (SELECT               sa_id, MAX(start_dt) AS start_dt, MAX(end_dt) AS end_dt FROM stg.ci_sa_conterm     
#                     WHERE bf_cd IN ('AFDBDOMR', 'DFDBDOMR', 'DDDBDOMR', 'DDDMDOMR', 'OCDBDOMR') GROUP BY              sa_id )   sacon ON sacon.sa_id = sa.sa_id)  A) B 
#                     where 'ED_' + B.SA_ID = c.ServiceAgreementID and c.contracttype = B.contracttype);'''
#         cursor.execute(query)
#         row = cursor.fetchone()
#         assert row[0] == 0 
#     else: 
#         assert False    
#     cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate SeasonOfSignUp in ucdm contract table",
)
def test_SeasonOfSignUp_in_ucdm_contract_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate SeasonOfSignUp in ucdm contract table')
def validate_seasonofsignup_in_ucdm_contract_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Contract")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.[Contract] c where currentflag=1 and load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM  ctl.LoadLog WHERE  TableName = 'ucdm.Contract' AND InsertedRows>0  AND Status= 'SUCCESS')  
                    and not exists (select 1 from  
                    (select SA_ID, SeasonOfSignUp from ( 
                    SELECT   
                    SA.sa_id, CASE 
                        WHEN Month ( CASE WHEN SC1.EFFDT IS NOT NULL THEN CAST(SC1.[EFFDT] AS DATE) ELSE SACON.[START_DT] END ) in (12,1,2) THEN  'Winter' 
                        WHEN Month ( CASE WHEN SC1.EFFDT IS NOT NULL THEN CAST(SC1.[EFFDT] AS DATE) ELSE SACON.[START_DT] END ) in (3,4,5) THEN  'Spring' 
                        WHEN Month ( CASE WHEN SC1.EFFDT IS NOT NULL THEN CAST(SC1.[EFFDT] AS DATE) ELSE SACON.[START_DT] END ) in (6,7,8) THEN  'Summer' 
                        WHEN Month ( CASE WHEN SC1.EFFDT IS NOT NULL THEN CAST(SC1.[EFFDT] AS DATE) ELSE SACON.[START_DT] END ) in (9,10,11) THEN  'Autumn' 
                    END as SeasonOfSignUp  
                    FROM stg.[CI_SA] SA LEFT JOIN stg.[CI_SA_CHAR] SC1 ON SA.[SA_ID] = SC1.[SA_ID] AND SC1.[CHAR_TYPE_CD] = 'CONTPERD'  
                    AND SC1.EFFDT = (SELECT MAX(EFFDT) FROM stg.[CI_SA_CHAR] SC1a WHERE sa.[SA_ID] = SC1a.[SA_ID]  
                    AND SC1a.[CHAR_TYPE_CD] = 'CONTPERD' )         
                                LEFT JOIN           ( SELECT sa_id, MAX(start_dt) AS start_dt, MAX(end_dt)    AS end_dt  
                    FROM stg.ci_sa_conterm WHERE bf_cd IN ('AFDBDOMR', 'DFDBDOMR', 'DDDBDOMR', 'DDDMDOMR', 'OCDBDOMR') GROUP BY  sa_id )   sacon  
                    ON         sacon.sa_id = sa.sa_id )  A) B 
                                where 'ED_' + B.SA_ID = c.ServiceAgreementID);'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate cash back amount in ucdm contract table",
)
def test_cashbackamount_in_ucdm_contract_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate cash back amount in ucdm contract table')
def validate_cashbackamount_in_ucdm_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.Contract")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from UCDM.[Contract] c where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM      
                    ctl.LoadLog WHERE        TableName = 'ucdm.Contract' AND InsertedRows>0  AND     Status= 'SUCCESS')  and currentflag=1
                    and not exists (select 1 from (
                    SELECT SA.SA_ID, isnull(cashbackAmount, 0) as cashbackAmount FROM stg.[CI_SA] SA LEFT JOIN(SELECT SUM(ADJ_AMT) AS cashbackAmount, [SA_ID] FROM stg.[CI_ADJ] AS A WHERE [ADJ_TYPE_CD] = 'CASHBACK'
                                                AND [ADJ_STATUS_FLG] = '50' AND [CRE_DT] = (SELECT MAX([CRE_DT]) FROM stg.[CI_ADJ] AS AJ  WHERE A.[sa_id] = AJ.[sa_id]
                    AND [ADJ_TYPE_CD] = 'CASHBACK' AND [ADJ_STATUS_FLG] = '50') GROUP BY [SA_ID]) AS ADJ ON RIGHT(sa.[SA_ID], 10) = ADJ.[SA_ID]) B
                    where 'ED_' + B.SA_ID = c.ServiceAgreementID and isnull(c.cashbackAmount, 0) = isnull(B.cashbackAmount, 0))'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate billing type in  ucdm Accountperson table",
)
def test_billing_type_in_ucdm_accountperson_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate billing type in  ucdm Accountperson table')
def validate_billing_type_in_ucdm_accountperson_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from UCDM.AccountPerson")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from  ucdm.AccountPerson uap where currentflag=1 and 
                    load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM    ctl.LoadLog WHERE  TableName = 'ucdm.AccountPerson' AND InsertedRows>0  AND  Status= 'SUCCESS')  
                    and not exists (select 1 from stg.CI_ACCT_PER sap  where  uap.personid='ED_' + sap.per_id and uap.accountid ='ED_' + sap.acct_id and uap.accreltypecd = sap.acct_rel_type_cd) ;'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to check If EnergyOnline Available",
)
def test_energyonline_available():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate If EnergyOnline Available')
def validate_energyonline_available(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.CI_ACCT_PER")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from    ucdm.AccountPerson uap
                    where
                    uap.load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM ctl.LoadLog WHERE      
                    TableName = 'ucdm.AccountPerson' AND InsertedRows>0  AND Status= 'SUCCESS')  and currentflag=1
                    and not exists
                    (select 1 from  stg.CI_ACCT_PER sap where
                      uap.personid='ED_' + sap.per_id and uap.accountid ='ED_' + sap.acct_id and
                      isnull(uap.accreltypecd, '') = isnull(sap.acct_rel_type_cd, '')
                    and isnull(uap.BillRteTypeCd, '') = isnull(sap.BILL_RTE_TYPE_CD, '')
                    )'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to check If EnergyOnlineID Available",
)
def test_energyonlineid_available():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate If EnergyOnlineID Available')
def validate_energyonlineid_available(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.CI_PER")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ucdm.Person p  where currentflag=1 and 
				load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 
				FROM ctl.LoadLog WHERE TableName = 'ucdm.Person' AND InsertedRows>0  AND InsertedRows>0 
				AND  Status='SUCCESS')  and not exists
				(select 1 FROM stg.CI_PER ci_per  
				INNER JOIN    stg.ci_acct_per ci_acct_per ON ci_per.per_id = ci_acct_per.per_id
				INNER JOIN    stg.ci_acct ci_acct ON ci_acct_per.acct_id = ci_acct.acct_id
				LEFT JOIN stg.[CI_PER_ID] PID2 ON PID2.PER_ID = CI_PER.PER_ID and PID2.ID_TYPE_CD = 'WEB'
				 where   'ED_' + ci_per.per_id = p.PersonID 
				and (CASE WHEN PID2.per_id_nbr is null then 'N' ELSE 'Y' END)
				= p.EnergyOnlineID  and ci_acct.[cis_division] IN ('ROI'))'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg.ci_sa table",
)
def test_record_count_in_stg_ci_sa_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data in stg.ci_sa table')
def validate_records_in_stg_ci_sa_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_sa")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_sa where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_sa' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in ucdm person table",
)
def test_count_in_ucdm_person_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in ucdm person table')
def validate_records_in_ucdm_person_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Person")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ucdm.Person where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'ucdm.Person' AND InsertedRows>0 AND Status= 'SUCCESS') ;'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg.ci_per table",
)
def test_record_count_in_stg_ci_per_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data in stg.ci_per table')
def validate_records_in_stg_ci_per_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_per")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_per where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_per' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg.ci_bseg table",
)
def test_record_count_in_stg_ci_bseg_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate  data in stg.ci_bseg table')
def validate_records_in_stg_ci_bseg_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_bseg")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_bseg where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_bseg' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in ucdm contract table",
)
def test_count_in_ucdm_contract_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data in ucdm contract table')
def validate_records_in_ucdm_contract_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Contract")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ucdm.Contract where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'ucdm.Contract' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg.ci_cc table",
)
def test_record_count_in_stg_ci_cc_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data in stg.ci_cc table')
def validate_records_in_stg_ci_cc_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_cc")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_cc where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_cc' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg ci_per table",
)
def test_count_in_stg_ci_per_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data in stg.ci_per table')
def validate_records_in_stg_ci_per_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_per")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_per where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_per' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg.ci_prem table",
)
def test_record_count_in_stg_ci_prem_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data in stg.ci_prem table')
def validate_records_in_stg_ci_prem_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_prem")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_prem where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_prem' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg.ci_case table",
)
def test_record_count_in_stg_ci_case_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data in stg.ci_case table')
def validate_records_in_stg_ci_case_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_case")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_case where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_case' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg.ci_bill table",
)
def test_record_count_in_stg_ci_bill_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data in stg.ci_bill table')
def validate_records_in_stg_ci_bill_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_bill")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_bill where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_bill' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg.ci_acct_per table",
)
def test_record_count_in_stg_ci_acct_per_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate records in stg.ci_acct_per table')
def validate_records_in_stg_ci_acct_per_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_acct_per")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_acct_per where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_acct_per' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data in stg.ci_acct table",
)
def test_record_count_in_stg_ci_acct_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data in stg.ci_acct table')
def validate_records_in_stg_ci_acct_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_acct")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_acct where load_date_time >=(SELECT 
					ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') FROM 
                   ctl.loadlog WHERE TableName = 'stg.ci_acct' AND InsertedRows>0 AND Status= 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate Level Pay Query",
)
def test_level_pay_query():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate Level Pay Query')
def validate_level_pay_query(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.CI_CC")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( SELECT cc_id, case when count( CC_ID ) >0 then  'Y' else 'N' end HasNBBQuery  
                    FROM stg.CI_CC ci_cc where CC_CL_CD IN ('DD','PAYS') and CC_TYPE_CD IN ('DDQUERY','QUERY')   
                    and ci_cc.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM	ctl.LoadLog WHERE	TableName = 'ucdm.CustomerContactsComplaintsSummary'  
                    AND	 Status= 'SUCCESS') group by ci_cc.cc_id ) A where  not exists (select 1 from  [ucdm].[CustomerContactsComplaintsSummary] ucc  
                    where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM	ctl.LoadLog WHERE	TableName = 'ucdm.CustomerContactsComplaintsSummary'  
                    AND	 Status= 'SUCCESS') and 'ED_' + A.cc_id = ucc.personid);'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate meter read inquiry",
)
def test_meter_read_inquiry():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate meter read inquiry')
def validate_meter_read_inquiry(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.CI_CC")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( SELECT cc_id, case when count( CC_ID ) >0 then  'Y' else 'N' end HasNBBQuery  
                    FROM stg.CI_CC ci_cc where CC_CL_CD IN  ('MRD', 'SMTR') AND CC_TYPE_CD IN  ('ENQ', 'SMTRENQ')   
                    and ci_cc.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM	ctl.LoadLog WHERE	TableName = 'ucdm.CustomerContactsComplaintsSummary'  
                    AND	 Status= 'SUCCESS') group by ci_cc.cc_id ) A where  not exists (select 1 from  [ucdm].[CustomerContactsComplaintsSummary] ucc  
                    where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM	ctl.LoadLog WHERE	TableName = 'ucdm.CustomerContactsComplaintsSummary'  
                    AND	 Status= 'SUCCESS') and 'ED_' + A.cc_id = ucc.personid);'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate meter read dispute",
)
def test_meter_read_dispute():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate meter read dispute')
def validate_meter_read_dispute(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.CI_CC")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( SELECT cc_id, case when count( CC_ID ) >0 then  'Y' else 'N' end HasNBBQuery  
                    FROM stg.CI_CC ci_cc where CC_CL_CD = 'MRD' AND CC_TYPE_CD = 'DISPUTE'   
                    and ci_cc.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM	ctl.LoadLog WHERE	TableName = 'ucdm.CustomerContactsComplaintsSummary'  
                    AND	 Status= 'SUCCESS') group by ci_cc.cc_id ) A where  not exists (select 1 from  [ucdm].[CustomerContactsComplaintsSummary] ucc  
                    where load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM	ctl.LoadLog WHERE	TableName = 'ucdm.CustomerContactsComplaintsSummary'  
                    AND	 Status= 'SUCCESS') and 'ED_' + A.cc_id = ucc.personid) ;'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate open complaints variable",
)
def test_open_complaints_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate open complaints variable')
def validate_open_complaints_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_case")
    data = cursor.fetchone()
    cursor.execute("select count(*) from ucdm.CustomerContactsComplaintsSummary")
    ucdm_data = cursor.fetchone()
    #print(data)
    if data[0] != 0 and ucdm_data[0] != 0:
        query = '''select count(*) from (
                    select * from
                    (select    case_id, p.personid,
                    case when ci.per_id is null then 'N' else 'Y' end  OpenComplaints
                    from ucdm.person p left join  (select distinct  per_id, case_id, case_status, case_type_cd from  stg.ci_case where  case_status = 'Open'
                    and    case_type_cd in (SELECT l.case_type_cd FROM stg.ci_case_type_l l
                                            WHERE (UPPER(l.descr) LIKE '%COMPLAINT%' OR case_type_cd LIKE '%ARCOM%')
                                            AND EXISTS (SELECT l.[case_type_cd]))
                    ) ci on p.personid= 'ED_' + ci.per_id
                     where p.currentflag=1
                    ) ci where  not exists
                    (select 1 from [ucdm].[CustomerContactsComplaintsSummary] cc where cc.currentflag=1 and  cc.PersonID =  ci.personid
                    and ci.OpenComplaints = cc.OpenComplaints))  A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate average consumption electricity variable",
)
def test_average_consumption_elec_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate average consumption electricity variable')
def validate_average_consumption_elec_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.BillSegment")
    data = cursor.fetchone()   
    cursor.execute("select count(*) from ucdm.satransactions")
    ucdm_data = cursor.fetchone()
    #print(data)
    if data[0] != 0 and ucdm_data[0] != 0:
        query = ''' select count(*)  from ucdm.satransactions st where st.currentflag = 1 and
                    not exists (select 1 from  (SELECT c.ServiceAgreementID,
                        DATEDIFF(D,MIN(b.StartDate), MAX(b.EndDate)) AS BilledDays,
                        SUM(isnull(b.PeakUsage, 0) + isnull(b.HeatingUsage, 0) + isnull(b.DayUsage, 0) + isnull(b.StandardUsage, 0) +
                        isnull(b.NightUsage, 0) + isnull(b.NightUsageHighUsage, 0) + isnull(b.DayUsageHighUsage, 0)) AS TotalUnits
                    FROM
                    ucdm.[Contract] c left join
                    ucdm.BillSegment b on c.ServiceAgreementID  = b.ServiceAgreementID
                    and b.currentflag = 1 and c.currentflag=1
                    GROUP BY c.ServiceAgreementID ) bs
                    where st.ServiceAgreementID = bs.ServiceAgreementID
                    and cast(case when  isnull(BilledDays, 0)=0 then 0 else (TotalUnits/BilledDays) * 365/12 end
                    as numeric( 38, 6)) =
                    cast(isnull(ElecAvgMonthlyConsumption, 0.0)  as numeric( 38, 6)))'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

# @pytest.mark.reconciliation_cc_and_b
# @scenario(
#     "../../features/cc&b_variables.feature",
#     "Test to validate last bill amount variance variable",
# )
# def test_last_bill_amount_variance():
#     pass

# @given('I have Database connection details')
# def database_connection_details(kv):
#     pass

# @when('I was able to connect to database')
# def database_connection(sql_connection):
#     pass

# @then('I can validate last bill amount variance variable')
# def validate_last_bill_amount_variance(sql_connection):
#     cursor = sql_connection.cursor()
#     cursor.execute("select count(*) from stg.CI_CC")
#     data = cursor.fetchone()
#     print(data)
#     if data[0] != 0:
#         query = ''';with billing_fttemp as (SELECT	*   
# 		            FROM( SELECT bill_id,  
# 	                ft_type,  
# 								correction_sw,  
# 								SUM(tot_amt) AS amount 
# 					FROM( 
# 							SELECT	CASE 
# 												 WHEN ft.ft_type_flg IS NOT NULL THEN ft.bill_id 
# 												 ELSE ( 
# 														SELECT TOP(1)	bill_id  
# 														FROM			stg.ci_bseg bs  
# 														WHERE			bs.bill_id = ft.bill_id 
# 													) 
# 												 END AS BILL_ID,									 
# 											CASE 
# 												 WHEN ft.ft_type_flg IN ('PS', 'PX') THEN 'PAYMENT' 
# 												 WHEN ft.ft_type_flg IN ('BS', 'BX') THEN 'BILLING'   
# 												 WHEN ft.ft_type_flg IN ('AD', 'AX') AND ft.parent_id = 'CASHBACK' THEN 'CASHBACK' 
# 												 WHEN ft.ft_type_flg IN ('AD', 'AX') AND ft.parent_id = 'XREFAPR' THEN 'REFUND' 
# 												 WHEN ft.ft_type_flg IN ('AD', 'AX') AND ft.parent_id IN ('CMEROITC','CMGROITC') THEN 'TERMINATION' 
# 												 WHEN ft.ft_type_flg IN ('AD', 'AX') AND ft.parent_id = 'DD-REVRI' THEN 'DDRev' 
# 												 ELSE 'OTHER' 
# 											END AS ft_type,  
# 											correction_sw,  
# 											ft.tot_amt								 
# 									FROM	(select distinct * from  stg.ci_ft	 
# 									WHERE	cis_division IN ('ROI')	)  ft  
									
 
# 								) AS T  
# 					GROUP BY	bill_id,  
# 								ft_type,  
# 								correction_sw 
                        
#                                     ) AS tmp  
#                                     ) 
#                     select count(*) from   ucdm.Bill b where currentflag=1 and not exists  
#                     ( 
#                         select * from (  
# 					SELECT BillID, BillAmount,BillDate, 
#                     ROW_NUMBER() OVER (ORDER BY EffectiveEnd) AS BillSK, LEAD(BillAmount,1,0) OVER (Partition BY AccountID Order BY BillDate Desc) LBillAmount, 
#                     AccountID, cast((BillAmount - LEAD(BillAmount,1,0) OVER (Partition BY AccountID Order BY BillDate Desc))/CASE WHEN LEAD(BillAmount,1,0) OVER (Partition BY AccountID Order BY BillDate Desc) = 0 THEN 1 ELSE LEAD(BillAmount,1,0) OVER (Partition BY AccountID Order BY BillDate Desc) END as numeric(16, 2)) AS LastBillAmountVariance, 
#                     EffectiveStart, EffectiveEnd, rno 
#                     FROM (  
#                     SELECT row_number() over (partition by ci_bill.bill_id order by ci_bill.cre_dttm desc) rno,  
#                     ci_bill.bill_id AS BillID, ci_bill.acct_id AS AccountID, bseg.cre_dttm AS BillDate,  
#                     ISNULL(ft1.amount, 0) + ISNULL(ft2.amount, 0) + ISNULL(ft3.amount, 0) + ISNULL(ft4.amount, 0) + ISNULL(ft5.amount, 0) AS BillAmount, 
#                     ci_bill.src_commit_time  AS EffectiveStart, '9999-12-31 00:00:00.0000000'  AS EffectiveEnd 
#                     FROM stg.ci_bill   ci_bill  
# 						INNER JOIN	stg.ci_acct												ci_acct 
# 				ON			 ci_bill.acct_id = ci_acct.acct_id and ci_acct.[cis_division] IN ('ROI') 
#                     LEFT JOIN stg.ci_bseg bseg  ON ci_bill.bill_id = bseg.bill_id 
#                     LEFT JOIN billing_fttemp ft1 ON ft1.bill_id = bseg.bill_id AND ft1.ft_type = 'BILLING'  
#                     AND ft1.correction_sw = 'N' LEFT JOIN billing_fttemp ft2  
#                     ON ft2.bill_id = bseg.bill_id AND ft2.ft_type = 'OTHER'  AND ft2.correction_sw = 'N' 
#                     LEFT JOIN billing_fttemp ft3 ON ft3.bill_id = bseg.bill_id AND ft3.ft_type = 'CASHBACK'  
#                     AND ft3.correction_sw = 'N' 
#                     LEFT JOIN billing_fttemp ft4  
#                     ON ft4.bill_id = bseg.bill_id AND ft4.ft_type = 'TERMINATION' AND ft4.correction_sw = 'N' 
#                     LEFT JOIN billing_fttemp ft5  
#                     ON ft5.bill_id = bseg.bill_id AND ft5.ft_type = 'REFUND' AND ft5.correction_sw = 'N' 
#                   ) l  
# 					) tq  
# 				where b.BillID = tq.BillID  
#                     and b.LastBillAmountVariance = tq.LastBillAmountVariance)'''
#         cursor.execute(query)
#         row = cursor.fetchone()
#         assert row[0] == 0 
#     else: 
#         assert False    
#     cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate tariff(only for electricity) variable",
)
def test_tariff():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate tariff(only for electricity) variable')
def validate_tariff(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.CI_CC")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from  ucdm.ServiceAgreement sa 
				where currentflag=1 and  not exists ( 
				select 1  
				FROM stg.ci_sa ci_sa LEFT JOIN stg.ci_sa_rs_hist rsh  
				ON ci_sa.sa_id = rsh.sa_id  
				AND rsh.effdt = ( SELECT MAX(effdt)  FROM stg.ci_sa_rs_hist rsha  
				WHERE ci_sa.sa_id = rsha.sa_id) 
				JOIN stg.ci_rs_l rsl  ON rsh.rs_cd = rsl.rs_cd   
				where  sa.ServiceAgreementID = 'ED_' + ci_sa.sa_id  and  ci_sa.[cis_division] IN ('ROI') 
				and rsl.descr = sa.TariffName)'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate Have you hit threshold/Cap ( Day/Night and Night Storage) variable",
)
def test_have_you_hit_threshold_or_cap_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate Have you hit threshold/Cap ( Day/Night and Night Storage) variable')
def validate_have_you_hit_threshold_or_cap_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.CI_CC")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''declare @Prefix varchar(5) = 'ED_'
;with cteci_bseg_calc_ln_temp
AS
(SELECT bseg_id,
char_type_cd,
char_val,
dst_id,
uom_cd,
CASE
WHEN uom_cd = 'KWH' AND tou_cd IS NULL THEN '01' ELSE tou_cd
END AS tou_cd,
CASE
WHEN CHARINDEX(' at', descr_on_bill) > 0 AND (CHARINDEX(' at', descr_on_bill) < CHARINDEX('PER UNIT', descr_on_bill)) AND currency_cd = 'EUR' THEN RTRIM(LTRIM(SUBSTRING(descr_on_bill, CHARINDEX(' at', descr_on_bill)+5, CHARINDEX('PER UNIT', descr_on_bill) - CHARINDEX(' at', descr_on_bill)-6)))
WHEN CHARINDEX('£', descr_on_bill) > 0 AND (CHARINDEX('£', descr_on_bill) < CHARINDEX('PER UNIT', descr_on_bill)) AND currency_cd = 'UK' THEN RTRIM(LTRIM(SUBSTRING(descr_on_bill, CHARINDEX('£', descr_on_bill)+1, CHARINDEX('PER UNIT', descr_on_bill) - CHARINDEX('£', descr_on_bill)-1)))
WHEN CHARINDEX(' at', descr_on_bill) > 0 AND (CHARINDEX(' at', descr_on_bill) < CHARINDEX('PER UNIT', descr_on_bill)) AND currency_cd = 'UK' THEN RTRIM(LTRIM(SUBSTRING(descr_on_bill, CHARINDEX(' at', descr_on_bill)+4, CHARINDEX('PER UNIT', descr_on_bill) - CHARINDEX(' at', descr_on_bill)-6)))
WHEN CHARINDEX(' at', descr_on_bill) <= 0 OR (CHARINDEX(' at', descr_on_bill) >= CHARINDEX('PER UNIT', descr_on_bill)) THEN ''
ELSE 'String Error'
END AS unitprice,
CASE
WHEN CHARINDEX(' AT', descr_on_bill) > 0 AND (CHARINDEX(' AT', descr_on_bill) < CHARINDEX('%', descr_on_bill)) AND descr_on_bill NOT LIKE '%Reduced%' THEN RTRIM(LTRIM(SUBSTRING(descr_on_bill, CHARINDEX(' AT', descr_on_bill)+4, CHARINDEX('%', descr_on_bill) - CHARINDEX(' AT', descr_on_bill)+3)))
WHEN CHARINDEX(' AT', descr_on_bill) <= 0 OR (CHARINDEX(' AT', descr_on_bill) >= CHARINDEX('%', descr_on_bill)) OR descr_on_bill LIKE '%Reduced%' THEN ''
ELSE 'String Error'
END AS Disc,
rc_seq,
prt_sw,
app_in_summ_sw,
calc_amt AS ln_amt,
base_amt,
sqi_cd,
bill_sq,
REPLACE(descr_on_bill,'¤','€') AS calc_ln_descr
FROM stg.ci_bseg_calc_ln
WHERE dst_id IN ('AP-E-PSOR', 'AP-E-VATRI', 'AP-G-CRBTX', 'E-E-AD', 'E-E-CRD', 'E-E-DDDR', 'E-E-DFD', 'E-E-MDDDR', 'E-E-OCD', 'E-G-CRD', 'E-G-DDDR','E-G-DFD', 'E-G-MDDDR', 'E-G-OCD', 'R-E-DOMR', 'R-G-DOMR','E-E-ADY1','E-G-ADY1','E-E-ADY2','E-G-ADY2','E-G-AD')
AND bseg_id IS NOT NULL
AND bseg_id <> ' '
AND (prt_sw = 'Y' OR app_in_summ_sw = 'Y')
AND currency_cd = 'EUR'
),
cteBillSeg as (
SELECT BillSegmentID, BillID, ServiceAgreementID, StandardGasUsage, StandardUsage,
DayUsage, DayUsageHighUsage,NightUsage,NightUsageHighUsage,HeatingUsage,PeakUsage,
StartDate,EndDate,HighUsageThreshold
FROM
(
SELECT DISTINCT CONCAT(@Prefix, bseg.bseg_id) AS BillSegmentID,
CONCAT(@Prefix, bseg.bill_id) AS BillID,
CONCAT(@Prefix, bseg.sa_id) AS ServiceAgreementID,cl2.bill_sq AS StandardGasUsage,
cl4.bill_sq AS StandardUsage,cl6.bill_sq AS DayUsage,cl7.bill_sq AS DayUsageHighUsage,
cl8.bill_sq AS NightUsage,cl9.bill_sq AS NightUsageHighUsage,cl10.bill_sq AS HeatingUsage,
cl11.bill_sq AS PeakUsage,bseg.start_dt AS StartDate,bseg.end_dt AS EndDate,
CASE
WHEN (cl7.bill_sq > 0 OR cl9.bill_sq > 0) THEN 1
ELSE 0
END AS HighUsageThreshold,
bseg.src_commit_time AS EffectiveStart,
'9999-12-31 00:00:00.0000000' AS EffectiveEnd,
bseg.load_date_time,
bseg.version
FROM stg.ci_bseg bseg INNER JOIN stg.ci_sa sa ON bseg.sa_id = sa.sa_id
LEFT JOIN (
SELECT SUM(CASE WHEN ISNUMERIC(unitprice) = 1 THEN CONVERT(NUMERIC(18,4), unitprice) ELSE NULL END) AS unitprice,
SUM(bill_sq) AS bill_sq,
SUM(ln_amt) AS ln_amt,
bseg_id
FROM cteci_bseg_calc_ln_temp bct
WHERE bct.dst_id IN ('R-G-DOMR') AND bct.uom_cd = 'KWH'
AND bct.tou_cd = '01' AND bct.calc_ln_descr NOT LIKE '%HIGH USAGE%'
GROUP BY bseg_id
) cl2
ON cl2.bseg_id = bseg.bseg_id
LEFT JOIN (
SELECT SUM(CASE WHEN ISNUMERIC(unitprice) = 1 THEN CONVERT(NUMERIC(18,4), unitprice) ELSE NULL END) AS unitprice,
SUM(bill_sq) AS bill_sq,SUM(ln_amt) AS ln_amt,bseg_id
FROM cteci_bseg_calc_ln_temp bct
WHERE bct.dst_id IN ('R-E-DOMR') AND bct.uom_cd = 'KWH' AND bct.tou_cd = '01'
AND bct.calc_ln_descr NOT LIKE '%HIGH USAGE%'
GROUP BY bseg_id
) cl4
ON cl4.bseg_id = bseg.bseg_id
LEFT JOIN (
SELECT SUM(CASE WHEN ISNUMERIC(unitprice) = 1 THEN CONVERT(NUMERIC(18,4), unitprice) ELSE NULL END) AS unitprice,
SUM(bill_sq) AS bill_sq,
SUM(ln_amt) AS ln_amt,
bseg_id
FROM cteci_bseg_calc_ln_temp bct
WHERE bct.dst_id IN ('R-E-DOMR')
AND bct.uom_cd = 'KWH'
AND bct.tou_cd IN ('02','78','01D')
AND bct.calc_ln_descr NOT LIKE '%HIGH USAGE%'
GROUP BY bseg_id
) cl6
ON cl6.bseg_id = bseg.bseg_id
LEFT JOIN (
SELECT SUM(CASE WHEN ISNUMERIC(unitprice) = 1 THEN CONVERT(NUMERIC(18,4), unitprice) ELSE NULL END) AS unitprice,
SUM(bill_sq) AS bill_sq,SUM(ln_amt) AS ln_amt,bseg_id
FROM cteci_bseg_calc_ln_temp bct WHERE bct.dst_id IN ('R-E-DOMR')
AND bct.uom_cd = 'KWH'
AND bct.tou_cd IN ('02','78','01D')
AND bct.calc_ln_descr LIKE '%HIGH USAGE%'
GROUP BY bseg_id
) cl7
ON cl7.bseg_id = bseg.bseg_id
LEFT JOIN (
SELECT SUM(CASE WHEN ISNUMERIC(unitprice) = 1 THEN CONVERT(NUMERIC(18,4), unitprice) ELSE NULL END) AS unitprice,
SUM(bill_sq) AS bill_sq,
SUM(ln_amt) AS ln_amt,
bseg_id
FROM cteci_bseg_calc_ln_temp bct
WHERE bct.dst_id IN ('R-E-DOMR')
AND bct.uom_cd = 'KWH'
AND bct.tou_cd IN ('03','79','01N')
AND bct.calc_ln_descr NOT LIKE '%HIGH USAGE%'
GROUP BY bseg_id
) cl8
ON cl8.bseg_id = bseg.bseg_id
LEFT JOIN (
SELECT SUM(CASE WHEN ISNUMERIC(unitprice) = 1 THEN CONVERT(NUMERIC(18,4), unitprice) ELSE NULL END) AS unitprice,
SUM(bill_sq) AS bill_sq,
SUM(ln_amt) AS ln_amt,
bseg_id
FROM cteci_bseg_calc_ln_temp bct
WHERE bct.dst_id IN ('R-E-DOMR')
AND bct.uom_cd = 'KWH'
AND bct.tou_cd IN ('03','79','01N')
AND bct.calc_ln_descr LIKE '%HIGH USAGE%'
GROUP BY bseg_id
) cl9
ON cl9.bseg_id = bseg.bseg_id
LEFT JOIN (
SELECT SUM(CASE WHEN ISNUMERIC(unitprice) = 1 THEN CONVERT(NUMERIC(18,4), unitprice) 
ELSE NULL END) AS unitprice,SUM(bill_sq) AS bill_sq,SUM(ln_amt) AS ln_amt,
bseg_id
FROM cteci_bseg_calc_ln_temp bct
WHERE bct.dst_id IN ('R-E-DOMR')
AND bct.uom_cd = 'KWH'
AND bct.tou_cd = '04'
AND bct.calc_ln_descr NOT LIKE '%HIGH USAGE%'
GROUP BY bseg_id
) cl10
ON cl10.bseg_id = bseg.bseg_id
LEFT JOIN (
SELECT SUM(CASE WHEN ISNUMERIC(unitprice) = 1 THEN CONVERT(NUMERIC(18,4), unitprice) ELSE NULL END) AS unitprice,
SUM(bill_sq) AS bill_sq,
SUM(ln_amt) AS ln_amt,
bseg_id
FROM cteci_bseg_calc_ln_temp bct
WHERE bct.dst_id IN ('R-E-DOMR')
AND bct.uom_cd = 'KWH'
AND bct.tou_cd IN ('80','01P')
AND bct.calc_ln_descr NOT LIKE '%HIGH USAGE%'
GROUP BY bseg_id
) cl11
ON cl11.bseg_id = bseg.bseg_id
WHERE sa.[cis_division] IN ('ROI')
) l
)
select count(*) from
[ucdm].[BillSegment]  bs
where not exists (select 1 from  cteBillSeg bsegq where 
    bs.BillSegmentID = bsegq.BillSegmentID and  bs.billid = bsegq.billid 
	and isnull(bs.HighUsageThreshold, 0) = isnull(bsegq.HighUsageThreshold, 0) 
	and isnull(bs.DayUsageHighUsage, 0) = isnull(bsegq.DayUsageHighUsage, 0) and 
	isnull(bs.NightUsageHighUsage, 0) = isnull(bsegq.NightUsageHighUsage, 0))  '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

# @pytest.mark.reconciliation_cc_and_b
# @scenario(
#     "../../features/cc&b_variables.feature",
#     "Test to validate Is Discount offered is equal to discount availed variable",
# )
# def test_discount_offered_is_equal_to_discount_availed():
#     pass

# @given('I have Database connection details')
# def database_connection_details(kv):
#     pass

# @when('I was able to connect to database')
# def database_connection(sql_connection):
#     pass

# @then('I can validate Is Discount offered is equal to discount availed variable')
# def validate_discount_offered_is_equal_to_discount_availed(sql_connection):
#     cursor = sql_connection.cursor()
#     cursor.execute("select count(*) from stg.CI_CC")
#     data = cursor.fetchone()
#     print(data)
#     if data[0] != 0:
#         query = ''' ;with ci_bseg_calc_ln_temp111 as 
# 		(SELECT	bseg_id, char_type_cd, char_val, dst_id, uom_cd, 
# 				CASE  
# 					WHEN uom_cd = 'KWH' AND LEN(RTRIM(LTRIM(tou_cd))) = 0 THEN '01' ELSE tou_cd  
# 				END	AS tou_cd, 
# 				CASE  
# 					WHEN CHARINDEX(' AT', descr_on_bill) > 0 AND (CHARINDEX(' AT', descr_on_bill) < CHARINDEX('%', descr_on_bill)) AND descr_on_bill NOT LIKE '%Reduced%'	THEN RTRIM(LTRIM(SUBSTRING(descr_on_bill, CHARINDEX(' AT', descr_on_bill)+4, CHARINDEX('%', descr_on_bill) - CHARINDEX(' AT', descr_on_bill)+3)))  
# 					WHEN CHARINDEX(' AT', descr_on_bill) <= 0 OR (CHARINDEX(' AT', descr_on_bill) >= CHARINDEX('%', descr_on_bill)) OR descr_on_bill LIKE '%Reduced%'		THEN '' 
# 					ELSE 'String Error' 
# 				END	AS disc, 
# 				rc_seq, prt_sw, app_in_summ_sw, calc_amt AS ln_amt,  
# 				base_amt, sqi_cd, bill_sq, REPLACE(descr_on_bill,'¤','€') AS calc_ln_descr 
# 		FROM	stg.ci_bseg_calc_ln 
# 		WHERE	dst_id IN ('AP-E-PSOR', 'AP-E-VATRI', 'AP-G-CRBTX', 'E-E-AD', 'E-E-CRD', 'E-E-DDDR', 'E-E-DFD', 'E-E-MDDDR', 'E-E-OCD', 'E-G-CRD', 'E-G-DDDR','E-G-DFD', 'E-G-MDDDR', 'E-G-OCD', 'R-E-DOMR', 'R-G-DOMR','E-E-ADY1','E-G-ADY1','E-E-ADY2','E-G-ADY2','E-G-AD')  
# 		AND		bseg_id IS NOT NULL  
# 		AND		bseg_id <> ' ' AND		 (prt_sw = 'Y' OR app_in_summ_sw = 'Y') 
# 		AND		currency_cd = 'EUR'), 
# 		cm_discount_achieved111 as 
# 		(SELECT		DISTINCT	bsc.bseg_id	AS bseg_id, 
# 								bs.sa_id AS sa_id, 
# 								MAX(bs.cre_dttm) AS cre_dttm, 
# 								ROUND(SUM(bsc.ln_amt),2) AS ln_amt, 
# 								bsc.base_amt AS base_amt, 
# 								SUM(CAST(REPLACE(bsc.disc, '%', '') AS INT)) AS disc_pct 
# 		FROM					ci_bseg_calc_ln_temp111		bsc  
# 		LEFT JOIN	stg.ci_bseg	bs ON	bs.bseg_id = bsc.bseg_id 
# 		LEFT JOIN stg.ci_sa	sa ON	bs.sa_id = sa.sa_id 
# 		WHERE	bsc.dst_id IN ('E-E-DDDR', 'E-E-MDDDR', 'E-G-MDDR', 'E-E-OCD', 'E-G-OCD', 'E-E-DFD', 'E-G-DFD', 'E_E_ADY1', 'E-G-ADY2', 'E-E-AD', 'E-G-AD') 
# 		AND	sa.cis_division IN ('ROI') AND	bs.sa_id IS NOT NULL 
# 		AND	bsc.disc <> '' AND	bsc.char_val IS NULL  
# 		GROUP BY bsc.bseg_id, bs.sa_id, bsc.base_amt) 
# 		select count(*) from ucdm.Contract c  
# 			where    currentflag=1 and not exists  
# 		(SELECT	1 
# 				FROM ( SELECT	 
# 				ServiceAgreementID,	ContractStartDate,				 
# 				DiscountOffered,	DiscountApplied, DiscountAchieved,		CashbackAmount,				 
# 				CASE 
# 					WHEN	DiscountOffered = DiscountAchieved THEN 'Equal' 
# 					WHEN	DiscountOffered > DiscountAchieved THEN 'Achieved Lower' 
# 					ELSE											'Achieved Higher' 
# 				END		AS DiscOfferedEqualDiscAchieved	 
# 		FROM ( SELECT	sa.sa_id																																		AS ServiceAgreementID, 
# 							CASE  
# 								WHEN sc1.effdt IS NOT NULL THEN CAST(sc1.effdt AS DATE) 
# 								ELSE sacon.start_dt END	AS ContractStartDate, 
# 							ISNULL(sct1.val, 0) + ISNULL(sct2.val, 0) +	ISNULL(sct4.val, 0) + ISNULL(sct3.val, 0) + ISNULL(sct5.AcquisitionDisc, 0)		AS DiscountOffered, 
# 							CASE  
# 								WHEN ISNULL(sct1.val, 0) + ISNULL(sct2.val, 0) + ISNULL(sct4.val, 0) + ISNULL(sct3.val, 0) + ISNULL(sct5.AcquisitionDisc, 0) <> 0 THEN 'Y' 
# 								ELSE 'N' END		AS DiscountApplied,  
# 							ISNULL(da.disc_pct, 0)	AS DiscountAchieved, 
# 							adj.CashBackAmount  
# 				FROM	(select sa_id, acct_id, end_dt, cis_division from	stg.ci_sa ) sa 
# 				LEFT JOIN	( SELECT DISTINCT	sa2.acct_id, sa2.end_dt,  
# 									MAX(start_dt)	AS start_dt  
# 								FROM	stg.ci_sa	sa2 JOIN	stg.ci_sa_type	sat 
# 								ON	sat.sa_type_cd = sa2.sa_type_cd                       
# 								WHERE	sa2.sa_status_flg	IN ('20','30')  
# 								AND	sat.svc_type_cd	= 'N' 
# 								GROUP BY	sa2.acct_id, sa2.end_dt, sa2.start_dt 
# 							) nbb	 
# 				ON nbb.acct_id = sa.acct_id LEFT JOIN	stg.ci_sa_char	sc1  
# 				ON	sa.sa_id = sc1.sa_id AND sc1.char_type_cd = 'CONTPERD'  
# 				AND	sc1.effdt = ( SELECT	MAX(effdt) FROM	stg.ci_sa_char	sc1a  
# 										WHERE	sa.sa_id = sc1a.sa_id  
# 										AND		sc1a.char_type_cd = 'CONTPERD' 
# 										) 
# 				LEFT JOIN	stg.ci_sa_conterm	sct1  
# 				ON			 sa.sa_id = sct1.sa_id  
# 				AND			 sct1.bf_cd = 'AFDBDOMR'  
# 				AND			 sct1.start_dt = ( 
# 												 SELECT	MAX(start_dt)  
# 												 FROM	stg.ci_sa_conterm	sct1a  
# 												 WHERE	sa.sa_id = sct1a.sa_id  
# 												 AND		sct1a.bf_cd = 'AFDBDOMR' 
# 												 ) 
# 				LEFT JOIN	stg.ci_sa_conterm	sct2  
# 				ON			 sa.sa_id = sct2.sa_id  
# 				AND			 sct2.bf_cd = 'DFDBDOMR'  
# 				AND			 sct2.start_dt = ( SELECT	MAX(start_dt)  
# 												 FROM	stg.ci_sa_conterm	sct2a  
# 												 WHERE	sa.sa_id = sct2a.sa_id  
# 												 AND		sct2a.bf_cd = 'DFDBDOMR' ) 
# 				LEFT JOIN	stg.ci_sa_conterm	sct3 ON	sa.sa_id = sct3.sa_id  
# 				AND			 sct3.bf_cd = 'OCDBDOMR'  
# 				AND			 sct3.start_dt = ( 
# 											SELECT	MAX(start_dt)  
# 											FROM	stg.ci_sa_conterm	sct3a  
# 											WHERE	sa.sa_id = sct3a.sa_id  
# 											AND		sct3a.bf_cd = 'OCDBDOMR') 
# 				LEFT JOIN	stg.ci_sa_conterm sct4 ON	sa.sa_id = sct4.sa_id  
# 		 		AND	sct4.bf_cd =	CASE 
# 										WHEN nbb.acct_id IS NOT NULL AND  
# 										(nbb.end_dt IS NULL OR nbb.end_dt > sa.end_dt) THEN 'DDDBDOMR'  
# 									ELSE 'DDDMDOMR' 
# 											END      
# 				AND	sct4.start_dt =	(SELECT	MAX(start_dt)	 
# 											FROM	stg.ci_sa_conterm sct4x  
# 											WHERE	sa.sa_id = sct4x.sa_id  
# 											AND		sct4x.bf_cd = CASE	 
# 												 WHEN nbb.acct_id IS NOT NULL AND (nbb.end_dt IS NULL OR nbb.end_dt > sa.end_dt) THEN 'DDDBDOMR'  
# 												 ELSE 'DDDMDOMR' 
# 											END 
# 											) 
# 				LEFT JOIN	( SELECT		sa_id, MAX(start_dt)AS start_dt,  
# 											SUM(val)	AS AcquisitionDisc 
# 								FROM		stg.ci_sa_conterm	scsa 
# 								WHERE		scsa.bf_cd LIKE 'AY%'  
# 								GROUP BY	sa_id 
# 							)	sct5 ON	RIGHT(sa.sa_id, 10) = sct5.sa_id 
# 				LEFT JOIN	cm_discount_achieved111	da  
# 				ON	da.sa_id = sa.sa_id 
# 				AND	da.cre_dttm = ( 
# 									SELECT	MAX(da1.cre_dttm)  
# 									FROM	cm_discount_achieved111	da1 
# 									WHERE	da.sa_id = da1.sa_id 
# 								) 
# 				LEFT JOIN	( SELECT	SUM(adj_amt) AS CashBackAmount, MAX(cre_dt)	AS cre_dt, sa_id 
# 								FROM	stg.ci_adj	AS A 
# 								WHERE	adj_type_cd = 'CASHBACK'  
# 								AND		adj_status_flg = '50' 
# 								GROUP BY sa_id ) AS adj 
# 				ON	RIGHT(sa.sa_id, 10) = adj.sa_id 
# 				LEFT JOIN	(SELECT		sa_id ,MAX(start_dt) AS start_dt  
# 								FROM		stg.ci_sa_conterm                                              
# 								WHERE		bf_cd IN ('AFDBDOMR', 'DFDBDOMR', 'DDDBDOMR', 'DDDMDOMR', 'OCDBDOMR')  
# 								GROUP BY	sa_id 
# 							)	sacon  
# 				ON			 sacon.sa_id = sa.sa_id  
# 				 and sa.[cis_division] IN ('ROI')  
# 			) l ) A  where A.ServiceAgreementID = c.ServiceAgreementID and  
# 				A.DiscOfferedEqualDiscAchieved = c.DiscOfferedEqualDiscAchieved)'''
#         cursor.execute(query)
#         row = cursor.fetchone()
#         assert row[0] == 0 
#     else: 
#         assert False    
#     cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate Average consumption for gas variable",
)
def test_average_consumption_gas():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate Average consumption for gas variable')
def validate_average_consumption_gas(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.SATransactions")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ucdm.SATransactions where GasAvgMonthlyConsumption is not null  
                    and load_date_time >=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM	ctl.LoadLog  
                    WHERE	TableName = 'ucdm.SATransactions' AND	Status= 'SUCCESS')'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate Average consumption for gas variable in ucdm",
)
def test_average_consumption_gas_case2():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate Average consumption for gas variable in ucdm')
def validate_average_consumption_gas_case2(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.BillSegment")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from (SELECT ServiceAgreementID, DATEDIFF(D,MIN(StartDate), MAX(EndDate))    AS BilledDays,
        SUM(StandardGasUsage) AS TotalUnits FROM ucdm.[BillSegment] b
        WHERE b.currentflag = 1   and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime
        FROM ctl.LoadLog WHERE    TableName = 'ucdm.billsegment' AND    Status= 'SUCCESS')
        GROUP BY    ServiceAgreementID ) bs'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate Level Pay (NBB) Amount Increase variable",
)
def test_level_pay_amount_increase():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate Level Pay (NBB) Amount Increase variable')
def validate_level_pay_amount_increase(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_sa")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT	count(*) FROM stg.ci_sa	SA INNER JOIN stg.ci_adj ADJ ON	SA.sa_id = ADJ.sa_id where ADJ.adj_amt  is not null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()


@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate NBBPCChange variable",
)
def test_nbbpc_change_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate NBBPCChange variable')
def validate_nbbpc_change_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.nbbreview")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM	ucdm.nbbreview where NBBPCChange  is not null  and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	                FROM ctl.LoadLog WHERE TableName = 'ucdm.nbbreview' AND	Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()


@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate NBBIncrease variable",
)
def test_nbb_increase_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate NBBIncrease variable')
def validate_nbb_increase_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.nbbreview")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM ucdm.nbbreview where NBBIncrease  is not null  and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	                FROM ctl.LoadLog WHERE	TableName = 'ucdm.nbbreview' AND Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()


@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate NBBDecrease variable",
)
def test_nbb_decrease_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate NBBDecrease variable')
def validate_nbb_decrease_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.nbbreview")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM	ucdm.nbbreview where NBBDecrease  is not null  and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	                FROM ctl.LoadLog WHERE	TableName = 'ucdm.nbbreview' AND	Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()


@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate DidNBBChangeAtReview variable",
)
def test_did_nbb_change_at_review_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate DidNBBChangeAtReview variable')
def validate_did_nbb_change_at_review_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.nbbreview")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM	  ucdm.nbbreview where DidNBBChangeAtReview   is not null  and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	               FROM ctl.LoadLog WHERE	TableName = 'ucdm.nbbreview' AND	Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate ElecMeterRead(MeterReadType) variable",
)
def test_ElecMeterRead_MeterReadType_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate ElecMeterRead(MeterReadType) variable')
def validate_ElecMeterRead_MeterReadType_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.[ci_reg_read]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT	count(*) FROM	stg.[ci_reg_read]	rr
		JOIN	(
				SELECT	[mtr_config_id]
					,	[read_dttm]
					,	[mr_id]
				  FROM	stg.[ci_mr]												
				 WHERE	[use_on_bill_sw] = 'Y'
				)	mr ON	rr.[mr_id] = mr.[mr_id]	where rr.read_type is not null 
				and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	               FROM ctl.LoadLog WHERE	TableName = 'stg.[ci_reg_read]' 
				   and InsertedRows>0 AND	Status= 'SUCCESS')'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate GasMeterRead(MeterReadType) variable",
)
def test_gasmeterread_meterreadtype_variable_stg():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate GasMeterRead(MeterReadType) variable')
def validate_gasmeterread_meterreadtype_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.[ci_reg_read]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT	count(*) FROM	stg.[ci_reg_read]	rr
		JOIN	(
				SELECT	[mtr_config_id]
					,	[read_dttm]
					,	[mr_id]
				  FROM	stg.[ci_mr]												
				 WHERE	[use_on_bill_sw] = 'Y'
				)	mr ON	rr.[mr_id] = mr.[mr_id]	where rr.read_type is not null 
				and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	               FROM ctl.LoadLog WHERE	TableName = 'stg.[ci_reg_read]' 
				   and InsertedRows>0 AND	Status= 'SUCCESS')'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate ElecMeterRead(MeterReadType values check) variable",
)
def test_elecmeterread_meterreadtype_values_check():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate ElecMeterRead(MeterReadType values check) variable')
def validate_elecmeterread_meterreadtype_values_check(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.ElecMeterRead")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT	count(*) FROM ucdm.ElecMeterRead where MeterReadType   is not null  and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	               FROM ctl.LoadLog WHERE	TableName = 'ucdm.ElecMeterRead' and InsertedRows>0 AND	Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate GasMeterRead(MeterReadType values check) variable in ucdm",
)
def test_gasmeterread_meterreadtype_values_check_in_ucdm():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate GasMeterRead(MeterReadType values check) variable in ucdm')
def validate_gasmeterread_meterreadtype_values_check_in_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.GasMeterRead")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' SELECT	count(*) FROM ucdm.GasMeterRead where MeterReadType   is  not null  
                    and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
                    FROM	ctl.LoadLog WHERE	TableName = 'ucdm.GasMeterRead' and InsertedRows>0 AND	Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate active bad debt variable",
)
def test_active_bad_debt_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate active bad debt variable')
def validate_active_bad_debt_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Debt")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM	ucdm.Debt where load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	               FROM ctl.LoadLog WHERE TableName = 'ucdm.Debt' AND	Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate active bad debt amount variable",
)
def test_active_bad_debt_amount():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate active bad debt amount variable')
def validate_elecmeterread_meterreadtype_values_check_in_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Debt")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM ucdm.Debt where load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	               FROM ctl.LoadLog WHERE TableName = 'ucdm.Debt' AND	Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate total number of times bad debt in ucdm variable",
)
def test_total_number_of_times_bad_debt_in_ucdm():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate total number of times bad debt in ucdm variable')
def validate_total_number_of_times_bad_debt_in_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Debt")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' SELECT	count(*) FROM ucdm.Debt where TotalTimesInDebt   is not null  and load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	                FROM ctl.LoadLog WHERE	TableName = 'ucdm.Debt' and InsertedRows>0 AND	Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate total bad debt amount variable",
)
def test_total_bad_debt_amount_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate total bad debt amount variable')
def validate_total_bad_debt_amount_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.Debt")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT	count(*) FROM ucdm.Debt where load_date_time>=(SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime  
	               FROM	ctl.LoadLog WHERE	TableName = 'ucdm.Debt' and InsertedRows>0 AND	Status= 'SUCCESS') and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate active bad debt variable",
)
def test_active_bad_debt_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate active bad debt variable')
def validate_active_bad_debt_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.CI_COLL_PROC")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from  ( 
                    select CASE WHEN cp.bad_debt IS NULL THEN 'None' ELSE cp.bad_debt END AS [badDebt] 
                    FROM [stg].[ci_sa] sa 
                    LEFT JOIN stg.[CI_ACCT] A ON SA.[acct_id] = A.[acct_id]  
                    LEFT JOIN (SELECT [ACCT_ID], [COLL_STATUS_FLG], [CRE_DTTM], [ars_amt], [coll_proc_id], [coll_proc_tmpl_cd] , bad_debt 
                                FROM stg.[CI_COLL_PROC] ) CP							 
                                ON CP.[ACCT_ID] = A.[ACCT_ID]	AND CP.[CRE_DTTM] =  
                                (SELECT MAX(CP1.[CRE_DTTM]) as maxdate	FROM stg.[CI_COLL_PROC] CP1	WHERE CP1.[ACCT_ID] = A.[ACCT_ID] )  
                                and	sa.load_date_time>=  (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 
                            FROM	ctl.LoadLog WHERE	TableName	= 'ucdm.Debt' AND	SourceTableName = 'stg.ci_sa' AND	Status = 'SUCCESS') ) A;'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate active bad debt amount stage variable",
)
def test_active_bad_debt_amount_stage():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate active bad debt amount stage variable')
def validate_active_bad_debt_amount_stage(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.CI_COLL_PROC")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from  ( 
                    select CASE WHEN cp.bad_debt IS NULL THEN 'None' ELSE cp.ars_amt END AS [badDebtAmount] 
                    FROM [stg].[ci_sa] sa 
                    LEFT JOIN stg.[CI_ACCT] A ON SA.[acct_id] = A.[acct_id]  
                    LEFT JOIN (SELECT [ACCT_ID], [COLL_STATUS_FLG], [CRE_DTTM], [ars_amt], [coll_proc_id], [coll_proc_tmpl_cd] , bad_debt 
                                FROM stg.[CI_COLL_PROC] ) CP							 
                                ON CP.[ACCT_ID] = A.[ACCT_ID]	AND CP.[CRE_DTTM] =  
                                (SELECT MAX(CP1.[CRE_DTTM]) as maxdate	FROM stg.[CI_COLL_PROC] CP1	WHERE CP1.[ACCT_ID] = A.[ACCT_ID] )  
                                and	sa.load_date_time>=  (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 
                            FROM	ctl.LoadLog WHERE	TableName	= 'ucdm.Debt' AND	SourceTableName = 'stg.ci_sa' AND	Status = 'SUCCESS') ) A;'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate total number of times bad debt in stg",
)
def test_total_number_of_times_bad_debt_in_stg():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate total number of times bad debt in stg')
def validate_total_number_of_times_bad_debt_in_stg(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_coll_proc")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT COUNT(*) FROM (
                    SELECT CASE WHEN coll.[numInDebt] IS NULL THEN  0 ELSE coll.[numInDebt] END    AS [totalTimesInDebt]    
                    FROM [stg].[ci_sa] sa
                    LEFT JOIN (SELECT [ACCT_ID], COUNT(COLL_PROC_ID) AS numInDebt FROM stg.[ci_coll_proc]
                                GROUP BY ACCT_ID) coll ON coll.[acct_id] = sa.[acct_id]
                                where    sa.load_date_time >=  (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime
                            FROM    ctl.LoadLog WHERE    TableName    = 'stg.ci_sa' and InsertedRows>0  AND    Status = 'SUCCESS') ) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate total bad debt amount in stg",
)
def test_total_bad_debt_amount_in_stg():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate total bad debt amount in stg')
def validate_total_bad_debt_amount_in_stg(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_sa")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT COUNT(*) FROM (
                    SELECT  coll_bd.totalBadDebt AS [totalbadDebtAmount]    
                    FROM [stg].[ci_sa] sa
                    LEFT JOIN (SELECT [ACCT_ID], SUM(ars_amt) AS totalBadDebt FROM [stg].[ci_coll_proc]
                        WHERE bad_debt in ('Active','Closed') GROUP BY ACCT_ID ) coll_bd ON coll_bd.[acct_id] = sa.[acct_id]
                                where    sa.load_date_time >=  (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime
                            FROM    ctl.LoadLog WHERE    TableName = 'stg.ci_sa' and InsertedRows>0 AND    Status = 'SUCCESS') ) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate price increase source",
)
def test_price_increase_source_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate price increase source')
def validate_price_increase_source(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.domestic_price_change_history")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.domestic_price_change_history  where change_type	= 'increase' and company='Energia'  
                    and	load_date_time >=  (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 
                    FROM	ctl.LoadLog WHERE	TableName = 'stg.domestic_price_change_history' and InsertedRows>0  AND	Status = 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate price decrease source",
)
def test_price_decrease_source_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate price decrease source')
def validate_price_decrease_source(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.domestic_price_change_history")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from stg.domestic_price_change_history  where change_type	= 'decrease' and company='Energia'  
                    and	load_date_time >=  (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 
                            FROM ctl.LoadLog WHERE	TableName = 'stg.domestic_price_change_history' and InsertedRows>0 AND Status = 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate discount applied  variable in stg",
)
def test_discount_applied_variable_in_stg():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate discount applied variable in stg')
def validate_discount_applied_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_bseg_calc_ln")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from stg.ci_bseg_calc_ln where descr_on_bill is not null   
                    and	load_date_time >=  (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 
                    FROM	ctl.LoadLog WHERE	TableName	= 'ucdm.contract' AND	SourceTableName = 'stg.ci_bseg_calc_ln' AND	Status = 'SUCCESS');'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate initial signup channel in ucdm",
)
def test_initial_signup_channel_variable_in_ucdm():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate initial signup channel in ucdm')
def validate_initial_signup_channel_variable_in_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.person")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ucdm.person 
                    where load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 
		            FROM ctl.LoadLog WHERE TableName= 'ucdm.person' AND	Status = 'SUCCESS')  and SignedUpChannel is not null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate initial signup channel in stg",
)
def test_initial_signup_channel_in_stg():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate initial signup channel in stg')
def validate_initial_signup_channel_in_stg(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.ci_char_val_l")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( SELECT	char_type_cd, char_val, 
                    CASE WHEN (descr = 'Bonkers' OR descr = 'Switcher') THEN 'PCW' WHEN (descr = 'Interaction Domestic') THEN 'Telesales'  
                        WHEN (descr = 'N/A') THEN 'Web' WHEN (descr = 'OneBigSwitch') THEN 'OBS' -- Revision 11 15/06/2020 JMcM- DRS-3398 
                        WHEN (descr = 'C3 Marketing' OR descr = 'DNE' OR descr = 'Appco' OR descr = 'NK Communications Domestic' OR descr = 'Lites') THEN 'Field Sales' 
                    ELSE 'Other' END AS [SignedUpChannel] FROM stg.ci_char_val_l ) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()   

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate eoc contract notifications variable",
)
def test_eoc_contract_notifications_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate eoc contract notifications variable')
def validate_eoc_contract_notifications_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.[Customer_Contacts]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
				SELECT top 100 	cc.[PersonID],	MAX(c.[ContractEndDate]) as [CurrentContractEndNotification]  
				FROM ucdm.[Customer_Contacts] cc  LEFT JOIN	ucdm.[Person] p  ON	cc.[PersonID] = p.[PersonID]  
				LEFT JOIN	ucdm.[Complaints] cs 
					ON	p.[PersonID] = cs.[PersonID]  LEFT JOIN	ucdm.[AccountPerson] ap 
				ON	 p.[PersonID] = ap.[PersonID] LEFT JOIN	ucdm.[ServiceAgreement]	sa 
				ON	ap.[AccountID] = sa.[AccountID] 
				LEFT JOIN	ucdm.[Contract]	c  ON	sa.[ServiceAgreementID] = c.[ServiceAgreementID]  
				WHERE	cc.[CurrentFlag] = 1 and p.currentflag=1  
				and sa.currentflag=1 and c.[CurrentFlag] = 1 group by cc.[PersonID]  
				order by MAX(c.[ContractEndDate]) desc ) A  
				inner join [ucdm].[CustomerContactsSummary] cc on A.personID = cc.personid'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close() 

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate complaints ever total variable",
)
def test_complaints_ever_total_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate complaints ever total variable')
def validate_complaints_ever_total_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.[Customer_Contacts]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
				SELECT top 100 	cc.[PersonID],	SUM(CASE WHEN cs.[ComplaintsCategory] NOT IN ('CANCEL1', 'CANCEL2', 'CANCEL3') THEN 1 ELSE 0 END) as [TotalComplaints]  
				FROM ucdm.[Customer_Contacts]	cc   left JOIN	ucdm.[Person] p  ON	cc.[PersonID] = p.[PersonID]  
				left JOIN	ucdm.[Complaints] cs 
					ON	p.[PersonID] = cs.[PersonID]  left JOIN	ucdm.[AccountPerson] ap 
				ON	 p.[PersonID] = ap.[PersonID] left JOIN	ucdm.[ServiceAgreement]	sa 
				ON	ap.[AccountID] = sa.[AccountID] 
				left JOIN	ucdm.[Contract]	c  ON	sa.[ServiceAgreementID] = c.[ServiceAgreementID]  
				WHERE	cc.[CurrentFlag] = 1 and p.currentflag=1  
				and sa.currentflag=1 and c.[CurrentFlag] = 1 group by cc.[PersonID]  
				order by SUM(CASE WHEN cs.[ComplaintsCategory] NOT IN ('CANCEL1', 'CANCEL2', 'CANCEL3') THEN 1 ELSE 0 END) desc ) A  
				inner join [ucdm].[CustomerContactsSummary] cc on A.personID = cc.personid'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate complaints ever L3 variable",
)
def test_to_validate_complaints_ever_L3_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate complaints ever L3 variable')
def validate_complaints_ever_L3_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.[Customer_Contacts]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
					SELECT top 100 	cc.[PersonID],	SUM(CASE WHEN cs.[ComplaintsCategory] IN ('L3', 'CLOSED3') THEN 1 ELSE 0 END) as [L3Complaints]  
					FROM		ucdm.[Customer_Contacts]	cc   LEFT JOIN	ucdm.[Person] p  
					ON	cc.[PersonID] = p.[PersonID]  LEFT JOIN	ucdm.[Complaints] cs 
						ON	p.[PersonID] = cs.[PersonID]  LEFT JOIN	ucdm.[AccountPerson] ap 
					ON	 p.[PersonID] = ap.[PersonID] LEFT JOIN	ucdm.[ServiceAgreement]	sa 
					ON	ap.[AccountID] = sa.[AccountID] 
					LEFT JOIN	ucdm.[Contract]	c  ON	sa.[ServiceAgreementID] = c.[ServiceAgreementID]  
					WHERE	cc.[CurrentFlag] = 1 and p.currentflag=1  
					and sa.currentflag=1 and c.[CurrentFlag] = 1 group by cc.[PersonID]   
					order by SUM(CASE WHEN cs.[ComplaintsCategory] IN ('L3', 'CLOSED3') THEN 1 ELSE 0 END) desc ) A  
					inner join [ucdm].[CustomerContactsSummary] cc on A.personID = cc.personid'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate complaints ever L2 variable",
)
def test_complaints_ever_L2_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate complaints ever L2 variable')
def validate_complaints_ever_L2_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.[Customer_Contacts]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
				SELECT top 100 	cc.[PersonID],	SUM(CASE WHEN cs.[ComplaintsCategory] IN ('L2', 'CLOSED2') THEN 1 ELSE 0 END) as [L2Complaints]  
				FROM ucdm.[Customer_Contacts]	cc   LEFT JOIN	ucdm.[Person] p  ON	cc.[PersonID] = p.[PersonID]  
				LEFT JOIN	ucdm.[Complaints] cs 
					ON	p.[PersonID] = cs.[PersonID]  LEFT JOIN	ucdm.[AccountPerson] ap 
				ON	 p.[PersonID] = ap.[PersonID] LEFT JOIN	ucdm.[ServiceAgreement]	sa 
				ON	ap.[AccountID] = sa.[AccountID] 
				LEFT JOIN	ucdm.[Contract]	c  ON	sa.[ServiceAgreementID] = c.[ServiceAgreementID]  
				WHERE	cc.[CurrentFlag] = 1 and p.currentflag=1  
				and sa.currentflag=1 and c.[CurrentFlag] = 1 group by cc.[PersonID]  
				order by SUM(CASE WHEN cs.[ComplaintsCategory] IN ('L2', 'CLOSED2') THEN 1 ELSE 0 END)	desc ) A  
				inner join [ucdm].[CustomerContactsSummary] cc on A.personID = cc.personid'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate complaints ever L1 variable",
)
def test_complaints_ever_L1_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate complaints ever L1 variable')
def validate_complaints_ever_L1_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.[Customer_Contacts]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
				SELECT top 100 	cc.[PersonID],	SUM(CASE WHEN cs.[ComplaintsCategory] IN ('L1', 'CLOSED3') THEN 1 ELSE 0 END) as [L3Complaints]  
				FROM		ucdm.[Customer_Contacts]	cc   LEFT JOIN	ucdm.[Person] p  
				ON	cc.[PersonID] = p.[PersonID]  LEFT JOIN	ucdm.[Complaints] cs 
					ON	p.[PersonID] = cs.[PersonID]  LEFT JOIN	ucdm.[AccountPerson] ap 
				ON	 p.[PersonID] = ap.[PersonID] LEFT JOIN	ucdm.[ServiceAgreement]	sa 
				ON	ap.[AccountID] = sa.[AccountID] 
				LEFT JOIN	ucdm.[Contract]	c  ON	sa.[ServiceAgreementID] = c.[ServiceAgreementID]  
				WHERE	cc.[CurrentFlag] = 1 and p.currentflag=1  
				and sa.currentflag=1 and c.[CurrentFlag] = 1 group by cc.[PersonID]   
				order by SUM(CASE WHEN cs.[ComplaintsCategory] IN ('L1', 'CLOSED3') THEN 1 ELSE 0 END) desc ) A  
				inner join [ucdm].[CustomerContactsSummary] cc on A.personID = cc.personid'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate complaints ever one and done variable",
)
def test_complaints_ever_one_and_done_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate complaints ever one and done variable')
def validate_complaints_ever_one_and_done_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.[Customer_Contacts]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
				SELECT top 100 	cc.[PersonID],	sum(CASE WHEN cc.[ContactClassCode] IN (	'C1B',	'C1BT',	'C1C',	'C1CO',	'C1CS',	'C1CT',	'C1CU',	'C1DC',	'C1DD',	'C1DR',	 
				'C1DT',	'C1EE',	'C1EH',	'C1EI',	'C1EO',	'C1ER',	'C1ES',	'C1GT',	'C1KP',	'C1MA',	'C1MK',	'C1NP',	'C1PL',	'C1PT',	'C1PY',	'C1RD',	'C1RG',	'C1RP',	'C1SA',	'C1SM',	'CCC1',	'CCC2' 
				,	'CCCE',	'CCR',	'CERC',	'CERE',	'CERS',	'DCCR') THEN 1 ELSE 0 END	) as [Check_OneAndDone]  
				FROM		ucdm.[Customer_Contacts]	cc   INNER JOIN	ucdm.[Person] p  ON	cc.[PersonID] = p.[PersonID]  
				INNER JOIN	ucdm.[AccountPerson] ap 
				ON	 p.[PersonID] = ap.[PersonID] INNER JOIN	ucdm.[ServiceAgreement]	sa 
				ON	ap.[AccountID] = sa.[AccountID] 
				left JOIN	ucdm.[Contract]	c  ON	sa.[ServiceAgreementID] = c.[ServiceAgreementID]  
				WHERE	cc.[CurrentFlag] = 1 and p.currentflag=1  
				and sa.currentflag=1 and c.[CurrentFlag] = 1 group by cc.[PersonID]  order by sum(CASE WHEN cc.[ContactClassCode] IN (	'C1B',	'C1BT',	'C1C',	'C1CO',	 
				'C1CS',	'C1CT',	'C1CU',	'C1DC',	'C1DD',	'C1DR',	'C1DT',	'C1EE',	'C1EH' ,	'C1EI',	'C1EO',	'C1ER',	'C1ES',	'C1GT',	'C1KP',	'C1MA',	'C1MK',	'C1NP',	'C1PL',	'C1PT',	 
				'C1PY',	'C1RD',	'C1RG',	'C1RP',	'C1SA',	'C1SM',	'CCC1',	'CCC2' ,	'CCCE',	'CCR',	'CERC',	'CERE',	'CERS',	'DCCR') THEN 1 ELSE 0 END	) desc ) A  
				inner join [ucdm].[CustomerContactsSummary] cc on A.personID = cc.personid'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate Any DD Auto rejection in last 30 days prior to Prediction Window (Day 335)  variable",
)
def test_Any_DD_Auto_rejection_in_last_30days_prior_to_Prediction_Window_Day335_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate Any DD Auto rejection in last 30 days prior to Prediction Window (Day 335)  variable')
def validate_Any_DD_Auto_rejection_in_last_30days_prior_to_Prediction_Window_Day335_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.[Customer_Contacts]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
				SELECT top 10 	cc.[PersonID],	 
				case when sum(CASE WHEN cc.[ContactClassCode] = 'DD'  AND cc.[ContactTypeCode] = 'DDR'  AND cc.[ContactDate] < DATEADD(DD, -30, c.[ContractEndDate]) 
				THEN 1 ELSE 0 END)>1 then 1 else 0 end as [Check_HasDDRej]  
				FROM		ucdm.[Customer_Contacts]	cc   INNER JOIN	ucdm.[Person] p  ON	cc.[PersonID] = p.[PersonID]  INNER JOIN	ucdm.[AccountPerson] ap 
				ON	 p.[PersonID] =  ap.[PersonID] INNER JOIN	ucdm.[ServiceAgreement]	sa 
				ON	ap.[AccountID] = sa.[AccountID] 
				INNER JOIN	ucdm.[Contract]	c  ON	sa.[ServiceAgreementID] = c.[ServiceAgreementID]  
				WHERE	cc.[CurrentFlag] = 1 and p.currentflag=1  
				and sa.currentflag=1 and c.[CurrentFlag] = 1 group by cc.[PersonID]  order by case when sum(CASE WHEN cc.[ContactClassCode] = 'DD'  AND cc.[ContactTypeCode] = 'DDR'   
				AND cc.[ContactDate] < DATEADD(DD, -30, c.[ContractEndDate])  THEN 1 ELSE 0 END)>1 then 1 else 0 end desc 
						) A inner join [ucdm].[CustomerContactsSummary] cc on A.personID = cc.personid '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.reconciliation_cc_and_b_set2
@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate Did they cancel DD prior to Prediction Window (Day 335) variable",
)
def test_Did_they_cancel_DD_prior_to_Prediction_Window_Day335_variable():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate Did they cancel DD prior to Prediction Window (Day 335) variable')
def validate_Did_they_cancel_DD_prior_to_Prediction_Window_Day335_variable(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ucdm.[Customer_Contacts]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( SELECT top 10 	cc.[PersonID],	case when sum(CASE WHEN cc.[ContactClassCode] IN ('DD','PAYS','YYY')  
				AND cc.[ContactTypeCode] IN ('WITHDRAWL','DDWITHDRWL','DIRDBWITH')  
				AND cc.[ContactDate] < DATEADD(DD, -30, c.[ContractEndDate]) THEN 1 ELSE 0 
					END)>1 then 1 else 0 end	AS [Check_HasCancelledDD] 
				FROM	ucdm.[Person] p   LEFT JOIN  ucdm.[Customer_Contacts]	cc 
				ON	cc.[PersonID] = p.[PersonID]  
				LEFT JOIN	ucdm.[AccountPerson] ap 
				ON	 p.[PersonID] = ap.[PersonID] 
				LEFT JOIN	ucdm.[ServiceAgreement]	sa 
				ON	ap.[AccountID] = sa.[AccountID] 
				LEFT JOIN	ucdm.[Contract]	c  ON	sa.[ServiceAgreementID] = c.[ServiceAgreementID]  
				WHERE	cc.[CurrentFlag] = 1 and p.currentflag=1  
				and sa.currentflag=1 and c.[CurrentFlag] = 1 group by cc.[PersonID]  order by case when sum(CASE 
				WHEN cc.[ContactClassCode] IN ('DD','PAYS','YYY') AND cc.[ContactTypeCode] 
				IN ('WITHDRAWL','DDWITHDRWL','DIRDBWITH') 
				AND cc.[ContactDate] < DATEADD(DD, -30, c.[ContractEndDate]) 
				THEN 1 ELSE 0 END)>1 then 1 else 0 end desc ) A inner join 
				[ucdm].[CustomerContactsSummary] cc on A.personID = cc.personid'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()


@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate external table CI_ACCT_APAY does not contain the ext_acct_id column",
)
def test_external_table_CI_ACCT_APAY_does_not_contain_the_ext_acct_id_column():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate external table CI_ACCT_APAY does not contain the ext_acct_id column')
def validate_records_in_ucdm_complaints_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.CI_ACCT_APAY")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''IF EXISTS 
        (
        SELECT * 
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_name = 'CI_ACCT_APAY'
        AND column_name = 'ext_acct_id'
        AND table_schema = 'ext'
        )
        SELECT 0 AS [Status] ;
        ELSE
        SELECT 1 AS [Status];'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 1
    else: 
        assert False    
    cursor.close()


@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate staging table CI_ACCT_APAY does not contain the ext_acct_id column",
)
def test_staging_table_CI_ACCT_APAY_does_not_contain_the_ext_acct_id_column():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate staging table CI_ACCT_APAY does not contain the ext_acct_id column')
def validate_records_in_ucdm_complaints_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.CI_ACCT_APAY")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''IF EXISTS 
        (
        SELECT * 
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_name = 'CI_ACCT_APAY'
        AND column_name = 'ext_acct_id'
        AND table_schema = 'stg'
        )
        SELECT 0 AS [Status] ;
        ELSE
        SELECT 1 AS [Status];'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 1
    else: 
        assert False    
    cursor.close()


@pytest.mark.reconciliation_cc_and_b
@scenario(
    "../../features/cc&b_variables.feature",
    "Test to validate data between external and staging table are matching for CI_ACCT_APAY",
)
def test_data_between_external_and_staging_table_are_matching_for_CI_ACCT_APAY():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data between external and staging table are matching for CI_ACCT_APAY')
def validate_records_in_ucdm_complaints_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.CI_ACCT_APAY")
    ext_data = cursor.fetchone()
    cursor.execute("select count(*) from stg.CI_ACCT_APAY")
    stg_data = cursor.fetchone()
    if ext_data[0] != 0 and stg_data[0] != 0:
        query = '''select
        [acct_apay_id],[acct_id],[start_dt],[end_dt],[apay_src_cd],[expire_dt],[entity_name],[comments],[version],[apay_max_wdrwl_amt],[apay_method_flg],[hvr_seq],[hvr_target_integrate_time],[source_operation],[src_commit_time] 
        from stg.ci_acct_apay
        except
        select
        [acct_apay_id],[acct_id],[start_dt],[end_dt],[apay_src_cd],[expire_dt],[entity_name],[comments],[version],[apay_max_wdrwl_amt],[apay_method_flg],[hvr_seq],[hvr_target_integrate_time],[source_operation],[src_commit_time]
        from ext.ci_acct_apay'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else: 
            assert False
    else: 
        assert False    
    cursor.close()