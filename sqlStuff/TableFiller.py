# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import math
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

## Import Liberaries
import pandas as pd
import sqlite3
from sqlite3 import Error

## Read the file
df_movies = pd.read_csv('C:/Users/19493/Documents/CPSC408/Final_Project/sqlStuff/MoviesOnStreamingPlatforms.csv')
df_tvshows = pd.read_csv('C:/Users/19493/Documents/CPSC408/Final_Project/sqlStuff/tv_shows.csv')


# import sqlalchemy and create a sqlite engine
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

# add the data to our sql database from the dataframe
conn = sqlite3.connect('C:/Users/19493/Documents/CPSC408/Final_Project/finalProject.db')

#Sets up database
tableInit = '''
CREATE TABLE media (
  media_id INTEGER PRIMARY KEY,
  title VARCHAR(256),
  media_type VARCHAR(256),
  release_year INTEGER,
  rating VARCHAR(32),
  ageRating VARCHAR(32)
);
'''
conn.execute(tableInit)

tableInit = '''
CREATE TABLE platform (
    platform_id INTEGER PRIMARY KEY,
    platform_name VARCHAR(256),
    platform_cost INTEGER
);
'''
conn.execute(tableInit)

tableInit = '''
CREATE TABLE platform_media (
    platform_id INTEGER,
    media_id INTEGER,
    FOREIGN KEY (platform_id) REFERENCES platform(platform_id),
    FOREIGN KEY (media_id) REFERENCES media(media_id),
    PRIMARY KEY (platform_id,media_id)
);
'''
conn.execute(tableInit)

tableInit = '''
CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT ,
  name TEXT
);
'''
conn.execute(tableInit)

tableInit = '''
CREATE TABLE watchlist (
  watchlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
  media_id INTEGER,
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
  FOREIGN KEY (media_id) REFERENCES media(media_id)
);
'''
conn.execute(tableInit)

tableInit = '''
--populate platform table
INSERT INTO  platform (platform_id, platform_name, platform_cost)
    VALUES (1, 'Netflix', 10);
'''
conn.execute(tableInit)

tableInit = '''
INSERT INTO  platform (platform_id, platform_name, platform_cost)
    VALUES (2, 'Prime Video', 9);
'''
conn.execute(tableInit)

tableInit = '''
INSERT INTO  platform (platform_id, platform_name, platform_cost)
    VALUES (3, 'Hulu', 8);
'''
conn.execute(tableInit)

tableInit = '''
INSERT INTO  platform (platform_id, platform_name, platform_cost)
    VALUES (4, 'Disney+', 8);
'''

conn.execute(tableInit)

media_id = 0
for index, row in df_movies.iterrows():
    title = row['Title'].replace('\'','') 
    media_type = 'Movie'
    release_year = row['Year']
    rating = row['Rotten Tomatoes']
    if (rating != rating): #checks if its nan
        rating = 'Not Rated'
    ageRating = row['Age']
    if (ageRating != ageRating): #checks if its nan
        ageRating = 'Not Rated'
    media_id +=1
    conn.execute('INSERT INTO media (media_id, title, media_type, release_year, rating, ageRating) VALUES ('+str(media_id)+',\''+title+'\',\''+media_type+'\','+str(release_year)+',\''+rating+'\',\''+ageRating+'\');') #insert row into table media, also thanks python for automatically typecasting my strings into integers and then not being able to concotinate the two
    if row['Netflix'] == 1:
        conn.execute('INSERT INTO platform_media (platform_id, media_id) VALUES (1,'+str(media_id)+');') #insert into platform-media table with netflix
    if row['Hulu'] == 1:
        conn.execute('INSERT INTO platform_media (platform_id, media_id) VALUES (2,'+str(media_id)+');') #insert into platform-media table with Hulu
    if row['Prime Video'] == 1:
        conn.execute('INSERT INTO platform_media (platform_id, media_id) VALUES (3,'+str(media_id)+');') #insert into platform-media table with Prime Viedo
    if row['Disney+'] == 1:
        conn.execute('INSERT INTO platform_media (platform_id, media_id) VALUES (4,'+str(media_id)+');') #insert into platform-media table with Disney+
    conn.commit()


for index, row in df_tvshows.iterrows():
    title = row['Title'].replace('\'','') #removes ' characters. I tried to replace them with \' but python was being VERY difficult
    media_type = 'TV Show'
    release_year = row['Year']
    rating = row['Rotten Tomatoes']
    if (rating != rating): #checks if its nan
        rating = 'Not Rated'
    ageRating = row['Age']
    if (ageRating != ageRating): #checks if its nan
        ageRating = 'Not Rated'
    media_id +=1
    conn.execute('INSERT INTO media (media_id, title, media_type, release_year, rating, ageRating) VALUES ('+str(media_id)+',\''+title+'\',\''+media_type+'\','+str(release_year)+',\''+rating+'\',\''+ageRating+'\');') #insert row into table media, also thanks python for automatically typecasting my strings into integers and then not being able to concotinate the two
    if row['Netflix'] == 1:
        conn.execute('INSERT INTO platform_media (platform_id, media_id) VALUES (1,'+str(media_id)+');') #insert into platform-media table with netflix
    if row['Hulu'] == 1:
        conn.execute('INSERT INTO platform_media (platform_id, media_id) VALUES (2,'+str(media_id)+');') #insert into platform-media table with Hulu
    if row['Prime Video'] == 1:
        conn.execute('INSERT INTO platform_media (platform_id, media_id) VALUES (3,'+str(media_id)+');') #insert into platform-media table with Prime Viedo
    if row['Disney+'] == 1:
        conn.execute('INSERT INTO platform_media (platform_id, media_id) VALUES (4,'+str(media_id)+');') #insert into platform-media table with Disney+
    conn.commit()



conn.close()
