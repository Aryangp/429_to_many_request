import axios from 'axios';

const instance = axios.create({
  // baseURL: "http://34.172.228.104:8000",
  baseURL: "http://34.136.190.153:8000",
  timeout: 90000,
})

export default instance;