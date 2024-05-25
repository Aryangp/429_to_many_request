import weaviate
import os 
from dotenv import load_dotenv
import json
import pandas as pd
from fastapi import HTTPException, Request
import io 
import requests
import base64
from urllib.parse import urlparse

load_dotenv()

def weaviate_image_init():
    client = weaviate.Client("http://35.235.126.154:8080")
    return client


def weaviate_image_create_schema(className,properties):
    client=weaviate_image_init()
    client.schema.delete_class(className)
    class_search_schema={
            "class": className,
            "description": "Each object contains product image",
            "vectorizer": "img2vec-neural",
            "moduleConfig": {
            "img2vec-neural": {
                "imageFields": [
                "main_image"
                ]
            }
            },
            "properties": properties
          
        }
    client.schema.create_class(class_search_schema)
    return json.dumps({"message":"Schema created successfully"},indent=2)       


# convert image url to base64
def url_to_base64(url):
    response = requests.get(url)
    if response.status_code == 200:
        return base64.b64encode(response.content).decode('utf-8')
    else:
        #  raise error if image not found() and skip that object
        raise HTTPException(status_code=404, detail="Image not found")

# with image as file path
def weaviate_image_middleware_search(className,imageUrl):
    # current_dir = os.getcwd()
    # imagePath = file.save(os.path.join(current_dir,"images","class.jpg"))
    print(imageUrl)
    base64_image = url_to_base64(imageUrl)
    sourceImage = {"image": base64_image}
    client = weaviate_image_init()
    response = (
        client.query
        .get(className, ["title","main_image","description","raw_description","price","primary_category"])
        .with_near_image(sourceImage,encode=False)
        .with_limit(4)
        .do()
    )
    print(response)
    return json.dumps(response["data"]["Get"][className],indent=2)

# with image as base64
def weaviate_image_middleware_search_base64(request:Request):
    imageBase64 = request.query_params.get('imageBase64')
    sourceImage = { "main_image": imageBase64}
    className = request.query_params.get('className')
    client = weaviate_image_init()
    response = (
        client.query
        .get(className, ["title","main_image","description","raw_description","price","primary_category"])
        .with_near_image(sourceImage,encode=False)
        .with_limit(4)
        .do()
    )
    print(response)
    return json.dumps(response["data"]["Get"][className],indent=2)

def weaviate_image_add_data(data1,className):
    client=weaviate_image_init()
    uuid = client.data_object.create(
         class_name=className,
         data_object=data1
    )
    return uuid

# data1 format
# data1 = {
#             "title":base64_image,
#             "brand":42419	 ,
#             "main_image":"" ,
#             "description":"" ,
#             "raw_description":"url",
#             "price":0,
#             "primary_category":""
#} 

# helper function to add data to weaviate
def add_data(data1,className):
    client=weaviate_image_init()
    uuid = client.data_object.create(
         class_name= className,
         data_object=data1
    )
    print(uuid)
    return uuid

def get_objects(uuid,className):
    client=weaviate_image_init()
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




def weaviate_image_middleware_add_data(request,current_user,db,fileObject):
    className=current_user[1].className
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
        percentage = 100
            # Check if there are any null values in the DataFrame
        if df.isnull().values.any():
            # Iterate over each column
            for column in df.columns:
                # Check if the column has null values
                if df[column].isnull().any():
                    # Fill the null values with a default value (e.g. 0)
                    df[column].fillna(0, inplace=True)

        # Get the image_url column from the DataFrame
        image_urls = df['main_image']

        # Convert each image_url to base64 and save it back in its row
        for index, url in enumerate(image_urls):
            try:
                base64_image = url_to_base64(url)
                df.at[index, 'main_image'] = base64_image
            except HTTPException as e:
                raise HTTPException(status_code=404, detail=str(e))
            
        # Calculate the number of rows to sample based on the percentage
        sample_size = int(len(df) * percentage / 100)
        # Use the sample method to randomly select the specified percentage of data
        test_data = df.sample(n=sample_size)
        test_data = test_data.round(4)  # Adjust the precision as needed
        dict_df=convert_data(test_data)
        try:
            for data in dict_df:
                uuid=add_data(data,className)
            return json.dumps({"message":"Data added successfully","uuid":uuid},indent=2)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        





#   "properties": [
#             {
#                 "dataType": [
#                 "blob"
#                 ],
#                 "description": "Product Image",
#                 "name": "main_image"
#             },
#             {
#                 "dataType": [
#                     "text"
#                 ], 
#                 "description": "Title of the product",
#                 "name": "title"
#             },
#             {
#                 "dataType": [
#                     "text"
#                 ], 
#                 "description": "Brand of the product",
#                 "name": "brand"
#             },
#             {
#                 "dataType": [
#                     "text"
#                 ], 
#                 "description": "Description of the product",
#                 "name": "description"
#             },
#             {
#                 "dataType": [
#                     "text"
#                 ], 
#                 "description": "Raw Description of the product",
#                 "name": "raw_description"
#             },
#             {
#                 "dataType": [
#                     "number"
#                 ], 
#                 "description": "Price of the product",
#                 "name": "price"
#             },
#             {
#                 "dataType": [
#                     "text"
#                 ], 
#                 "description": "Primary Category of the product",
#                 "name": "primary_category"
#             } 
#         ]