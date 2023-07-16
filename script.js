const form = document.getElementById('url-form');
const urlInput = document.getElementById('url');
const graphContainer = document.getElementById('graphTable');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const url = urlInput.value;

    // Make an API request or perform necessary operations with the URL
    // to generate or retrieve the knowledge graph data

    // Example: Display the URL as plain text in the graph container
    graphContainer.innerHTML = `<tr><td>${url}</td></tr>`;
});
