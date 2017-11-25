===============
Yify for Python 
===============

This is Python Library which is used to get the Top seeded torrents at any given time and get the entire movie details and ratings .      

Its also useful to search for any movie using different parameters and obtain their magnet link or torrent file of any preferred quality.


-------------
Features :
-------------

* **Search for movie torrents**
* **Get the details of any movie which includes**
    - Torrent details of 720p,1080p,3D quality
    - Torrent Magnet links and hashes along with their size and seeds
    - imdb_code
    - Imdb Rating and MPA rating
    - Year
    - Runtime
    - Summary
    - Movie Description

All the above Details are obtained in the form of attributes of Yify.movie object each object representing a movie.


* Get the Top Most Seeded Torrents listed in the Yify Website
* Download the torrent file of a corresponding torrent.
* Start the torrent download directly without having to download it from the user's default torrent client.


---------------
Installation :
---------------


^^^^^^^
Python3
^^^^^^^
::

    pip install pyYify

or

::

    pip3 install pyYify


----------------
Usage :
----------------


* **First import yify to use its functions.**
 
::

    from pyYify import yify


There are two classes in yify namely 'movie' and 'torrent'.



* **Search for movies.**

On searching , it returns a list of movies (movie objects) .

::


    movies_list = yify.search_movies(search_string , quality , minimum_rating , genre)


The search_string for the movie can be 'Movie Title/IMDb Code, Actor Name, Director Name'.
quality = 'All' , '720p' , '1080p' , '3D'.
minimum_rating is an imdb_rating.
genre = See https://www.imdb.com/genre/ for a list of genres.



* **Get the top seeded movies from Yify**

::

    movies_list  = yify.get_top_seeded_torrents() ;


Returns a list of movies, each movie object only contains its Name and Webpage unlike the searching method which has all the details in the returned movies.
To get the rest of the movie details use getinfo() method . 

::


    for movie in movies_list:
        movie.getinfo() ;

    
* **Each movie Object has has the following data :**

  - id
  - url
  - imdb_code
  - title
  - title_long
  - slug
  - year
  - rating
  - runtime
  - genres
  - summary
  - description
  - language
  - mpa_rating
  - image_links
  - torrents


The movie.torrents is a list of torrents each of which corresponds to the torrent of same movie but of different quality. ('720p' , '1080p' or '3D' ) 
    

* **Each torrent has the following data :**

  - name
  - url
  - magnet
  - hash
  - quality
  - seeds
  - peers
  - size
  - date_uploaded


::

    movie1 = movies_list[0] 
    torrent1 = movie1.torrents[0]

    print("Magnet link = " , torrent1.magnet)


* **Downloading the Torrent file of a movie**

::

    torrent1.download_torrent_file( path , filename )


* **Starting the download directly using magnet link without downloading the torrent file .**


This starts the default torrent client prompting the download dialog
::

    torrent1.start_download()

