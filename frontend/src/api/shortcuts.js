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
    return httpClient.post('/api/v1/auth/users/', { username, email, password, first_name: firstName, last_name: lastName })
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

const sendVerificationEmail = (email, verification_code) => {
    return httpClient.post('/api/v1/auth/send-mail/', { 'email': email, "link": 'http://localhost:8080/verify-email/' + verification_code })
}

const verifyEmailCode = (uuid) => {
    return httpClient.get('/api/v1/auth/verify-email-code/' + uuid + '/')
}

export { obtainToken, verifyToken, loadProductsResults, sendOrder, getUsersOrders, getProductBySlug, getCategoriesList, registerUser, sendVerificationEmail, verifyEmailCode }