// pages/restricted.tsx
import { GetServerSidePropsContext } from "next"
import { getSession } from "next-auth/react"

export default function RestrictedPage() {
  return (
    <div className="pt-10 bg-custom1 min-h-screen">
      <div className="max-w-md w-full mx-auto rounded-none md:rounded-2xl p-4 md:p-8 shadow-input bg-custom2 dark:bg-black mt-10">
        <h2 className="font-bold text-2xl text-white dark:text-neutral-200 text-center mb-10">
          Restricted Content
        </h2>
        <p className="text-white dark:text-neutral-200 text-center">
          This content is only accessible by authenticated users.
        </p>
      </div>
    </div>
  )
}

export async function getServerSideProps(context: GetServerSidePropsContext) {
  const session = await getSession(context)
  if (!session) {
    return {
      redirect: {
        destination: "/login",
        permanent: false,
      },
    }
  }

  return {
    props: { session },
  }
}
