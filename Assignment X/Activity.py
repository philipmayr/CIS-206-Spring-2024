import datetime
import urllib.request
import urllib.parse
import re

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

current_date = datetime.date.today()
current_year = current_date.year
current_month = current_date.month
previous_month = current_month - 1

print(current_date)
print(current_year)
print(current_month)

url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access"

# top_1000_most_visited_articles
