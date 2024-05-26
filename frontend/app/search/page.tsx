"use client"
import React, { useState, useEffect } from "react"
import SearchBar from "../components/SearchBar"
import Filter from "../components/Filter"
import Card from "../components/Card"
import { useDebounce } from "../components/hooks/useDebounce"
import axios from "../../utils/axios"

type AdditionalData =
  | {
      distance: number
    }
  | {
      score: number
    }

type SearchResult = {
  additional: AdditionalData
  brand: string
  category: string
  market_price: number
  product_desc: string
  product_name: string
  rating: number
  sale_price: number
  sub_category: string
  unique_id: string
}

const Search = () => {
  const [inputValue, setInputValue] = useState<string>("")
  const [searchResults, setSearchResults] = useState<SearchResult[]>([])
  const searchQuery = useDebounce(inputValue, 1000)

  useEffect(() => {
    const fetchData = async () => {
      try {
        // const { data } = await axios.post("/search", {
        //   query: searchQuery,
        //   className: "CatalogSearchWithDescription",
        // })
        // const parsedData = JSON.parse(data)
        //  console.log("working")
        const dummyData = [
          {
            additional: {
              distance: 10,
            },
            brand: "Brand 1",
            category: "Category 1",
            market_price: 100,
            product_desc: "Product 1 description",
            product_name: "Product 1",
            rating: 4.5,
            sale_price: 90,
            sub_category: "Sub Category 1",
            unique_id: "1",
          },
          {
            additional: {
              score: 95,
            },
            brand: "Brand 2",
            category: "Category 2",
            market_price: 200,
            product_desc: "Product 2 description",
            product_name: "Product 2",
            rating: 4.0,
            sale_price: 180,
            sub_category: "Sub Category 2",
            unique_id: "2",
          },
          // Add more dummy data as needed
        ]

        setSearchResults(dummyData)
      } catch (error) {
        console.error("Error fetching search results:", error)
        // Handle error gracefully (e.g., show an error message)
      }
    }

    if (searchQuery) {
      fetchData()
    } else {
      // Clear search results if search query is empty
      setSearchResults([])
    }
  }, [searchQuery])

  console.log("data in the searchResult", searchResults)
  // type AdditionaData = {
  //   distance: number
  // }

  // type SearchResult = {
  //   additional: AdditionaData
  //   brand: string
  //   category: string
  //   market_price: number
  //   product_desc: string
  //   product_name: string
  //   rating: number
  //   sale_price: number
  //   sub_category: string
  //   unique_id: string
  // }

  // const Search = () => {
  //   const [inputValue, setInputValue] = useState<string>("")
  //   const [searchResults, setSearchResults] = useState<SearchResult[]>([])
  //   const searchQuery = useDebounce(inputValue, 1000)

  //   useEffect(() => {
  //     const fetchData = async () => {
  //       try {
  //         const { data } = await axios.post("/search", {
  //           query: searchQuery,
  //           className: "CatalogSearchWithDescription",
  //         })
  //         const parsedData = JSON.parse(data)
  //         setSearchResults(parsedData)
  //       } catch (error) {
  //         console.error("Error fetching search results:", error)
  //         // Handle error gracefully (e.g., show an error message)
  //       }
  //     }

  //     if (searchQuery) {
  //       fetchData()
  //     } else {
  //       // Clear search results if search query is empty
  //       setSearchResults([])
  //     }
  //   }, [searchQuery])

  //   console.log("data in the searchResult", searchResults)

  return (
    <div className="bg-custom1 h-[100vh] pt-10">
      <div className="ml-3 flex justify-center flex-row gap-2">
        <div>
          <SearchBar
            inputValue={inputValue}
            setInputValue={setInputValue}
          />
        </div>
        <div className="m-6">
          <Filter />
        </div>
      </div>

      <div className="flex flex-row flex-wrap gap-4 gap-x-6 m-4 justify-center text-white">
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
    </div>
  )
}

export default Search
