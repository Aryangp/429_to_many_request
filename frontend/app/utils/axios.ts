import axios from 'axios';

const instance = axios.create({
  baseURL: 'process.env.BACKEND_APP_API_URL',
  timeout: 1000,
});