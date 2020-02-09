import requests
from requests import HTTPError
import json
from getpass import getpass
from requests.exceptions import Timeout
from requests.adapters import HTTPAdapter


response = requests.get("https://www.engineerspock.com/")
print(response)
print(type(response))
print(response.status_code)
if response:
    print('Works!')

for url in ["https://www.engineerspock.com/", "https://www.engineerspock.com/inexistent"]:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Error: {http_err}')
    except Exception as err:
        print(f'Unknown error: {err}')
    else:
        print('Connected Successfully!')

response = requests.get("https://www.engineerspock.com/")
print(response.content)
# response.encoding = 'uft-8'
# print(response.text)
response = requests.get('https://api.github.com')
print(response.text)
data = response.json()
print(data)
print()

blog_response = requests.get("https://www.engineerspock.com/")
github_response = requests.get("https://api.github.com/")
print(blog_response.headers, end='\n')
print()
print(github_response.headers, end='\n')
print(blog_response.headers['content-type'])  # case insensitive. The same as 'Content-Type'

placeholder_response = requests.get('https://jsonplaceholder.typicode.com/comments', params=b'postId=1')
print(placeholder_response.json())


class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


class ChessPlayer:
    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data['tournaments']))
        return cls(tournaments)


t1 = Tournament("Aeroflot Open", 2010)
t2 = Tournament("FIDE World Cup", 2018)
t3 = Tournament("FIDE Grand Prix", 2016)
p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1, default=lambda obj: obj.__dict__, indent=4, sort_keys=True)
response = requests.post('https://httpbin.org/post', json=json_data)
json_response = response.json()
print(json_response)
print(json_response['data'])
print(json_response['headers']['Content-Type'])
print('---------------------------------------------------------------------------------------------------------------')


# auth_response = requests.get('https://api.github.com/user', auth=('Voorhees2019', getpass()))
# print(auth_response.json())


try:
    response = requests.get("https://www.engineerspock.com/", timeout=1)
except Timeout:
    print('The request timed out')
print(response)


# with requests.Session() as session:
#     session.auth = ('Voorhees2019', getpass())
#     response = session.get('https://api.github.com/user')
#     # do a lot of stuff
# print(response.json())


# amount of connection retries
# adapter = HTTPAdapter(max_retries=3)
# with requests.Session() as session:
#     session.mount('https://api.github.com/', adapter)
#     session.auth = ('Voorhees2019', getpass())
#     try:
#         session.get('https://api.github.com/user')
#     except ConnectionError as err:
#         print(f'Failed to connect: {err}')
#     else:
#         print('OK')





