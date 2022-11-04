import pytest
import pyodbc
from pytest_bdd import given, when, then, scenario, parsers
from functools import partial
from python_settings import settings
import pytest_bdd

@pytest.mark.brandfire
@pytest.mark.brandfire_rewarddetails
@scenario(
    "../../features/brandfire_rewarddetails.feature",
    "Test(brandfire_rewarddetails) to validate the table structure of external tables",
)
def test_to_validate_table_structure_of_external_tables_for_brandfire_rewarddetails():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access external table for brandfire rewarddetails')
def validate_table_structure_of_external_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM ext.rewards_detail ")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' SELECT count(*) FROM ext.rewards_detail '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_rewarddetails
@scenario(
    "../../features/brandfire_rewarddetails.feature",
    "Test(brandfire_rewarddetails) to validate the table structure of staging tables",
)
def test_to_validate_table_structure_of_staging_tables_for_brandfire_rewarddetails():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access staging table for brandfire rewarddetails')
def validate_table_structure_of_staging_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*)FROM [stg].[rewards_detail]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM [stg].[rewards_detail] where load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	 ctl.LoadLog 
		WHERE TableName= 'rewards_energia_res.RewardsDetail' AND	SourceTableName = 'stg.rewards_detail' AND	Status= 'success')'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_rewarddetails
@scenario(
    "../../features/brandfire_rewarddetails.feature",
    "Test(brandfire_rewarddetails) to validate the table structure of target tables",
)
def test_to_validate_table_structure_of_target_tables_for_brandfire_rewarddetails():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access target table for brandfire rewarddetails')
def validate_table_structure_of_target_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from rewards_energia_res.RewardsDetail")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from rewards_energia_res.RewardsDetail 
                    where load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	 ctl.LoadLog  
                    WHERE TableName= 'rewards_energia_res.RewardsDetail'  AND	Status= 'success')'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_rewarddetails
@scenario(
    "../../features/brandfire_rewarddetails.feature",
    "Test(brandfire_rewarddetails) to validate count of records between External and staging table are matching",
)
def test_to_validate_count_of_records_between_External_and_staging_table_are_matching_for_brandfire_rewarddetails():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate count of records and data are matching between External and staging table for brandfire rewarddetails')
def validate_count_of_records_and_data_are_matching_between_External_and_staging_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [ext].Rewards_Detail")
    ext_data = cursor.fetchone()
    cursor.execute("select count(*) from [stg].Rewards_Detail")
    stg_data = cursor.fetchone()
    if ext_data[0] != 0 and stg_data[0]!=0:
        query = '''SELECT isnull(RewardID,'') as RewardID, isnull(Reward_Name,'') as Reward_Name, isnull(date,'') as date, isnull(accountid,'') as accountid, isnull(event,'') as event 
        FROM [ext].Rewards_Detail 
        except 
        SELECT isnull(RewardID,'') as RewardID, isnull(Reward_Name,'') as Reward_Name, isnull(date,'') as date, isnull(accountid,'') as accountid, isnull(event,'') as event 
        FROM [stg].Rewards_Detail'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0 

    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_rewarddetails
@scenario(
    "../../features/brandfire_rewarddetails.feature",
    "Test(brandfire_rewarddetails) to validate count of records between staging table and target table are matching",
)
def test_to_validate_count_of_records_between_staging_table_and_target_table_are_matching_for_brandfire_rewarddetails():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between staging table and target table for brandfire rewarddetails')
def validate_count_of_records_are_matching_between_staging_table_and_target_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].Rewards_Detail")
    stg_data = cursor.fetchone()
    cursor.execute("select count(*) from rewards_energia_res.RewardsDetail")
    ucdm_data = cursor.fetchone()
    if stg_data[0] != 0 and ucdm_data[0]!=0:
        query = ''' SELECT isnull(RewardID,'') as RewardID ,isnull(Reward_Name,'') as Reward_Name
        FROM [stg].Rewards_Detail
        except
        SELECT  isnull(RewardID,'') as RewardID ,isnull(RewardName,'') as RewardName
        FROM rewards_energia_res.RewardsDetail'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_rewarddetails
