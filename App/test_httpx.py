import requests

r = requests.get(
    "https://api.themoviedb.org/3/movie/popular",
    params={
        "api_key": "42d064dfd224fb7e6c6553a611228791",
        "language": "en-US",
        "page": 1
    },
    timeout=30
)

print(r.status_code)