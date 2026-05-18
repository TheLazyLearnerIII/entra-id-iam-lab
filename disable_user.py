from dotenv import load_dotenv
import requests
import os

load_dotenv()

ms_client_id = os.getenv("CLIENT_ID")
ms_client_secret = os.getenv("CLIENT_SECRET")
ms_tenant_id = os.getenv("TENANT_ID")


token_data = {
    "client_id": ms_client_id,
    "client_secret": ms_client_secret,
    "scope": "https://graph.microsoft.com/.default",
    "tenant_id": ms_tenant_id,
    "grant_type": "client_credentials"
}

token_url = f"https://login.microsoftonline.com/{ms_tenant_id}/oauth2/v2.0/token" # token url is combining https://login.microsoftonline.com + Tenant ID + adding /oauth2/v2.0/token at the end.
response = requests.post(token_url, data=token_data)
access_token = response.json()['access_token'] # Authentication

headers = {
    "Authorization": "Bearer " + access_token
}

user_id = "testuser5@usanyc.onmicrosoft.com"
endpoint_url = f"https://graph.microsoft.com/v1.0/users/{user_id}"

disable_data = {
    "accountEnabled": False
}

disable_response = requests.patch(endpoint_url, headers=headers, json=disable_data)

if disable_response.status_code == 204:
    print(f"User Disabled Status Code: {disable_response.status_code}")
else:
    print(f"Status code {disable_response.status_code}: {disable_response.json()}")

