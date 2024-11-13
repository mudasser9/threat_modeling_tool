document.addEventListener("DOMContentLoaded", () => {
    showSection('home');  // Default section to show
    
    const draw = document.getElementById('drawioIframe');  // Ensure ID matches the iframe in HTML

    // Function to request an export from draw.io
    function exportDiagram() {
        draw.contentWindow.postMessage(
            JSON.stringify({ action: "export", format: "xmlsvg" }), "*"
        );
    }

    // Attach export button event listener
    document.querySelector("button[onclick='exportDiagram()']").onclick = exportDiagram;

    // Listen for messages from draw.io
    window.addEventListener("message", (event) => {
        if (event.data) {
            const data = JSON.parse(event.data);
            if (data.action === "export") {
                const diagramXml = data.xml;
                console.log("Diagram exported:", diagramXml);

                // Send the exported XML data to your server
                fetch('/api/export', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ diagramXml })
                })
                .then(response => response.json())
                .then(data => {
                    console.log("Diagram saved:", data);
                })
                .catch(error => console.error('Error exporting diagram:', error));
            }
        }
    });
});

// Load diagram from API
function loadDiagram() {
    fetch('/api/load')
        .then(response => response.json())
        .then(data => {
            if (data.diagramXml) {
                // Send the XML to draw.io iframe to load it
                draw.contentWindow.postMessage(
                    JSON.stringify({ action: "load", xml: data.diagramXml }), "*"
                );
            }
        })
        .catch(error => console.error('Error loading diagram:', error));
}

// Show specific section
function showSection(sectionId) {
    const sections = document.querySelectorAll("section");
    sections.forEach(section => {
        section.classList.remove("active");
        if (section.id === sectionId) {
            section.classList.add("active");
        }
    });
}
