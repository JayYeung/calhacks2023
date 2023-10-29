import uuid
import os
import openai
from time import sleep
from pymilvus import Milvus, DataType

class Database:
    def __init__(self, URI, TOKEN, collection_name):
        self.uri = URI
        self.token = TOKEN
        self.collection_name = collection_name
        self.embed_model = "text-embedding-ada-002"
        self.client = Milvus(uri=self.uri, token=self.token)

    def create_embeddings(self, texts):
        try:
            res = openai.Embedding.create(input=texts, engine=self.embed_model)
        except:
            done = False
            while not done:
                sleep(5)
                try:
                    res = openai.Embedding.create(input=texts, engine=self.embed_model)
                    done = True
                except:
                    pass
        return res['data'][0]['embedding']

    def insert(self, text):
        embedding = self.create_embeddings(text)
        print("embeddings length", len(embedding))
        res = self.client.insert(
            collection_name=self.collection_name,
            
            data={
                'id': 0, 
                'title': 'The Reported Mortality Rate of Coronavirus Is Not Important', 
                'link': 'https://medium.com/swlh/the-reported-mortality-rate-of-coronavirus-is-not-important-369989c8d912', 
                'reading_time': 13, 
                'publication': 'The Startup', 
                'claps': 1100, 
                'responses': 18, 
                'vector': embedding
            }
        )
        print(f'Inserted IDs: {res}')

    def retrieve(self, text):
        query_embedding = self.create_embeddings(text)
        query = {
            "bool": {
                "must": [
                    {
                        "vector": {
                            "embedding": {"topk": 10, "query": [query_embedding], "metric_type": "L2"}
                        }
                    }
                ]
            }
        }
        results = self.client.search(self.collection_name, query)
        return results

URI = 'https://in03-9728d08fb18f6ac.api.gcp-us-west1.zillizcloud.com:19530'
TOKEN = 'c9cbe44a6b289610acfe8bedb9fafe51f708f3bbf9922f3b2965c3fadca831cb1eaa128a60a6b8ec82b61c8aec115666d3bb57e6'

COLLECTION_NAME = 'calhacks'

db = Database(URI, TOKEN, COLLECTION_NAME)

db.insert( "Hello, this is another test message from abc.")

retrieval_results = db.retrieve("i have a fever")

print("Retrieval Results:")
print(retrieval_results)
