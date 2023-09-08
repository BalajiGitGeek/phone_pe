import datetime 

def get_year_list():
    year_list = []
    for i in range(2018,datetime.datetime.now().year):
        year_list.append(i)
    return year_list
    
