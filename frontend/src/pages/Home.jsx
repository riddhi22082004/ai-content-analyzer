import { useState } from "react";

import SearchBar from "../components/SearchBar";
import LoadingScreen from "../components/LoadingScreen";
import ErrorMessage from "../components/ErrorMessage";

import MetadataCard from "../components/MetadataCard";
import AnalysisCard from "../components/AnalysisCard";
import TrustScoreCard from "../components/TrustScoreCard";
import FeaturesCard from "../components/FeaturesCard";
import InsightListCard from "../components/InsightListCard";
import RiskFlagsCard from "../components/RiskFlagsCard";
import PagesCard from "../components/PagesCard";

import { analyzeWebsite } from "../api/analyzer";

const Home = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [data, setData] = useState(null);

  const handleAnalyze = async (url) => {
    try {
      setLoading(true);
      setError("");
      setData(null);

      const result = await analyzeWebsite(url);
      setData(result);
    } catch (err) {
      setError(err?.response?.data?.error || "Failed to analyze website.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-950 text-white px-4 py-10">
      <div className="max-w-6xl mx-auto">

        <div className="text-center mb-10">
          <h1 className="text-5xl font-bold mb-4 text-cyan-400">
            AI Website Analyzer
          </h1>
        </div>

        <SearchBar onAnalyze={handleAnalyze} />

        {loading && <LoadingScreen />}
        {error && <ErrorMessage message={error} />}

        {data && (
          <div className="space-y-6 mt-8">

            <MetadataCard
              metadata={data.metadata}
              url={data.url}
            />

            <TrustScoreCard
              trust={data.trust_analysis}
            />

            <AnalysisCard
              analysis={data.analysis}
            />

            <InsightListCard
              title="Overview"
              items={data.analysis?.overview ? [data.analysis.overview] : []}
            />

            <InsightListCard
              title="Purpose"
              items={data.analysis?.purpose ? [data.analysis.purpose] : []}
            />

            <InsightListCard
              title="History"
              items={data.analysis?.history ? [data.analysis.history] : []}
            />

            {/* ONLY ONE TIME */}
            <FeaturesCard
              features={data.analysis?.key_features || []}
            />

            <InsightListCard
              title="Ratings & Reputation"
              items={data.analysis?.ratings_reputation ? [data.analysis.ratings_reputation] : []}
            />

            <InsightListCard
              title="Reviews Summary"
              items={data.analysis?.reviews_summary ? [data.analysis.reviews_summary] : []}
            />

            <InsightListCard
              title="Trust & Safety"
              items={data.analysis?.trust_safety ? [data.analysis.trust_safety] : []}
            />

            <InsightListCard
              title="Final Verdict"
              items={data.analysis?.final_verdict ? [data.analysis.final_verdict] : []}
            />

            <RiskFlagsCard
              risks={data.trust_analysis?.risk_flags || []}
            />

            <PagesCard 
              pages={data.pages_crawled || []} 
            />
          </div>
        )}
      </div>
    </div>
  );
};

export default Home;