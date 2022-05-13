import requests

url = "http://localhost:3000/digilocker/doc_type"

payload = "{\n\t\"organssizationId\": \"001891\"\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)