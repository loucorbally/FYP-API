import os
import requests
import flask
import redis
import datetime
import json

class RedisProvider(object):
    def __init__(self, items: list=[]):
        self._items = items

        
    def HelloWorld(self) -> str:
        return "Hello World"

    #Function to set score
    def setPlayerScore(self, productPayload) -> str:
        #Connect to Redis
        pool = redis.ConnectionPool(host=os.environ.get('REDIS_SERVER','86.43.201.231'), port=6379, db=0)
        r = redis.Redis(connection_pool=pool)
        productPayload['score'] = float(productPayload['score'])
        r.zadd('score.mazegame:'+datetime.datetime.today().strftime('%Y-%m-%d'),  productPayload["userid"],productPayload["score"])
        r.zadd('score.mazegame', productPayload["userid"],productPayload["score"] )

        return "Success", 201      

    def getTodaysHighScore(self) -> str:

        #Connect to Redis
        pool = redis.ConnectionPool(host=os.environ.get('REDIS_SERVER','86.43.201.231'), port=6379, db=0)
        r = redis.Redis(connection_pool=pool)
        
        # Run zrevrange from docs zrevrange
        results = r.zrevrange(str('score.mazegame:'+datetime.datetime.today().strftime('%Y-%m-%d')) , 0, 5, withscores=True) 
        
        #Display results - Take winning player + highscore
        score = results[0]
        return "Todays high-score is : "+str(score[0].decode("utf-8"))+ " with score : "+str(score[1]), 200 

    def getLeaderboard(self) -> str:
        self.formatted_results = []
        #Connect to redis
        pool = redis.ConnectionPool(host=os.environ.get('REDIS_SERVER','86.43.201.231'), port=6379, db=0)
        r = redis.Redis(connection_pool=pool)
        
        # Run zrevrange from docs zrevrange
        raw_results = r.zrevrange(str('score.mazegame:'+datetime.datetime.today().strftime('%Y-%m-%d')) , 0, 5, withscores=True) 
        #Format results
        for score in raw_results:
            self.formatted_results.append([score[0].decode("utf-8"), score[1]])
        

        return json.dumps(self.formatted_results), 200    