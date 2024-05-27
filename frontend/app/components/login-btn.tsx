import Link from "next/link"

export default function Component() {
  return (
    <>
      Not signed in <br />
      <button>
        <Link href="/login">login</Link>
      </button>
    </>
  )
}
