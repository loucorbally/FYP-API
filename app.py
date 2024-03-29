import os
from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
import connexion
from services.RedisProvider import RedisProvider

# Connexion can only receive 2 params
application = connexion.App(__name__, specification_dir='swagger/')

#Setup with Swagger and RestyResolver
application.add_api('api-docs.yaml', resolver=RestyResolver('api'))
def configure(binder: Binder) -> Binder:
    binder.bind(
        RedisProvider
        
    )

#Redefine application as a connexion app. 
application = connexion.App(__name__, specification_dir='swagger/')
application.add_api('api-docs.yaml', resolver=RestyResolver('api'))

#FlaskInjector Setup defined after configure
FlaskInjector(app=application.app, modules=[configure])

if __name__ == '__main__':
    
  
    #Start the flask server on either on port 2025
    application.run(server='tornado', port=int(os.environ.get('PORT', 2025)))