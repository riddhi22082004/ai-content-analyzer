export default function AnalysisCard({ data }) {

  if (!data) return null

  return (
    <div className='bg-slate-800 p-6 rounded-xl'>

      <h2 className='text-2xl font-bold mb-4'>
        AI Analysis
      </h2>

      <div className='space-y-4'>

        <p>
          <strong>Overview:</strong>
          {' '}
          {data.overview}
        </p>

        <p>
          <strong>Purpose:</strong>
          {' '}
          {data.purpose}
        </p>

        <p>
          <strong>Final Verdict:</strong>
          {' '}
          {data.final_verdict}
        </p>
      </div>
    </div>
  )
}