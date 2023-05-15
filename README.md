# Open-source Machine Learning techniques and solutions for identifying drug markets on social media


Hi, welcome to this open-source repository.In this repository you have a chance
to challenge your knowledge about machine learning, data scraping and data analysis.

## Starting out
The starting code is not very complex, in the `scraper.py` file, you can see some base code 
for scraping data from Reddit using the [Praw library](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html).
In order to run the file, you first need to get your [Reddit Api credentials](https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/)
and put them in the `credentials.json` file. Then, you are pretty much ready to go!

## Scraping 
In the `info.json` file you can see the names of subreddits from which you want have the data scraped. Feel free to adapt it to your neeeds.
Later, by running `scraper.py` top comments will be scraped from the "hottest" submissions in the given subreddit. Then 
files csv (names comments + <name of the subreddit>) should be created. For privacy reasons you should not push changes with those files included 
and rather use the files locally to implement solutions to analyse the scraped data.

Enjoy!

## More on this project
If you are more interested and want to understand more about the objective of this project and how to help contributing
towards online illicit drug market monitoring please request access to this document: [link](to be inseted)
