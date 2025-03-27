
const urlContainer = document.getElementById('url-container');
const fetchUrl = urlContainer.getAttribute('data-fetch-url');


        function reloadData() {
            console.log('hi')
            fetch(fetchUrl)
                .then(response => response.json())
                .then(data => {
                    alert(data.message);
                    if (data.status === "success") {
                        location.reload();  // Refresh page on success
                    }
                })
                .catch(error => console.error("Error:", error));
        }


        function liveSearch() {
            let query = document.getElementById('search-input').value;
            
            fetch(`/countries/?q=${query}`, { headers: { "X-Requested-With": "XMLHttpRequest" } })
            .then(response => response.json())
            .then(data => {
                let resultsContainer = document.getElementById('results');
                resultsContainer.innerHTML = '';  // Clear previous results

                if (data.countries.length === 0) {
                    resultsContainer.innerHTML = '<li>No countries found.</li>';
                } else {
                    data.countries.forEach(country => {
                        let li = document.createElement('li');
                        li.textContent = country.name;
                        resultsContainer.appendChild(li);
                    });
                }
            })
            .catch(error => console.error("Error fetching data:", error));
        }