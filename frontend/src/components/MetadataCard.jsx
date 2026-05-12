const MetadataCard = ({ metadata, url }) => {

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
        Website Metadata
      </h2>

      <div className="space-y-4">

        <div>

          <p className="text-slate-400 mb-1">
            URL
          </p>

          <p className="text-cyan-400 break-all">
            {url}
          </p>

        </div>

        <div>

          <p className="text-slate-400 mb-1">
            Title
          </p>

          <p className="text-white">
            {metadata?.title || "Unavailable"}
          </p>

        </div>

        <div>

          <p className="text-slate-400 mb-1">
            Description
          </p>

          <p className="text-slate-300">
            {metadata?.description || "Unavailable"}
          </p>

        </div>

      </div>

    </div>
  );
};

export default MetadataCard;