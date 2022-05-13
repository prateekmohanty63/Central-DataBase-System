import requests
import creds

url = "https://nationalapi.docsumo.com/api/v1/national/extract/?side=back&save_data=false&return_redacted=false&fraud_check=true"
file_path=r"C:\Users\BRBCO\Downloads\Aadhar Card_page.jpg"

payload = {}
files = [
  ('files', open(file_path,'rb'))
]
headers = {
  'X-API-KEY': creds.api_key,
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.json())
