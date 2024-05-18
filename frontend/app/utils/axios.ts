import axios from 'axios';

const instance = axios.create({
  baseURL: "http://34.125.198.169:5000",
  timeout: 90000,
});

export default instance;