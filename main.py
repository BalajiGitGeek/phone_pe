
import streamlit as st
import support.scripts as scripts
import support.sql_queries as sql_queries
from streamlit_option_menu import option_menu
import support.charts as charts

st.set_page_config(
    page_title='PhonePe Analysis',
    layout='wide')

st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: #ff5733;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        font-weight:bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">PhonePe Pulse Data Visualization</p>', unsafe_allow_html=True)

selected = option_menu(
    menu_title = None,
    options = ["ABOUT","HOME","INSIGHTS"],
    icons =['',"house","bar-chart"],
    default_index=0,
    orientation="horizontal",
    styles={
            "container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {"font-size": "20px","--hover-color": "lightgreen"},
            "nav-link-selected": {"background-color": "green"},
            })

if selected == 'HOME':
    m1,m2,m3,m4=st.columns([6,1,1,1])
    with m1:
        st.image('./images/PhonePe-Logo3.png')
    with m2:
        selected_year = st.selectbox('Enter the year',scripts.get_year_list(),index=4)
    with m3:
        quarter_mapping = {"Q1": "1", "Q2": "2", "Q3": "3", "Q4": "4"}
        selected_quarter = st.selectbox('Quarter',quarter_mapping.keys(),index = 1)

    with m4:
        option = st.selectbox('Type',['Transaction','User'])

    if option == 'Transaction':
        n1,n2 = st.columns([8,4])
        transactions = sql_queries.avg_transaction_value(selected_year,quarter_mapping[selected_quarter])
        Categories_df = sql_queries.transaction_type_country(selected_year,quarter_mapping[selected_quarter])

        with n1:
            st.plotly_chart(charts.main_map(selected_year,quarter_mapping[selected_quarter]))
        with n2:
            st.subheader(f'{option}')
            st.markdown(f"<p style='color:green;font-size:20px;margin:0;padding:0;'>All Transactions (UPI+Cards+Wallets)</p>",unsafe_allow_html=True)
            st.markdown(f"<h1 style='font-size:30px;margin:0;padding:0;'>{round(transactions['transactions'])}</h1>",unsafe_allow_html=True)
            
            rc1,rc2 = st.columns([1,1])
            with rc1:
                st.markdown(f"<p style='color:green;font-size:20px;margin:0;padding:0;'>Total payment value</p>",unsafe_allow_html=True)
                st.markdown(f"<h1 style='font-size:30px;margin:0;padding:0;'>{round(transactions['transaction_value'])}</h1>",unsafe_allow_html=True)
            with rc2:
                st.markdown(f"<p style='color:green;font-size:20px;margin:0;padding:0;'>Avg.transaction value</p>",unsafe_allow_html=True)
                st.markdown(f"<h1 style='font-size:30px;margin:0;padding:0;'>{round(transactions['avg_transaction'])}</h1>",unsafe_allow_html=True)
            st.markdown('<hr>', unsafe_allow_html=True)

            st.subheader('Categories')

            fc1,fc2 = st.columns([1.3,0.45])
            

            with fc1:
                st.markdown(f"<p style='color:green;font-size:25px;margin:0;padding:0;'>{Categories_df[0][0]}</p>",unsafe_allow_html=True)
                st.markdown(f"<p style='color:green;font-size:25px;margin:0;padding:0;'>{Categories_df[0][1]}</p>",unsafe_allow_html=True)
                st.markdown(f"<p style='color:green;font-size:25px;margin:0;padding:0;'>{Categories_df[0][2]}</p>",unsafe_allow_html=True)
                st.markdown(f"<p style='color:green;font-size:25px;margin:0;padding:0;'>{Categories_df[0][3]}</p>",unsafe_allow_html=True)
                st.markdown(f"<p style='color:green;font-size:25px;margin:0;padding:0;'>{Categories_df[0][4]}</p>",unsafe_allow_html=True)
            with fc2:
                st.markdown(f"<h2 style='font-size:30px;margin:0;padding:0;'>{Categories_df[1][0]}</h2>",unsafe_allow_html=True)
                st.markdown(f"<h2 style='font-size:30px;margin:0;padding:0;'>{Categories_df[1][1]}</h2>",unsafe_allow_html=True)
                st.markdown(f"<h2 style='font-size:30px;margin:0;padding:0;'>{Categories_df[1][2]}</h2>",unsafe_allow_html=True)
                st.markdown(f"<h2 style='font-size:30px;margin:0;padding:0;'>{Categories_df[1][3]}</h2>",unsafe_allow_html=True)
                st.markdown(f"<h2 style='font-size:30px;margin:0;padding:0;'>{Categories_df[1][4]}</h2>",unsafe_allow_html=True)

            st.markdown('<hr>',unsafe_allow_html=True)
            selected_radio = st.selectbox("",['Top States','Top District','Top Pincodes'])

            if selected_radio == 'Top Pincodes':
                st.write(sql_queries.top_pincode_country(selected_year,quarter_mapping[selected_quarter]))

            if selected_radio == 'Top States':
                st.write(sql_queries.top_state_country(selected_year,quarter_mapping[selected_quarter]))

            if selected_radio == 'Top District':
                st.write(sql_queries.top_districts_country(selected_year,quarter_mapping[selected_quarter]))

    if option == 'User':
        n1,n2 = st.columns([8,4])
        agg_user_data = sql_queries.registered_users(selected_year,quarter_mapping[selected_quarter])
        
        with n1: 
            st.plotly_chart(charts.user_map(selected_year,quarter_mapping[selected_quarter]))
        with n2:
            st.subheader(f'{option}')
            st.markdown(f"<p style='color:green;font-size:20px;margin:0;padding:0;'>Registered PhonePe users till {selected_quarter} {selected_year}</p>",unsafe_allow_html=True)
            st.markdown(f"<h1 style='font-size:30px;margin:0;padding:0;'>{agg_user_data['registeredUsers']}</h1>",unsafe_allow_html=True)
            st.markdown(f"<p style='color:green;font-size:20px;padding-top:20px;margin-bottom:0;'>PhonePe app opens in {selected_quarter} {selected_year}</p>",unsafe_allow_html=True)
            if agg_user_data['appOpens'] == 0:
                st.write(f"<h1 style='font-size:30px;margin:0;padding:0;'>Unavailable</h1>",unsafe_allow_html=True)
            else:
                st.write(f"<h1 style='font-size:30px;margin:0;padding:0;'>{agg_user_data['appOpens']}</h1>",unsafe_allow_html=True)

            selected_radio = st.selectbox("",['Top States','Top District','Top Pincodes'])

            if selected_radio == 'Top Pincodes':
                st.write(sql_queries.top_users_pincode_country(selected_year,quarter_mapping[selected_quarter]))

            if selected_radio == 'Top States':
                st.write(sql_queries.top_users_state_country(selected_year,quarter_mapping[selected_quarter]))

            if selected_radio == 'Top District':
                st.write(sql_queries.top_users_districts_country(selected_year,quarter_mapping[selected_quarter]))
                 
