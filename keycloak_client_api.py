# Maintainer: Uzair Khan

import requests

BASE_ADMIN_URL = "http://localhost:8080/admin/realms/scrs-core"

class KeycloakClient:
    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get_events(self):
        url = f"{BASE_ADMIN_URL}/events"
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        return r.json()
