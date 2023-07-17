const form = document.getElementById('url-form');
const urlInput = document.getElementById('url');
const graphContainer = document.getElementById('graphTable');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const url = urlInput.value;

    graphContainer.innerHTML = `<tr><td>${url}</td></tr>`;
});
