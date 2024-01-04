import streamlit as st
import pandas as pd
import sqlite3
from sqlite3 import Error


st.write('Remove item from watchlist')

st.write('Remove using user_id and media_id')
with st.form('Remove watchlist form'):
    userInfo = st.text_input('For which user_id would you like to remove from?')
    mediaInfo = st.text_input('What is the media_id you would like to remove?')
    Submitted = st.form_submit_button("Submit")
    if Submitted:
        conn = sqlite3.connect('C:/Users/19493/Documents/CPSC408/Final_Project/finalProject.db')

        # the query to delete an item from the watchlist
        query = 'DELETE FROM watchlist WHERE media_id ='+mediaInfo+' AND user_id ='+userInfo+';'

        # uses a transaction, if it is sucessful, we commit. if not, we rollback
        conn.execute('BEGIN TRANSACTION; ')
        try:
            conn.execute(query)
            conn.execute('COMMIT;')
            
        except sqlite3.Error as ex:
            st.write('An error has occured')
            st.write(ex)
            conn.execute('ROLLBACK;')
        
        
        #tells the user what we removed
        st.write('The following media has been removed from the following user\'s watchlist.')
        statement = 'SELECT * FROM media WHERE media_id = '+mediaInfo+' ;'

        sql_query = pd.read_sql(statement, conn)
        df = pd.DataFrame(sql_query)
        st.write(df)

        statement = 'SELECT * FROM users WHERE user_id = '+userInfo+' ;'

        sql_query = pd.read_sql(statement, conn)
        df = pd.DataFrame(sql_query)
        st.write(df)

        conn.commit()
        conn.close()


st.write('Remove using watchlist_id')
with st.form('Remove by ID'):
    watchlistId = st.text_input('What is the ID of the item you would like to remove?')
    Submitted = st.form_submit_button("Submit")
    if Submitted:
        conn = sqlite3.connect('C:/Users/19493/Documents/CPSC408/Final_Project/finalProject.db')

        # gets the information on what we are about to remove. we will use this later to tell the user the details of what we removed
        statement = '''
        SELECT * FROM (
            SELECT w.watchlist_id, w.user_id, u.name,m.media_id, m.title, m.media_type, m.release_year, m.rating, m.ageRating 
            FROM watchlist w 
            INNER JOIN users u
            ON w.user_id = u.user_id
            INNER JOIN media m
            ON w.media_id = m.media_id)
        WHERE watchlist_id = ''' + watchlistId + ' ;'
         
        sql_query = pd.read_sql(statement, conn)
        df = pd.DataFrame(sql_query)
        
        #query fo what we are going to delete
        query = 'DELETE FROM watchlist WHERE watchlist_id = '+watchlistId+' ;'

        # uses a transaction, if it is sucessful, we commit. if not, we rollback
        conn.execute('BEGIN TRANSACTION; ')
        try:
            conn.execute(query)
            conn.execute('COMMIT;')
            
        except sqlite3.Error as ex:
            st.write('An error has occured')
            st.write(ex)
            conn.execute('ROLLBACK;')
        
        # tells the user what we removed
        st.write('The following item has been removed from the watchlist.')
        st.write(df)

        conn.commit()
        conn.close()

