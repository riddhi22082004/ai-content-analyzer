import { useState } from "react";

import SearchBar from "../components/SearchBar";
import TrustScoreCard from "../components/TrustScoreCard";
import AnalysisCard from "../components/AnalysisCard";

import FeaturesCard from "../components/FeaturesCard";
import RiskFlagsCard from "../components/RiskFlagsCard";
import InsightListCard from "../components/InsightListCard";

import { analyzeWebsite } from "../api/analyzer";


const Home = () => {

  const [loading, setLoading] = useState(false);

  const [data, setData] = useState(null);

  const [error, setError] = useState("");


  const handleAnalyze = async (url) => {

    try {

      setLoading(true);

      setError("");

      const result = await analyzeWebsite(url);

      console.log("API RESULT:", result);

      setData(result);

    }

    catch (err) {

      console.error(err);

      setError(
        "Failed to analyze website."
      );
    }

    finally {

      setLoading(false);
    }
  };


  return (

    <div className="min-h-screen bg-slate-950 text-white">

      <div className="max-w-7xl mx-auto px-6 py-16">


        {/* HERO */}

        <div className="text-center mb-16">

          <h1 className="text-6xl font-bold mb-6">

            AI Website Intelligence

          </h1>

          <p className="text-slate-400 text-lg mb-10">

            Analyze trust, structure,
            reputation, business intelligence,
            and security signals using AI.

          </p>

          <div className="flex justify-center">

            <SearchBar
              onAnalyze={handleAnalyze}
              loading={loading}
            />

          </div>

        </div>


        {/* ERROR */}

        {error && (

          <div
            className="
              bg-red-500/10
              border
              border-red-500/20
              text-red-300
              rounded-2xl
              p-4
              mb-8
            "
          >

            {error}

          </div>
        )}


        {/* RESULTS */}

        {data && (

          <div className="space-y-8">


            {/* TOP SECTION */}

            <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">


              {/* TRUST SCORE */}

              <TrustScoreCard
                trust={data?.trust_analysis}
              />


              {/* METADATA */}

              <div
                className="
                  xl:col-span-2
                  bg-slate-900
                  border
                  border-slate-800
                  rounded-3xl
                  p-8
                "
              >

                <h2 className="text-2xl font-bold mb-6">

                  Website Metadata

                </h2>

                <div className="space-y-6">


                  {/* URL */}

                  <div>

                    <div className="text-slate-400 mb-2">

                      URL

                    </div>

                    <div className="text-blue-400 break-all">

                      {data?.url ||
                        "No URL"}

                    </div>

                  </div>


                  {/* TITLE */}

                  <div>

                    <div className="text-slate-400 mb-2">

                      Title

                    </div>

                    <div className="text-xl">

                      {
                        data?.metadata?.title
                        || "No title detected"
                      }

                    </div>

                  </div>


                  {/* DESCRIPTION */}

                  <div>

                    <div className="text-slate-400 mb-2">

                      Description

                    </div>

                    <div className="text-slate-300 leading-7">

                      {
                        data?.metadata?.description
                        || "No description detected"
                      }

                    </div>

                  </div>

                </div>

              </div>

            </div>


            {/* MAIN ANALYSIS */}

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">

              <AnalysisCard
                title="Overview"
                content={
                  data?.analysis?.overview
                }
              />

              <AnalysisCard
                title="Purpose"
                content={
                  data?.analysis?.purpose
                }
              />

              <AnalysisCard
                title="History"
                content={
                  data?.analysis?.history
                }
              />

              <AnalysisCard
                title="Final Verdict"
                content={
                  data?.analysis?.final_verdict
                }
              />

            </div>


            {/* FEATURES */}

            <FeaturesCard
              features={
                data?.analysis?.key_features || []
              }
            />


            {/* BUSINESS INFO */}

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">

              <AnalysisCard
                title="Target Audience"
                content={
                  data?.analysis?.target_audience
                }
              />

              <AnalysisCard
                title="Business Model"
                content={
                  data?.analysis?.business_model
                }
              />

            </div>


            {/* STRENGTHS + WEAKNESSES */}

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">

              <InsightListCard
                title="Strengths"
                items={
                  data?.analysis?.strengths || []
                }
                type="positive"
              />

              <InsightListCard
                title="Weaknesses"
                items={
                  data?.analysis?.weaknesses || []
                }
                type="negative"
              />

            </div>


            {/* REPUTATION */}

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">

              <AnalysisCard
                title="Ratings & Reputation"
                content={
                  data?.analysis?.ratings_reputation
                }
              />

              <AnalysisCard
                title="Reviews Summary"
                content={
                  data?.analysis?.reviews_summary
                }
              />

            </div>


            {/* TRUST & SAFETY */}

            <AnalysisCard
              title="Trust & Safety"
              content={
                data?.analysis?.trust_safety
              }
            />


            {/* RISK FLAGS */}

            <RiskFlagsCard
              risks={
                data?.trust_analysis?.risk_flags || []
              }
            />


            {/* POSITIVE SIGNALS */}

            <InsightListCard
              title="Positive Signals"
              items={
                data?.trust_analysis?.positive_signals || []
              }
              type="positive"
            />


            {/* PAGES ANALYZED */}

            <div
              className="
                bg-slate-900
                border
                border-slate-800
                rounded-3xl
                p-8
              "
            >

              <h2 className="text-2xl font-bold mb-6">

                Pages Analyzed

              </h2>

              <div className="space-y-4">

                {
                  data?.pages_crawled?.length > 0
                  ? (

                      data.pages_crawled.map(
                        (page, index) => (

                          <div
                            key={index}
                            className="
                              p-4
                              rounded-2xl
                              bg-slate-800
                              text-slate-300
                              break-all
                            "
                          >

                            {page}

                          </div>
                        )
                      )

                    )
                  : (

                      <div className="text-slate-400">

                        No pages analyzed

                      </div>
                    )
                }

              </div>

            </div>

          </div>
        )}

      </div>

    </div>
  );
};

export default Home;