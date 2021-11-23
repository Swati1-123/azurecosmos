from azure.cosmos import CosmosClient, exceptions
import os

url = os.environ['ACCOUNT_URI']"https://rgdb.documents.azure.com:443/"
key = os.environ['ACCOUNT_KEY']"qetiOLTp1XaE1CyG3E6NMKyfXIG9b7aIZHKBz8AsljxoQ6kMozErxqUetSEOiu8tbVjWsXLEjP5DT8wcnVbF3g=="
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'
try:
    database = client.create_database(database_name)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)