if selected == "ABOUT":

    st.markdown("<h1 style='font-size:36px;'>Project Overview</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px;'>This project involves data extraction, transformation, database integration, dashboard development, and deployment.</p>", unsafe_allow_html=True)

    col1,col2 = st.columns(2)
    with col1:
        mobile_overview = open("./images/mobile_overview.png", "rb").read()
        st.image(mobile_overview)
    with col2:
                
        st.markdown("<h1 style='font-size:20px;'>1. Data Extraction: The project involves scripting to extract data from the PhonePe Pulse GitHub repository, ensuring the data is available for analysis and visualization.</h1>",unsafe_allow_html=True)
        st.markdown("<h1 style='font-size:20px;'>2. Data Transformation: The collected data undergoes cleaning and transformation using Python and Pandas to make it suitable for analysis, addressing issues like missing values.</h1>",unsafe_allow_html=True)
        st.markdown("<h1 style='font-size:20px;'>3. Database Integration: The transformed data is efficiently stored in a MySQL database using Python's 'mysql-connector-python' library, enabling structured storage and retrieval.</h1>",unsafe_allow_html=True)
        st.markdown("<h1 style='font-size:20px;'>4. Dashboard Development: A user-friendly and interactive dashboard is created using Streamlit and Plotly in Python, facilitating the exploration of data with dropdown menus and dynamic updates.</h1>",unsafe_allow_html=True)
        st.markdown("<h1 style='font-size:20px;'>5. Deployment and Accessibility: The final dashboard is securely deployed, allowing users to access and interact with real-time geo visualizations and valuable insights derived from PhonePe's data from anywhere via web browsers.</h1>",unsafe_allow_html=True)

