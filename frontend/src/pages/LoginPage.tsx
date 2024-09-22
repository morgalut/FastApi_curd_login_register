import React, { useState } from 'react';
import { loginUser, LoginDTO } from '../api/authApi';
import { useNavigate } from 'react-router-dom';

const LoginPage: React.FC = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const [loading, setLoading] = useState(false); // Loading state
    const navigate = useNavigate(); // Initialize useNavigate

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const loginData: LoginDTO = { username, password };

        setLoading(true); // Set loading to true

        try {
            const response = await loginUser(loginData);
            const token = response?.token; // Extract the token from the response
            if (token) {
                localStorage.setItem('authToken', token); // Store token in localStorage
                setSuccess('Login successful!');
                setError('');
                // Navigate to the home page after a successful login
                navigate('/'); // Redirect to the home page
            }
        } catch (error) {
            setError('Login failed. Please check your credentials.');
            setSuccess('');
        } finally {
            setLoading(false); // Reset loading state
        }
    };

    return (
        <div>
            <h2>Login</h2>
            {loading && <div className="loading-spinner">Loading...</div>} {/* Loading spinner */}
            <form onSubmit={handleSubmit}>
                <input 
                    type="text" 
                    value={username} 
                    onChange={(e) => setUsername(e.target.value)} 
                    placeholder="Username" 
                    required
                />
                <input 
                    type="password" 
                    value={password} 
                    onChange={(e) => setPassword(e.target.value)} 
                    placeholder="Password" 
                    required
                />
                {error && <p className="error">{error}</p>}
                {success && <p className="success">{success}</p>}
                <button type="submit" disabled={loading}>Login</button> {/* Disable button while loading */}
            </form>
        </div>
    );
};

export default LoginPage;
