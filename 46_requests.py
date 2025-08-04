# --------------------------
# Requests
# --------------------------

"""
A third-party library (not in the standard library).
Makes HTTP requests easy (no need to manually handle sockets or raw urllib).
Often used for APIs, web scraping, downloading data, etc.
"""
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200 (success)
print(response.text)         # Raw response as text
print(response.json())       # Parsed JSON

data = {"name": "Genius", "role": "Developer"}
response = requests.post("https://httpbin.org/post", json=data)
print(response.status_code)
print(response.json())

# Update data
# requests.put("https://httpbin.org/put", json={"update": "yes"})

# Delete data
# requests.delete("https://httpbin.org/delete")

# headers = {"Authorization": "Bearer mytoken123"}
# response = requests.get("https://api.example.com/data", headers=headers)

# try:
#     response = requests.get("https://example.com", timeout=5)
#     response.raise_for_status()  # Raises HTTPError for bad responses
# except requests.exceptions.Timeout:
#     print("Request timed out")
# except requests.exceptions.HTTPError as err:
#     print(f"HTTP error: {err}")

