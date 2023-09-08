import mysql.connector as mysql
import pandas as pd

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="Balaji@1999",
)
mycursor = mydb.cursor()

def migrate_to_mysql():
    mycursor.execute("create table top_district_country(year int,quarter int,district varchar(40),transaction_count bigint)")
    df = pd.read_csv("./csv_files/top_district_country.csv")
    for index,row in df.iterrows():
        mycursor.execute("INSERT INTO top_district_country VALUES(%s,%s,%s,%s)",(row[0],row[1],row[2],row[3]))
    mydb.commit()

    mycursor.execute("create table top_district_state(state varchar(45),year int,quarter int,disctrict_name varchar(30),transaction_count bigint)")
    df = pd.read_csv("./csv_files/top_district_state.csv")
    for index,row in df.iterrows():
        mycursor.execute("INSERT INTO top_district_state VALUES(%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4]))
    mydb.commit()

    mycursor.execute("CREATE TABLE top_pincode_country(year int,quarter int,pincode bigint,transaction_count bigint)")
    df = pd.read_csv("./csv_files./top_pincode_country.csv")
    for index,row in df.iterrows():
        mycursor.execute("INSERT INTO top_pincode_country VALUES(%s,%s,%s,%s)",(row[0],row[1],row[2],row[3]))
    mydb.commit()

    mycursor.execute("CREATE TABLE top_pincode_state(state varchar(45),year int,quarter int,postal_code varchar(25),transaction_count bigint)")
    df = pd.read_csv("./csv_files/top_pincode_state.csv")
    df = df.fillna('')
    for index,row in df.iterrows():
        mycursor.execute("INSERT INTO top_pincode_state VALUES(%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4]))
    mydb.commit()

    mycursor.execute("CREATE TABLE top_state_country(year int,quarter int,state varchar(45),transaction_count bigint)")
    df = pd.read_csv("./csv_files/top_state_country.csv")
    for index,row in df.iterrows():
        mycursor.execute("INSERT INTO top_state_country VALUES(%s,%s,%s,%s)",(row[0],row[1],row[2],row[3]))
    mydb.commit()

    mycursor.execute("CREATE TABLE transaction_data_district(state varchar(45),year int,quarter int,district varchar(45),transaction_count bigint,transaction_amount bigint)")
    df = pd.read_csv("./csv_files/transaction_data_district.csv")
    for index,row in df.iterrows():
        mycursor.execute("INSERT INTO transaction_data_district VALUES(%s,%s,%s,%s,%s,%s)",tuple(row))
    mydb.commit()

    mycursor.execute("CREATE TABLE transaction_data_state(year int,quarter int,state varchar(45),transaction_count bigint,transaction_amount bigint)")
    df = pd.read_csv("./csv_files/transaction_data_state.csv")
    for index,row in df.iterrows():
        mycursor.execute("INSERT INTO transaction_data_state VALUES(%s,%s,%s,%s,%s)",tuple(row))
    mydb.commit()

    mycursor.execute("CREATE TABLE transaction_type_state(state varchar(45),year int,quarter int,transaction_type varchar(30),transaction_count bigint,transaction_amount bigint)")
    df = pd.read_csv("./csv_files/transaction_type_state.csv")
    for index,row in df.iterrows():
        mycursor.execute("INSERT INTO transaction_type_state VALUES(%s,%s,%s,%s,%s,%s)",tuple(row))
    mydb.commit()

    mycursor.execute("CREATE TABLE transaction_type_country(year int,quarter int,transaction_type varchar(30),transaction_count bigint,transaction_amount bigint)")
    df = pd.read_csv("./csv_files/transaction_type_year.csv")
    for index,row in df.iterrows():
        mycursor.execute("INSERT INTO transaction_type_country VALUES(%s,%s,%s,%s,%s)",tuple(row))
    mydb.commit()

    df = pd.read_csv('./csv_files/user_data/aggregated_user_state.csv')
    mycursor.execute("CREATE TABLE user_state(state varchar(40),year int,quarter int,registeredUsers bigint,appOpens bigint)")
    for index,rows in df.iterrows():
        mycursor.execute("INSERT INTO user_state VALUES(%s,%s,%s,%s,%s)",tuple(rows))
    mydb.commit()

    df = pd.read_csv('./csv_files/user_data/user_map_state.csv')
    mycursor.execute("CREATE TABLE user_map_state(state varchar(40),year int,quarter int,District varchar(40),registeredUsers bigint,appOpens bigint)")
    for index,rows in df.iterrows():
        mycursor.execute("INSERT INTO user_map_state VALUES(%s,%s,%s,%s,%s,%s)",tuple(rows))
    mydb.commit()

    df = pd.read_csv('./csv_files/user_data/top_user_pincode_state.csv')
    mycursor.execute("CREATE TABLE top_user_pincode_state(state varchar(40),year int,quarter int,pincode varchar(20),registeredUsers bigint)")
    for index,rows in df.iterrows():
        mycursor.execute("INSERT INTO top_user_pincode_state VALUES(%s,%s,%s,%s,%s)",tuple(rows))
    mydb.commit()

    df = pd.read_csv('./csv_files/user_data/top_user_district_state.csv')
    mycursor.execute("CREATE TABLE top_user_district_state(state varchar(40),year int,quarter int,district varchar(40),registeredUsers bigint)")
    for index,rows in df.iterrows():
        mycursor.execute("INSERT INTO top_user_district_state VALUES(%s,%s,%s,%s,%s)",tuple(rows))
    mydb.commit()

    df = pd.read_csv('./csv_files/user_data/agg_users_country.csv')
    mycursor.execute("CREATE TABLE users_country(year int,quarter int,registeredUsers bigint,appOpens bigint)")
    for index,rows in df.iterrows():
        mycursor.execute("INSERT INTO users_country VALUES(%s,%s,%s,%s)",tuple(rows))
    mydb.commit()

    # No need to include
    # df = pd.read_csv('./csv_files/user_data/user_data_state.csv')
    # mycursor.execute("CREATE TABLE user_state(state varchar(40),year int,quarter int,registeredUsers bigint,appOpens bigint)")
    # for index,rows in df.iterrows():
    #     mycursor.execute("INSERT INTO user_state VALUES(%s,%s,%s,%s,%s)",tuple(rows))
    # mydb.commit()

    df = pd.read_csv('./csv_files/user_data/top_state_country.csv')
    mycursor.execute("CREATE TABLE top_user_state_country(year int,quarter int,state varchar(40),registeredUsers bigint)")
    for index,rows in df.iterrows():
        mycursor.execute("INSERT INTO top_user_state_country VALUES(%s,%s,%s,%s)",tuple(rows))
    mydb.commit()

    df = pd.read_csv('./csv_files/user_data/top_district_country.csv')
    mycursor.execute("CREATE TABLE top_user_district_country(year int,quarter int,district varchar(40),registeredUsers bigint)")
    for index,rows in df.iterrows():
        mycursor.execute("INSERT INTO top_user_district_country VALUES(%s,%s,%s,%s)",tuple(rows))
    mydb.commit()

    df = pd.read_csv('./csv_files/user_data/top_pincode_country.csv')
    mycursor.execute("CREATE TABLE top_user_pincode_country(year int,quarter int,pincode varchar(20),registeredUsers bigint)")
    for index,rows in df.iterrows():
        mycursor.execute("INSERT INTO top_user_pincode_country VALUES(%s,%s,%s,%s)",tuple(rows))
    mydb.commit()

def get_db_list():
    db_list=[]
    mycursor.execute("SHOW DATABASES")
    for each in mycursor:
        db_list.append(each[0])
    return db_list

def transfer():
    if 'phonepe_data_analysis' not in get_db_list():
        mycursor.execute("CREATE DATABASE phonepe_data_analysis")
        mycursor.execute("use phonepe_data_analysis")
        migrate_to_mysql()

if __name__ == '__main__':
    print("Migrating data to MYSQL.....")
    transfer()
