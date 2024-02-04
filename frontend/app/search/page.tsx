"use client";
import React, { useState, useEffect } from "react";
import SearchBar from "../components/SearchBar";
import Card from "../components/Card";
import Filter from "../components/Filter";
import { useDebounce } from "../components/hooks/useDebounce";

const Search = () => {
  const [inputValue, setInputValue] = useState<string>("");
  const searchQuery = useDebounce(inputValue, 1000);
  const [searchResults, setSearchResults] = useState<string[]>([]);

  useEffect(() => {
    // fetch data from the API
    // set the data to searchResults
  }, [searchQuery]);

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
      <div className=" text-green-300 font-bold text-xl m-5">{searchQuery}</div>
      <div className="flex flex-row flex-wrap gap-4 gap-x-6 m-4 justify-center">
        <div className="basis-1/4">
          <Card />
        </div>
        <div className="basis-1/4">
          <Card />
        </div>
        <div className="basis-1/4">
          <Card />
        </div>
        <div className="basis-1/4">
          <Card />
        </div>
        <div className="basis-1/4">
          <Card />
        </div>
      </div>
    </>
  );
};

export default Search;
