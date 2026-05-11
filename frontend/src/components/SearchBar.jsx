import { useState } from "react";
import { FaSearch } from "react-icons/fa";

const SearchBar = ({ onAnalyze, loading }) => {

  const [url, setUrl] = useState("");

  const handleSubmit = (e) => {

    e.preventDefault();

    if (!url.trim()) return;

    onAnalyze(url);
  };

  return (

    <form
      onSubmit={handleSubmit}
      className="w-full max-w-3xl flex gap-3"
    >

      <input
        type="text"
        placeholder="Enter website URL..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="
          flex-1
          px-5
          py-4
          rounded-2xl
          bg-slate-900
          border
          border-slate-700
          text-white
          outline-none
          focus:border-blue-500
        "
      />

      <button
        type="submit"
        disabled={loading}
        className="
          px-6
          py-4
          rounded-2xl
          bg-blue-600
          hover:bg-blue-700
          transition
          flex
          items-center
          gap-2
          disabled:opacity-50
        "
      >

        <FaSearch />

        {loading ? "Analyzing..." : "Analyze"}

      </button>

    </form>
  );
};

export default SearchBar;