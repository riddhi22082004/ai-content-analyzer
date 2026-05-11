const FeaturesCard = ({ features }) => {

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
        Key Features
      </h2>

      <div className="flex flex-wrap gap-3">

        {features?.map((feature, index) => (

          <div
            key={index}
            className="
              px-4
              py-2
              rounded-xl
              bg-blue-500/20
              border
              border-blue-500/30
              text-blue-300
            "
          >
            {feature}
          </div>
        ))}

      </div>

    </div>
  );
};

export default FeaturesCard;