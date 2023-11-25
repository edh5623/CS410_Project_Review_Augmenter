// Passing the current tab URL to the flask server
var submitQueryButton = document.getElementById("submit_button");

document.getElementById("ratings").style.display = "none";
document.getElementById("loader").style.display = "none";

submitQueryButton.addEventListener("click", async function () {

        // show the loading wheel
        document.getElementById("loader").style.display = "block";

        // Getting tabs
        const tabs = await chrome.tabs.query({
            active: true,
            lastFocusedWindow: true,
            url: [
                "https://www.target.com/*",
            ],
        });

        // Adding the tab URLs to an array
        const urls = [];
        for (const tab of tabs) {
            urls.push(tab.url)
        }

        var itemUrl = urls.join(' ');
        var query = document.getElementById("search_bar").value.toString();

        // Send the request to the python flask server
        fetch(`http://localhost:5000/tra/query?query_text=${query}&item_url=${itemUrl}`).then(r => r.json()).then(result => {
            // hide the loading wheel
            document.getElementById("loader").style.display = "none";

            // show and populate the rating numbers
            document.getElementById("ratings").style.display = "block";
            document.getElementById("five_star_rating").innerText = result["five_star_rating"];
            document.getElementById("tra_sentiment").innerText = result["sentiment_rating"];

            const reviewLst = document.getElementById("review_lst");

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
                for (const review of result["ranked_reviews"]) {
                    let li = document.createElement('li');
                    li.innerText = review;
                    reviewLst.appendChild(li);
                }
            }
        })
    }
)