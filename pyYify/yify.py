import os
import json
import urllib3
import urllib
import time
from bs4 import BeautifulSoup
from requests import get
import re 


#TODO : add user related functions like registering new users , 
# Posting COmments from a user and movie reviewing .


# class yify():

homepage = "https://www.yify-torrent.org"

class torrent():
    def __repr__(self):
        return 'torrent object : quality = {} , size = {}\n'.format(self.quality , self.size) ; 

    def __str__(self):
        return 'torrent object : quality = {} , size = {}\n'.format(self.quality , self.size) ; 

    def __init__(self , torrent_dict : dict  , name =''):
        self.name = name ; 
        self.url = torrent_dict.get('url')
        self.hash = torrent_dict.get('hash')
        self.quality = torrent_dict.get('quality')
        self.seeds = torrent_dict.get('seeds')
        self.peers = torrent_dict.get('peers')
        self.size = torrent_dict.get('size')
        self.date_uploaded = torrent_dict.get('date_uploaded')


        trackers = [
        'udp://open.demonii.com:1337/announce',
        'udp://tracker.openbittorrent.com:80',
        'udp://tracker.coppersurfer.tk:6969',
        'udp://glotorrents.pw:6969/announce',
        'udp://tracker.opentrackr.org:1337/announce',
        'udp://torrent.gresille.org:80/announce',
        'udp://p4p.arenabg.com:1337',
        'udp://tracker.leechers-paradise.org:6969',
        'http://track.one:1234/announce',
        'udp://track.two:80'
        ]

        movie_name_encoded = urllib3.request.urlencode({'dn':self.name}) ; 
        self.magnet = 'magnet:?xt=urn:btih:{}&{}'.format(self.hash , movie_name_encoded) ; 
        for tracker in trackers:
            self.magnet+=('&tr='+tracker)
        

    
    
    def download_torrent_file(self , path : str = os.path.expanduser('~/Downloads/') , filename = '' ):
        '''Downloads the torrent file into given path directory with the specified filename'''
        
        if not filename:
            filename = self.name+'.torrent'
        else:
            filename = filename.strip('.torrent') + '.torrent'  
            
        print(self.url) ;
        urlopen = urllib.request.URLopener() ; 
        urlopen.addheaders=[('User-Agent' , 'Mozilla/5.0')]
        urlopen.retrieve(self.url , path+filename)



    def start_downlod(self):
        if os.name=='nt':
            os.startfile(self.magnet) ; 
        else:
            os.system("xdg-open "+self.magnet) ; 
        
            


class movie():
    def __init__(self , name='' , page = ''):
        self.name = name ;
        self.page = page ; #Link to the torrent page

    def __str__(self):
        return "Name : {}\nPage : {}\n".format(self.name , self.page) ;

    def __repr__(self):
        return '''Name : {}\nPage : {}\nTorrent info obtained : {}\n\n'''.format(self.name , self.page , True if hasattr(self , 'id') else False);


    def getinfo(self , quality='All' , minimum_rating = 0 , 
    query_term = '' , genre='' , sort_by='date_added' ,
    order_by = 'desc' , with_rt_ratings='false'):
        '''
        Gets all the info about the torrent and returns a dictionary containing all the info
        '''

        self.name = re.search("^[^\(]+" ,self.name).group(0).strip() ; 
        # print(self.name) ; 
        url = "https://yts.ag/api/v2/list_movies.json" ;

        url = url+ '?' +  urllib3.request.urlencode({
            'quality' : quality , 
            'minimum_rating' : minimum_rating , 
            'query_term' : self.name, 
            'genre' : genre , 
            'sort_by' : sort_by , 
            'order_by' : order_by , 
            'with_rt_ratings' : with_rt_ratings
        })            

        resp = get(url , timeout = 3) ;
        data = json.loads(resp.text) ; 
        movie = data.get('data').get("movies")[0] ;
        # print(url) ;
        self.__get_movies_obj__(movie) ;  

    


    def __get_movies_obj__(self , movie : dict) : 
            self.id = movie.get('id')
            self.url = movie.get('url')
            self.imdb_code = movie.get('imdb_code')
            self.title = movie.get('title')
            self.title_long = movie.get('title_long')
            self.slug  = movie.get('slug')
            self.year = movie.get('year')
            self.rating = movie.get('rating')
            self.runtime = movie.get('runtime')
            self.genres = movie.get('genres') 
            self.summary = movie.get('summary')
            self.description = movie.get('description') 
            self.language = movie.get('language')
            self.mpa_rating = movie.get('mpa_rating')
            self.image_links = [movie.get('background_image'),
            movie.get('background_image_original'), 
            movie.get('small_cover_image'),
            movie.get('medium_cover_image'),
            movie.get('large_cover_image')]


            self.torrents = [] ;
            for torrent_item in movie.get('torrents'):
                # print(torrent_item);
                mytorrent = torrent(torrent_item  , name=self.name)
                self.torrents.append(mytorrent) ; 
                
            # print(self.torrents) ;





def search_movies(search_string : str = ''  , quality: str = 'All', minimum_rating : float  = 0 , 
    genre  : str = '') -> list:
    '''Used to search for particular movies which match the given parameters. 
    The Search String can be a Movie Title/IMDb Code, Actor Name/IMDb Code, Director Name/IMDb Code 
    Returns a list of Movies each movie object having complete details about it '''

    name = re.search("^[^\(]+" , search_string).group(0).strip() ; 
    # print(self.name) ; 
    url = "https://yts.ag/api/v2/list_movies.json" ;

    url = url+ '?' +  urllib3.request.urlencode({
        'minimum_rating' : minimum_rating , 
        'quality' : quality , 
        'query_term' : search_string, 
        'genre' : genre , 
    })            

    resp = get(url , timeout = 3) ;
    
    data  = json.loads(resp.text) ; 

    if(data.get('data').get('movies')):
        movies = [] ;
        for i in data.get('data').get('movies'):
            mymovie = movie(name = i.get('title')) ; 
            mymovie.__get_movies_obj__(i) ; 
            movies.append(movie) ; 

        return movies ; 

    else:
        return [] ;  


        


def get_top_seeded_torrents() -> list:
    '''Returns a list of Top Seeded Torrent's Movies which are listed in the Yify Website. 
    Each movie in the returned list contains only the 'movie name' and its corresponding 'page' attributes .
    All the rest of the details about the movie and the torrent can be obtained after calling the get_movie_info function on the movie object'''

    soup = BeautifulSoup(get(homepage , timeout=3).text , 'html.parser') ;
    topseeds = soup.find(id="topseed").find_all('a');

    top_torrents = [] 
    name_link = {} ; 


    for i in topseeds:
        name = re.search('^[^\(]+' , i.text).group(0).strip() ; 
        name_link[name] = homepage + i.get('href') ; 

    # print(name_link)

    for key,val in name_link.items():
        mymovie = movie(name = key , page  = val) ; 
        top_torrents.append(mymovie) ; 

    return top_torrents ; 

    

        
if __name__=='__main__':

    movies  = get_top_seeded_torrents() ;

    for movie in movies:
        movie.getinfo()
    
    
    
    torrent = movies[0].torrents[0] ;
    
    torrent.start_downlod() ;
