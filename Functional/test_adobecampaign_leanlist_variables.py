import pytest
import pyodbc
from pytest_bdd import given, when, then, scenario, parsers
from functools import partial
from python_settings import settings
import pytest_bdd

@pytest.mark.adobe
@pytest.mark.adobe_campaignTracking
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the table structure of CampaignTracking table",
)
def test_to_validate_table_structure_of_campaigntracking_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the table structure of CampaignTracking table')
def validate_table_structure_of_campaigntracking_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM [campaign_energia_res].[CampaignTracking]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM [campaign_energia_res].[CampaignTracking]'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()


@pytest.mark.adobe
@pytest.mark.adobe_campaignTracking
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the DeliveryDescription column is not null in CampaignTracking table",
)
def test_to_validate_the_DeliveryDescriptionColumn_is_not_null_in_CampaignTracking_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the DeliveryDescription column is not null in CampaignTracking table')
def validate_DeliveryDescriptionColumn_is_not_null_in_CampaignTracking_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM [campaign_energia_res].[CampaignTracking]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [campaign_energia_res].[CampaignTracking] where [DeliveryDescription] is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0

    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignTracking
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate primary key is not null in CampaignTracking table",
)
def test_to_validate_the_primarykey_is_not_null_in_CampaignTracking_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate primary key is not null in CampaignTracking table')
def validate_the_primarykey_is_not_null_in_CampaignTracking_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM [campaign_energia_res].[CampaignTracking]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT	count(*) FROM campaign_energia_res.CampaignTracking 
        where EventId is null and ServiceAgreementId is null and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0

    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignTracking
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate AccountID is not null in CampaignTracking table",
)
def test_to_validate_the_AccountID_is_not_null_in_CampaignTracking_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate AccountID is not null in CampaignTracking table')
def validate_the_AccountID_is_not_null_in_CampaignTracking_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM [campaign_energia_res].[CampaignTracking]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from  [ext].[campaign_sa_delivery] where account_id is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0

    else: 
        assert False    
    cursor.close() 

