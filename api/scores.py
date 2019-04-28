from flask_injector import inject
from services.RedisProvider import RedisProvider
import flask

from flask import request, Response

@inject(data_provider=RedisProvider)
def HelloWorld(data_provider) -> str:
   return data_provider.HelloWorld()

@inject(data_provider=RedisProvider)
def setPlayerScore(data_provider, productPayload) -> str:
    return data_provider.setPlayerScore(productPayload)

@inject(data_provider=RedisProvider)
def getTodaysHighScore(data_provider) -> str:
    return data_provider.getTodaysHighScore() 