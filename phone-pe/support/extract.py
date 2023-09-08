import os
import json
import pandas as pd
from git import Repo

def clone_repository():
    url_to_clone = 'https://github.com/PhonePe/pulse.git'
    cloning_path = './github_data'
    if not os.path.exists(cloning_path):
        Repo.clone_from(url_to_clone,cloning_path)

# Extract transaction type in each state/quarter in a year from india
def aggregated_transaction_state(path):
    states = os.listdir(path)
    agg_state_data = {'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
    for each_state in states:
        state_folder_path = path+'/'+each_state
        years = os.listdir(state_folder_path)
        for each_year in years:
            each_year_path = state_folder_path+'/'+each_year
            quarter_data = os.listdir(each_year_path)
            for each_quarter in quarter_data:
                each_quarter_path = each_year_path+'/'+each_quarter
                with open(each_quarter_path) as f:
                    data = f.read()
                for each_type in json.loads(data)["data"]["transactionData"]:
                    agg_state_data['State'].append(each_state)
                    agg_state_data['Year'].append(each_year)
                    agg_state_data['Quarter'].append(each_quarter.strip('.json'))
                    agg_state_data['Transaction_type'].append(each_type["name"])
                    agg_state_data['Transaction_count'].append(each_type["paymentInstruments"][0]["count"])
                    agg_state_data['Transaction_amount'].append(each_type["paymentInstruments"][0]["amount"])
    df = pd.DataFrame(agg_state_data)
    df.to_csv('./csv_files/transaction_type_state.csv',index=False)

# Extract transaction data in each district/quarter in a year from india
def map_state(path):
    states = os.listdir(path)
    agg_district_data = {'State':[], 'Year':[],'Quarter':[],'DistrictName':[], 'Transaction_count':[], 'Transaction_amount':[]}
    for each_state in states:
        state_folder_path = path+'/'+each_state
        years = os.listdir(state_folder_path)
        for each_year in years:
            year_path = state_folder_path+'/'+each_year
            quarter_data = os.listdir(year_path)
            for each_quarter in quarter_data:
                each_quarter_path = year_path+'/'+each_quarter
                with open(each_quarter_path) as f:
                    data=f.read()
                district_data = json.loads(data)["data"]["hoverDataList"]
                for each_data in district_data:
                    agg_district_data['State'].append(each_state)
                    agg_district_data['Year'].append(each_year)
                    agg_district_data['Quarter'].append(each_quarter.strip('.json'))
                    agg_district_data['DistrictName'].append(each_data["name"])
                    agg_district_data['Transaction_count'].append(each_data["metric"][0]["count"])
                    agg_district_data['Transaction_amount'].append(each_data["metric"][0]["amount"])
    df = pd.DataFrame(agg_district_data)
    df.to_csv('./csv_files/transaction_data_district.csv',index=False)

# Extract top 10 postal code in a state/quarter in a year from each state
# Extract top 10 district in a state/quarter in a year from each state
def top_state(path):
    states = os.listdir(path)
    top_disctrict_data = {'State':[], 'Year':[],'Quarter':[],'DistrictName':[], 'Transaction_count':[], 'Transaction_amount':[]}
    top_postal_code_data = {'State':[], 'Year':[],'Quarter':[],'PostalCode':[], 'Transaction_count':[], 'Transaction_amount':[]}
    for each_state in states:
        state_folder_path = path+'/'+each_state
        years = os.listdir(state_folder_path)
        for each_year in years:
            each_year_path = state_folder_path+'/'+each_year
            quarter_data = os.listdir(each_year_path)
            for each_quarter in quarter_data:
                each_quarter_path = each_year_path+'/'+each_quarter
                with open(each_quarter_path) as f:
                    data = f.read()
                for each_data in json.loads(data)["data"]["districts"]:
                    top_disctrict_data["State"].append(each_state)
                    top_disctrict_data["Year"].append(each_year)
                    top_disctrict_data["Quarter"].append(each_quarter.strip('.json'))
                    top_disctrict_data["DistrictName"].append(each_data["entityName"])
                    top_disctrict_data["Transaction_count"].append(each_data["metric"]["count"])
                    top_disctrict_data["Transaction_amount"].append(each_data["metric"]["amount"])
                for each_data in json.loads(data)["data"]["pincodes"]:
                    top_postal_code_data["State"].append(each_state)
                    top_postal_code_data["Year"].append(each_year)
                    top_postal_code_data["Quarter"].append(each_quarter.strip('.json'))
                    top_postal_code_data["PostalCode"].append(each_data["entityName"])
                    top_postal_code_data["Transaction_count"].append(each_data["metric"]["count"])
                    top_postal_code_data["Transaction_amount"].append(each_data["metric"]["amount"])
    df = pd.DataFrame(top_postal_code_data)
    df.to_csv('./csv_files/top_pincode_state.csv',index=False)
    df = pd.DataFrame(top_disctrict_data)
    df.to_csv('./csv_files/top_district_state.csv',index=False)

# Extract transaction type data in a year/quarter from india
def aggregate_transaction_country(path):
    years = os.listdir(path)
    transaction_type = {'Year':[],'Quarter':[],'TransactionType':[], 'Transaction_count':[], 'Transaction_amount':[]}
    for each_year in years:
        each_year_path = path+'/'+each_year
        quarter_data = os.listdir(each_year_path)
        for each_quarter in quarter_data:
            if each_quarter.endswith('.json'):
                each_quarter_path = each_year_path+'/'+each_quarter
                with open(each_quarter_path) as f:
                    data = f.read()
                for each_data in json.loads(data)["data"]["transactionData"]:
                    transaction_type["Year"].append(each_year)
                    transaction_type["Quarter"].append(each_quarter.strip('.json'))
                    transaction_type["TransactionType"].append(each_data["name"])
                    transaction_type["Transaction_count"].append(each_data["paymentInstruments"][0]["count"])
                    transaction_type["Transaction_amount"].append(each_data["paymentInstruments"][0]["amount"])
    df = pd.DataFrame(transaction_type)
    df.to_csv('./csv_files/transaction_type_year.csv',index=False)

# Extract transaction data in a each state/quarter in a year from india
def map_country(path):
    years = os.listdir(path)
    hover_state = {'Year':[],'Quarter':[],'State Name':[], 'Transaction_count':[], 'Transaction_amount':[]}
    for each_year in years:
        each_year_path = path+'/'+each_year
        quarter_data = os.listdir(each_year_path)
        for each_quarter in quarter_data:
            each_quarter_path = each_year_path+'/'+each_quarter
            if os.path.isfile(each_quarter_path):
                with open(each_quarter_path,'r') as f:
                    data = f.read()
                for each_data in json.loads(data)["data"]["hoverDataList"]:
                    hover_state['Year'].append(each_year)
                    hover_state['Quarter'].append(each_quarter.strip('.json'))
                    hover_state['State Name'].append(each_data["name"])
                    hover_state['Transaction_count'].append(each_data["metric"][0]["count"])
                    hover_state['Transaction_amount'].append(each_data["metric"][0]["amount"])
    df = pd.DataFrame(hover_state)
    df.to_csv('./csv_files/transaction_data_state.csv',index=False)

# Extract Top 10 state/quarter in a year from india
# Extract Top 10 district/quarter in a year from india
# Extract Top 10 pincode/quarter in a year from india
def top_in_country(path):
    years = os.listdir(path)
    top_state = {'Year':[],'Quarter':[],'State':[], 'Transaction_count':[], 'Transaction_amount':[]}
    top_district = {'Year':[],'Quarter':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}
    top_pincode = {'Year':[],'Quarter':[],'pincode':[], 'Transaction_count':[], 'Transaction_amount':[]}
    for each_year in years:
        each_year_path = path+'/'+each_year
        quarter_data = os.listdir(each_year_path)
        for each_quarter in quarter_data:
            each_quarter_path = each_year_path+'/'+each_quarter
            if os.path.isfile(each_quarter_path):
                with open(each_quarter_path,'r') as f:
                    data = f.read()
                for each_data in json.loads(data)["data"]["states"]:
                    top_state["Year"].append(each_year)
                    top_state["Quarter"].append(each_quarter.strip('.json'))
                    top_state["State"].append(each_data["entityName"])
                    top_state["Transaction_count"].append(each_data["metric"]["count"])
                    top_state["Transaction_amount"].append(each_data["metric"]["amount"])
                for each_data in json.loads(data)["data"]["districts"]:
                    top_district["Year"].append(each_year)
                    top_district["Quarter"].append(each_quarter.strip('.json'))
                    top_district["District"].append(each_data["entityName"])
                    top_district["Transaction_count"].append(each_data["metric"]["count"])
                    top_district["Transaction_amount"].append(each_data["metric"]["amount"])
                for each_data in json.loads(data)["data"]["pincodes"]:
                    top_pincode["Year"].append(each_year)
                    top_pincode["Quarter"].append(each_quarter.strip('.json'))
                    top_pincode["pincode"].append(each_data["entityName"])
                    top_pincode["Transaction_count"].append(each_data["metric"]["count"])
                    top_pincode["Transaction_amount"].append(each_data["metric"]["amount"])
    
    df = pd.DataFrame(top_state)
    df.to_csv('./csv_files/top_state_country.csv',index=False)
    df = pd.DataFrame(top_district)
    df.to_csv('./csv_files/top_district_country.csv',index=False)
    df = pd.DataFrame(top_pincode)
    df.to_csv('./csv_files/top_pincode_country.csv',index=False)

def aggregated_user_state(path):
    states = os.listdir(path)
    agg_user_data = {'State':[], 'Year':[],'Quarter':[],'registeredUsers':[], 'appOpens':[]}
    for each_state in states:
        state_folder_path = path+'/'+each_state
        years = os.listdir(state_folder_path)
        for each_year in years:
            each_year_path = state_folder_path+'/'+each_year
            quarter_data = os.listdir(each_year_path)
            for each_quarter in quarter_data:
                each_quarter_path = each_year_path+'/'+each_quarter
                with open(each_quarter_path) as f:
                    data = f.read()
                user_data = json.loads(data)["data"]["aggregated"]
                agg_user_data['State'].append(each_state)
                agg_user_data['Year'].append(each_year)
                agg_user_data['Quarter'].append(each_quarter.strip('.json'))
                agg_user_data['registeredUsers'].append(user_data["registeredUsers"])
                agg_user_data['appOpens'].append(user_data["appOpens"])
    df = pd.DataFrame(agg_user_data)
    df.to_csv('./csv_files/user_data/aggregated_user_state.csv',index=False)

def user_map_state(path):
    states = os.listdir(path)
    user_district_data = {'State':[], 'Year':[],'Quarter':[],'DistrictName':[], "registeredUsers":[], "appOpens":[]}
    for each_state in states:
        state_folder_path = path+'/'+each_state
        years = os.listdir(state_folder_path)
        for each_year in years:
            year_path = state_folder_path+'/'+each_year
            quarter_data = os.listdir(year_path)
            for each_quarter in quarter_data:
                each_quarter_path = year_path+'/'+each_quarter
                with open(each_quarter_path) as f:
                    data=f.read()
                district_data = json.loads(data)["data"]["hoverData"]
                for each_district in district_data:
                    user_district_data['State'].append(each_state)
                    user_district_data['Year'].append(each_year)
                    user_district_data['Quarter'].append(each_quarter.strip('.json'))
                    user_district_data['DistrictName'].append(each_district)
                    user_district_data['registeredUsers'].append(district_data[each_district]["registeredUsers"])
                    user_district_data['appOpens'].append(district_data[each_district]["appOpens"])
    df = pd.DataFrame(user_district_data)
    df.to_csv('./csv_files/user_data/user_map_state.csv',index=False)

def top_user_state(path):
    states = os.listdir(path)
    top_disctrict_data = {'State':[], 'Year':[],'Quarter':[],'DistrictName':[], 'registeredUsers':[]}
    top_postal_code_data = {'State':[], 'Year':[],'Quarter':[],'PostalCode':[], "registeredUsers":[]}
    for each_state in states:
        state_folder_path = path+'/'+each_state
        years = os.listdir(state_folder_path)
        for each_year in years:
            each_year_path = state_folder_path+'/'+each_year
            quarter_data = os.listdir(each_year_path)
            for each_quarter in quarter_data:
                each_quarter_path = each_year_path+'/'+each_quarter
                with open(each_quarter_path) as f:
                    data = f.read()
                for each_data in json.loads(data)["data"]["districts"]:
                    top_disctrict_data["State"].append(each_state)
                    top_disctrict_data["Year"].append(each_year)
                    top_disctrict_data["Quarter"].append(each_quarter.strip('.json'))
                    top_disctrict_data["DistrictName"].append(each_data["name"])
                    top_disctrict_data["registeredUsers"].append(each_data["registeredUsers"])
                for each_data in json.loads(data)["data"]["pincodes"]:
                    top_postal_code_data["State"].append(each_state)
                    top_postal_code_data["Year"].append(each_year)
                    top_postal_code_data["Quarter"].append(each_quarter.strip('.json'))
                    top_postal_code_data["PostalCode"].append(each_data["name"])
                    top_postal_code_data["registeredUsers"].append(each_data["registeredUsers"])
    df = pd.DataFrame(top_postal_code_data)
    df.to_csv('./csv_files/user_data/top_user_pincode_state.csv',index=False)
    df = pd.DataFrame(top_disctrict_data)
    df.to_csv('./csv_files/user_data/top_user_district_state.csv',index=False)

def aggregate_user_country(path):
    years = os.listdir(path)
    users = {'Year':[],'Quarter':[],'registeredUsers':[], 'appOpens':[]}
    for each_year in years:
        each_year_path = path+'/'+each_year
        quarter_data = os.listdir(each_year_path)
        for each_quarter in quarter_data:
            if each_quarter.endswith('.json'):
                each_quarter_path = each_year_path+'/'+each_quarter
                with open(each_quarter_path) as f:
                    data = f.read()
                user_data = json.loads(data)["data"]["aggregated"]
                users["Year"].append(each_year)
                users["Quarter"].append(each_quarter.strip('.json'))
                users["registeredUsers"].append(user_data["registeredUsers"])
                users["appOpens"].append(user_data["appOpens"])
    df = pd.DataFrame(users)
    df.to_csv('./csv_files/user_data/agg_users_country.csv',index=False)

# No need to use
# def user_map_country(path):
#     years = os.listdir(path)
#     hover_state = {'Year':[],'Quarter':[],'State Name':[], 'registeredUsers':[], 'appOpens':[]}
#     for each_year in years:
#         each_year_path = path+'/'+each_year
#         quarter_data = os.listdir(each_year_path)
#         for each_quarter in quarter_data:
#             each_quarter_path = each_year_path+'/'+each_quarter
#             if os.path.isfile(each_quarter_path):
#                 with open(each_quarter_path,'r') as f:
#                     data = f.read()
#                 user_data = json.loads(data)["data"]["hoverData"]
#                 for each_data in user_data:
#                     hover_state['Year'].append(each_year)
#                     hover_state['Quarter'].append(each_quarter.strip('.json'))
#                     hover_state['State Name'].append(each_data)
#                     hover_state['registeredUsers'].append(user_data[each_data]['registeredUsers'])
#                     hover_state['appOpens'].append(user_data[each_data]['appOpens'])
#     df = pd.DataFrame(hover_state)
#     df.to_csv('./csv_files/user_data/user_data_state.csv',index=False)

def top_user_country(path):
    years = os.listdir(path)
    top_state = {'Year':[],'Quarter':[],'State':[], 'registeredUsers':[]}
    top_district = {'Year':[],'Quarter':[],'District':[], 'registeredUsers':[]}
    top_pincode = {'Year':[],'Quarter':[],'pincode':[], 'registeredUsers':[]}
    for each_year in years:
        each_year_path = path+'/'+each_year
        quarter_data = os.listdir(each_year_path)
        for each_quarter in quarter_data:
            each_quarter_path = each_year_path+'/'+each_quarter
            if os.path.isfile(each_quarter_path):
                with open(each_quarter_path,'r') as f:
                    data = f.read()
                for each_data in json.loads(data)["data"]["states"]:
                    top_state["Year"].append(each_year)
                    top_state["Quarter"].append(each_quarter.strip('.json'))
                    top_state["State"].append(each_data["name"])
                    top_state["registeredUsers"].append(each_data["registeredUsers"])
                for each_data in json.loads(data)["data"]["districts"]:
                    top_district["Year"].append(each_year)
                    top_district["Quarter"].append(each_quarter.strip('.json'))
                    top_district["District"].append(each_data["name"])
                    top_district["registeredUsers"].append(each_data["registeredUsers"])
                for each_data in json.loads(data)["data"]["pincodes"]:
                    top_pincode["Year"].append(each_year)
                    top_pincode["Quarter"].append(each_quarter.strip('.json'))
                    top_pincode["pincode"].append(each_data["name"])
                    top_pincode["registeredUsers"].append(each_data["registeredUsers"])
    
    df = pd.DataFrame(top_state)
    df.to_csv('./csv_files/user_data/top_state_country.csv',index=False)
    df = pd.DataFrame(top_district)
    df.to_csv('./csv_files/user_data/top_district_country.csv',index=False)
    df = pd.DataFrame(top_pincode)
    df.to_csv('./csv_files/user_data/top_pincode_country.csv',index=False)
    
def generate_csv_files():
    clone_repository()
    if not os.path.exists('./csv_files'):
        os.makedirs('./csv_files')
        os.makedirs('./csv_files/user_data')
        aggregated_transaction_state('./github_data/data/aggregated/transaction/country/india/state')
        map_state('./github_data/data/map/transaction/hover/country/india/state')
        top_state('./github_data/data/top/transaction/country/india/state')
        aggregate_transaction_country('./github_data/data/aggregated/transaction/country/india')
        map_country('./github_data/data/map/transaction/hover/country/india')
        top_in_country('./github_data/data/top/transaction/country/india')
        aggregated_user_state('./github_data/data/aggregated/user/country/india/state')
        user_map_state('./github_data/data/map/user/hover/country/india/state')
        top_user_state('./github_data/data/top/user/country/india/state')
        aggregate_user_country('./github_data/data/aggregated/user/country/india')
        top_user_country('./github_data/data/top/user/country/india')

if __name__ == '__main__':
    print('Extracting the CSV Files.....')
    generate_csv_files()
