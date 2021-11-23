from azure.cosmos import CosmosClient, exceptions,PartitionKey
import os

os.environ['ACCOUNT_URI']="https://rgdb.documents.azure.com:443/"
os.environ['ACCOUNT_KEY']="qetiOLTp1XaE1CyG3E6NMKyfXIG9b7aIZHKBz8AsljxoQ6kMozErxqUetSEOiu8tbVjWsXLEjP5DT8wcnVbF3g=="

url = os.environ['ACCOUNT_URI']
key = os.environ['ACCOUNT_KEY']
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'

try:
    database = client.create_database(database_name)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)

container_name="smhproducts"
try:
	container=database.create_container(id=container_name, partition_key=PartitionKey(path="/productName"))
except exceptions.CosmosResourceExistsError:
	container=database.get_container_client(container_name)
except exceptions.CosmosHttpResponseError:
	raise
    