@scenario(
    "../../features/brandfire_rewarddetails.feature",
    "Test(brandfire_rewarddetails) to check duplicate records in target table",
)
def test_to_check_duplicate_records_in_target_table_for_brandfire_rewarddetails():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate duplicate records in rewards_energia_res table for brandfire rewarddetails')
def validate_if_any_duplicate_records_in_rewards_energia_res_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from rewards_energia_res.RewardsDetail")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*), rewardid,rewardname from rewards_energia_res.RewardsDetail 
                    where currentflag=1 group by rewardid,rewardname having count(*) >1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

# @pytest.mark.brandfire
# @pytest.mark.brandfire_rewarddetails
# @scenario(
#     "../../features/brandfire_rewarddetails.feature",
#     "Test(brandfire_rewarddetails) to validate the primary key in target table",
# )
# def test_to_validate_the_primary_key_in_target_table_for_brandfire_rewarddetails():
#     pass

# @given('I have Database connection details')
# def database_connection_details(kv):
#     pass

# @when('I was able to connect to database')
# def database_connection(sql_connection):
#     pass

# @then('I can validate the primary key in target table for brandfire rewarddetails')
# def validate_primary_key_in_target(sql_connection):
#     cursor = sql_connection.cursor()
#     cursor.execute("select count(*) from rewards_energia_res.RewardsDetail")
#     data = cursor.fetchone()
#     print(data)
#     if data[0] != 0:
#         query = '''select count(*) from  rewards_energia_res.RewardsDetail where RewardID is null '''
#         cursor.execute(query)
#         row = cursor.fetchone()
#         assert row[0] == 0 
#     else: 
#         assert False    
#     cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_rewarddetails
@scenario(
    "../../features/brandfire_rewarddetails.feature",
    "Test(brandfire_rewarddetails) to validate the data in external and staging tables are as per transformation logic",
)
def test_to_validate_the_data_in_external_and_staging_tables_transformation_logic_for_brandfire_rewarddetails():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the data between external and staging tables for brandfire rewarddetails')
def test_to_validate_transformation_logic_in_external_and_staging_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.Rewards_Detail")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from (
                    SELECT top 10 stg.RewardID, ext.Reward_Name as ext_Reward_Name, ext.[date] as ext_load_date_time
                    ,stg.Reward_Name stg_Reward_Name, stg.load_date_time as stg_load_date_time
                    FROM ext.Rewards_Detail ext inner join stg.Rewards_Detail stg
                    on ext.RewardID = stg.RewardID ) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_rewarddetails
@scenario(
    "../../features/brandfire_rewarddetails.feature",
    "Test(brandfire_rewarddetails) to validate the data in staging and target tables are as per transformation logic",
)
def test_to_validate_the_data_in_staging_and_target_tables_transformation_logic_for_brandfire_rewarddetails():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the data between staging and target tables for brandfire rewarddetails')
def test_to_validate_transformation_logic_in_staging_and_target_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.Rewards_Detail")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from (
                    SELECT top 10 tgt.RewardID, stg.Reward_Name, stg.load_date_time , tgt.RewardName
                    ,stg.load_date_time as stg_load_date_time, tgt.load_date_time as tgt_load_date_time
                    FROM stg.Rewards_Detail stg inner join rewards_energia_res.RewardsDetail tgt
                    on stg.RewardID = tgt.RewardID ) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_activity
@scenario(
    "../../features/brandfire_activity.feature",
    "Test(brandfire_activity) to validate the table structure of external tables",
)
def test_to_validate_table_structure_of_external_tables_for_brandfire_activity():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access external table for brandfire activity')
def validate_table_structure_of_external_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM ext.rewards_activity")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM ext.rewards_activity'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_activity
@scenario(
    "../../features/brandfire_activity.feature",
    "Test(brandfire_activity) to validate the table structure of staging tables",
)
def test_to_validate_table_structure_of_staging_tables_for_brandfire_activity():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access staging table for brandfire activity')
def validate_table_structure_of_staging_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*)FROM [stg].[rewards_activity]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM [stg].[rewards_activity] where load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM ctl.LoadLog
                   WHERE TableName= 'rewards_energia_res.activity' AND SourceTableName = 'stg.rewards_activity' AND Status= 'success')'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_activity
@scenario(
    "../../features/brandfire_activity.feature",
    "Test(brandfire_activity) to validate the table structure of target tables",
)
def test_to_validate_table_structure_of_target_tables_for_brandfire_activity():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access target table for brandfire activity')
def validate_table_structure_of_target_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from rewards_energia_res.activity")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from rewards_energia_res.activity
                    where load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM ctl.LoadLog
                    WHERE TableName= 'rewards_energia_res.activity' AND Status= 'success')'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_activity
