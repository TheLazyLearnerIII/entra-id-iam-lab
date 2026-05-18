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

user_data = {
    "accountEnabled": True,
    "displayName": "Test_User_Five",
    "mailNickname": "testuser5",
    "userPrincipalName": "testuser5@usanyc.onmicrosoft.com",
    "passwordProfile": {
        "forceChangePasswordNextSignIn": True,
        "password": "Pa$$W0rDD777"
    }
}

create_response = requests.post("https://graph.microsoft.com/v1.0/users", headers=headers, json=user_data)

if create_response.status_code == 201:
    print("User Created")
else:
    print(f"Status Code {create_response.status_code}: {create_response.json()}")