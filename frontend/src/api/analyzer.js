import axios from "axios";

const API_URL =
  "http://127.0.0.1:8000/analyze";

export const analyzeWebsite = async (url) => {

  const response = await axios.post(
    API_URL,
    { url }
  );

  return response.data;
};