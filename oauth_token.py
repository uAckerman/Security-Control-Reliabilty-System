import requests

TOKEN_URL = "http://localhost:8080/realms/scrs-core/protocol/openid-connect/token"

def get_service_token(client_id, client_secret):
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    r = requests.post(TOKEN_URL, data=data)
    r.raise_for_status()
    return r.json()["access_token"]
