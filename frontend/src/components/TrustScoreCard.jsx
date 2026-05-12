const TrustScoreCard = ({ trust }) => {

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
        Trust Analysis
      </h2>

      <div className="space-y-5">

        <div>

          <p className="text-slate-400">
            Trust Score
          </p>

          <h3 className="text-5xl font-bold text-cyan-400">
            {trust?.trust_score || 0}
          </h3>

        </div>

        <div>

          <p className="text-slate-400">
            Trust Level
          </p>

          <p className="text-xl font-semibold text-white">
            {trust?.trust_level || "Unknown"}
          </p>

        </div>

      </div>

    </div>
  );
};

export default TrustScoreCard;