from azure.cosmos import CosmosClient
import os

os.environ['ACCOUNT_URI']="https://rgdb.documents.azure.com:443/"
os.environ['ACCOUNT_KEY']="qetiOLTp1XaE1CyG3E6NMKyfXIG9b7aIZHKBz8AsljxoQ6kMozErxqUetSEOiu8tbVjWsXLEjP5DT8wcnVbF3g=="

url = os.environ['ACCOUNT_URI']
key = os.environ['ACCOUNT_KEY']
client = CosmosClient(url, credential=key)
database_name = 'testDatabase'
database = client.get_database_client(database_name)
container_name = 'smhproducts'
container = database.get_container_client(container_name)

# Enumerate the returned items
import json
for item in container.query_items(
        query='SELECT * FROM smhproducts r WHERE r.id="item3"',
        enable_cross_partition_query=True):
    print(json.dumps(item, indent=True))
