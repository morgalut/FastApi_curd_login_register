import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Navbar.css';

const Navbar: React.FC = () => {
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
    const navigate = useNavigate();

    useEffect(() => {
        const checkLoginStatus = () => {
            const token = localStorage.getItem('authToken');
            setIsLoggedIn(!!token); // Check if the user is logged in
        };

        // Initial check
        checkLoginStatus();

        // Listen for storage changes (to handle token updates)
        window.addEventListener('storage', checkLoginStatus);

        // Cleanup listener on unmount
        return () => {
            window.removeEventListener('storage', checkLoginStatus);
        };
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('authToken'); // Clear the token
        setIsLoggedIn(false); // Update login state
        navigate('/login'); // Redirect to login
    };

    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <Link to="/">Task Manager</Link>
            </div>
            <ul className="navbar-links">
                <li><Link to="/">Home</Link></li>
                {isLoggedIn ? (
                    <>
                        <li><Link to="/tasks">Tasks</Link></li>
                        <li><button onClick={handleLogout} className="logout-button">Logout</button></li>
                    </>
                ) : (
                    <>
                        <li><Link to="/login">Login</Link></li>
                        <li><Link to="/register">Register</Link></li>
                    </>
                )}
            </ul>
        </nav>
    );
};

export default Navbar;
