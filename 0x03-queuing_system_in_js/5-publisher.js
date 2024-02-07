import { createClient } from 'redis';

// Create a Redis client
const publisher = createClient();

// Connect to the Redis server
publisher.on('connect', () => {
    console.log('Redis client connected to the server');

    // Function to publish a message after a specified time
    function publishMessage(message, time) {
        setTimeout(() => {
            console.log(`About to send ${message}`);
            publisher.publish('holberton school channel', message);
        }, time);
    }

    // Call the publishMessage function with different messages and times
    publishMessage('Holberton Student #1 starts course', 100);
    publishMessage('Holberton Student #2 starts course', 200);
    publishMessage('KILL_SERVER', 300);
    publishMessage('Holberton Student #3 starts course', 400);

    // Close the Redis client after all messages are published
    setTimeout(() => {
        publisher.quit();
    }, 500);
});

// Handle connection errors
publisher.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

