import mysql.connector as connection
import numpy as np
import pandas as pd
import os


def sheet_name(excel_file):
    """Getting all sheet names"""
    sheet_names = []
    for sheet in pd.ExcelFile(excel_file).sheet_names:
        sheet_names.append(sheet)
    return sheet_names


def create_dataframe(excel_file, sheets):
    """Creating dataframe for each sheet"""
    dframe = {}
    for sheet in sheets:
        try:
            #appending file name to the path
            dframe[sheet] = pd.read_excel(excel_file, sheet_name=sheet)
        except UnicodeDecoderError:
            dframe[sheet] = pd.read_excel(excel_file, sheet_name=sheet, encoding='ISO-8859-1')
            
        except Exception as e:
            print(e)

    return dframe


def clean_table_name(sheet_name):
    """Removing all unnecessary symbols from sheet name"""
    clean_table_name = sheet_name.lower().replace(" ","_").replace("-","_")
    
    table_name = '{}'.format(clean_table_name)
    return table_name


def clean_column_name(dataframe):
    """Generating column names with datatype"""
   
    dataframe.columns = [c.lower().replace(" ","_").replace("-","").replace("$","") for c in dataframe.columns]
    
    #convert datatypes to sql datatypes 
    replace_dtype = {
        'object' : 'varchar(100)',
        'float64' : 'float',
        'int64' : 'int',
        'datetime64[ns]' : 'varchar(50)',
        'timedelta64[ns]': 'varchar'
    }
    
    col_name = ', '.join("`{}` {}".format(n, d) for (n, d) in zip(dataframe.columns, dataframe.dtypes.replace(replace_dtype)))
  
    return col_name, dataframe.columns


def insert_into_db(host, db_name, user, passwd, table_name, column_name, file, dataframe, df_columns):
    """- Connecting to database 
    - Create table, insert values"""
    try:
        conn = connection.connect(host=host, user=user, passwd=passwd, database=db_name, use_pure=True, \
                                  autocommit=True)
        cursor = conn.cursor()
        print('** opened database successfully **')

        #drop table with same name
        cursor.execute("drop table if exists %s;" %(table_name))
        
        #create table
        cursor.execute("create table %s (%s);" %(table_name, column_name))
        print('** {} created successfully **'.format(table_name))

        ## insert values into the table
        for i,row in dataframe.iterrows():

            #string variable to generate '%s' for each column
            n = len(column_name.split(','))
            string = ", ".join('%s' for i in range(n))

            query = "INSERT INTO {t} VALUES({s})".format(t=table_name,s=string)

            cursor.execute(query, tuple(row))
    
    except Exception as e:
        print(e)
        
    
    cursor.close()
    conn.close()
    return
    

