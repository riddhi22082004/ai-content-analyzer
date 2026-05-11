const RiskFlagsCard = ({ risks }) => {

  return (

    <div
      className="
        bg-slate-900
        border
        border-slate-800
        rounded-3xl
        p-6
      "
    >

      <h2 className="text-2xl font-bold mb-6">
        Risk Flags
      </h2>

      <div className="space-y-3">

        {risks?.length > 0 ? (

          risks.map((risk, index) => (

            <div
              key={index}
              className="
                p-4
                rounded-2xl
                bg-red-500/10
                border
                border-red-500/20
                text-red-300
              "
            >
              ⚠ {risk}
            </div>
          ))

        ) : (

          <div className="text-slate-400">
            No major risk flags detected.
          </div>
        )}

      </div>

    </div>
  );
};

export default RiskFlagsCard;