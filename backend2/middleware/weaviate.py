import weaviate
import os 
from dotenv import load_dotenv
import json
import pandas as pd
from flask import jsonify
import base64, requests

load_dotenv()

def weaviate_init():
    # client = weaviate.Client(
    #     url = "https://new-cluster-testing-ygkcz16f.weaviate.network",  # Replace with your endpoint
    #     auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY")),  # Replace w/ your Weaviate instance API key
    #     additional_headers = {
    #         "X-HuggingFace-Api-Key": os.getenv("HUGGINGFACE_API_KEY")  # Replace with your Hugging Face API key
    #     }
    # )
    client = weaviate.Client(
        url = "http://34.125.130.73:8080",  # Replace with your endpoint
    )
    return client

def weaviate_middleware_search(request):
    query = request.get_json().get('query')
    className = request.get_json().get('className')
    client = weaviate_init()
    response = (
        client.query
        .get(className, ["unique_id", "product_name","category","sub_category","brand","sale_price","market_price","product_type","rating","product_desc"])
        .with_near_text({
            "concepts": [query],
        })
        .with_limit(4)
        .with_additional(["distance"])
        .do()
    )
    return json.dumps(response["data"]["Get"]["CatalogSearchWithDescription"],indent=2)

def weaviate_middleware_filter_search(request):
    query = request.get_json().get('query')
    className = request.get_json().get('className')

    ######### expecting price, brand, category, sub_category, rating as filters #########

    upper_price_limit = request.get_json().get('upper_price_limit')
    lower_price_limit = request.get_json().get('lower_price_limit')
    brand = request.get_json().get('brand')
    category = request.get_json().get('category')
    sub_category = request.get_json().get('sub_category')
    min_rating = request.get_json().get('min_rating')

    client = weaviate_init()
    response = (
        client.query
        .get(className, ["unique_id", "product_name","category","sub_category","brand","sale_price","market_price","product_type","rating","product_desc"])
        .with_hybrid(
            query=query,
        )
        .with_where({
            # check whether the filter to be applied on sale price or market price
            "operator": "And",
            "operands": [
                {
                    "path": ["sale_price"],
                    "operator": "GreaterThan",
                    "valueInt": lower_price_limit
                },
                {
                    "path": ["sale_price"],
                    "operator": "LessThan",
                    "valueInt": upper_price_limit
                },
                {
                    "path": ["brand"],
                    "operator": "Equal",
                    "valueString": brand
                },
                {
                    "path": ["category"],
                    "operator": "Equal",
                    "valueString": category
                },
                {
                    "path": ["sub_category"],
                    "operator": "Equal",
                    "valueString": sub_category
                },
                {
                    "path": ["rating"],
                    "operator": "GreaterThan",
                    "valueInt": min_rating
                }
            ]
        })
        .with_limit(30)
        .with_additional(["distance"])
        .do()
    )
    return json.dumps(response["data"]["Get"]["CatalogSearchWithDescription"],indent=2)


##### For Image Search  changes in schema to be done are : ##### 
    #  {
    #       "dataType": [
    #         "blob"
    #       ],
    #       "description": "product image",
    #       "name": "image"
    #     },

##### Fot image search implementation we need to create a new weavaite container and enable img2vec-neural module using weavaite docker compose refer here :  
# https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/img2vec-neural#nearimage 

def weaviate_image_search(request):
    client=weaviate_init()
    image=request.get_json().get('image')
    class_name = request.get_json().get('className')
    response = (
    client.query
    .get(class_name, ["unique_id", "product_name","category","sub_category","brand","sale_price","market_price","product_type","rating","product_desc","image"])
    .with_near_image({"image": image})  # default `encode=True` reads & encodes the file
    .with_limit(10)
    .do()
)

def weaviate_create_schema(className,properties):
    client=weaviate_init()
    client.schema.delete_class("CatalogSearchWithDescription")
    class_search_schema={
        "class": className,
        "description": f"A class called {className} and used for doing vector search on {className} data.",
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
        "properties": properties
        }
    client.schema.create_class(class_search_schema)

#dummy data of the properties
    
    #  "properties": [
    #         {
    #         "name": "unique_id",
    #         "dataType": ["int"],
    #         "description": "user id",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": True,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         },
    #         {
    #         "name": "product_name",
    #         "dataType": ["text"],
    #         "description": "product_name",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": True,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         },

    #         {
    #         "name": "product_desc",
    #         "dataType": ["text"],
    #         "description": "product description",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": True,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         },

    #         {
    #         "name": "category",
    #         "dataType": ["text"],
    #         "description": "category of product",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": False,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         },
    #         {
    #         "name": "sub_category",
    #         "dataType": ["text"],
    #         "description": "sub category of product",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": False,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         },
    #         {
    #         "name": "brand",
    #         "dataType": ["text"],
    #         "description": "product brand",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": False,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         },
    #         {
    #         "name": "sale_price",
    #         "dataType": ["number"],
    #         "description": "color of product",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": False,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         },
    #         {
    #         "name": "product_type",
    #         "dataType": ["text"],
    #         "description": "type of product",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": False,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         },
    #         {
    #         "name": "market_price",
    #         "dataType": ["number"],
    #         "description": "product title",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": False,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         },
    #         {
    #         "name": "rating",
    #         "dataType": ["number"],
    #         "description": "rating",
    #         "moduleConfig": {
    #             "text2vec-huggingface": {
    #             "skip": False,
    #             "vectorizePropertyName": True
    #             }
    #         }
    #         }
    #     ]


# helper function to add data to weaviate
def add_data(data1):
    client=weaviate_init()
    uuid = client.data_object.create(
         class_name="CatalogSearchWithDescription",
         data_object=data1
    )
    return uuid

def get_objects(uuid,className):
    client=weaviate_init()
    data_object = client.data_object.get_by_id(
      uuid,
      class_name=className,
  )
    return json.dumps(data_object,indent=2)

def convert_data(df_new):
    rows_as_dicts=[]
    for index, row in df_new.iterrows():
        row_dict = row.to_dict()
        rows_as_dicts.append(row_dict)
    return rows_as_dicts


# Main function to add the data to weaviate
def weaviate_middleware_add_data(request):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    
    allowed_extensions = {'csv'}
    if '.' not in file.filename or file.filename.split('.')[-1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file type. Only CSV files are allowed.'}), 400

    if file:
        try:
            file.save(file.filename)
            df = pd.read_csv(file.filename)
        except Exception as e:
            return jsonify({'error': f'Failed to read the file: {str(e)}'}), 400
        percentage = 10
        # Calculate the number of rows to sample based on the percentage
        sample_size = int(len(df) * percentage / 100)
        # Use the sample method to randomly select the specified percentage of data
        test_data = df.sample(n=sample_size)
        test_data = test_data.round(4)  # Adjust the precision as needed
        test_data_new=test_data.head(200)
        dict_df=convert_data(test_data_new)
        try:
            for data in dict_df:
                uuid=add_data(data)
            return jsonify({'message': 'Data added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        

