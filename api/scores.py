from flask_injector import inject
from services.RedisProvider import RedisProvider
import flask

from flask import request, Response

@inject(data_provider=RedisProvider)
def HelloWorld(data_provider) -> str:
   # return data_provider.getLeaderboard()
   return data_provider.HelloWorld()