import pytest
import pyodbc
from pytest_bdd import given, when, then, scenario, parsers
from functools import partial
from python_settings import settings
import pytest_bdd

@pytest.mark.experian
@pytest.mark.experian_TypeLookUp
@scenario(
    "../../features/experian_variables.feature",
    "Test(Mosaic) to validate data between external and staging table are matching for TypeLookUp table",
)
def test_to_validate_data_between_external_and_staging_table_are_matching_for_experian_TypeLookUp():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between external and staging table for TypeLookUp table')
def validate_data_between_external_and_staging_table_are_matching_for_experian_TypeLookUp(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [ext].[mosaic_types]")
    data_external_typelookup = cursor.fetchone()   
    cursor.execute("select count(*) FROM [stg].[mosaic_types]")
    data_staging_typelookup = cursor.fetchone()
    if data_external_typelookup[0] != 0 and data_staging_typelookup[0] != 0:
        query = '''SELECT [MosaicType],[TypeDescription] FROM [ext].[mosaic_types]
        except
        SELECT [MosaicType],[TypeDescription] FROM [stg].[mosaic_types]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.experian
@pytest.mark.experian_TypeLookUp
@scenario(
    "../../features/experian_variables.feature",
    "Test(Mosaic) to validate data between staging and UCDM table are matching for TypeLookUp table",
)
def test_to_validate_data_between_staging_and_UCDM_table_are_matching_for_experian_TypeLookUp():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between staging and UCDM table for TypeLookUp table')
def validate_data_between_staging_and_UCDM_table_are_matching_for_experian_TypeLookUp(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [stg].[mosaic_types]")
    data_staging_typelookup = cursor.fetchone()   
    cursor.execute("select count(*) FROM [mosaic_energia_res].[Mosaic_Types]")
    data_UCDM_typelookup = cursor.fetchone()
    if data_staging_typelookup[0] != 0 and data_UCDM_typelookup[0] != 0:
        query = '''SELECT [MosaicType],[TypeDescription] FROM [stg].[mosaic_types]
        except
        SELECT [MosaicType],[TypeDescription] FROM [mosaic_energia_res].[Mosaic_Types]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.experian
@pytest.mark.experian_GroupLookUp
@scenario(
    "../../features/experian_variables.feature",
    "Test(Mosaic) to validate data between external and staging table are matching for GroupLookUp table",
)
def test_to_validate_data_between_external_and_staging_table_are_matching_for_experian_GroupLookUp():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between external and staging table for GroupLookUp table')
def validate_data_between_external_and_staging_table_are_matching_for_experian_GroupLookUp(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [ext].[mosaic_groups]")
    data_external_grouplookup = cursor.fetchone()   
    cursor.execute("select count(*) FROM [stg].[mosaic_groups]")
    data_staging_grouplookup = cursor.fetchone()
    if data_external_grouplookup[0] != 0 and data_staging_grouplookup[0] != 0:
        query = '''SELECT [MosaicGroup] ,[GroupDescription] FROM [ext].[mosaic_groups]
        except
        SELECT  [MosaicGroup] ,[GroupDescription] FROM [stg].[mosaic_groups]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.experian
@pytest.mark.experian_GroupLookUp
@scenario(
    "../../features/experian_variables.feature",
    "Test(Mosaic) to validate data between staging and UCDM table are matching for GroupLookUp table",
)
def test_to_validate_data_between_staging_and_UCDM_table_are_matching_for_experian_GroupLookUp():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between staging and UCDM table for GroupLookUp table')
def validate_data_between_staging_and_UCDM_table_are_matching_for_experian_GroupLookUp(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [stg].[mosaic_groups]")
    data_staging_typelookup = cursor.fetchone()   
    cursor.execute("select count(*) FROM [mosaic_energia_res].[Mosaic_Groups]")
    data_UCDM_typelookup = cursor.fetchone()
    if data_staging_typelookup[0] != 0 and data_UCDM_typelookup[0] != 0:
        query = '''SELECT [MosaicGroup] ,[GroupDescription] FROM [stg].[mosaic_groups]
        except
        SELECT [MosaicGroup] ,[GroupDescription] FROM [mosaic_energia_res].[Mosaic_Groups]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.experian
@pytest.mark.experian_Mosaic
@scenario(
    "../../features/experian_variables.feature",
    "Test(Mosaic) to validate data between external and staging table are matching for Mosaic table",
)
def test_to_validate_data_between_external_and_staging_table_are_matching_for_experian_Mosaic():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between external and staging table for Mosaic table')
def validate_data_between_external_and_staging_table_are_matching_for_experian_Mosaic(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [ext].[mosaic_experian]")
    data_external_Mosaic = cursor.fetchone()   
    cursor.execute("select count(*) FROM [stg].[mosaic_experian]")
    data_staging_Mosaic = cursor.fetchone()
    if data_external_Mosaic[0] != 0 and data_staging_Mosaic[0] != 0:
        query = '''SELECT
        [PremiseID] ,[PersonID] ,[Address1] ,[Address2] ,[Address3] ,[Address4] ,[City] ,[Postcode] ,[County] 
        ,[SmallAreaBoundaryID] ,[MosaicGroup] ,[MosaicType] ,[MosaicTypeDescr] ,[Factor1Score] ,[Factor2Score] 
        ,[Factor3Score] ,[Factor4Score] ,[Factor5Score] ,[Factor6Score] ,[Factor1Percentage] ,[Factor2Percentage] 
        ,[Factor3Percentage] ,[Factor4Percentage] ,[Factor5Percentage] ,[Factor6Percentage] ,[Factor1Decimal] 
        ,[Factor2Decimal] ,[Factor3Decimal] ,[Factor4Decimal] ,[Factor5Decimal] ,[Factor6Decimal]
        FROM [stg].[mosaic_experian]
        except
        SELECT
        [PremiseID] ,[PersonID] ,[Address1] ,[Address2] ,[Address3] ,[Address4] ,[City] ,[Postcode] 
        ,[County] ,[SmallAreaBoundaryID] ,[MosaicGroup] ,[MosaicType]
        ,case when [MosaicTypeDescr] ='' or [MosaicTypeDescr] = 'NULL' then NULL ELSE [MosaicTypeDescr] END as [MosaicTypeDescr]
        ,case when [Factor1Score] ='' or [Factor1Score] = 'NULL' then NULL ELSE [Factor1Score] END as [Factor1Score]
        ,case when [Factor2Score]='' or [Factor2Score]= 'NULL' then NULL ELSE [Factor2Score] END as [Factor2Score]
        ,case when [Factor3Score] ='' or [Factor3Score] = 'NULL' then NULL ELSE [Factor3Score] END as [Factor3Score]
        ,case when [Factor4Score] ='' or [Factor4Score] = 'NULL' then NULL ELSE [Factor4Score] END as [Factor4Score]
        ,case when [Factor5Score] ='' or [Factor5Score] = 'NULL' then NULL ELSE [Factor5Score] END as [Factor5Score]
        ,case when [Factor6Score] ='' or [Factor6Score] = 'NULL' then NULL ELSE [Factor6Score] END as [Factor3Score]
        ,case when [Factor1Percentage] ='' or [Factor1Percentage] = 'NULL' then NULL ELSE [Factor1Percentage] END as [Factor1Percentage]
        ,case when [Factor2Percentage] ='' or [Factor2Percentage] = 'NULL' then NULL ELSE [Factor2Percentage] END as [Factor2Percentage]
        ,case when [Factor3Percentage] ='' or [Factor3Percentage] = 'NULL' then NULL ELSE [Factor3Percentage] END as [Factor3Percentage]
        ,case when [Factor4Percentage] ='' or [Factor4Percentage] = 'NULL' then NULL ELSE [Factor4Percentage] END as [Factor4Percentage]
        ,case when [Factor5Percentage] ='' or [Factor5Percentage] = 'NULL' then NULL ELSE [Factor5Percentage] END as [Factor5Percentage]
        ,case when [Factor6Percentage] ='' or [Factor6Percentage] = 'NULL' then NULL ELSE [Factor6Percentage] END as [Factor6Percentage]
        ,case when [Factor1Decimal] ='' or [Factor1Decimal] = 'NULL' then NULL ELSE [Factor1Decimal] END as [Factor1Decimal]
        ,case when [Factor2Decimal] ='' or [Factor2Decimal] = 'NULL' then NULL ELSE [Factor2Decimal] END as [Factor2Decimal]
        ,case when [Factor3Decimal] ='' or [Factor3Decimal] = 'NULL' then NULL ELSE [Factor3Decimal] END as [Factor3Decimal]
        ,case when [Factor4Decimal] ='' or [Factor4Decimal] = 'NULL' then NULL ELSE [Factor4Decimal] END as [Factor4Decimal]
        ,case when [Factor5Decimal] ='' or [Factor5Decimal] = 'NULL' then NULL ELSE [Factor5Decimal] END as [Factor5Decimal]
        ,case when [Factor6Decimal] ='' or [Factor6Decimal] = 'NULL' then NULL ELSE [Factor6Decimal] END as [Factor6Decimal]
        FROM [ext].[mosaic_experian]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.experian
@pytest.mark.experian_Mosaic
@scenario(
    "../../features/experian_variables.feature",
    "Test(Mosaic) to validate data between staging and UCDM table are matching for Mosaic table",
)
def test_to_validate_data_between_staging_and_UCDM_table_are_matching_for_experian_Mosaic():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate data are matching between staging and UCDM table for Mosaic table')
def validate_data_between_staging_and_UCDM_table_are_matching_for_experian_Mosaic(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) FROM [stg].[mosaic_experian]")
    data_staging_Mosaic = cursor.fetchone()   
    cursor.execute("select count(*) FROM [mosaic_energia_res].[Mosaic]")
    data_UCDM_Mosaic = cursor.fetchone()
    if data_staging_Mosaic[0] != 0 and data_UCDM_Mosaic[0] != 0:
        query = '''SELECT [PremiseID],[PersonID],[Address1],[Address2],[Address3],[Address4],[City],[Postcode],[County],[SmallAreaBoundaryID],[MosaicGroup],[MosaicType],[Factor1Score],[Factor2Score],[Factor3Score],[Factor4Score],[Factor5Score],[Factor6Score],[Factor1Percentage],[Factor2Percentage],[Factor3Percentage],[Factor4Percentage],[Factor5Percentage],[Factor6Percentage],[Factor1Decimal],[Factor2Decimal],[Factor3Decimal],[Factor4Decimal],[Factor5Decimal],[Factor6Decimal]  
        FROM [mosaic_energia_res].[Mosaic] 
        except 
        SELECT [PremiseID],[PersonID],[Address1],[Address2],[Address3],[Address4],[City],[Postcode],[County],[SmallAreaBoundaryID],[MosaicGroup],[MosaicType],[Factor1Score],[Factor2Score],[Factor3Score],[Factor4Score],[Factor5Score],[Factor6Score],[Factor1Percentage],[Factor2Percentage],[Factor3Percentage],[Factor4Percentage],[Factor5Percentage],[Factor6Percentage],[Factor1Decimal],[Factor2Decimal],[Factor3Decimal],[Factor4Decimal],[Factor5Decimal],[Factor6Decimal]   
        FROM [stg].[mosaic_experian]'''    
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            assert True
        else:
            assert row[0] == 0  
    else: 
        assert False    
    cursor.close()

@pytest.mark.experian
@pytest.mark.experian_Mosaic
@scenario(
    "../../features/experian_variables.feature",
    "Test(Mosaic) to validate primary key is not null in Mosaic table",
)
def test_to_validate_primary_key_is_not_null_in_Mosaic_table_for_experian():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate primary key is not null in Mosaic table')
def validate_primary_key_is_not_null_in_Mosaic_table_for_experian(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [mosaic_energia_res].[Mosaic]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [mosaic_energia_res].[Mosaic] where premiseid is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.experian
@pytest.mark.experian_GroupLookUp
@scenario(
    "../../features/experian_variables.feature",
    "Test(Mosaic) to validate primary key is not null in GroupLookUp table",
)
def test_to_validate_primary_key_is_not_null_in_GroupLookUp_table_for_experian():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate primary key is not null in GroupLookUp table')
def validate_primary_key_is_not_null_in_GroupLookUp_table_for_experian(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [mosaic_energia_res].[Mosaic_Groups]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [mosaic_energia_res].[Mosaic_Groups] where MosaicGroup is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()

@pytest.mark.experian
@pytest.mark.experian_TypeLookUp
@scenario(
    "../../features/experian_variables.feature",
    "Test(Mosaic) to validate primary key is not null in TypeLookUp table",
)
def test_to_validate_primary_key_is_not_null_in_TypeLookUp_table_for_experian():
    pass

@given('I have Database connection details')
def database_connection_details(kv):
    pass

@when('I was able to connect to database')
def database_connection(sql_connection):
    pass

@then('I can validate primary key is not null in TypeLookUp table')
def validate_primary_key_is_not_null_in_TypeLookUp_table_for_experian(sql_connection):
    cursor = sql_connection.cursor()
    cursor.execute("select count(*) from [mosaic_energia_res].[Mosaic_Types]")
    data = cursor.fetchone()
    print(data)
    if data[0] != 0:
        query = '''select count(*) from [mosaic_energia_res].[Mosaic_Types] where MosaicType is null'''
        cursor.execute(query)
        row = cursor.fetchone()
        assert row[0] == 0 
    else: 
        assert False    
    cursor.close()