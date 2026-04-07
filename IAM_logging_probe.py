# Maintainer : Uzair Khan

import time

def check_auth_logging(events, login_time, max_delay):
    for event in events:
        event_time = event.get("time", 0) / 1000
        if abs(event_time - login_time) <= max_delay:
            return True
    return False
