import json
import datetime
from urllib.request import urlopen

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

current_date = datetime.date.today()
current_year = current_date.year
current_month = current_date.month
previous_month = current_month - 1

url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/"

# top_1000_most_visited_articles

url = url + str(current_year) + '/' + str(previous_month).rjust(2, '0') + "/all-days"

with urlopen(url) as url:
    data = json.load(url)
    top_articles = data["items"][0]["articles"]
    print(top_articles)
