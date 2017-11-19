import time;
from bs4 import BeautifulSoup
from requests import get


class yify():

    class torrent():
        def __init__(self , name='' , link = ''):
            self.name = name ;
            self.link = link ; #Link to the torrent page

        def __str__(self):
            return "Name : {}   |   Page : {}".format(self.name , self.link) ;
        def __repr__(self):
            return "Name : {}   |   Page : {}".format(self.name , self.link) ;
            
        def getinfo(self):
            soup  = BeautifulSoup(get(self.link).text , 'html.parser') ;



    class topseed():
        def __init__(self):
            pass ; 

        def get_top_seeded_torrents(self):
            '''Returns the top seeded torrent objects'''
            raise NotImplementedError ;

        


    def __init__(self):
        resp = '';
        while(not resp):
            try:
                resp = get('https://www.yify-torrent.org/', timeout=3);

            except Exception as e:
                print(e);
                print(
                    "\nServer refused connection . \nSleeping for 5 seconds .....\nZZZzzzzzzzzz\n\n");
                time.sleep(5);

        self.soup = BeautifulSoup(resp.text, 'html.parser');



    def get_top_seeds(self):
        self.topseeds = self.soup.find(id="topseed").find_all('a');


        topseeds_names =  [];
        topseeds_links = [] ; 


        for i in self.topseeds:
            topseeds_names.append(i.text);
            topseeds_links.append(i.get('href')) ;


        # for i in range(len(topseeds)):
        #     topseeds[i] = topseeds[i].strip('1080p').strip() ; 

        # topseeds = list(set(topseeds)) ;

        self.names = topseeds_names
        self.links = topseeds_links 
        
        return topseeds ;

 
        
