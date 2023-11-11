# CS410_Project_Review_Augmenter

Chrome extension to augment target.com with BM25 search on product reviews and a product review sentiment score.

## Setup
This Chrome extension runs with a Python backend and uses a Flask webserver to allow JavaScript to call Python code. 

To run this extension we need to first add the extension to Chrome and additionally run the Flask server included in this repo.

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
   * From the CS410_Project_Review_Augmenter directory, clone the Conda environment for this project with the environment.yml as such: `conda env create -f environment.yml`
   * Activate the environment: `conda activate cs410-35`
 * 4\. Run the Flask Server
   * From the CS410_Project_Review_Augmenter directory with the cs410-35 environment active run: `python python/flaskapp.py`
 * 5\. Now the extension is ready to use in Chome
 * 6\. When done using the extension close the server with ctrl-c. To use the extension in the future, run the flaskapp server before use.

 ## Use
