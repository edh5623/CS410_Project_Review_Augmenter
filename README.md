# CS410_Project_Review_Augmenter

Chrome extension to augment Target.com with BM25 search on product reviews and a product review sentiment score.

## Overview 

The primary function of the Target Review Augmenter is to enable a user with BM25 search over a collection Target.com of product reviews. The extension will take a query from the user, 
fetch the product reviews from the Target product page they are currently on, query the reviews using BM25, and display the top results to the user. This allows the user
to more intelligently search through product reviews to answer any questions they may have about a product.

Additionally, this extension will calculate an aggregated sentiment score over all of the reviews for a given product and display this to the user. This allows the user to compare
the average star rating that Target provides for a product with the sentiment score as a second opinion on the quality of the product.

### Use

Upon opening the extension the user is greeted with a search box and a search button.
![intro](assets/intro_screen.PNG)

To use the extension, navigate to a Target.com product page that has reviews. For example: https://www.target.com/p/wilson-nba-forge-size-7-basketball/-/A-82153614#lnk=sametab
![intro](assets/full_screen.PNG)

Next type a query into the search bar and select the Search button to submit the query.
![intro](assets/enter_query.PNG)

Wait a few seconds for the extension to retrieve the reviews and then the query results will be displayed:
![intro](assets/query_results.PNG)

The results are displayed in order of relevance. Additionally, the average 5-star rating provided by target is 
displayed as well as the sentiment rating score.

## Implementation 
2. how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement.

This extension was implemented as a Chrome extension following the guidelines here https://developer.chrome.com/docs/extensions/mv3/getstarted/. This means that the 
interface was developed using HTML and styled with CSS. The button and search UI functionality is controlled by JavaScript.

### Key Components:
* Google Chrome Extensions: https://developer.chrome.com/docs/extensions/mv3/getstarted/
* Flask: https://github.com/pallets/flask
* RedCircle API: https://www.redcircleapi.com/
* Rank_BM25: https://github.com/dorianbrown/rank_bm25/
* NLTK: https://www.nltk.org/


## Setup
3. Documentation of the usage of the software including either documentation of usages of APIs or detailed instructions on how to install and run a software, whichever is applicable.
   
This Chrome extension runs with a Python backend and uses a Flask webserver to allow JavaScript to call Python code. The Python code makes requests to the RedCircle API to get Target product review data.

To run this extension we need to first add the extension to Chrome, run the Flask server included in this repo, and add a RedCircle API key.

 * 1\. Clone this repo to your local machine.
 * 2\. Load the extension in Chrome: https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/
   * Go to chrome://extensions
   * Enable developer mode with the switch in the top right
   * Click "Load unpacked"
   * Select the cloned CS410_Project_Review_Augmenter folder
     * This folder should contain the manifest.json
   * Now the extension is in Chrome. It is helpful to pin the extension during use by selecting the extensions menu in Chrome and selecting the pin icon. See https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/ for more details.
 * 3\. Set up the Python environment as follows:
   * Download Conda:
     * Windows: https://docs.anaconda.com/free/anaconda/install/windows/
     * MacOS: https://docs.anaconda.com/free/anaconda/install/mac-os/
   * From the CS410_Project_Review_Augmenter directory, clone the Conda environment for this project using the environment.yml with this command: `conda env create -f environment.yml`
   * Activate the environment: `conda activate cs410-35`
 * 4\. Set up the RedCircle API key to retrieve reviews for a given product.
   * Create a free acount on the RedCircle API website: https://www.redcircleapi.com/
   * Log into your account and click on the "API Playground" tab on your account page.
   * Copy the API key in the upper right corner.
   * In your cloned CS410_Project_Review_Augmenter folder, navigate to the `CS410_Project_Review_Augmenter/python` directory and open the `config.py` file in any editor.
   * Paste the copied API key into the `api_key` variable defined in `config.py`.
   * `config.py` should now look like this:
     * ```
       api_key = "YOUR_COPIED_API_KEY"
       ```
   * This free RedCircle account will give you 100 free requests for testing. A request is made every time a query is submitted via the "Search" button.
 * 5\. Run the Flask Server
   * From the `CS410_Project_Review_Augmenter/python` directory with the cs410-35 environment active run: `python python/flaskapp.py`
   * The Flask server is now running
 * 6\. The extension is now ready to use in Chome

When done using the extension close the server with ctrl-c. To use the extension in the future, run the flaskapp server before use.

## Contributors
Ethan Howes - edhowes2@illinois.edu

This project was solely completed by Ethan Howes on a 1-person team.
