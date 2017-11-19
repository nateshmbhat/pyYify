import time;
from bs4 import BeautifulSoup
from requests import get
import re 

class yify():

    class torrent():
        def __init__(self , name='' , page = ''):
            self.name = name ;
            self.page = page ; #Link to the torrent page

        def __str__(self):
            return "Name : {}   |   Page : {}".format(self.name , self.page) ;
        def __repr__(self):
            return "Name : {}   |   Page : {}".format(self.name , self.page) ;
            
        def getinfo(self):
            '''
            Gets all the info about the torrent and returns a dictionary containing all the info
            
            '''
            soup  = BeautifulSoup(get(self.page).text , 'html.parser') ;
            magnet  = soup.select("a[class='large button orange']")[0].get('href') ;
            link = soup.select("a[class='middle button orange'")[0].get('href') ;
            link2 = soup.select("a[class='middle button red'")[0].get('href') ;

            self.magnet = magnet ; 
            self.link = link ;

            attrs = soup.select("div[class='inattr']") ;
            
            infos ={'magnet' : magnet, 
            'link' : link , 
            'link2' : link2} ;

            for info in attrs.find_all('li'):
                infos[info.b] = re.search("{}\s*:(.*)" , info.text ).group(1).strip() ;

            return info ;

                


                
                




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



    def get_top_seeded_torrents(self):
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
        

 
        
