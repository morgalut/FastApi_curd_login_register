import axios from 'axios';

const API_URL = 'http://localhost:8000/auth';

// Configure axios to include the token in all requests
axios.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('authToken');
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`; // Attach token to Authorization header
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export interface User {
    id: number;
    username: string;
    email: string;
}

export interface LoginDTO {
    username: string;
    password: string;
}

export interface RegisterDTO {
    username: string;
    email: string;
    password: string;
}

export const registerUser = async (data: RegisterDTO) => {
    const response = await axios.post<User>(`${API_URL}/register`, data);
    return response.data;
};

export const loginUser = async (data: LoginDTO) => {
    const response = await axios.post(`${API_URL}/login`, data);
    return response.data;  // Assuming the response contains the token and user data
};
