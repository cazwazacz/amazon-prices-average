#  Amazon UK average price checker #
A simple python script to get the average price from the first page of results for an [Amazon UK](https://www.amazon.co.uk/) search.

### Usage: ###
Clone the repo and install dependencies:
```
git clone https://github.com/cazwazacz/amazon-prices-average.git
cd amazon-prices-average
pip install -r requirements.txt
```
Make sure you have a `USER_AGENT_STRING` environment variable set. Then run the command, passing in your search query as such:
```
python index.py 'gaming pc gtx 1050 ssd'
```
An average will be printed, or you will be notified if no results were found.

