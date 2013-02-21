#coding:utf-8
from base import BaseHandler

class HomeHandler(BaseHandler):
    'Home Page'
    
    def get(self):
        'Index Page'
        
        self.render('home.html')