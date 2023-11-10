import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        const socket = new WebSocket('ws://localhost:8000/ws/dashboard/');

        socket.onopen = () => {
            console.log('WebSocket Connected');
        };

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setMessage(data.message);
        };

        socket.onclose = () => {
            console.log('WebSocket Closed');
        };

        return () => {
            socket.close();
        };
    }, []);

    return (
        <div>
            <h1>Social Media Dashboard</h1>
            <p>{message}</p>
        </div>
    );
}

export default App;
