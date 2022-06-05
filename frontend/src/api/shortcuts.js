import axios from 'axios'

// const ENDPOINT = "api/auth/";
const httpClient = axios.create({
    baseURL: "http://localhost:8000/",
    headers: {
        "Content-Type": "application/json",
    },
});

const obtainToken = (username, password) => {
    console.log(username, password)
    return httpClient.post("api/token/", {
        username: username,
        password,
    });
}

const verifyToken = (token) => {
    return httpClient.post('api/token/verify/', { token })
}

const registerUser = (username, email, password, firstName, lastName) => {
    return httpClient.post('/api/v1/auth/', { username, email, password, first_name: firstName, last_name: lastName })
}

const loadProductsResults = () => {
    return httpClient.get('/api/v1/shop/products/')
}

const sendOrder = (order) => {
    return httpClient.post('/api/v1/shop/orders/', order)
}

const getUsersOrders = (userId) => {
    return httpClient.get('/api/v1/shop/orders/user/' + userId + "/")
}

const getProductBySlug = (slug) => {
    return httpClient.get('/api/v1/shop/product/' + slug + "/")
}

const getCategoriesList = () => {
    return httpClient.get('/api/v1/shop/categories/')
}

export { obtainToken, verifyToken, loadProductsResults, sendOrder, getUsersOrders, getProductBySlug, getCategoriesList, registerUser }