if selected == "INSIGHTS":
    st.markdown("<h1 style='font-size:36px;'>Basic Insights</h1>", unsafe_allow_html=True)
    options=["Trend of PhonePe transactions over the years?",
            "List the top 10 states with the highest number of PhonePe users",
            "Trend of PhonePe Users over the years?",
            "What is the distribution of transaction types?",
            "How the app open rates have changed over time?",
            "Which state has the highest average spending per person on PhonePe transactions?",
            "What are the top 10 states with the highest transaction value?",
            "In which state is the merchant payment higher compared to other states?",
            "Which state has the highest number of app opens in PhonePe?"]
    
    selected_option = st.selectbox("Select an Option",options)

    if selected_option == "Trend of PhonePe transactions over the years?":
        c1,c2 = st.columns([4,6])
        df =sql_queries.ques1()
        with c1:
            st.markdown("<h1 style='font-size:36px;color:red;'>PhonePe Transaction Trend</h1>", unsafe_allow_html=True)
            st.write(df)
        with c2:
            st.plotly_chart(charts.ques1(df))
            
    if selected_option == "List the top 10 states with the highest number of PhonePe users":
        c1,c2 = st.columns([4,6])
        df =sql_queries.ques2()
        with c1:
            st.markdown("<h1 style='font-size:36px;color:red;'>Registered Users</h1>", unsafe_allow_html=True)
            st.write(df)
        with c2:
            st.plotly_chart(charts.ques2(df))
    
    if selected_option == "Trend of PhonePe Users over the years?":
        c1,c2 = st.columns([4,6])
        df =sql_queries.ques3()
        with c1:
            st.markdown("<h1 style='font-size:36px;color:red;'>Registered Users</h1>", unsafe_allow_html=True)
            st.write(df)
        with c2:
            st.plotly_chart(charts.ques3(df))

    if selected_option == "What is the distribution of transaction types?":
        c1,c2 = st.columns([4,6])
        df =sql_queries.ques4()
        with c1:
            st.markdown("<h1 style='font-size:36px;color:red;'>Transaction Type Distribution</h1>", unsafe_allow_html=True)
            st.write(df)
        with c2:
            st.plotly_chart(charts.ques4(df))
    
    if selected_option == "How the app open rates have changed over time?":
        c1,c2 = st.columns([4,6])
        df =sql_queries.ques5()
        with c1:
            st.markdown("<h1 style='font-size:36px;color:red;'>App Opens Trend</h1>", unsafe_allow_html=True)
            st.write(df)
        with c2:
            st.plotly_chart(charts.ques5(df))

    if selected_option == "Which state has the highest average spending per person on PhonePe transactions?":
        c1,c2 = st.columns([4,6])
        df =sql_queries.ques6()
        with c1:
            st.markdown("<h1 style='font-size:36px;color:red;'>Average Spending/Person</h1>", unsafe_allow_html=True)
            st.write(df)
        with c2:
            st.plotly_chart(charts.ques6(df))

    if selected_option == "What are the top 10 states with the highest transaction value?":
        c1,c2 = st.columns([4,6])
        df =sql_queries.ques7()
        with c1:
            st.markdown("<h1 style='font-size:36px;color:red;'>Highest Transaction Value</h1>", unsafe_allow_html=True)
            st.write(df)
        with c2:
            st.plotly_chart(charts.ques7(df))

    if selected_option == "In which state is the merchant payment higher compared to other states?":
        c1,c2 = st.columns([4,6])
        df =sql_queries.ques8()
        with c1:
            st.markdown("<h1 style='font-size:36px;color:red;'>Merchant Payment</h1>", unsafe_allow_html=True)
            st.write(df)
        with c2:
            st.plotly_chart(charts.ques8(df))

    if selected_option == "Which state has the highest number of app opens in PhonePe?":
        c1,c2 = st.columns([4,6])
        df =sql_queries.ques9()
        with c1:
            st.markdown("<h1 style='font-size:36px;color:red;'>App Opens</h1>", unsafe_allow_html=True)
            st.write(df)
        with c2:
            st.plotly_chart(charts.ques9(df))

            