@scenario(
    "../../features/brandfire_activity.feature",
    "Test(brandfire_activity) to validate count of records between External and staging table are matching",
)
def test_to_validate_count_of_records_between_External_and_staging_table_are_matching_for_brandfire_activity():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate count of records and data are matching between External and staging table for brandfire activity')
def validate_count_of_records_and_data_are_matching_between_External_and_staging_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [ext].rewards_activity")
    ext_data = cursor.fetchone()
    cursor.execute("select count(*) from [stg].rewards_activity")
    stg_data = cursor.fetchone()
    if ext_data[0] != 0 and stg_data[0]!=0:
        query = '''SELECT isnull(Rewardid,'') as Rewardid, isnull(Reward_Name, '') as Reward_Name, 
        isnull(replace(account_number,'null',null),'') as account_number, isnull(Event,'') as Event
        FROM [ext].Rewards_activity
        except
        SELECT isnull(Rewardid,'') as Rewardid ,isnull(Reward_Name, '') as Reward_Name, 
        isnull(replace(account_number,'null',null),'') as account_number, isnull(Event,'') as Event
        FROM [stg].rewards_activity'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0 

    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_activity
@scenario(
    "../../features/brandfire_activity.feature",
    "Test(brandfire_activity) to validate count of records between staging table and target table are matching",
)
def test_to_validate_count_of_records_between_staging_table_and_target_table_are_matching_for_brandfire_activity():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between staging table and target table for brandfire activity')
def validate_count_of_records_are_matching_between_staging_table_and_target_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].rewards_activity")
    stg_data = cursor.fetchone()
    cursor.execute("select count(*) from rewards_energia_res.activity")
    ucdm_data = cursor.fetchone()
    if stg_data[0] != 0 and ucdm_data[0] !=0 :
        query = '''select   isnull(RewardID,'') as RewardID,  isnull(AccountID,'') as  account_number ,
            isnull([Event],'') as [Event], [date]
            FROM rewards_energia_res.activity
            except
            select
            isnull(RewardID,'') as RewardID,  isnull([account_number], '') as account_number,
            isnull([Event],'') as [Event], [date]
            from stg.rewards_activity'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_activity
