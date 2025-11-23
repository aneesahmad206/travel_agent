import requests

response = requests.get("https://iam.cloud.ibm.com/identity/token", timeout=5)
print(response.status_code)
print(response.text[:200])  # first 200 chars
