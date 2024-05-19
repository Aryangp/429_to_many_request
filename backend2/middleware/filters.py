import weaviate
import os 
from dotenv import load_dotenv
import json
import base64, requests

load_dotenv()


def weaviate_init():
    client = weaviate.Client(
        url = "https://test-q86eb9wz.weaviate.network",  # Replace with your endpoint
        auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY")),  # Replace w/ your Weaviate instance API key
        additional_headers = {
            "X-HuggingFace-Api-Key": os.getenv("HUGGINGFACE_API_KEY")  # Replace with your Hugging Face API key
        }
    )
    # client = weaviate.Client(
    #     url = "http://34.125.130.73:8080",  # Replace with your endpoint
    # )
    return client

client = weaviate_init()

def weaviate_search(request):
    query = request.get_json().get('query')
    className = request.get_json().get('className')
    response = (
        client.query
        .get(className, ["unique_id", "product_name","category","sub_category","brand","sale_price","market_price","product_type","rating","product_desc"])
        .with_hybrid(
            query=query,
        )
        .with_limit(20)
        .with_additional(["distance"])
        .do()
    )
    return json.dumps(response["data"]["Get"][className],indent=2)

def weaviate_filter_price(request):
    query = request.get_json().get('query')
    className = request.get_json().get('className')
    upper_price_limit = request.get_json().get('upper_price_limit')
    lower_price_limit = request.get_json().get('lower_price_limit')
    response = (
        client.query
        .get(className, ["unique_id", "product_name","category","sub_category","brand","sale_price","market_price","product_type","rating","product_desc"])
        .with_hybrid(
            query=query,
        )
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
        .with_limit(20)
        .with_additional(["distance"])
        .do()
    )
    return json.dumps(response["data"]["Get"][className],indent=2)


def weaviate_filter_rating(request):
    query = request.get_json().get('query')
    className = request.get_json().get('className')
    min_rating = request.get_json().get('min_rating')
    response = (
        client.query
        .get(className, ["unique_id", "product_name","category","sub_category","brand","sale_price","market_price","product_type","rating","product_desc"])
        .with_hybrid(
            query=query,
        )
        .with_where(
            {
                "path": ["rating"],
                "operator": "GreaterThan",
                "valueInt": min_rating
            }
        )               
        .with_limit(20)
        .with_additional(["distance"])
        .do()
    )
    return json.dumps(response["data"]["Get"][className],indent=2)


def weaviate_filter_rating_price(request):
    query = request.get_json().get('query')
    className = request.get_json().get('className')

    upper_price_limit = request.get_json().get('upper_price_limit')
    lower_price_limit = request.get_json().get('lower_price_limit')
    min_rating = request.get_json().get('min_rating')

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
                    "path": ["rating"],
                    "operator": "GreaterThan",
                    "valueInt": min_rating
                }
            ]
        })
        .with_limit(20)
        .with_additional(["distance"])
        .do()
    )
    return json.dumps(response["data"]["Get"][className],indent=2)


