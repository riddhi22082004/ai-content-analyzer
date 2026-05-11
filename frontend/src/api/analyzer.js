import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const analyzeWebsite = async (url) => {

  const response = await API.post("/analyze", {
    url,
  });

  return response.data;
};