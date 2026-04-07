# Maintainer : Uzair Khan

import requests
import time

TOKEN_URL = "http://localhost:8080/realms/scrs-core/protocol/openid-connect/token"

def test_mfa_enforcement(client_id, client_secret, username, password):
    data = {
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password
    }

    start = time.time()
    r = requests.post(TOKEN_URL, data=data)
    duration = time.time() - start

    return {
        "status_code": r.status_code,
        "response": r.text,
        "duration": duration
    }