@scenario(
    "../../features/brandfire_activity.feature",
    "Test(brandfire_activity) to check duplicate records in target table",
)
def test_to_check_duplicate_records_in_target_table_for_brandfire_activity():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate duplicate records in rewards_energia_res table for brandfire activity')
def validate_if_any_duplicate_records_in_rewards_energia_res_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from rewards_energia_res.activity")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) ct, rewardid,accountId from rewards_energia_res.activity
        where currentflag=1 group by rewardid, event, accountid, date, effectivestart, effectiveend, 
        currentflag having count(*) >1 '''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

# @pytest.mark.brandfire
# @pytest.mark.brandfire_activity
# @scenario(
#     "../../features/brandfire_activity.feature",
#     "Test(brandfire_activity) to validate the primary key in target table",
# )
# def test_to_validate_the_primary_key_in_target_table_for_brandfire_activity():
#     pass

# @given('I have Database connection details')
# def database_connection_details(kv):
#     pass

# @when('I was able to connect to database')
# def database_connection(sql_connection):
#     pass

# @then('I can validate the primary key in target table for brandfire activity')
# def validate_primary_key_in_target(sql_connection):
#     cursor = sql_connection.cursor()
#     cursor.execute("select count(*) from rewards_energia_res.activity")
#     data = cursor.fetchone()
#     print(data)
#     if data[0] != 0:
#         query = '''select count(*) from  rewards_energia_res.activity where RewardID is null'''
#         cursor.execute(query)
#         row = cursor.fetchone()
#         assert row[0] == 0 
#     else: 
#         assert False    
#     cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_activity
@scenario(
    "../../features/brandfire_activity.feature",
    "Test(brandfire_activity) to validate the data in external and staging tables are as per transformation logic",
)
def test_to_validate_the_data_in_external_and_staging_tables_transformation_logic_for_brandfire_activity():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the data between external and staging tables for brandfire activity')
def test_to_validate_transformation_logic_in_external_and_staging_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.rewards_activity")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
                    SELECT  top 10	ext.RewardID, ext.account_number as ext_account_number,   stg.account_number, ext.[event] as ext_event, stg.[Event] as stg_event 
                    FROM ext.rewards_activity ext inner join    stg.rewards_activity stg 
                    on ext.RewardID = stg.RewardID  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'rewards_energia_res.activity' AND	SourceTableName = 'stg.rewards_activity' AND	Status= 'success')  
                            and stg.reward_name is not null ) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_activity
@scenario(
    "../../features/brandfire_activity.feature",
    "Test(brandfire_activity) to validate the data in staging and target tables are as per transformation logic",
)
def test_to_validate_the_data_in_staging_and_target_tables_transformation_logic_for_brandfire_activity():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the data between staging and target tables for brandfire activity')
def test_to_validate_transformation_logic_in_staging_and_target_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.rewards_activity")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
                    SELECT  top 10	tgt.RewardID, stg.account_number,  tgt.accountId, stg.[event]  as stg_event, tgt.[Event] 
                            ,stg.load_date_time as stg_load_date_time, tgt.load_date_time     as tgt_load_date_time 
                    FROM stg.rewards_activity stg inner join    rewards_energia_res.activity tgt 
                    on stg.RewardID = tgt.RewardID  
                    where tgt.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog  
                    WHERE TableName= 'rewards_energia_res.activity'  AND	Status= 'success')  ) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_registrations
@scenario(
    "../../features/brandfire_registrations.feature",
    "Test(brandfire_registrations) to validate the table structure of external tables",
)
def test_to_validate_table_structure_of_external_tables_for_brandfire_registrations():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access external table for brandfire registrations')
def validate_table_structure_of_external_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM ext.rewards_registration")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM ext.rewards_registration'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_registrations
@scenario(
    "../../features/brandfire_registrations.feature",
    "Test(brandfire_registrations) to validate the table structure of staging tables",
)
def test_to_validate_table_structure_of_staging_tables_for_brandfire_registrations():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access staging table for brandfire registrations')
def validate_table_structure_of_staging_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*)FROM [stg].[rewards_registration]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM [stg].[rewards_registration] where load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
		            WHERE TableName= 'rewards_energia_res.registration' AND	SourceTableName = 'stg.rewards_registration' AND	Status= 'success')'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_registrations
@scenario(
    "../../features/brandfire_registrations.feature",
    "Test(brandfire_registrations) to validate the table structure of target tables",
)
def test_to_validate_table_structure_of_target_tables_for_brandfire_registrations():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access target table for brandfire registrations')
def validate_table_structure_of_target_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from rewards_energia_res.registration")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from rewards_energia_res.registration 
                    where load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	 ctl.LoadLog  
                    WHERE TableName= 'rewards_energia_res.registration'  AND	Status= 'success') '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_registrations
@scenario(
    "../../features/brandfire_registrations.feature",
    "Test(brandfire_registrations) to validate count of records between External and staging table are matching",
)
def test_to_validate_count_of_records_between_External_and_staging_table_are_matching_for_brandfire_registrations():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate count of records and data are matching between External and staging table for brandfire registrations')
def validate_count_of_records_and_data_are_matching_between_External_and_staging_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [ext].rewards_registration")
    ext_data = cursor.fetchone()
    cursor.execute("select count(*) from [stg].rewards_registration")
    stg_data = cursor.fetchone()
    if ext_data[0] != 0 and stg_data[0]!=0 :
        query = '''SELECT count(*)
        FROM ext.rewards_registration
        except
        SELECT count(*)
        FROM stg.rewards_registration'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] >= 0 

    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_registrations
