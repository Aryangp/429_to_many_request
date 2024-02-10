"use client"
import React, { useState, useEffect } from "react";
import SearchBar from "../components/SearchBar";
import Filter from "../components/Filter";
import Card from "../components/Card";
import { useDebounce } from "../components/hooks/useDebounce";
import axios from "../utils/axios";

type AdditionaData={
  distance:number
}

type SearchResult= {
  additional: AdditionaData,
  brand: string,
  category: string,
  market_price: number,
  product_desc: string,
  product_name: string,
  rating: number,
  sale_price: number,
  sub_category: string,
  unique_id: string
}


const Search = () => {
  const [inputValue, setInputValue] = useState<string>("");
  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  const searchQuery = useDebounce(inputValue, 1000);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const { data } = await axios.post("/search", {
          query: searchQuery,
          className: "CatalogSearchWithDescription"
        });
        const parsedData = JSON.parse(data);
        setSearchResults(parsedData);
      } catch (error) {
        console.error("Error fetching search results:", error);
        // Handle error gracefully (e.g., show an error message)
      }
    };

    if (searchQuery) {
      fetchData();
    } else {
      // Clear search results if search query is empty
      setSearchResults([]);
    }
  }, [searchQuery]);

  console.log("data in the searchResult", searchResults);

  return (
    <>
      <div className="ml-3 flex justify-center flex-row gap-2">
        <div>
          <SearchBar inputValue={inputValue} setInputValue={setInputValue} />
        </div>
        <div className="m-6">
          <Filter />
        </div>
      </div>
      
      <div className="flex flex-row flex-wrap gap-4 gap-x-6 m-4 justify-center">
        {searchResults.length === 0 ? (
          <p>No results found</p>
        ) : (
          searchResults.map((result) => (
            <div key={result.unique_id}>
              <Card cardDetails={result} />
            </div>
          ))
        )}
      </div>
    </>
  );
};

export default Search;
