import base64
import requests
import sys

filepath = sys.argv[1]
filename = file_path.split('/')[-1]
encoded_file = None
with open(filepath, "rb") as img_file:
    encoded_file = base64.b64encode(img_file.read()).decode('utf-8')

req_json = { 'name': filename, 'type': 'image', 'isPublic': True, 'data': encoded_file, 'parentId': sys.argv[3] }
req_headers = { 'X-Token': sys.argv[2] }

req = requests.post("http://0.0.0.0:5000/files", json=req_json, headers=req_headers)
print(req.json())