@pytest.mark.adobe
@pytest.mark.adobe_campaignTracking
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to check for duplicate records in CampaignTracking table",
)
def test_to_check_duplicate_records_in_CampaignTracking_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate for duplicate records in CampaignTracking table')
def validate_duplicate_records_in_CampaignTracking_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignTracking]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*), EventId, ServiceAgreementId from campaign_energia_res.CampaignTracking
        where currentflag=1
        group by EventId,ServiceAgreementId having count(*) >1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else: 
            assert row[0]==0
    else:
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignTracking
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the data between External and UCDM table are matching for CampaignTracking",
)
def test_to_validate_data_between_External_and_UCDM_table_are_matching_in_CampaignTracking_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between External and UCDM table for CampaignTracking')
def validate_data_between_External_and_UCDM_table_are_matching_in_CampaignTracking_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [ext].[campaign_sa_tracking]")
    data_external_adobe = cursor.fetchone()   
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignTracking]")
    data_UCDM_adobe = cursor.fetchone()
    if data_external_adobe[0] != 0 and data_UCDM_adobe[0] != 0:
        query = '''SELECT [person_id],[account_id],[satl_delivery_description],[event_id],[event_type],[service_agreement_id],[contract_term_start_date],[contract_term_end_date],[contract_type] 
        FROM [ext].[campaign_sa_tracking]  
        except 
        SELECT [PersonID],[AccountID],[DeliveryDescription],[EventId],[EventType],[ServiceAgreementId],[ContractStart],[ContractEnd],[ContractType]
        FROM [campaign_energia_res].[CampaignTracking]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignDelivery
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the data between External and UCDM table are matching for CampaignDelivery",
)
def test_to_validate_data_between_External_and_UCDM_table_are_matching_in_CampaignDelivery_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between External and UCDM table for CampaignDelivery')
def validate_data_between_External_and_UCDM_table_are_matching_in_CampaignDelivery_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [ext].[campaign_sa_delivery]")
    data_external_adobe = cursor.fetchone()   
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignDelivery]")
    data_UCDM_adobe = cursor.fetchone()
    if data_external_adobe[0] != 0 and data_UCDM_adobe[0] != 0:
        query = '''SELECT  [PersonID],[AccountID],[DeliveryDescription],[ControlPopulation],[Status],[EventId],[EventType],[ServiceAgreementId],[ContractStart],[ContractEnd],[ContractType]        
        FROM [campaign_energia_res].[CampaignDelivery] 
        except 
        SELECT [person_id],[account_id],[sad_delivery_description],[sad_control_population],[sad_status],[event_id],[event_type],[service_agreement_id],[contract_term_start_date],[contract_term_end_date],[contract_type]
        FROM [ext].[campaign_sa_delivery]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignDelivery
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate primary key is not null in CampaignDelivery table",
)
def test_to_validate_the_primarykey_is_not_null_in_CampaignDelivery_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate primary key is not null in CampaignDelivery table')
def validate_the_primarykey_is_not_null_in_CampaignDelivery_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM [campaign_energia_res].[CampaignDelivery]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT	count(*) FROM campaign_energia_res.CampaignDelivery 
        where EventId is null and ServiceAgreementId is null and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0

    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignDelivery
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the table structure of CampaignDelivery table",
)
def test_to_validate_table_structure_of_CampaignDelivery_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the table structure of CampaignDelivery table')
def validate_table_structure_of_CampaignDelivery_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM [campaign_energia_res].[CampaignDelivery]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM [campaign_energia_res].[CampaignDelivery]'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignDelivery
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to check for duplicate records in CampaignDelivery table",
)
def test_to_check_duplicate_records_in_CampaignDelivery_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate for duplicate records in CampaignDelivery table')
def validate_duplicate_records_in_CampaignDelivery_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignDelivery]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT	count(*) FROM campaign_energia_res.CampaignDelivery 
        where EventId is null and ServiceAgreementId is null and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True 
        else: 
            assert row[0] == 0
    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignMeta
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the data between External and UCDM table are matching for CampaignMeta",
)
def test_to_validate_data_between_External_and_UCDM_table_are_matching_in_CampaignMeta_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between External and UCDM table for CampaignMeta')
def validate_data_between_External_and_UCDM_table_are_matching_in_CampaignMeta_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [ext].[campaign_sa_delivery]")
    data_external_adobe = cursor.fetchone()   
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignMetaData]")
    data_UCDM_adobe = cursor.fetchone()
    if data_external_adobe[0] != 0 and data_UCDM_adobe[0] != 0:
        query = '''SELECT  isnull([DeliveryDescription],''),isnull([DeliveryCode],''),[DeliveryLabel]
        FROM [campaign_energia_res].[CampaignMetaData]
        except
        SELECT isnull([sad_delivery_description],''),isnull([sad_delivery_code],''),[sad_delivery_label]
        FROM [ext].[campaign_sa_delivery]
        '''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignMeta
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the table structure of CampaignMeta table",
)
def test_to_validate_table_structure_of_CampaignMeta_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the table structure of CampaignMeta table')
def validate_table_structure_of_CampaignMeta_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute(" SELECT count(*) FROM [campaign_energia_res].[CampaignMetaData]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM [campaign_energia_res].[CampaignMetaData]'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignMeta
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the primary key is not null in CampaignMeta table",
)
def test_to_validate_the_primarykey_is_not_null_in_CampaignMeta_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate primary key is not null in CampaignMeta table')
def validate_the_primarykey_is_not_null_in_CampaignMeta_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM [campaign_energia_res].[CampaignMetaData]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT	count(*) FROM campaign_energia_res.CampaignMetaData 
        where DeliveryCode is null and DeliveryLabel is null and currentflag=1'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0

    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignMeta
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to check for duplicate records in CampaignMeta table",
)
def test_to_check_duplicate_records_in_CampaignMeta_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate for duplicate records in CampaignMeta table')
def validate_duplicate_records_in_CampaignMeta_table_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignMetaData]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [campaign_energia_res].[CampaignMetaData] where currentflag=1 group by DeliveryCode, DeliveryLabel, effectivestart, effectiveend having count(*) >1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignSummary
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the data between External and UCDM table are matching for CampaignSummary",
)
def test_to_validate_data_between_External_and_UCDM_table_are_matching_in_CampaignSummary_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between External and UCDM table for CampaignSummary')
def validate_data_between_External_and_UCDM_table_are_matching_in_CampaignSummary_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignDelivery]")
    data_external_adobe = cursor.fetchone()   
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignSummary]")
    data_UCDM_adobe = cursor.fetchone()
    if data_external_adobe[0] != 0 and data_UCDM_adobe[0] != 0:
        query = '''SELECT  isnull([DeliveryDescription],''),isnull([DeliveryCode],''),[DeliveryLabel]
        FROM [campaign_energia_res].[CampaignMetaData]
        except
        SELECT isnull([sad_delivery_description],''),isnull([sad_delivery_code],''),[sad_delivery_label]
        FROM [ext].[campaign_sa_delivery]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignSummary
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to check for duplicate records in CampaignSummary table",
)
def test_to_check_duplicate_records_in_CampaignSummary_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate for duplicate records in CampaignSummary table')
def validate_duplicate_records_in_CampaignSummary_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignSummary]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from campaign_energia_res.CampaignSummary
        where currentflag=1
        group by accountid, effectivestart, effectiveend having count(*) >1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0 
    else: 
        assert False    
    cursor.close()
    
@pytest.mark.adobe
@pytest.mark.adobe_campaignSummary
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to validate the data between External and UCDM table are matching for CampaignSummary",
)
def test_to_validate_data_between_External_and_UCDM_table_are_matching_in_CampaignSummary_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between External and UCDM table for CampaignSummary')
def validate_data_between_External_and_UCDM_table_are_matching_in_CampaignSummary_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignDelivery]")
    data_external_adobe = cursor.fetchone()   
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignSummary]")
    data_UCDM_adobe = cursor.fetchone()
    if data_external_adobe[0] != 0 and data_UCDM_adobe[0] != 0:
        query = '''select [ServiceAgreementId],[DeliveryDescription]    
        from  [campaign_energia_res].[CampaignSummary]
        except
        select [ServiceAgreementId],[DeliveryDescription] 
        from [campaign_energia_res].[CampaignDelivery]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert True
    else: 
        assert False    
    cursor.close()

@pytest.mark.adobe
@pytest.mark.adobe_campaignSummary
@scenario(
    "../../features/adobecampaign_variables.feature",
    "Test(adobe) to check for duplicate records in CampaignSummary table",
)
def test_to_check_duplicate_records_in_CampaignSummary_table_for_adobe():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate for duplicate records in CampaignSummary table')
def validate_duplicate_records_in_CampaignSummary_for_adobe(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [campaign_energia_res].[CampaignSummary]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from campaign_energia_res.CampaignSummary
        where currentflag=1
        group by accountid, effectivestart, effectiveend having count(*) >1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0 
    else: 
        assert False    
    cursor.close()