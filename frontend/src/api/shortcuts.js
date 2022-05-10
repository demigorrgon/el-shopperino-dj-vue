import axios from 'axios'

// const ENDPOINT = "api/auth/";
const httpClient = axios.create({
    baseURL: "http://localhost:8000/",
    headers: {
        "Content-Type": "application/json",
    },
});

const obtainToken = (username, password) => {
    return httpClient.post("api/token/", {
        username: username,
        password,
    });
}

const verifyToken = (token) => {
    return httpClient.post('api/token/verify/', { token })
}

const loadProductsResults = () => {
    return httpClient.get('/api/v1/shop/')
}

export { obtainToken, verifyToken, loadProductsResults }