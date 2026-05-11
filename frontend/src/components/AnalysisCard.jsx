const AnalysisCard = ({ title, content }) => {

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

      <h3 className="text-xl font-semibold mb-4">
        {title}
      </h3>

      <p className="text-slate-300 leading-7">
        {content}
      </p>

    </div>
  );
};

export default AnalysisCard;