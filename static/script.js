function createSnippet() {
    let content = document.getElementById("snippet-content").value;
    let isPublic = document.getElementById("snippet-public").checked;

    fetch("/snippets/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: content, is_public: isPublic })
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

function updateSnippet() {
    let snippetId = document.getElementById("edit-snippet-id").value;
    let newContent = document.getElementById("edit-snippet-content").value;

    fetch(`/snippets/${snippetId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: newContent, is_public: true }) 
    })
    .then(response => response.json())
    .then(data => {
        if (data.detail) {
            document.getElementById("output").innerText = "Failed to update snippet!";
        } else {
            document.getElementById("output").innerText = "Snippet updated successfully!";
        }
    })
    .catch(error => console.error("Error:", error));
}