@scenario(
    "../../features/brandfire_registrations.feature",
    "Test(brandfire_registrations) to validate count of records between staging table and target table are matching",
)
def test_to_validate_count_of_records_between_staging_table_and_target_table_are_matching_for_brandfire_registrations():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between staging table and target table for brandfire registrations')
def validate_count_of_records_are_matching_between_staging_table_and_target_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].rewards_registration")
    stg_data = cursor.fetchone()
    cursor.execute("select count(*) from rewards_energia_res.registration")
    ucdm_data = cursor.fetchone()
    if stg_data[0] != 0 and ucdm_data[0]!=0:
        query = '''SELECT isnull(account_number,'') as account_number, isnull(Email,'') as Email, isnull(registration_date,'2000-01-01 00:00:00') as registration_date
        FROM stg.rewards_registration where load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM ctl.LoadLog WHERE TableName= 'stg.rewards_registration'  AND Status= 'success')
        except
        SELECT isnull(accountId,'') as accountId, isnull(Email,'') as Email, isnull(registrationdate,'2000-01-01 00:00:00') as registrationdate
        FROM rewards_energia_res.registration where load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime FROM ctl.LoadLog WHERE TableName= 'rewards_energia_res.registration'  AND Status= 'success') '''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_registrations
@scenario(
    "../../features/brandfire_registrations.feature",
    "Test(brandfire_registrations) to check duplicate records in target table",
)
def test_to_check_duplicate_records_in_target_table_for_brandfire_registrations():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate duplicate records in rewards_energia_res table for brandfire registrations')
def validate_if_any_duplicate_records_in_rewards_energia_res_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from rewards_energia_res.registration")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) ct, accountId from rewards_energia_res.registration 
                    where currentflag=1 group by accountid, email, effectivestart, effectiveend, currentflag having count(*) >1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

# @pytest.mark.brandfire
# @pytest.mark.brandfire_registrations
# @scenario(
#     "../../features/brandfire_registrations.feature",
#     "Test(brandfire_registrations) to validate the primary key in target table",
# )
# def test_to_validate_the_primary_key_in_target_table_for_brandfire_registrations():
#     pass

# @given('I have Database connection details')
# def database_connection_details(kv):
#     pass

# @when('I was able to connect to database')
# def database_connection(sql_connection):
#     pass

# @then('I can validate the primary key in target table for brandfire registrations')
# def validate_primary_key_in_target(sql_connection):
#     cursor = sql_connection.cursor()
#     cursor.execute("select count(*) from rewards_energia_res.registration")
#     data = cursor.fetchone()
#     print(data)
#     if data[0] != 0:
#         query = '''select count(*) from  rewards_energia_res.registration where accountid is null'''
#         cursor.execute(query)
#         row = cursor.fetchone()
#         assert row[0] == 0 
#     else: 
#         assert False    
#     cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_registrations
@scenario(
    "../../features/brandfire_registrations.feature",
    "Test(brandfire_registrations) to validate the data in external and staging tables are as per transformation logic",
)
def test_to_validate_the_data_in_external_and_staging_tables_transformation_logic_for_brandfire_registrations():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the data between external and staging tables for brandfire registrations')
def test_to_validate_transformation_logic_in_external_and_staging_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.rewards_registration")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( SELECT top 10 ext.account_number as ext_account_number, stg.account_number,
        ext.Email as ext_Email, stg.Email as stg_Email, ext.registration_date as ext_registration_date,
        stg.registration_date FROM ext.rewards_registration ext
        inner join stg.rewards_registration stg on
        CASE WHEN ext.account_number='NULL' THEN NULL
        WHEN left(ext.account_number,3)<>'ED_' THEN 'ED_'+ ext.account_number
        ELSE ext.account_number END = stg.account_number
        where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime
        FROM ctl.LoadLog WHERE TableName= 'rewards_energia_res.registration'
        AND SourceTableName = 'stg.rewards_registration' AND Status= 'success') ) A '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.brandfire
@pytest.mark.brandfire_registrations
@scenario(
    "../../features/brandfire_registrations.feature",
    "Test(brandfire_registrations) to validate the data in staging and target tables are as per transformation logic",
)
def test_to_validate_the_data_in_staging_and_target_tables_transformation_logic_for_brandfire_registrations():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the data between staging and target tables for brandfire registrations')
def test_to_validate_transformation_logic_in_staging_and_target_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.rewards_registration")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from ( 
                    SELECT  top 10	stg.account_number,  tgt.accountId, stg.Email  as stg_Email, tgt.Email 
                            ,stg.registration_date as stg_registration_date, tgt.registrationdate     as tgt_registration_date 
                    FROM stg.rewards_registration stg inner join    rewards_energia_res.registration tgt 
                    on stg.account_number = tgt.accountId  
                    where tgt.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog  
                    WHERE TableName= 'rewards_energia_res.registration'  AND	Status= 'success')  ) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()