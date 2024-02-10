
# Catalog Indexing Engine

We present a robust catalog searching engine tailored for the dynamic landscape of e-commerce, with the flexibility to extend its architecture for diverse applications. The project revolves around efficiently processing and retrieving information from client-provided CSV files containing detailed product or item information.

## Architecture Overview


![App Screenshot](https://github.com/code-inhub/NewsApp3.0/assets/95998892/36177606-700e-41cb-aa8d-6a3fe8d53367)

- **CSV Data Ingestion & Embedding:**
  Stores item data in the Weavite Vector Database for efficient and fast retrieval.

- **Unstructured Text Search:**
  Utilizes an inverted index for keyword matching, enabling versatile and precise search capabilities.

- **Image Search:** Enables image-based product discovery, enhancing the visual exploration of the catalog.

- **AI-Powered Filtering:** Refines search results based on user intent through intelligent AI-powered filtering.

- **Re-Ranking:** Prioritizes the most relevant items using advanced re-ranking algorithms.

- **Benefits:** Provides fast and accurate search capabilities for large catalogs.
  
  Adaptable to various domains, ensuring versatility in application.
## AI Models: Boosting Search Power

Our project harnesses the capabilities of multiple AI models to elevate search intelligence:

- **Embeddings & Re-ranking (all-MiniLM-L6-v2):**
  - Captures product meaning and refines search results for optimal relevance.

- **Image Summarization (LLaVA):**
  - Extracts key visuals from images, enhancing the efficiency of image-based search.

- **Planned: Token-based Transformers (Mixtral-8x7B-Instruct-v0.1):**
  - Upcoming implementation aimed at further enhancing embeddings and re-ranking.

This AI-powered approach ensures that your searches deliver the results you crave.

## Usage
![catalog_test](https://github.com/Aryangp/429_to_many_request/assets/91003905/8ff560c2-05fb-47e1-88ad-dd1eeaf04a8c)

#### I. Querying:

- **Submit Queries:**
  Enter keywords, phrases, or voice commands to initiate searches.

- **Filters and Refinement:** Refine search results by applying filters such as category, price, etc. AI-powered suggestions may assist in the refinement process.

- **Understanding Results:**
  Results are ranked by relevance and presented in paginated form for user convenience.
- Re-ranking functionality (under development) aims to further enhance result accuracy.


#### II. Image Searching (Production Feature):

- **Upload or Provide Image Link:**
  Upload a product image or provide a link to search for similar items.
  Image search results are intelligently combined with text-based results.

**Note:**
Re-ranking, Image searching and AI filtering  functionalites is currently under development.


## API Reference

#### Get Search Result

```http
  POST /search
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` | **Required**. Your Query|
| `className` | `string` | **Required**. Your class name of weaviate schema |

#### Create Weaviate Schema

```http
  POST /weaviate/schema
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `className`      | `string` | **Required**. class Name of the weaviate schema |
| `properties`      | `mentioned below` | **Required**. Id of item to fetch |

```
   "properties": [
           {
             "name": "unique_id",
             "dataType": ["int"],
             "description": "user id",
             "moduleConfig": {
                 "text2vec-huggingface": {
                 "skip": True,
                 "vectorizePropertyName": True
                 }
             }
             },
             {
             "name": "product_name",
             "dataType": ["text"],
             "description": "product_name",
             "moduleConfig": {
                 "text2vec-huggingface": {
                 "skip": True,
                 "vectorizePropertyName": True
                 }
             }
           }
        ]

```
#### Add Data

```http
  POST /add/data
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `datafile`      | `csv` | **Required**. Data file for adding data |

#### format of the file

```
# This should be the title of each column and type of data
  brand: string,
  category: string,
  market_price: number,
  product_desc: string,
  product_name: string,
  rating: number,
  sale_price: number,
  sub_category: string,
  unique_id: string
```

## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## Running Tests

To run tests, run the following command

```bash
  npm run test
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

