import streamlit as st
import pandas as pd
import sqlite3
from sqlite3 import Error

def addUser(userInfo):
    conn = sqlite3.connect('C:/Users/19493/Documents/CPSC408/Final_Project/finalProject.db')
    conn.execute('INSERT INTO users (name) VALUES (\''+userInfo+'\');')
    conn.commit()
    conn.close()



with st.form('User add form'):
    #prompts the info for the new user
    userInfo = st.text_input('What is the name of the user you would like to add?')

    Submitted = st.form_submit_button('Submit')
    
    if Submitted:
        # adds new user
        if (userInfo != ''):
            addUser(userInfo)
            st.write('User ',userInfo,' added succesfully!')

conn = sqlite3.connect("finalProject.db") #opens a connection to our database

# shows a table with all users and how many items are in their watchlist
statement = '''
SELECT u.user_id, u.name, COUNT(m.media_id) as items_in_watchlist
FROM users u
LEFT JOIN watchlist w ON w.user_id = u.user_id
LEFT JOIN media m ON m.media_id = w.media_id
GROUP BY u.user_id, u.name;
'''
sql_query = pd.read_sql(statement, conn)
df = pd.DataFrame(sql_query)
conn.close() #closes database connection

st.table(df) #writes our tables