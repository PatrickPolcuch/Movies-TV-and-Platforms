# Movies-TV-and-Platforms
### Overview

The TV streaming landscape has expanded, offering a multitude of platforms with extensive libraries. Our project aimed to simplify this experience by creating a comprehensive database to streamline the process of finding favorite movies and TV shows across various platforms. Our team, comprising Marisa Mini, Patrick Polcuch, and Pelin Top, developed a solution to facilitate effortless content discovery.

### Run Instructions
1. Install Python ([download site](https://www.python.org/downloads/))
2. Install Streamlit (instruction found [here](https://docs.streamlit.io/get-started/installation))
3. Clone our repository
4. Run
```streamlit run home.py```

Our application should then open in your default browser

### Key Features

- **Centralized Information:** Our database stores details about TV shows and movies, along with their availability across different streaming platforms.
- **User-Friendly Interface:** Users can easily browse titles, add them to a watchlist, and track what they want to watch, all in one place.
- **Streamlined Search:** Utilizing filters for platform, genre, and other criteria, users can quickly pinpoint their preferred content.

### How We Built It

We constructed the database using SQLite, leveraging data from sources like Kaggle, which provided a rich dataset encompassing over 1400 columns of information. Python scripts aided in populating the database by parsing and adding the collected data.

### Streamlit Integration

To enhance usability, we incorporated Streamlit, an open-source Python library, to create an intuitive interface. The platform information is prominently displayed for each title, simplifying the streaming platform selection process.

### Interface Highlights

Our user-friendly interface boasts several features:
- **Filtering Options:** Users can select specific columns, filter by media type (movies/TV shows), and sort by various parameters (title, release year, rating, and media ID).
- **Watchlist Management:** Users can add multiple individuals to create separate watchlists, unlike platforms limiting users to a fixed number of profiles.
- **Search Flexibility:** Users can search for titles similar to their query, aiding in discovering related content.

### Conclusion

Our TV streaming database empowers users to effortlessly discover and track their favorite content while staying informed about new releases. As streaming platforms continue to thrive, we believe our database serves as an indispensable tool for anyone navigating the vast array of available content.
