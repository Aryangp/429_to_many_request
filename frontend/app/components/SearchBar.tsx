// Code: SearchBar Component
import React, { useEffect, useState } from "react"
import { AnimatePresence, motion } from "framer-motion"

type SearchBarProps = {
    inputValue: string;
    setInputValue: (value: string) => void;
    };

function SearchBar({ inputValue, setInputValue }: SearchBarProps) {
  const [currentPlaceholder, setCurrentPlaceholder] = useState(0)
  const placeholders = [
    "Search...",
    "Find your favorite topics...",
    "Explore...",
  ]
  useEffect(() => {
    let interval: NodeJS.Timeout
    const startAnimation = () => {
      interval = setInterval(() => {
        setCurrentPlaceholder((prev) => (prev + 1) % placeholders.length)
      }, 1500)
    }
    startAnimation()
    return () => clearInterval(interval)
  }, [placeholders.length])
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value)
    console.log("Button clicked: ", inputValue)
  }
  return (
    <>
      <div className="m-6 flex md:order-2">
        <button
          type="button"
          data-collapse-toggle="navbar-search"
          aria-controls="navbar-search"
          aria-expanded="true"
          className="md:hidden text-custom4 dark:text-gray-400 hover:bg-custom4 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-custom4 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5 me-1"
        >
          <svg
            className="w-5 h-5"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 20 20"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
            />
          </svg>
          <span className="sr-only">Search</span>
        </button>
        <div className="relative hidden md:block w-[46vw]">
          <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
            <svg
              className="w-4 h-4 text-custom4 dark:text-gray-400 ml-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 20"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
              />
            </svg>
            <span className="sr-only">Search icon</span>
          </div>
          <input
            type="text"
            id="search-navbar"
            className="block w-full p-2 ps-10 text-base text-custom4 border-1 border-custom4 rounded-full bg-custom2 focus:ring-custom4 focus:border-custom4 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 "
            placeholder={placeholders[currentPlaceholder]}
            value={inputValue}
            onChange= {handleInputChange}
          ></input>
        </div>
        {/* <button
          data-collapse-toggle="navbar-search"
          type="button"
          className="inline-flex items-center p-2 w-10 h-10 justify-center text-base text-custom4 rounded-full md:hidden hover:bg-custom4 focus:outline-none focus:ring-2 focus:ring-custom4 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
          aria-controls="navbar-search"
          aria-expanded="true"
        >
          <span className="sr-only">Open main menu</span>
          <svg
            className="w-5 h-5"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 17 14"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M1 1h15M1 7h15M1 13h15"
            />
          </svg>
        </button> */}
      </div>
    </>
  )
}

export default SearchBar;
