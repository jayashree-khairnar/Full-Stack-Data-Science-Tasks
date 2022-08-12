import mysql.connector as connection
import numpy as np
import pandas as pd
import os

def csv_file():
    """for getting csv file names"""
    csv_files = []
    for file in os.listdir(os.getcwd()):
        if file.endswith('.csv'):
            csv_files.append(file)
            
    return csv_files


def new_dir(csv_files, dataset_dir):
    """make new directory to process csv files and moving csv files to new folder"""
    try:
        mkdir = 'mkdir {0}'.format(dataset_dir)
        os.system(mkdir)
        
    except:
        pass
    
    for i in csv_files:
        add_file = "mv '{}' {}".format(i, dataset_dir)
        os.system(add_file)
        
    return


    
def create_dataframe(dataset_dir, csv_files):
    """Convert csv files to pandas DataFrame"""
    file_path = os.getcwd()+'/'+dataset_dir+'/'
    
    dframe = {}
    for file in csv_files:
        try:
            #appending file name to the path
            dframe[file] = pd.read_csv(file_path+file)
        except UnicodeDecoderError:
            dframe[file] = pd.read_csv(file_path+file, encoding='ISO-8859-1')
            
    return dframe


def clean_table_name(file_name):
    """rename csv, convert to lowercase, remove unnecessary symbols"""
    #we can add more symbols to remove if required
    clean_table_name = file_name.lower().replace(" ","_").replace("-","_")

    #extract file name
    table_name = '{}'.format(clean_table_name.split('.')[0])
    return table_name


def clean_column_name(dataframe):
    """Clean column names, make it lower case, remove spaces and dashes"""

    dataframe.columns = [c.lower().replace(" ","_").replace("-","").replace("$","") for c in dataframe.columns]

    #convert pandas datatypes to sql datatypes 
    replace_dtype = {
        'object' : 'varchar(100)',
        'float64' : 'float',
        'int64' : 'bigint',
        'datetime64' : 'timestamp'
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
        print('** Opened database successfully **')

        #drop table with same name
        cursor.execute("drop table if exists %s;" %(table_name))

        #create table
        cursor.execute("create table %s (%s);" %(table_name, column_name))
        print('** {} table created successfully **'.format(table_name))

        ## insert values into the table
        for i,row in dataframe.iterrows():

            #string variable to generate '%s' for each column
            n = len(column_name.split(','))
            string = ", ".join('%s' for i in range(n))

            query = "INSERT INTO {0} VALUES({1})".format(table_name,string)

            cursor.execute(query, tuple(row))
    
    except:
        pass
    
    cursor.close()
    conn.close()
    return




