from mysql.connector import connect
import pandas as pd

mydb = connect(
    host='localhost',
    user = 'root',
    password='Balaji@1999'
)
mycursor = mydb.cursor()

mycursor.execute("use phonepe_data_analysis")

# To get the top 10 districts in a country
def top_districts_country(year,quarter):
    mycursor.execute(f"SELECT district,transaction_count FROM top_district_country WHERE year={year} AND quarter={quarter}")
    return (pd.DataFrame(mycursor.fetchall(),columns=['District','Transaction Count']))

# To get the top 10 postal code in a country
def top_pincode_country(year,quarter):
    mycursor.execute(f"SELECT pincode,transaction_count FROM top_pincode_country WHERE year={year} AND quarter={quarter}")
    return (pd.DataFrame(mycursor.fetchall(),columns=['Postal Code','Transaction Count']))

# To get the top 10 states in a country
def top_state_country(year,quarter):
    mycursor.execute(f"SELECT state,transaction_count FROM top_state_country WHERE year={year} AND quarter={quarter}")
    return (pd.DataFrame(mycursor.fetchall(),columns=['State','Transaction Count']))

def top_users_districts_country(year,quarter):
    mycursor.execute(f"SELECT district,registeredUsers FROM top_user_district_country WHERE year={year} and quarter={quarter}")
    return (pd.DataFrame(mycursor.fetchall(),columns=['District','Registered Users']))

# To get the users of top 10 postal code in a country
def top_users_pincode_country(year,quarter):
    mycursor.execute(f"SELECT pincode,registeredUsers FROM top_user_pincode_country WHERE year={year} AND quarter={quarter}")
    return (pd.DataFrame(mycursor.fetchall(),columns=['Postal Code','Registered Users']))

# # To get the user of top 10 states in a country
def top_users_state_country(year,quarter):
    mycursor.execute(f"SELECT state,registeredUsers FROM top_user_state_country WHERE year={year} AND quarter={quarter}")
    return (pd.DataFrame(mycursor.fetchall(),columns=['State','Registered Users']))

# To get the transaction type in a country
def transaction_type_country(year,quarter):
    mycursor.execute(f"SELECT transaction_type,transaction_count FROM transaction_type_country WHERE year={year} AND quarter={quarter}")
    return (pd.DataFrame(mycursor.fetchall()))

def transaction_data_state(year,quarter):
    mycursor.execute(f"SELECT state,transaction_count,transaction_amount,transaction_amount/transaction_count AS average FROM transaction_data_state WHERE year={year} AND quarter={quarter}")
    return (pd.DataFrame(mycursor.fetchall(),columns=['State','Transaction Count','Transaction Value','Average']))

# To get the total transaction/value and avg_value in a country
def avg_transaction_value(year,quarter):
    mycursor.execute(f"SELECT sum(transaction_count) FROM transaction_type_country WHERE year={year} AND quarter={quarter}")
    transaction_count_country = mycursor.fetchone()[0]
    mycursor.execute(f"SELECT sum(transaction_amount) FROM transaction_type_country WHERE year={year} AND quarter={quarter}")
    transaction_value_country = mycursor.fetchone()[0]
    avg_transaction_value_country = transaction_value_country/transaction_count_country
    return {
        'transactions':transaction_count_country,
        'transaction_value':transaction_value_country,
        'avg_transaction':avg_transaction_value_country
    }

# To get the registeredUsers and appOpens
def registered_users(year,quarter):
    mycursor.execute(f'SELECT registeredUsers,appOpens FROM users_country WHERE year={year} AND quarter={quarter}')
    user_data = mycursor.fetchall()
    return {
        'registeredUsers':user_data[0][0],
        'appOpens':user_data[0][1]
    }

# To get registered users in state
def users_state(year,quarter):
    mycursor.execute(f"SELECT state,registeredUsers,appOpens FROM user_state WHERE year={year} AND quarter={quarter}")
    return (pd.DataFrame(mycursor.fetchall(),columns=['State','Registered Users','AppOpens']))
    
def ques1():
    mycursor.execute("select year,quarter,sum(transaction_count) from transaction_type_country group by quarter,year")
    return (pd.DataFrame(mycursor.fetchall(),columns=['year','quarter','transactions']))

def ques2():
    mycursor.execute("SELECT state,registeredUsers FROM top_user_state_country WHERE year=2023 AND quarter=2")
    return(pd.DataFrame(mycursor.fetchall(),columns=['State','Registered Users']))

def ques3():
    mycursor.execute("SELECT year,quarter,registeredUsers FROM users_country")
    return (pd.DataFrame(mycursor.fetchall(),columns=['Year','Quarter','Registered Users']))

def ques4():
    mycursor.execute("SELECT transaction_type,sum(transaction_count) as transaction_count FROM transaction_type_country GROUP BY transaction_type")
    return (pd.DataFrame(mycursor.fetchall(),columns=['Transaction Type','Transaction Count']))

def ques5():
    mycursor.execute("SELECT year,quarter,appOpens FROM users_country")
    return (pd.DataFrame(mycursor.fetchall(),columns=['Year','Quarter','App Opens']))

def ques6():
    mycursor.execute("SELECT state,AVG(transaction_amount/transaction_count) AS average FROM transaction_data_state GROUP BY state ORDER BY average DESC LIMIT 10;")
    return (pd.DataFrame(mycursor.fetchall(),columns=['State','Average']))

def ques7():
    mycursor.execute("SELECT state,sum(transaction_amount) AS value FROM transaction_data_state GROUP BY state ORDER BY value DESC LIMIT 10")
    return (pd.DataFrame(mycursor.fetchall(),columns=['State','Transaction Value']))

def ques8():
    mycursor.execute("SELECT state,SUM(transaction_count) AS value FROM transaction_type_state WHERE transaction_type='Merchant payments' GROUP BY state ORDER BY value DESC LIMIT 10")
    return (pd.DataFrame(mycursor.fetchall(),columns=['State','Transaction Value']))

def ques9():
    mycursor.execute("SELECT state,SUM(appOpens) AS appOpens FROM user_state GROUP BY state ORDER BY appOpens DESC LIMIT 10;")
    return (pd.DataFrame(mycursor.fetchall(),columns=['State','App Opens']))