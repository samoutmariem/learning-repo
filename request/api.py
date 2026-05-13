# =========================
# JSON DATA + REQUESTS API
# =========================


# #################################################
# 1. JSON BASICS
# #################################################

import json

# Python dictionary
data = {
    "name": "Mariem",
    "age": 25,
    "skills": ["Python", "Odoo", "SQL"]
}

# Convert Python -> JSON string
json_string = json.dumps(data)

print(json_string)
# {"name": "Mariem", "age": 25, "skills": ["Python", "Odoo", "SQL"]}


# Convert JSON -> Python
parsed = json.loads(json_string)

print(parsed["name"])
# Mariem


# #################################################
# 2. WRITE JSON TO FILE
# #################################################

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


# #################################################
# 3. READ JSON FROM FILE
# #################################################

with open("data.json", "r") as file:
    loaded = json.load(file)

print(loaded)
print(loaded["skills"])


# #################################################
# 4. UPDATE JSON DATA
# #################################################

loaded["age"] = 26

with open("data.json", "w") as file:
    json.dump(loaded, file, indent=4)


# #################################################
# 5. PRETTY JSON FORMAT
# #################################################

print(json.dumps(data, indent=2))


# #################################################
# 6. SIMPLE API CALL USING REQUESTS
# #################################################

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)
# 200


# Convert response to JSON
users = response.json()

print(users[0]["name"])
# First user name


# #################################################
# 7. LOOP THROUGH API DATA
# #################################################

for user in users:
    print(user["id"], user["name"])


# #################################################
# 8. FILTER API DATA
# #################################################

filtered = []

for user in users:
    if user["id"] <= 3:
        filtered.append(user["name"])

print(filtered)


# #################################################
# 9. POST REQUEST (SEND DATA)
# #################################################

payload = {
    "name": "Mariem",
    "job": "Developer"
}

post_response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload
)

print(post_response.status_code)
print(post_response.json())


# #################################################
# 10. PUT REQUEST (UPDATE DATA)
# #################################################

update_payload = {
    "name": "Mariem Updated",
    "job": "Senior Developer"
}

put_response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=update_payload
)

print(put_response.json())


# #################################################
# 11. DELETE REQUEST
# #################################################

delete_response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print(delete_response.status_code)
# 200


# #################################################
# 12. ERROR HANDLING WITH API
# #################################################

try:
    res = requests.get("https://jsonplaceholder.typicode.com/users")

    if res.status_code == 200:
        data = res.json()
        print("Success:", len(data))
    else:
        print("API Error:", res.status_code)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)


# #################################################
# 13. TIMEOUT HANDLING
# #################################################

try:
    res = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )
    print(res.json())
except requests.exceptions.Timeout:
    print("Request timed out")


# #################################################
# 14. HEADERS IN REQUEST
# #################################################

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    headers=headers
)

print(res.status_code)


# #################################################
# 15. REAL WORLD MINI PROJECT
# #################################################

def get_user_names():
    try:
        res = requests.get("https://jsonplaceholder.typicode.com/users")

        users = res.json()

        return [u["name"] for u in users]

    except Exception as e:
        return str(e)


print(get_user_names())


# #################################################
# 16. SAVE API DATA TO JSON FILE
# #################################################

import json
import requests

res = requests.get("https://jsonplaceholder.typicode.com/users")

if res.status_code == 200:
    with open("users.json", "w") as file:
        json.dump(res.json(), file, indent=4)


# #################################################
# 17. IMPORTANT SUMMARY
# #################################################

# JSON:
# - json.dumps()  -> Python to JSON string
# - json.loads()  -> JSON string to Python
# - json.dump()   -> write JSON to file
# - json.load()   -> read JSON from file

# Requests:
# - GET    -> read data
# - POST   -> create data
# - PUT    -> update data
# - DELETE -> remove data