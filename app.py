import connexion

if __name__ == '__main__':
    
    #Set up Connexion with swagger file
    application = connexion.App(__name__, specification_dir='swagger/')

    #Specify name of swagger file
    application.add_api('api-docs.yaml')

    #Start the flask server on 2025
    application.run(port=2025)