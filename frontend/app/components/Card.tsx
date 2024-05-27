import React, { useState } from "react"
import { AnimatePresence, motion } from "framer-motion"
import { cn } from "@/utils/cn"
import parse from "html-react-parser"
import { htmlToText } from "html-to-text" // Import the utility

type AdditionalData =
  | {
      distance: number
    }
  | {
      score: number
    }
  | {}

type SearchData = {
  _additional: AdditionalData | null
  category: string
  description: string
  raw_description: string
  title: string
  price: number
  primary_category: string
}

type CardProps = {
  cardDetails: SearchData
  className?: string
}

const Card = ({ cardDetails, className }: CardProps) => {
  const [hovered, setHovered] = useState<boolean>(false)

  // Function to limit the description to 20 words
  const getLimitedDescription = (
    htmlDescription: string,
    wordLimit: number
  ) => {
    const text = htmlToText(htmlDescription, {
      wordwrap: false,
      preserveNewlines: false,
      singleNewlineParagraphs: true,
    })

    const words = text.split(" ").slice(0, wordLimit).join(" ") + "..."
    return parse(words)
  }

  return (
    <div
      className={cn(
        "relative group block p-2 h-full w-full max-w-sm mx-auto",
        className
      )}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
    >
      <AnimatePresence>
        {hovered && (
          <motion.span
            className="absolute inset-0 h-full w-full bg-custom4 dark:bg-slate-800/[0.8] block rounded-3xl"
            layoutId="hoverBackground"
            initial={{ opacity: 0 }}
            animate={{
              opacity: 1,
              transition: { duration: 0.15 },
            }}
            exit={{
              opacity: 0,
              transition: { duration: 0.1, delay: 0.1 },
            }}
          />
        )}
      </AnimatePresence>
      <div
        className={cn(
          "rounded-2xl h-full w-full p-4 overflow-hidden bg-custom2 border border-transparent dark:border-white/[0.2] group-hover:border-slate-700 relative z-20"
        )}
      >
        <div className="relative z-50 p-4">
          <h4 className="text-zinc-100 font-bold tracking-wide mt-4">
            {cardDetails.title}
          </h4>
          <p className="mt-8 text-zinc-400 tracking-wide leading-relaxed text-sm">
            {getLimitedDescription(cardDetails.description, 20)}
          </p>
          <span className="text-xl text-custom4 dark:text-white">
            ${cardDetails.price}
          </span>
        </div>
      </div>
    </div>
  )
}

export default Card
