// Passing the current tab URL to the flask server
var submitQueryButton = document.getElementById("submit_button");

submitQueryButton.addEventListener("click", async function () {

        // Getting tabs
        const tabs = await chrome.tabs.query({
            active: true,
            lastFocusedWindow: true,
            url: [
                "https://www.target.com/*",
            ],
        });

        // Adding the tab URLs to an array
        const urls = []
        for (const tab of tabs) {
            urls.push(tab.url)
        }

        var itemUrl = urls.join(' ')
        var query = document.getElementById("search_bar").value.toString()

        // Send the request to the python flask server
        fetch(`http://localhost:5000/tra/query?query_text=${query}&item_url=${itemUrl}`).then(r => r.json()).then(result => {
            // Add review contents to html list
            const reviewLst = document.getElementById("review_lst")
            for (const review of result.reviews) {
                let li = document.createElement('li');
                li.innerText = review.body;
                reviewLst.appendChild(li);
            }
        })
    }
)