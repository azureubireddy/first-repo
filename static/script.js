document.addEventListener('DOMContentLoaded', () => {
    const messageElement = document.getElementById('message');
    const refreshButton = document.getElementById('refreshButton');

    async function fetchData() {
        try {
            const response = await fetch('/api/data');
            const data = await response.json();
            messageElement.textContent = data.message;
        } catch (error) {
            messageElement.textContent = 'Failed to load message.';
        }
    }

    // Fetch data when the page loads
    fetchData();

    // Fetch data when the button is clicked
    refreshButton.addEventListener('click', fetchData);
});
