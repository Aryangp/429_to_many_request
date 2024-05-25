import { HoverBorderGradient } from "../ui/hover-border-gradient"

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
    </div>
  )
}
export default Hero
