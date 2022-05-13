import requests
import creds


url = "https://passportapi.docsumo.com/api/v1/passport/extract/?side=back&save_data=false&fraud_check=false"
file_path=r"C:\Users\BRBCO\Downloads\PassportJaydeep2021.pdf"

payload = {}
files = [
  ('files', open(file_path,'rb'))
]
headers = {
  'X-API-KEY': creds.api_key,
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.json())
