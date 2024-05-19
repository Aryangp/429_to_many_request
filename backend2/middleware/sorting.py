def sort_by_price_ascending(data, price_key='sale_price'):
    # Ensure the price_key exists in the dictionaries
    if not data or price_key not in data[0]:
        raise ValueError(f"Key '{price_key}' not found in the data")

    # Sort the data by the price_key
    sorted_data = sorted(data, key=lambda x: x[price_key])

    return sorted_data



def sort_by_price_descending(data, price_key='sale_price'):
    # Ensure the price_key exists in the dictionaries
    if not data or price_key not in data[0]:
        raise ValueError(f"Key '{price_key}' not found in the data")

    # Sort the data by the price_key in descending order
    sorted_data = sorted(data, key=lambda x: x[price_key], reverse=True)

    return sorted_data


# # Example usage:
# data = [
#     {"unique_id": 1, "product_name": "Product A", "category": "Category 1", "sub_category": "Subcategory 1", "brand": "Brand A", "sale_price": 20.0, "market_price": 25.0, "product_type": "Type 1", "rating": 4.5, "product_desc": "Description A"},
#     {"unique_id": 2, "product_name": "Product B", "category": "Category 1", "sub_category": "Subcategory 1", "brand": "Brand B", "sale_price": 10.0, "market_price": 15.0, "product_type": "Type 1", "rating": 4.0, "product_desc": "Description B"},
#     {"unique_id": 3, "product_name": "Product C", "category": "Category 1", "sub_category": "Subcategory 2", "brand": "Brand C", "sale_price": 30.0, "market_price": 35.0, "product_type": "Type 2", "rating": 5.0, "product_desc": "Description C"},
# ]

# sorted_data = sort_by_price_descending(data)
# for product in sorted_data:
#     print(product)