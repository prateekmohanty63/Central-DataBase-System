import requests
import creds

url = "https://panapi.docsumo.com/api/v1/pan/extract/?save_data=false&fraud_check=true"
file_path=r"C:\Users\BRBCO\Downloads\pan-card-1.jpg"

payload = {}
files = [
  ('files', open(file_path,'rb'))
]
headers = {
  'X-API-KEY': creds.api_key,
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.json())

