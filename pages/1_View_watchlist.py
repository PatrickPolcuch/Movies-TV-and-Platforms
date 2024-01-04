import streamlit as st
import pandas as pd
import sqlite3
from sqlite3 import Error

with st.sidebar: #all of this will be on the side
    with st.form('Watchlist options'): # these are the options on what columns the user can view
        st.write('Show columns:')
        watchlist_id = st.checkbox('watchlist_id',value=True)
        user_id = st.checkbox('user_id', value=True)
        name = st.checkbox('name', value=True)
        media_id = st.checkbox('media_id', value=True)
        title = st.checkbox('title', value=True)
        media_type = st.checkbox('media_type', value=True)
        release_year = st.checkbox('release_year', value=True)
        rating = st.checkbox('rating', value=True)
        ageRating = st.checkbox('ageRating', value=True)

        selectUser = st.text_input('Watchlist for specific user (default all users).\nEnter user_id')

        Submit = st.form_submit_button()



conn = sqlite3.connect("finalProject.db") #opens a connection to our database


# puts the columns in the query
# w.watchlist_id, w.user_id, u.name, m.media_id, m.title, m.media_type, m.release_year, m.rating, m.ageRating
statement = 'SELECT '
if watchlist_id:
    statement += 'w.watchlist_id, '
if user_id:
    statement += 'w.user_id, '
if name:
    statement += 'u.name, '
if media_id:
    statement += 'm.media_id, '
if title:
    statement += 'm.title, '
if media_type:
    statement += 'm.media_type, '
if release_year:
    statement += 'm.release_year, '
if rating:
    statement += 'm.rating, '
if ageRating:
    statement += ' m.ageRating '

if statement[-2] == ',': #so we dont have a floating comma at the end of our SELECT statement, not the most elegant code, but it works
    statement = statement[:-2]

# joins the tabels so we can see the data from users and watchlist
statement += '''
FROM watchlist w
INNER JOIN users u
ON w.user_id = u.user_id
INNER JOIN media m
ON w.media_id = m.media_id 
'''

#the option for if we only want the watchlist for one user
if selectUser != '':
    statement += ' WHERE u.user_id = '+selectUser

statement +=';'
sql_query = pd.read_sql(statement, conn)

df = pd.DataFrame(sql_query)

st.write(df)
conn.close() #closes database connection, this should be the last line of our code I think