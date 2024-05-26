import { HoverBorderGradient } from "../ui/hover-border-gradient"
import { AnimatedTooltip } from "../ui/animated-tooltip"
const people = [
  {
    id: 1,
    name: "Rhythm Arora",
    image:
      "https://github-production-user-asset-6210df.s3.amazonaws.com/65298117/333845627-eaa47532-90eb-498b-bd00-bf80a0dd70ab.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240526%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240526T032605Z&X-Amz-Expires=300&X-Amz-Signature=5f2e7130872704cba73026265b8446be5f06f7213449f4414c0db9dcd55f0f49&X-Amz-SignedHeaders=host&actor_id=65298117&key_id=0&repo_id=799354253",
  },
  {
    id: 2,
    name: "Aryan Gupta",
    image:
      "https://github-production-user-asset-6210df.s3.amazonaws.com/65298117/333845762-20e95bbc-1c52-4023-a7e0-ff1a3f81e12d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240526%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240526T033141Z&X-Amz-Expires=300&X-Amz-Signature=ea3a37913f98c36c5891ec8aeb35e309e27b0c10db13536f8272f40234ee7537&X-Amz-SignedHeaders=host&actor_id=65298117&key_id=0&repo_id=799354253",
  },
  {
    id: 3,
    name: "Anshul Rana",
    image:
      "https://github-production-user-asset-6210df.s3.amazonaws.com/65298117/333845758-7ada4eb4-e2f9-4c40-aab8-cd0c82d34777.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240526%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240526T033341Z&X-Amz-Expires=300&X-Amz-Signature=f7c0b2cb76099e636c136de9c4612f30cf1d8180df494c92f9e92a59c048c6ed&X-Amz-SignedHeaders=host&actor_id=65298117&key_id=0&repo_id=799354253",
  },
  {
    id: 4,
    name: "Ayush Saini",
    image:
      "https://github-production-user-asset-6210df.s3.amazonaws.com/65298117/333845771-a6fafccb-7a86-4123-a9a7-cbae859886a9.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240526%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240526T033210Z&X-Amz-Expires=300&X-Amz-Signature=406f9361de352d47cb2a12e31b9574af295c4e89057d59d1e9f423e2d92093f5&X-Amz-SignedHeaders=host&actor_id=65298117&key_id=0&repo_id=799354253",
  },
]
const Hero = () => {
  return (
    <div className="h-[50rem] w-full dark:bg-custom1 bg-custom1 dark:bg-grid-white/[0.2] bg-grid-custom4/[0.2] relative flex flex-col items-center justify-center">
      <div className="absolute pointer-events-none inset-0 flex items-center justify-center dark:bg-custom1 bg-custom2 [mask-image:radial-gradient(ellipse_at_center,transparent_20%,white)]"></div>
      <p className="text-4xl sm:text-7xl font-bold relative z-20 bg-clip-text text-transparent bg-gradient-to-b from-custom4 to-custom5 py-8 mb-5 text-center">
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
