import streamlit as st
import pandas as pd
import sqlite3
from sqlite3 import Error

# our default query
query = '''
SELECT media_id, title, media_type, release_year, rating, ageRating, Netflix, Hulu, Prime, Disney FROM(
SELECT media.*,
       MAX(CASE WHEN platform.platform_name = 'Netflix' THEN 1 ELSE 0 END) AS Netflix,
       MAX(CASE WHEN platform.platform_name = 'Prime Video' THEN 1 ELSE 0 END) AS Prime,
       MAX(CASE WHEN platform.platform_name = 'Hulu' THEN 1 ELSE 0 END) AS Hulu,
       MAX(CASE WHEN platform.platform_name = 'Disney+' THEN 1 ELSE 0 END) AS Disney
FROM media
LEFT JOIN platform_media ON media.media_id = platform_media.media_id
LEFT JOIN platform ON platform.platform_id = platform_media.platform_id
GROUP BY media.media_id)
WHERE media_type LIKE '%' AND (Netflix= 1 OR Disney=1 OR Prime=1 OR Hulu=1)
ORDER BY rating DESC;
'''



with st.sidebar:
    with st.form('Sorting movies form'): # all the options we have for sorting the table
        sortBy = st.radio('Sort By:', options= ['Title ↑', 'Title ↓', 'Release Year ↑', 'Release Year ↓', 'Rating ↑', 'Rating ↓', 'media_id'], index=4)
        mediaType = st.radio('Type:', options= ['Movies and TV shows', 'Movies only', 'TV shows only'], index=0)
        st.write('Platforms (default any):')
        netflix = st.checkbox('Netflix')
        hulu = st.checkbox('Hulu')
        primeVideo = st.checkbox('Prime Video')
        disney = st.checkbox('Disney+')
        title = st.text_input('Title similar to:')
        
        Submitted = st.form_submit_button("Submit")
        
        if Submitted:
            query = 'SELECT media_id, title, media_type,release_year, rating, ageRating '
            if (not netflix and not hulu and not primeVideo and not disney): #if none of them are selected, we default to all of them
                query += ', Netflix, Hulu, Prime, Disney'
            else: #adds selected columns to query
                if netflix:
                    query += ', Netflix '
                if hulu:
                    query += ', Hulu '
                if primeVideo:
                    query += ', Prime ' 
                if disney:
                    query += ', Disney '

            #the meat of our query
            query += ''' FROM(
                        SELECT media.*,
                            MAX(CASE WHEN platform.platform_name = 'Netflix' THEN 1 ELSE 0 END) AS Netflix,
                            MAX(CASE WHEN platform.platform_name = 'Prime Video' THEN 1 ELSE 0 END) AS Prime,
                            MAX(CASE WHEN platform.platform_name = 'Hulu' THEN 1 ELSE 0 END) AS Hulu,
                            MAX(CASE WHEN platform.platform_name = 'Disney+' THEN 1 ELSE 0 END) AS Disney
                        FROM media
                        LEFT JOIN platform_media ON media.media_id = platform_media.media_id
                        LEFT JOIN platform ON platform.platform_id = platform_media.platform_id
                        GROUP BY media.media_id)
                        WHERE media_type LIKE 
                        '''
            # filters for media type
            if mediaType == 'Movies only':
                query += '\'Movie\' '
            elif mediaType == 'TV shows only':
                query += '\'TV Show\' '
            else:
                query += '\'%\' '

            # if we want to sort by specific platforms
            if not (not netflix and not hulu and not primeVideo and not disney):
                query +=  'AND ('
                if netflix:
                    query += ' Netflix= 1 OR '
                if hulu:
                    query += ' Hulu=1 OR '
                if primeVideo:
                    query += ' Prime=1 OR '
                if disney:
                    query += ' Disney=1 '
            
                if query[-3] == 'O':
                    query = query[:-3] # gets rid of the extra OR at the end if there is one
                
                query += ' ) '
            
            # sorts by title
            if title != '':
                query += ' AND title LIKE \'%' + title + '%\' '
            
            # selects what we order by
            query += ' ORDER BY '

            if sortBy ==  'Title ↑':
                query += ' title DESC'
            elif sortBy ==  'Title ↓':
                query += ' title ASC'
            elif sortBy ==  'Release Year ↑':
                query += 'release_year DESC'
            elif sortBy ==  'Release Year ↓':
                query += 'release_year ASC'
            elif sortBy ==  'Rating ↑':
                query += 'rating DESC'
            elif sortBy ==  'Rating ↓':
                query += 'rating ASC'
            elif sortBy ==  'media_id':
                query += 'media_id ASC'
            else:
                query += 'rating DESC' # default value
            
            query += ';'
            

            



# executes our query and displays it for the user
conn = sqlite3.connect("finalProject.db") #opens a connection to our database

sql_query = pd.read_sql(query, conn)

df = pd.DataFrame(sql_query)

st.write(df)
conn.close() 

