const TrustScoreCard = ({ trust }) => {

  const score = trust?.trust_score || 0;

  const level = trust?.trust_level || "Unknown";

  let color = "text-red-500";

  if (score >= 80) {
    color = "text-green-500";
  }

  else if (score >= 50) {
    color = "text-yellow-400";
  }

  return (

    <div
      className="
        bg-slate-900
        rounded-3xl
        p-8
        border
        border-slate-800
        shadow-xl
      "
    >

      <h2 className="text-2xl font-bold mb-6">
        Trust Score
      </h2>

      <div className="flex flex-col items-center">

        <div
          className={`
            text-7xl
            font-bold
            ${color}
          `}
        >
          {score}
        </div>

        <div className="text-xl mt-3 text-slate-300">
          {level}
        </div>

      </div>

    </div>
  );
};

export default TrustScoreCard;