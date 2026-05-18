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

group_id = "8f314a76-0e53-4053-9452-cee83d0b6344"
user_id = "7c6872fb-ff8c-4458-a499-f56b76372a71"

group_reference = f"https://graph.microsoft.com/v1.0/groups/{group_id}/members/$ref" # targets the group that I want to add members to.

member_data = {
    "@odata.id": f"https://graph.microsoft.com/v1.0/directoryObjects/{user_id}" # used to get the members information but you must use "@odata.id + the full link and user_id""
}

assign_response = requests.post(group_reference, json=member_data, headers=headers)

if assign_response.status_code == 204:
    print("Process Complete. User assigned to group")
else:
    print(f"Status code: {assign_response.status_code}. Error: {assign_response.json()}")