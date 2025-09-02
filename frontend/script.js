const API_BASE_URL = 'https://nombre-de-tu-api-en-render.onrender.com'; // URL de tu API local

// Función para obtener el mensaje del endpoint raíz
document.getElementById('getMessageBtn').addEventListener('click', async () => {
    const response = await fetch(`${API_BASE_URL}/`);
    const data = await response.json();
    document.getElementById('rootMessage').textContent = `La API responde: ${data.message}`;
});

// Función para saludar a una persona
document.getElementById('greetNameBtn').addEventListener('click', async () => {
    const name = document.getElementById('nameInput').value;
    const response = await fetch(`${API_BASE_URL}/saludo/${name}`);
    const data = await response.json();
    document.getElementById('greetingMessage').textContent = `La API responde: ${data.message}`;
});