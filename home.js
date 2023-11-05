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

// Passing the current tab URL to the flask server
var submitQueryButton = document.getElementById("submit_button");
submitQueryButton.addEventListener("click", () =>
    fetch(`http://localhost:5000/tra/query?item_url=${itemUrl}`).then(r => r.text()).then(result => {
        document.getElementById("review_lst").innerHTML = result
    })
)