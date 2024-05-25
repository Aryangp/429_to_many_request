// components/FilterComponent.js
"use client";
import { useState } from "react";

const Filter = () => {
  const [isFilterOpen, setIsFilterOpen] = useState(false);
  const [priceRange, setPriceRange] = useState([0, 1000]);
  const [minRating, setMinRating] = useState(0);

  const toggleFilter = () => {
    setIsFilterOpen(!isFilterOpen);
  };

  const applyFilters = () => {
    console.log("Price Range:", priceRange);
    console.log("Minimum Rating:", minRating);
    toggleFilter();
  };

  return (
    <div className="relative">
      {/* Filter button */}
      <button
        className="bg-custom1 text-custom4 px-4 py-2 focus:outline-none rounded-md h-11 font-medium border-2 border-custom5 hover:border-custom4 transition-all ease-linear duration-200"
        onClick={toggleFilter}
      >
        Filter
      </button>

      {/* Backdrop */}
      {isFilterOpen && (
        <div
          className="fixed top-0 left-0 w-full h-full bg-gray-800 opacity-50"
          onClick={toggleFilter}
        ></div>
      )}

      {/* Filter options */}
      {isFilterOpen && (
        <div className="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-custom2 p-6 rounded-lg flex flex-col items-center justify-center">
          <h2 className="text-xl text-center mb-4 text-custom4">
            Filter Options
          </h2>

          {/* Price Range */}
          <div className="mb-4">
            <label className="block text-lg font mb-2 text-custom4">
              Price Range
            </label>
            <div className="flex items-center space-x-2 text-custom4">
              <span>₹</span>
              <input
                type="range"
                min="0"
                max="100"
                value={priceRange[0]}
                onChange={(e) =>
                  setPriceRange([parseInt(e.target.value), priceRange[1]])
                }
                className="w-full"
              />
              <span>₹</span>
              <input
                type="range"
                min="0"
                max="100"
                value={priceRange[1]}
                onChange={(e) =>
                  setPriceRange([priceRange[0], parseInt(e.target.value)])
                }
                className="w-full"
              />
            </div>
            <div className="block text-custom4">
              Price Range: {priceRange[0]} - {priceRange[1]}
            </div>
          </div>

          {/* Minimum Rating */}
          <div className="mb-4 text-custom4">
            <label className="block text-lg mb-2 text-custom4 ">
              Minimum Rating
            </label>
            <input
              type="range"
              min="0"
              max="5"
              step="0.1"
              value={minRating}
              onChange={(e) => setMinRating(parseFloat(e.target.value))}
              className="w-full"
            />
            <span>Min Rating: {minRating}</span>
          </div>

          {/* Apply Filters button */}
          <button
            className="bg-custom2 border-2 border-custom5 text-custom4 px-4 py-2 rounded focus:outline-none hover:border-custom4 transition-all ease-linear duration-200"
            onClick={applyFilters}
          >
            Apply Filters
          </button>
        </div>
      )}
    </div>
  )
};

export default Filter;
