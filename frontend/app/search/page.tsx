  "use client"
  import React, { useState, useEffect } from "react"
  import SearchBar from "../components/SearchBar"
  import Filter from "../components/Filter"
  import Card from "../components/Card"
  import { useDebounce } from "../components/hooks/useDebounce"
  import axios from "../../utils/axios"
  import { TracingBeam } from "../ui/tracing-beam"


  type AdditionalData =
    | {
        distance: number
      }
    | {
        score: number
      }
      |
      {

      }

  type SearchResult = {
    _additional: AdditionalData | null
    category: string
    description: string
    raw_description: string
    title: string
    price: number
    primary_category: string
  }

  const Search = () => {
    const [inputValue, setInputValue] = useState<string>("")
    const [searchResults, setSearchResults] = useState<SearchResult[]>([])
    const searchQuery = useDebounce(inputValue, 1000)
    const [isImage,setIsImage]=useState(true)
    console.log(isImage)
    const handleImageCheck=()=>{
      if (isImage){
        setIsImage(false)
      }else{
        setIsImage(true)
      }   
    }

    useEffect(() => {
      const fetchData = async () => {
        let parsedData:SearchResult[]={} as SearchResult[]
        const token = localStorage.getItem("token")
        console.log("token---->",token)
        try {
            if (isImage){
              const headers={
                'Authorization':`Bearer ${token}`
              }  
              console.log(headers)
              const { data } = await axios.post("/search/search_query", 
                  {
                    query: searchQuery,  // This is the request body
                  },
                  {
                    headers: {
                      "Authorization": `Bearer ${token}`,
                      "Content-Type": "application/json",
                    },
                  })
              const parsedData = JSON.parse(data)
              console.log(data)
              console.log("parsed data",Array.isArray(parsedData))
              setSearchResults(parsedData)
        }else{
            
              const { data } = await axios.post("/search/search_query_image", 
                {
                    imageUrl: searchQuery,  // This is the request body
                  },
                  {
                    headers: {
                      "Authorization": `Bearer ${token}`,
                      "Content-Type": "application/json",
                    },
                  })
              const parsedData = JSON.parse(data)
              setSearchResults(parsedData)
            
        }
          console.log(Array.isArray(parsedData))
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
        <div className="ml-60 flex justify-center flex-row gap-2">
          <div>
            <SearchBar
              inputValue={inputValue}
              setInputValue={setInputValue}
            />
          </div>
          <div className="m-6">
            <Filter />
          </div>
          <label className="inline-flex items-center cursor-pointer">
            <input
              type="checkbox"
              value=""
              className="sr-only peer"
              checked={isImage}
              onChange={handleImageCheck}
            />
            <div className="relative w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-custom1 dark:peer-focus:ring-red-800 dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-custom5"></div>
            {/* <span className="ms-3 text-sm font-medium text-custom4 dark:text-gray-300">
              Image Search
            </span> */}
          </label>
        </div>
        <div className="bg-custom1 flex flex-row flex-wrap gap-4 gap-x-6 m-4 justify-center text-white">
          {searchResults?.length === 0 ? (
            <p>No results found</p>
          ) : (
            searchResults?.map((result) => (
              <div>
                <Card cardDetails={result} />
              </div>
            ))
          )}
        </div>
      </div>
    )
  }

  export default Search
