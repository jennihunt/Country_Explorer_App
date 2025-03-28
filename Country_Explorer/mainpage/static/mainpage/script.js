
const urlContainer = document.getElementById('url-container');
const fetchUrl = urlContainer.getAttribute('data-fetch-url');

// const urlContainer2 = document.getElementById('url-container-search');
// const fetchUrl2 = urlContainer.getAttribute('data-fetch-url');




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




// -------------------------------------------------------
        // still working on live search
        



    

         //Allows Live Search
    // function liveSearch(){
    //     console.log("hit")
    //     document.getElementById('search-form').submit()
    // }
     // this function with a oninput fires off but dodnt allow you too enter more than 1 letter



     //below function wouldnt fir off action or grab what was needed
        // function liveSearch() {

        //     let query = document.getElementById('search-input').value;
 
        // console.log(query)

        //     fetch(`/searchresults/?q=${query}`, { 
        //         method: 'GET',
        //         headers: { "X-Requested-With": "XMLHttpRequest" } // Identify as AJAX request
        //     })
        //     .then(response => response.json())
        //     console.log(response)
        //     .then(data => {
        //         let resultsContainer = document.getElementById('results');
        //         resultsContainer.innerHTML = '';  // Clear previous results

        //         if (data.countries.length === 0) {
        //             resultsContainer.innerHTML = '<li>No countries found.</li>';
        //         } else {
        //             data.countries.forEach(country => {
        //                 let li = document.createElement('li');
        //                 li.textContent = country.name;
        //                 resultsContainer.appendChild(li);
        //             });
        //         }
        //     })
        //     .catch(error => console.error("Error fetching data:", error));
        // }


// errors kept occuring with this url with the get 
// **The current path, searchresults/{% url 'search_results' %}, didn’t match any of these.

        // function liveSearch(value) {
        //     let query = value;
        //     let url = "{% url 'search_results' %}?q=" + encodeURIComponent(query);
            
        //     fetch(url)
        //     .then(response => response.text()) // Get response as HTML or JSON
        //     .then(data => {
        //         document.getElementById("search-results").innerHTML = data; // Update results
        //     })
        //     .catch(error => console.error("Error:", error));
        // };