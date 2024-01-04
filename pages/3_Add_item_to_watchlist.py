import streamlit as st
import pandas as pd
import sqlite3
from sqlite3 import Error


with st.form('Add to watchlist'):
    userInfo = st.text_input('For which user_id would you like to add to?')
    mediaInfo = st.text_input('What is the media_id you would like to add?')
    Submitted = st.form_submit_button("Submit")
    if Submitted:
        conn = sqlite3.connect('C:/Users/19493/Documents/CPSC408/Final_Project/finalProject.db')
        # Uses a transaction
        query = 'BEGIN TRANSACTION; '
        conn.execute(query)
        query = 'INSERT INTO watchlist (media_id, user_id) VALUES ('+mediaInfo+', '+userInfo+');'

        #trys to execute the query, if it doesnt work, we roll it back
        try:
            conn.execute(query)
        except sqlite3.Error:
            st.write('An error has occured')
            conn.execute('ROLLBACK;')
        
        #tells the user what it added
        st.write('The following media has been added to the following user\'s watchlist.')
        statement = 'SELECT * FROM media WHERE media_id = '+mediaInfo+' ;'

        sql_query = pd.read_sql(statement, conn)
        df = pd.DataFrame(sql_query)
        st.write(df)

        statement = 'SELECT * FROM users WHERE user_id = '+userInfo+' ;'

        sql_query = pd.read_sql(statement, conn)
        df = pd.DataFrame(sql_query)
        st.write(df)

        # finalizes the commit
        conn.execute('COMMIT;')

        conn.commit()
        conn.close()
