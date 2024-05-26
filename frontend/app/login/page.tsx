"use client"
import React, { useState } from "react"
import { Label } from "../ui/label"
import { Input } from "../ui/input"
import { cn } from "@/utils/cn"
import { IconBrandGithub, IconBrandGoogle } from "@tabler/icons-react"
import { signIn } from "next-auth/react"
import { useRouter } from "next/navigation" // Make sure to use next/navigation

export default function LogIn() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")
  const router = useRouter()

  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const result = await signIn("credentials", {
      redirect: false,
      username,
      password,
    })

    if (result?.error) {
      setError("Invalid username or password") // Set error message
      console.error("Login failed:", result.error)
    } else {
      router.push("/search")
    }
  }

  return (
    <section className="pt-10 bg-custom1 min-h-screen">
      <div className="max-w-md w-full mx-auto rounded-none md:rounded-2xl p-4 md:p-8 shadow-input bg-custom2 dark:bg-black mt-10">
        <h2 className="font-bold text-2xl text-white dark:text-neutral-200 text-center mb-9 mt-3">
          Welcome Back!
        </h2>
        <form
          className="my-8"
          onSubmit={handleLogin}
        >
          <LabelInputContainer className="mt-6 mb-6">
            <Label
              htmlFor="username"
              className="text-white "
            >
              Username
            </Label>
            <Input
              id="username"
              placeholder="Your Username"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </LabelInputContainer>
          <LabelInputContainer className="mt-6 mb-6">
            <Label
              htmlFor="password"
              className="text-white"
            >
              Password
            </Label>
            <Input
              id="password"
              placeholder="••••••••"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </LabelInputContainer>
          {error && ( // Display error message if error state is not empty
            <div className="text-red-500 text-sm mb-4">
              {error}
            </div>
          )}
          <button
            className="bg-custom2 dark:from-zinc-900 dark:to-zinc-900 to-neutral-600 block dark:bg-zinc-800 w-full text-custom4 rounded-md h-10 font-medium border-2 border-custom5 hover:border-custom4 transition-all ease-linear duration-200 mt-10"
            type="submit"
          >
            Log in &rarr;
            <BottomGradient />
          </button>

          {/* <div className="bg-gradient-to-r from-custom5 via-custom4 dark:via-neutral-700 to-transparent my-8 h-[1px] w-full" /> */}

          {/* <div className="flex flex-col space-y-4">
            <button
              type="button"
              onClick={() => signIn("github")}
              className="relative flex space-x-2 items-center justify-start px-4 w-full text-black rounded-md h-10 font-medium shadow-input bg-custom2 transition-all dark:bg-zinc-900 dark:shadow-[0px_0px_1px_1px_var(--neutral-800)] border-2 border-custom5 hover:border-custom4 transition-all ease-linear duration-200 group"
            >
              <IconBrandGithub className="h-4 w-4 text-custom5 dark:text-neutral-300 group-hover:text-custom4 transition-all ease-linear duration-200" />
              <span className="text-custom5 dark:text-neutral-300 text-sm group-hover:text-custom4 transition-all ease-linear duration-200">
                GitHub
              </span>
              <BottomGradient />
            </button>
            <button
              type="button"
              onClick={() => signIn("google")}
              className="relative flex space-x-2 items-center justify-start px-4 w-full text-black rounded-md h-10 font-medium shadow-input bg-custom2 transition-all dark:bg-zinc-900 dark:shadow-[0px_0px_1px_1px_var(--neutral-800)] border-2 border-custom5 hover:border-custom4 transition-all ease-linear duration-200 group"
            >
              <IconBrandGoogle className="h-4 w-4 text-custom5 dark:text-neutral-300 group-hover:text-custom4 transition-all ease-linear duration-200" />
              <span className="text-custom5 dark:text-neutral-300 text-sm group-hover:text-custom4 transition-all ease-linear duration-200">
                Google
              </span>
              <BottomGradient />
            </button>
          </div> */}
        </form>
      </div>
    </section>
  )
}

const BottomGradient = () => (
  <>
    <span className="group-hover/btn:opacity-100 block transition duration-500 opacity-0 absolute h-px w-full -bottom-px inset-x-0 bg-gradient-to-r from-transparent via-cyan-500 to-transparent" />
    <span className="group-hover/btn:opacity-100 blur-sm block transition duration-500 opacity-0 absolute h-px w-1/2 mx-auto -bottom-px inset-x-10 bg-gradient-to-r from-transparent via-indigo-500 to-transparent" />
  </>
)

const LabelInputContainer = ({
  children,
  className,
}: {
  children: React.ReactNode
  className?: string
}) => {
  return (
    <div className={cn("flex flex-col space-y-2 w-full", className)}>
      {children}
    </div>
  )
}
