import pytest
import pyodbc
from pytest_bdd import given, when, then, scenario, parsers
from functools import partial
from python_settings import settings
import pytest_bdd

@pytest.mark.qualtrics
@pytest.mark.qualtrics_questiontypelookup
@scenario(
    "../../features/qualtrics_questiontypelookup.feature",
    "Test(questiontype) to validate the table structure of external tables",
)
def test_to_validate_table_structure_of_external_tables_for_questiontype():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access external table')
def validate_table_structure_of_external_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM [ext].[qualtrics_question_type_lookup]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' SELECT count(*) FROM [ext].[qualtrics_question_type_lookup]'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_questiontypelookup
@scenario(
    "../../features/qualtrics_questiontypelookup.feature",
    "Test(questiontype) to validate the table structure of staging tables",
)
def test_to_validate_table_structure_of_staging_tables_for_questiontype():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access staging  table')
def validate_table_structure_of_staging_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*)FROM [stg].[qualtrics_question_type_lookup]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*)FROM [stg].[qualtrics_question_type_lookup]'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_questiontypelookup
@scenario(
    "../../features/qualtrics_questiontypelookup.feature",
    "Test(questiontype) to validate the table structure of UCDM tables",
)
def test_to_validate_table_structure_of_ucdm_tables_for_questiontype():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can able to access ucdm table')
def validate_table_structure_of_ucdm_tables(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[QuestionTypeLookup]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from [qualtrics_domestic_res].[QuestionTypeLookup]'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

# @pytest.mark.qualtrics
# @pytest.mark.qualtrics_questiontypelookup
# @scenario(
#     "../../features/qualtrics_questiontypelookup.feature",
#     "Test(questiontype) to validate count of records between External and staging table are matching",
# )
# def test_to_validate_count_of_records_between_External_and_staging_table_are_matching_for_questiontype():
#     pass

# @given('I have Database connection details')
# def database_connection_details(kv):
#     pass

# @when('I was able to connect to database')
# def database_connection(sql_connection):
#     pass

# @then('I can validate count of records and data are matching between External and staging table')
# def validate_count_of_records_and_data_are_matching_between_External_and_staging_table(sql_connection):
#     cursor = sql_connection.cursor()
#     cursor.execute("select count(*) from [ext].[qualtrics_survey_questions")
#     ext_data = cursor.fetchone()
#     cursor.execute("select count(*) from [stg].[qualtrics_survey_questions]")
#     stg_data = cursor.fetchone()
#     if ext_data[0] != 0 and stg_data[0]!=0:
#         query = ''' SELECT [question_id],[question],[survey_id],[header] FROM [ext].[qualtrics_survey_questions]
#                     except
#                     SELECT  [question_id],[question],[survey_id],[header] FROM [stg].[qualtrics_survey_questions]'''
#         cursor.execute(query)
#         row = cursor.fetchone()
#         if row is None:
#             assert True
#         else:
#             assert row[0] == 0 

#     else: 
#         assert False    
#     cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_questiontypelookup
@scenario(
    "../../features/qualtrics_questiontypelookup.feature",
    "Test(questiontype) to validate count of records between staging table and UCDM table are matching",
)
def test_to_validate_count_of_records_between_staging_table_and_UCDM_table_are_matching_for_questiontype():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate count of records are matching between staging table and UCDM table')
def validate_count_of_records_are_matching_between_staging_table_and_UCDM_table_for_questiontype(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[QuestionTypeLookup]")
    ucdm_data = cursor.fetchone()
    cursor.execute("select count(*) from [stg].[qualtrics_question_type_lookup]")
    stg_data = cursor.fetchone()
    if ucdm_data[0] != 0 and stg_data[0]!=0:
        query = ''' select count(*) from [qualtrics_domestic_res].[QuestionTypeLookup] where
                    load_date_time >=(Select max(enddatetime) from [ctl].[LoadLog] where tablename='qualtrics_domestic_res.QuestionTypeLookup')
                    Except
                    select count(*)FROM [stg].[qualtrics_question_type_lookup]'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_questiontypelookup
@scenario(
    "../../features/qualtrics_questiontypelookup.feature",
    "Test(questiontype) to validate the data between External and staging table are matching",
)
def test_to_validate_the_data_between_External_and_staging_table_are_matching_for_questiontype():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between External and staging table')
def validate_data_are_matching_between_External_and_staging_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].[qualtrics_question_type_lookup]")
    stg_data = cursor.fetchone()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[QuestionTypeLookup]")
    ucdm_data = cursor.fetchone()
    if stg_data[0]!=0 and ucdm_data[0]!=0 :
        query = '''SELECT [surveyID],[questionID] FROM [stg].[qualtrics_question_type_lookup]
        except
        SELECT  [SurveyID],[QuestionID] FROM [qualtrics_domestic_res].[QuestionTypeLookup]
        '''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] > 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_questiontypelookup
@scenario(
    "../../features/qualtrics_questiontypelookup.feature",
    "Test(questiontype) to check duplicate records in ucdm table",
)
def test_to_check_for_duplicate_records_in_ucdm_for_questiontype():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate duplicate records in UCDM table')
def check_for_duplicate_records_in_ucdm_for_questiontype(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[QuestionTypeLookup]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*), SurveyID,Questionid from [qualtrics_domestic_res].[QuestionTypeLookup]
                   where currentflag=1 group by SurveyID,Questionid having count(*) >1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] > 0          
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_questiontypelookup
@scenario(
    "../../features/qualtrics_questiontypelookup.feature",
    "Test(questiontype) to validate the data in Staging and UCDM tables are as per transformation logic",
)
def test_to_validate_the_data_in_Staging_and_UCDM_tables_are_as_per_transformation_logic_for_questiontype():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the primary key in Ucdm table for questiontype')
def validate_primary_key_in_ucdm(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[QuestionTypeLookup]")
    data = cursor.fetchone()
    print(data[0])
    if data[0] != 0:
        query = '''select count(*) from  [qualtrics_domestic_res].[QuestionTypeLookup] where SurveyID is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_questiontypelookup
@scenario(
    "../../features/qualtrics_questiontypelookup.feature",
    "Test(questiontype) to validate the date fields in the UCDM tables for date format and correctness",
)
def test_to_validate_the_date_fields_in_the_UCDM_tables_for_date_format_and_correctness_for_questiontype():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate question type  in the UCDM tables for date format and correctness')
def test_to_validate_question_type_in_the_UCDM_tables_for_date_format_and_correctness(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[QuestionTypeLookup]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*)  from [qualtrics_domestic_res].[QuestionTypeLookup] where questionid is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_surveytypelookup
@scenario(
    "../../features/qualtrics_surveytypelookup.feature",
    "Test(surveytype) to validate the table structure of external tables",
)
def test_to_validate_the_table_structure_of_external_tables_for_surveyquestions():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate table structure of external tables for surveytype')
def validate_table_structure_of_external_tables_for_surveyquestions(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [ext].[qualtrics_survey_questions]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) FROM [ext].[qualtrics_survey_questions]'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_surveytypelookup
@scenario(
    "../../features/qualtrics_surveytypelookup.feature",
    "Test(surveytype) to validate the table structure of staging tables",
)
def test_to_validate_the_table_structure_of_staging_tables_surveyquestions():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate table structure of staging tables for surveytype')
def validate_table_structure_of_staging_tables_surveyquestions(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].[qualtrics_survey_questions]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) FROM [stg].[qualtrics_survey_questions]'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_surveytypelookup
@scenario(
    "../../features/qualtrics_surveytypelookup.feature",
    "Test(surveytype) to validate the table structure of UCDM tables",
)
def test_to_validate_the_table_structure_of_UCDM_tables_for_surveyquestions():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate table structure of UCDM tables for surveytype')
def validate_table_structure_of_UCDM_tables_for_surveyquestions(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[SurveyQuestions]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from [qualtrics_domestic_res].[SurveyQuestions]'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

# @pytest.mark.qualtrics
# @pytest.mark.qualtrics_surveytypelookup
# @scenario(
#     "../../features/qualtrics_surveytypelookup.feature",
#     "Test(surveytype) to validate count of records between External and staging table are matching",
# )
# def test_to_validate_count_of_records_between_External_and_staging_table_are_matching_for_surveyquestions():
#     pass

# @given('I have Database connection details')
# def database_connection_details(kv):
#     pass

# @when('I was able to connect to database')
# def database_connection(sql_connection):
#     pass

@then('I can validate count of records and data are matching between External and staging table for surveytype')
def validate_count_of_records_and_data_are_matching_between_External_and_staging_table_for_surveyquestions(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].[qualtrics_survey_questions]")
    stg_data = cursor.fetchone()
    cursor.execute("select count(*) from [ext].[qualtrics_survey_questions]")
    ext_data = cursor.fetchone()
    if stg_data[0] != 0 and ext_data[0] !=0:
        query = ''' SELECT [question_id] ,[question],[survey_id],[header] FROM [ext].[qualtrics_survey_questions]
                    except
                    SELECT  [question_id],[question],[survey_id],[header] FROM [stg].[qualtrics_survey_questions]'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_surveytypelookup
@scenario(
    "../../features/qualtrics_surveytypelookup.feature",
    "Test(surveytype) to validate count of records between staging table and UCDM table are matching",
)
def test_to_validate_count_of_records_between_staging_table_and_UCDM_table_are_matching_for_surveyquestions():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate count of records are matching between staging table and UCDM table for surveytype')
def validate_count_of_records_are_matching_between_staging_table_and_UCDM_table_for_surveyquestions(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[SurveyQuestions]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) from [qualtrics_domestic_res].[SurveyQuestions] where
                    load_date_time >=(Select max(enddatetime) from [ctl].[LoadLog] where tablename='qualtrics_domestic_res.SurveyQuestions')
                    Except
                    select count(*)FROM [stg].[qualtrics_survey_questions]'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] > 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_surveytypelookup
@scenario(
    "../../features/qualtrics_surveytypelookup.feature",
    "Test(surveytype) to validate the data between External and staging table are matching",
)
def test_to_validate_the_data_between_External_and_staging_table_are_matching_for_surveyquestions():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between External and staging table for surveytype')
def validate_data_are_matching_between_External_and_staging_table_for_surveyquestions(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].[qualtrics_survey_questions]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' SELECT [survey_id],[question_id]  FROM [stg].[qualtrics_survey_questions]
                    except
                    SELECT [SurveyID],[QuestionID] FROM [qualtrics_domestic_res].[SurveyQuestions]'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] > 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_surveytypelookup
@scenario(
    "../../features/qualtrics_surveytypelookup.feature",
    "Test(surveytype) to check for duplicate records in UCDM table",
)
def test_to_check_for_duplicate_records_in_ucdm_table_for_surveyquestions():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate duplicate records in UCDM table for surveytype')
def validate_duplicate_records_in_ucdm_table_surveyquestions(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[SurveyQuestions]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*), SurveyID,surveysk from [qualtrics_domestic_res].[SurveyQuestions]
                    where currentflag=1 group by SurveyID,surveysk having count(*) >1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_surveytypelookup
@scenario(
    "../../features/qualtrics_surveytypelookup.feature",
    "Test(surveytype) to validate the data in Staging and UCDM tables are as per transformation logic",
)
def test_to_validate_the_data_in_Staging_and_UCDM_tables_are_as_per_transformation_logic_for_surveyquestions():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the primary key in Ucdm table for surveytype for surveytype')
def validate_primary_key_in_ucdm_for_surveyquestions(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[SurveyQuestions]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*)  from [qualtrics_domestic_res].[SurveyQuestions] where surveyid is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_surveytypelookup
@scenario(
    "../../features/qualtrics_surveytypelookup.feature",
    "Test(surveytype) to validate the date fields in the UCDM tables for date format and correctness",
)
def test_to_validate_the_date_fields_in_the_UCDM_tables_for_date_format_and_correctness_for_surveyquestions():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate surveyQuestions fields in the UCDM tables for date format and correctness for surveytype')
def validate_surveyquestions_fields_in_the_UCDM_tables_for_date_format_and_correctness_for_surveyquestions(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[SurveyQuestions]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*)  from [qualtrics_domestic_res].[SurveyQuestions] where questionid is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate the SurveyID column is not null in ucdm table",
)
def test_to_validate_surveyid_is_not_null_for_responsemetadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate SurveyId column is not null in ucdm table')
def validate_surveyid_is_not_null_in_ucdm_for_responsemetadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[ResponseMetaData]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [qualtrics_domestic_res].[ResponseMetaData]  where surveyid is  null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate the SurveyName column is not null in ucdm table",
)
def test_to_validate_surveyname_is_not_null_for_responsemetadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate SurveyName column is not null in ucdm table')
def validate_surveyname_is_not_null_in_ucdm_for_responsemetadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[ResponseMetaData]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [qualtrics_domestic_res].[ResponseMetaData]  where surveyname is  null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to check duplicates for ResponseID",
)
def test_to_check_duplicates_for_responseid_for_responsemetadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate if there were any duplicates for ResponseID')
def validate_if_there_are_any_duplicates_for_responseid_for_responsemetadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[ResponseMetaData]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) as ct from (select 1 as ct from [qualtrics_domestic_res].[ResponseMetaData]  where currentflag=1  
                   group by responseid having count(*)>1) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics relationship response metadata",
)
def test_to_validate_qualtrics_relationship_response_metadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics relationship response metadata')
def validate_qualtrics_relationship_response_metadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.qualtrics_relationship")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( 
                    select top 10 stg.SurveyID stg_SurveyID, tgt.surveyID tgt_SurveyID, tgt.surveyname, stg.[_recordId] stg_ResponseID, tgt.ResponseID tgt_ResponseID,  
                    stg.recipientEmail stg_recipientEmail, tgt.recipientEmail as tgt_recipientEmail 
                    from stg.qualtrics_relationship stg  inner join [qualtrics_domestic_res].[ResponseMetaData] tgt on stg.[_recordId]	= tgt.ResponseID  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_relationship' AND	Status= 'success')) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics pcw response metadata",
)
def test_to_validate_qualtrics_pcw_response_metadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics pcw response metadata')
def validate_qualtrics_pcw_response_metadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.qualtrics_pcw")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( 
                    select top 10 stg.SurveyID stg_SurveyID, tgt.surveyID tgt_SurveyID, tgt.surveyname, stg.[_recordId] stg_ResponseID, tgt.ResponseID tgt_ResponseID,  
                    stg.recipientEmail stg_recipientEmail, tgt.recipientEmail as tgt_recipientEmail 
                    from stg.qualtrics_pcw stg  inner join [qualtrics_domestic_res].[ResponseMetaData] tgt on stg.[_recordId]	= tgt.ResponseID  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_pcw' AND	Status= 'success')) A '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics onesurvey response metadata",
)
def test_to_validate_qualtrics_onesurvey_response_metadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics onesurvey response metadata')
def validate_qualtrics_onesurvey_response_metadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.qualtrics_onesurvey")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( 
                    select top 10 stg.SurveyID stg_SurveyID, tgt.surveyID tgt_SurveyID, tgt.surveyname, stg.[_recordId] stg_ResponseID, tgt.ResponseID tgt_ResponseID,  
                    stg.recipientEmail stg_recipientEmail, tgt.recipientEmail as tgt_recipientEmail 
                    from stg.qualtrics_onesurvey stg  inner join [qualtrics_domestic_res].[ResponseMetaData] tgt on stg.[_recordId]	= tgt.ResponseID  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_onesurvey' AND	Status= 'success')) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics complaints response metadata",
)
def test_to_validate_qualtrics_complaints_response_metadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics complaints response metadata')
def validate_qualtrics_complaints_response_metadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.qualtrics_complaints")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( 
                    select top 10 stg.SurveyID stg_SurveyID, tgt.surveyID tgt_SurveyID, tgt.surveyname, stg.[_recordId] stg_ResponseID, tgt.ResponseID tgt_ResponseID,  
                    stg.recipientEmail stg_recipientEmail, tgt.recipientEmail as tgt_recipientEmail 
                    from stg.qualtrics_complaints stg  inner join [qualtrics_domestic_res].[ResponseMetaData] tgt on stg.[_recordId]	= tgt.ResponseID  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_complaints' AND	Status= 'success')) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics registrations response metadata",
)
def test_to_validate_qualtrics_registrations_response_metadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics registrations response metadata')
def validate_qualtrics_registrations_response_metadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from stg.qualtrics_registrations")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from ( 
                    select top 10 stg.SurveyID stg_SurveyID, tgt.surveyID tgt_SurveyID, tgt.surveyname, stg.[_recordId] stg_ResponseID, tgt.ResponseID tgt_ResponseID,  
                    stg.recipientEmail stg_recipientEmail, tgt.recipientEmail as tgt_recipientEmail 
                    from stg.qualtrics_registrations stg  inner join [qualtrics_domestic_res].[ResponseMetaData] tgt on stg.[_recordId]	= tgt.ResponseID  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_registrations' AND	Status= 'success')) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate Missing Responses",
)
def test_to_validate_missing_responses_for_responsemetadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate Missing Responses')
def validate_missing_responses_for_responsemetadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[Responses]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select  count(*)  from [qualtrics_domestic_res].[Responses] r 
                    right join [qualtrics_domestic_res].[ResponseMetaData] rm on r.ResponseID= rm.ResponseID    
                    where r.ResponseID is null '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics complaints between External and Staging tables",
)
def test_to_validate_qualtrics_complaints_between_External_and_Staging_tables_for_responsemetadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics complaints between External and Staging tables')
def validate_qualtrics_complaints_between_External_and_Staging_tables_for_responsemetadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.[qualtrics_complaints]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) ct from (select top 10 1 as ct 
                    from ext.[qualtrics_complaints] ext  inner join stg.[qualtrics_complaints] stg on ext.[_recordId]	= stg.[_recordId]  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_complaints' AND	Status= 'success')) A'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics onesurvey between External and Staging tables",
)
def test_to_validate_qualtrics_onesurvey_between_External_and_Staging_tables_for_responsemetadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics onesurvey between External and Staging tables')
def validate_qualtrics_onesurvey_between_External_and_Staging_tables_for_responsemetadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.qualtrics_onesurvey")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = ''' select count(*) ct from (select top 10 1 as ct 
                    from ext.qualtrics_onesurvey ext  inner join stg.qualtrics_onesurvey stg on ext.[_recordId]	= stg.[_recordId]  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_onesurvey' AND	Status= 'success')) A '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics pcw between External and Staging tables",
)
def test_to_validate_qualtrics_pcw_between_External_and_Staging_tables_for_responsemetadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics pcw between External and Staging tables')
def validate_qualtrics_pcw_between_External_and_Staging_tables_for_responsemetadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.qualtrics_pcw")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) ct from (select top 10 1 as ct 
                    from ext.qualtrics_pcw ext  inner join stg.qualtrics_pcw stg on ext.[_recordId]	= stg.[_recordId]  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_pcw' AND	Status= 'success')) A '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics registrations between External and Staging tables",
)
def test_to_validate_qualtrics_registrations_between_External_and_Staging_tables_for_responsemetadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics registrations between External and Staging tables')
def validate_qualtrics_registrations_between_External_and_Staging_tables_for_responsemetadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.qualtrics_registrations")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) ct from (select top 10 1 as ct 
                    from ext.qualtrics_registrations ext  inner join stg.qualtrics_registrations stg on ext.[_recordId]	= stg.[_recordId]  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_registrations' AND	Status= 'success')) A '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsemetadata
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test to validate qualtrics relationship between External and Staging tables",
)
def test_to_validate_qualtrics_relationship_between_External_and_Staging_tables_for_responsemetadata():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate qualtrics relationship between External and Staging tables')
def validate_qualtrics_relationship_between_External_and_Staging_tables_for_responsemetadata(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from ext.qualtrics_relationship")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) ct from (select top 10 1 as ct 
                    from ext.qualtrics_relationship ext  inner join stg.qualtrics_relationship stg on ext.[_recordId]	= stg.[_recordId]  
                    where stg.load_date_time >= (SELECT ISNULL(MAX(EndDateTime),'2000-01-01 00:00:00') AS EndDateTime 	FROM	ctl.LoadLog 
                            WHERE TableName= 'qualtrics_domestic_res.ResponseMetaData' AND	SourceTableName = 'stg.qualtrics_relationship' AND	Status= 'success')) A '''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] > 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to validate the table structure of UCDM ResponseScoreLookup table",
)
def test_to_validate_the_table_structure_of_UCDM_ResponseScoreLookup_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate UCDM ResponseScoreLookup table')
def validate_table_structure_of_external_tables_for_UCDM_ResponseScoreLookup_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [qualtrics_domestic_res].[ResponseScoreLookup]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) FROM [qualtrics_domestic_res].[ResponseScoreLookup]'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row[0] != 0 or row[0] != None:
            assert True
        else:
            assert False 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to validate the primary key is not null in UCDM table",
)
def test_to_validate_the_primarykey_is_not_null_in_UCDM_table_for_responsescorelookup():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate primary key is not null in UCDM table')
def validate_primary_key_in_ucdm_for_responsescorelookup(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [qualtrics_domestic_res].[ResponseScoreLookup]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) FROM [qualtrics_domestic_res].[ResponseScoreLookup] where responseid is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to check duplicate responseid",
)
def test_to_check_duplicate_responseid_in_ucdm_table_for_responsescorelookup():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate duplicate responseid in UCDM table')
def validate_duplicate_responseid_in_ucdm_table_responsescorelookup(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [qualtrics_domestic_res].[ResponseScoreLookup]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*),responseid FROM [qualtrics_domestic_res].[ResponseScoreLookup] group by responseid having count(*) >1'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            assert False
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to validate the CreatedDate column is not null in ucdm table",
)
def test_to_validate_the_CreatedDateColumn_is_not_null_in_UCDM_table_for_responsescorelookup():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate CreatedDate column is not null in ucdm table')
def validate_CreatedDateColumn_in_ucdm_table_responsescorelookup(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("SELECT count(*) FROM [qualtrics_domestic_res].[ResponseScoreLookup]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''SELECT count(*) FROM [qualtrics_domestic_res].[ResponseScoreLookup] where [CreatedDate] is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0

    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to validate the responses between the Responses table and ResponseScoreLookup table",
)
def test_to_validate_the_responses_between_the_Responses_table_and_ResponseScoreLookup_table():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate the responses between the Responses table and ResponseScoreLookup table')
def validate_responses_between_the_Responses_table_and_ResponseScoreLookup_table(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [qualtrics_domestic_res].[Responses]")
    data_responses = cursor.fetchone()   
    cursor.execute("select count(*) FROM [qualtrics_domestic_res].[ResponseScoreLookup]")
    data_responsesscorelookup = cursor.fetchone()
    #print(data)
    if data_responses[0] != 0 and data_responsesscorelookup[0] != 0:
        query = '''SELECT count(*)
        FROM [qualtrics_domestic_res].[Responses] response
        left join [qualtrics_domestic_res].[ResponseScoreLookup] Rscore
        on response.ResponseID=Rscore.ResponseID'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row[0]==0:
            assert False 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to validate the recordId column is not null in staging qualtrics registrations table",
)
def test_to_check_recordId_column_is_not_null_in_stg_qualtrics_registrations_table_for_responsescorelookup():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate recordId column is not null in staging qualtrics registrations table')
def validate_recordId_column_is_not_null_in_stg_qualtrics_registrations_for_responsescorelookup(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].[qualtrics_registrations]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [stg].[qualtrics_registrations] where _recordId  is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0        
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to validate the recordId column is not null in staging qualtrics pcw table",
)
def test_to_check_recordId_column_is_not_null_in_stg_qualtrics_pcw_table_for_responsescorelookup():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate recordId column is not null in staging qualtrics pcw table')
def validate_recordId_column_is_not_null_in_stg_qualtrics_pcw_for_responsescorelookup(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].[qualtrics_pcw]")
    data = cursor.fetchone()

    if data[0] != 0:
        query = '''select count(*) from [stg].[qualtrics_pcw] where _recordId is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to validate the recordId column is not null in staging qualtrics complaints table",
)
def test_to_check_recordId_column_is_not_null_in_stg_qualtrics_complaints_table_for_responsescorelookup():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate recordId column is not null in staging qualtrics complaints table')
def validate_recordId_column_is_not_null_in_stg_qualtrics_complaints_for_responsescorelookup(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [stg].[qualtrics_complaints]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [stg].[qualtrics_complaints] where _recordId is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0

    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to validate the table structure of UCDM Responses table",
)
def test_to_validate_the_table_structure_of_UCDM_Responses_table_for_responsescorelookup():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate UCDM Responses table')
def validate_the_table_structure_of_UCDM_Responses_table_for_responsescorelookup(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [qualtrics_domestic_res].[Responses]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) FROM [qualtrics_domestic_res].[Responses]'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row[0] == 0:
            assert False 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_responsescorelookup
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(ResponseScoreLookup) to validate the unique SurveyName count in UCDM table",
)
def test_to_check_for_unique_SurveyName_count_in_ucdm_table_for_responsescorelookup():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate unique SurveyName count in UCDM table')
def validate_unique_SurveyName_count_in_ucdm_table_for_responsescorelookup(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [qualtrics_domestic_res].[ResponseMetaData]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(distinct [SurveyName]) from [qualtrics_domestic_res].[ResponseMetaData]'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row[0] != 5:
            assert False 
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_incremental
@scenario(
    "../../features/qualtrics_questiontypelookup.feature",
    "Test(Incremental) to validate responses table incremental load for qualtrics",
)
def test_to_validate_responses_table_incremental_load_for_qualtrics():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate responses table incremental load for qualtrics')
def validate_responses_table_incremental_load_for_qualtrics(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[Responses]")
    data = cursor.fetchone()
    if data[0] != 0:
        query = '''select count(*) from (select distinct responseid,questionid
        from [qualtrics_domestic_res].[Responses] where Currentflag =1 ) a
        except
        select count(*) from (select distinct responseid,questionid
        from [qualtrics_domestic_res].[Responses] ) a'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert False
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_incremental
@scenario(
    "../../features/qualtrics_responsemetadata.feature",
    "Test(Incremental) to validate ResponseMetaData table incremental load for qualtrics",
)
def test_to_validate_ResponseMetaData_table_incremental_load_for_qualtrics():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate ResponseMetaData table incremental load for qualtrics')
def validate_ResponseMetaData_table_incremental_load_for_qualtrics(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[ResponseMetaData]")
    data = cursor.fetchone()
    if data[0] != 0:
        query = '''select count(*) from ( SELECT distinct SurveyID, responseid
        FROM [qualtrics_domestic_res].[ResponseMetaData] where currentflag =1) b
        except
        select count(*) from ( SELECT distinct SurveyID, responseid
        FROM [qualtrics_domestic_res].[ResponseMetaData]) b'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert False
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_incremental
@scenario(
    "../../features/qualtrics_responsescorelookup.feature",
    "Test(Incremental) to validate ResponseScoreLookup table incremental load for qualtrics",
)
def test_to_validate_ResponseScoreLookup_table_incremental_load_for_qualtrics():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate ResponseScoreLookup table incremental load for qualtrics')
def validate_ResponseScoreLookup_table_incremental_load_for_qualtrics(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[ResponseScoreLookup]")
    data = cursor.fetchone()
    if data[0] != 0:
        query = '''select count(*) from (select distinct responseid from 
        [qualtrics_domestic_res].[ResponseScoreLookup] where currentflag =1) c
        except
        select count(*) from (select distinct responseid from 
        [qualtrics_domestic_res].[ResponseScoreLookup] ) c'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert False
    else: 
        assert False    
    cursor.close()

@pytest.mark.qualtrics
@pytest.mark.qualtrics_incremental
@scenario(
    "../../features/qualtrics_surveytypelookup.feature",
    "Test(Incremental) to validate SurveyQuestions table incremental load for qualtrics",
)
def test_to_validate_SurveyQuestions_table_incremental_load_for_qualtrics():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate SurveyQuestions table incremental load for qualtrics')
def validate_SurveyQuestions_table_incremental_load_for_qualtrics(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [qualtrics_domestic_res].[SurveyQuestions]")
    data = cursor.fetchone()
    if data[0] != 0:
        query = '''select count(*) from (SELECT distinct SurveyID      
        FROM [qualtrics_domestic_res].[SurveyQuestions] where currentflag =1) c
        except
        select count(*) from (SELECT distinct SurveyID      
        FROM [qualtrics_domestic_res].[SurveyQuestions] ) c'''
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert False
    else: 
        assert False    
    cursor.close()