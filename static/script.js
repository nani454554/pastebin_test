function createSnippet() {
    let content = document.getElementById("snippet-content").value;
    fetch("/snippets/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: content, is_public: true })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerHTML = `Snippet Created! <a href="/snippets/${data.id}">View Snippet</a>`;
    })
    .catch(error => console.error("Error:", error));
}

function getSnippet() {
    let snippetId = document.getElementById("snippet-id").value;
    fetch(`/snippets/${snippetId}`)
    .then(response => response.json())
    .then(data => {
        if (data.detail) {
            document.getElementById("output").innerText = "Snippet not found!";
        } else {
            document.getElementById("output").innerText = "Snippet: " + data.content;
        }
    })
    .catch(error => console.error("Error:", error));
}
