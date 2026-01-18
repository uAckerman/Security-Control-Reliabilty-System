import time
import yaml
from oauth_token import get_service_token
from keycloak_client_api import KeycloakClient
from mfa_probe import test_mfa_enforcement
from logging_probe import check_auth_logging
from alerting import send_alert

CONFIG = yaml.safe_load(open("expected_controls.yaml"))

CLIENT_ID = "security-prober"
CLIENT_SECRET = "sqMzQGAhpBIYFUhIOsLcWshOkIj58Bl6"
USERNAME = "uzair"
PASSWORD = "uzair"

def main():
    token = get_service_token(CLIENT_ID, CLIENT_SECRET)
    kc = KeycloakClient(token)

    # --- MFA PROBE ---
    result = test_mfa_enforcement(
        CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD
    )

    login_time = time.time()

    if CONFIG["mfa"]["required"] and result["status_code"] == 401:
        send_alert(
            "MFA Enforcement",
            "Enabled",
            "401 (Invalid Grant)",
            "MFA is actively preventing non-interactive authentication",
            "None"
        )

    if CONFIG["mfa"]["required"] and result["status_code"] == 200:
        send_alert(
            "MFA Enforcement",
            "Disabled",
            "200 (Grant)",
            "Succeed non-interactive authentication",
            "Enable OTP Authentication"
        )


if __name__ == "__main__":
    main()
