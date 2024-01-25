import weaviate
from dotenv import load_dotenv
import os

load_dotenv()

client = weaviate.Client(
    url = "https://429-many-request-il0pfr3n.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY")),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-HuggingFace-Api-Key": os.getenv("HUGGINGFACE_API_KEY")  # Replace with your Hugging Face API key
    }
)


def weaviate_search(query, filters):
    """
    Search Weaviate using the query and filters provided
    """
    pass



def create_schema():
    class_search_schema={
    "classes": [
        {
        "class": "CatalogSearch",
        "description": "A class called catalog search",
        "vectorizer": "text2vec-huggingface",
        "vectorIndexType": "hnsw",# can be set flat for that refer https://weaviate.io/developers/weaviate/manage-data/collections

        "vectorIndexConfig": {
        "pq": {
        "enabled": True,
        "trainingLimit": 100000,
        "segments": 512 # refer here https://weaviate.io/developers/weaviate/concepts/vector-index#:~:text=HNSW%20is%20an%20algorithm%20that,(adding%20data%20with%20vectors).
        },
        "distance": "cosine",
        },
        "moduleConfig": {
            "text2vec-huggingface": {
            "model": "sentence-transformers/all-MiniLM-L6-v2",
            "options": {
                "waitForModel": True,
                "useGPU": False,
                "useCache": True
            },
            "vectorizeClassName": False
            }
        },
        "properties": [
            {
            "name": "unique_id",
            "dataType": ["string"],
            "description": "user id",
            "moduleConfig": {
                "text2vec-huggingface": {
                "skip": False,
                "vectorizePropertyName": False
                }
            }
            },
            {
            "name": "product_id",
            "dataType": ["text"],
            "description": "product id",
            "moduleConfig": {
                "text2vec-huggingface": {
                "skip": True,
                "vectorizePropertyName": False
                }
            }
            },
            {
            "name": "category",
            "dataType": ["string"],
            "description": "category of product",
            "moduleConfig": {
                "text2vec-huggingface": {
                "skip": False,
                "vectorizePropertyName": False
                }
            }
            },
            {
            "name": "sub_category",
            "dataType": ["string"],
            "description": "sub category of product",
            "moduleConfig": {
                "text2vec-huggingface": {
                "skip": False,
                "vectorizePropertyName": False
                }
            }
            },
            {
            "name": "product_type",
            "dataType": ["string"],
            "description": "product type",
            "moduleConfig": {
                "text2vec-huggingface": {
                "skip": False,
                "vectorizePropertyName": False
                }
            }
            },
            {
            "name": "color",
            "dataType": ["string"],
            "description": "color of product",
            "moduleConfig": {
                "text2vec-huggingface": {
                "skip": False,
                "vectorizePropertyName": False
                }
            }
            },
            {
            "name": "usage",
            "dataType": ["string"],
            "description": "usage of product",
            "moduleConfig": {
                "text2vec-huggingface": {
                "skip": False,
                "vectorizePropertyName": False
                }
            }
            },
            {
            "name": "product_title",
            "dataType": ["string"],
            "description": "product title",
            "moduleConfig": {
                "text2vec-huggingface": {
                "skip": False,
                "vectorizePropertyName": False
                }
            }
            }
        ]
        }
    ]
    }

    client.schema.create_class(class_search_schema)    
    




def add_data(data):
    client.batch.create_objects(data)
