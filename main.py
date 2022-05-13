import requests

url = "https://nationalapi.docsumo.com/api/v1/national/extract/?side=back&save_data=false&return_redacted=false&fraud_check=true"
file_path=r"C:\Users\BRBCO\Downloads\Aadhar Card_page.jpg"

payload = {}
files = [
  ('files', open(file_path,'rb'))
]
headers = {
  'X-API-KEY': "TuCennjAaeYyJbAb00e4ZAFbpIwkgDYGwCgqnLT4dAT4uS6PohMi4tnnG4Ta",
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.json())
