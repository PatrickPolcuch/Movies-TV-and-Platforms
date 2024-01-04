import streamlit as st
import pandas as pd
import sqlite3
from sqlite3 import Error

st.write('Update a media record')

with st.form('Update Media'): #User input for updating media
    media_id = st.text_input('What is the id of the media you wish to update (REQUIRED)?')
    st.write('Enter the new information for the media, blank boxes will not be changed')
    title = st.text_input('New Title')
    type = st.text_input('New Media type')
    release = st.text_input('New Release year')
    rating = st.text_input('New Rating')
    age = st.text_input('New age rating')

    Submitted = st.form_submit_button('Submit')

    if Submitted:# executes media update
        query = 'UPDATE media SET '

        if title != '':
            query += 'title = \''+ title +'\' , '
        if type != '':
            query += 'media_type = \''+ type +'\' , '
        if release != '':
            query += 'release_year = '+ release +' , '
        if rating != '':
            query += 'rating = \''+ rating +'\' , '
        if age != '':
            query += 'ageRating = \''+ age +'\' , '
        
        if query[-2] == ',': #so we dont have a floating comma at the end of our SELECT statement, not the most elegant code, but it works
            query = query[:-2]

        query += 'WHERE media_id = ' + media_id + ';'

        conn = sqlite3.connect("finalProject.db") #opens a connection to our database

        #saves old information
        sql_query = pd.read_sql('SELECT * FROM MEDIA WHERE media_id = '+media_id+';', conn)
        df_old = pd.DataFrame(sql_query)

        #updates
        conn.execute(query)

        #gets the new data from the table
        sql_query = pd.read_sql('SELECT * FROM MEDIA WHERE media_id = '+media_id+';', conn)
        df_new = pd.DataFrame(sql_query)

        st.write('Changed:')
        st.write(df_old)
        st.write('To:')
        st.write(df_new)
        