from time import time
from time import sleep
from random import randint
from IPython.core.display import clear_output
from warnings import warn
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from requests import get
headers = {"Accept-Language": "en-US, en;q=0.5"}
# Redeclaring the lists to store data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2010,2021)]
# Preparing the monitoring of the loop
start_time = time()
max_request = 70
requests = 0
for year_url in years_url:
    # For every page in the interval 1-4
    for page in pages:
        # Make a get request
        url= 'http://www.imdb.com/search/title?release_date=' + year_url + '&sort=num_votes,desc&page=' + page +'&title_type=feature'
        response = get(url, headers = headers)
        # Pause the loop
       # sleep(randint(8,15))
        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)
        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))
        # Break the loop if the number of requests is greater than expected
        if requests > max_request:
            warn('Number of requests was greater than expected.')
            break
        # Parse the content of the request with BeautifulSoup