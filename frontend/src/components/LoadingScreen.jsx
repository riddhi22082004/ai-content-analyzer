const LoadingScreen = () => {

  return (

    <div
      className="
        mt-6
        bg-slate-900
        border
        border-slate-800
        rounded-3xl
        p-8
        text-center
      "
    >

      <div
        className="
          w-12
          h-12
          border-4
          border-cyan-400
          border-t-transparent
          rounded-full
          animate-spin
          mx-auto
          mb-4
        "
      />

      <h2 className="text-2xl font-bold text-cyan-400">
        Analyzing Website...
      </h2>

      <p className="text-slate-400 mt-2">
        Fetching metadata, trust signals,
        and AI insights.
      </p>

    </div>
  );
};

export default LoadingScreen;