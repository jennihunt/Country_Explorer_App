function reloadData() {
    fetch("{% url 'reload_countries' %}")
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.status === "success") {
            location.reload();  // Refresh page on success
        }
    })
    .catch(error => console.error("Error:", error));
}