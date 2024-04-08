import requests
from requests import request

# Task 1, 2
url = 'https://newsapi.org/v2/everything'
first_param = 'q=Apple'
second_param = 'from=2024-04-06'
third_param = 'sortBy=popularity'
fourth_param = 'apiKey=6902dbba3fcd44a48f31db8c6419f385'
url = f'{url}?{first_param}&{second_param}&{third_param}&{fourth_param}'
response = requests.get(url)

# Task 3
# url = 'https://newsapi.org/v2/everything'
# first_param = 'q=motorola'
# second_param = 'from=2024-04-06'
# third_param = 'apiKey=6902dbba3fcd44a48f31db8c6419f385'
# url = f'{url}?{first_param}&{second_param}&{third_param}'
# response = requests.get(url)

# Task 4
# url = 'https://newsapi.org/v2/everything?q=samsung&apiKey=6902dbba3fcd44a48f31db8c6419f385'
#
# response = requests.get(url, params={"source": {"id": "wired",
#                                                 "name": "Wired"},
#                                      "author": "Emma Roth"})
print(response.status_code)
print(response.json())

