import os
import requests
import flask
import redis
import datetime
import json

class RedisProvider(object):
    def __init__(self, items: list=[]):
        self._items = items
        self.formatted_results = []
        
    
    def HelloWorld(self) -> str:
        return "Hello World"