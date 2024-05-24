import weaviate
import os 
from dotenv import load_dotenv
import json
import pandas as pd
from fastapi import HTTPException, Request
import io 
load_dotenv()

def weaviate_init():
    client = weaviate.Client(
        url = "https://weaviatetest-8o6sm485.weaviate.network",  # Replace with your endpoint
        auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY")),  # Replace w/ your Weaviate instance API key
        additional_headers = {
            "X-HuggingFace-Api-Key": os.getenv("HUGGINGFACE_API_KEY")  # Replace with your Hugging Face API key
        }
    )
    # client = weaviate.Client(
    #     #http://34.168.110.14:8080
    #     url = "http://35.230.98.126:8080",  # Replace with your endpoint
    # )
    return client

def weaviate_middleware_search(request,db,current_data,query):
    className = current_data[1].className
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
    print(response)
    return json.dumps(response["data"]["Get"][className],indent=2)



def weaviate_filter_price(data,className,query):
    client=weaviate_init()
    upper_price_limit = data['price']['upper_price_limit']
    lower_price_limit =data['price']['lower_price_limit']
    print(upper_price_limit)
    print(lower_price_limit)
    response = (
        client.query
        .get(className, ["unique_id", "product_name","category","sub_category","brand","sale_price","market_price","product_type","rating","product_desc"])
        .with_near_text({
            "concepts": [query],
        })
        .with_where({
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
                }
            ]
        })
        .with_limit(10)
        .with_additional(["distance"])
        .do()
    )

    return json.dumps(response["data"]["Get"][className],indent=2)

def weaviate_create_schema(className,properties):
    client=weaviate_init()
    client.schema.delete_class(className)
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
    return json.dumps({"message":"Schema created successfully"},indent=2)

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
def weaviate_middleware_add_data(request,current_user,db,fileObject):
    if fileObject.filename == '':
        raise HTTPException(status_code=400, detail="No file selected for uploading")
    
    allowed_extensions = {'csv'}
    if '.' not in fileObject.filename or fileObject.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file")

    if fileObject:
        try:
            contents = fileObject.file.read()
            df = pd.read_csv(io.BytesIO(contents))
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        print("no error till now")
        percentage = 10
            # Check if there are any null values in the DataFrame
        if df.isnull().values.any():
            # Iterate over each column
            for column in df.columns:
                # Check if the column has null values
                if df[column].isnull().any():
                    # Fill the null values with a default value (e.g. 0)
                    df[column].fillna(0, inplace=True)
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
            return json.dumps({"message":"Data added successfully","uuid":uuid},indent=2)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        

