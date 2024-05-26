// pages/api/auth/[...nextauth].ts
import axios from "@/utils/axios"
import { log } from "console"
import NextAuth, { AuthOptions } from "next-auth"
import CredentialsProvider from "next-auth/providers/credentials"
import qs from "qs"

interface Credentials {
  username: string
  password: string
}

export const authOptions: AuthOptions = {
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: {
        username: {
          label: "Username",
          type: "text",
          placeholder: "yourusername",
        },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        if (!credentials) return null

        const data = qs.stringify({
          username: credentials.username,
          password: credentials.password,
        })

        try {
          const res = await axios.post("/auth/token", data, {
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
          })

          const user = res.data

          if (user) {
            return user
          } else {
            return null
          }
        } catch (error) {
          console.error("Error during authorization:", error)
          return null
        }
      },
    }),
  ],
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.user = user
      }
      return token
    },
    async session({ session, token }) {
      session.user = token.user
      return session
    },
  },
  pages: {
    signIn: "/login",
  },
}

export default NextAuth(authOptions)
