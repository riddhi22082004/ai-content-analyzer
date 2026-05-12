export default function PagesCard({ pages }) {

  return (
    <div className='bg-slate-800 p-6 rounded-xl'>

      <h2 className='text-2xl font-bold mb-4'>
        Pages Crawled
      </h2>

      <ul className='list-disc pl-6'>

        {pages.map((page, index) => (
          <li key={index}>{page}</li>
        ))}
      </ul>
    </div>
  )
}