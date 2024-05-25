import { HoverBorderGradient } from "../ui/hover-border-gradient"
import { AnimatedTooltip } from "../ui/animated-tooltip"
const people = [
  {
    id: 1,
    name: "Rhythm Arora",
    image:
      "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YXZhdGFyfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60",
  },
  {
    id: 2,
    name: "Aryan Gupta",
    image:
      "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YXZhdGFyfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60",
  },
  {
    id: 3,
    name: "Anshul Rana",
    image:
      "https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8YXZhdGFyfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60",
  },
  {
    id: 4,
    name: "Ayush Saini",
    image:
      "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGF2YXRhcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60",
  },
]
const Hero = () => {
  return (
    <div className="h-[50rem] w-full dark:bg-custom1 bg-custom1 dark:bg-grid-white/[0.2] bg-grid-custom4/[0.2] relative flex flex-col items-center justify-center">
      <div className="absolute pointer-events-none inset-0 flex items-center justify-center dark:bg-custom1 bg-custom2 [mask-image:radial-gradient(ellipse_at_center,transparent_20%,white)]"></div>
      <p className="text-4xl sm:text-7xl font-bold relative z-20 bg-clip-text text-transparent bg-gradient-to-b from-custom4 to-custom5 py-8 mb-5">
        The unique searching experience
      </p>
      <div className="m-20 flex justify-center text-center">
        <HoverBorderGradient
          containerClassName="rounded-full"
          as="button"
          className="dark:bg-black bg-custom2 text-white dark:text-white flex items-center space-x-2 p-2 px-14 text-xl"
        >
          <a href="/signup">Demo</a>
        </HoverBorderGradient>
      </div>
        <div className="flex flex-row fixed bottom-12 right-20 ">
          <AnimatedTooltip items={people} />
        </div>
    </div>
  )
}
export default Hero
