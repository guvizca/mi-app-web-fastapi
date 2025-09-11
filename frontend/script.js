const API_BASE_URL = 'https://mi-app-web-fastapi.onrender.com';

// El resto de tu código para las llamadas a la API
document.getElementById('getMessageBtn').addEventListener('click', async () => {
    const response = await fetch(`${API_BASE_URL}/`);
    const data = await response.json();
    document.getElementById('rootMessage').textContent = `La API responde: ${data.message}`;
});

document.getElementById('greetNameBtn').addEventListener('click', async () => {
    const name = document.getElementById('nameInput').value;
    const response = await fetch(`${API_BASE_URL}/saludo/${name}`);
    const data = await response.json();
    document.getElementById('greetingMessage').textContent = `La API responde: ${data.message}`;
});
