
const urlContainer = document.getElementById('url-container');
const fetchUrl = urlContainer.getAttribute('data-fetch-url');

const urlContainer2 = document.getElementById('url-container-search');
const fetchUrl2 = urlContainer.getAttribute('data-fetch-url');


        function reloadData() {
        
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

        // function darktoggle() {
        //     var element = document.getElementById('body');
        //     element.classList.toggle("dark-mode");


        // }


        function liveSearch() {

            let query = document.getElementById('search-input').value;
 
        console.log(query)

            fetch(urlContainer2 )
            .then(response => response.json())
            console.log(response)
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