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
            const reviewLst = document.getElementById("review_lst")

            // Remove the current contents of the html list
            while (reviewLst.firstChild) {
                reviewLst.removeChild(reviewLst.firstChild)
            }

            if (result.length === 0) {
                let li = document.createElement('li');
                li.innerText = "No reviews found";
                reviewLst.appendChild(li);
            } else {

                // Add review contents to html list
                for (const review of result) {
                    let li = document.createElement('li');
                    li.innerText = review;
                    reviewLst.appendChild(li);
                }
            }
        })
    }
)