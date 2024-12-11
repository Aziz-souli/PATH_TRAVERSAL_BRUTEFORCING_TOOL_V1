from mitmproxy import http
from datetime import datetime

# ANSI escape codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"
UNDERLINE = "\033[4m"

print("Proxy script with enhanced logs has been loaded!")

def log_request(flow: http.HTTPFlow):
    """
    Logs details about the intercepted HTTP request with enhanced styling.
    """
    print(f"\n{BOLD}{CYAN}[REQUEST]{RESET}")
    print(f"{YELLOW}Timestamp:{RESET} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{GREEN}Method:{RESET} {flow.request.method}")
    print(f"{BLUE}URL:{RESET} {flow.request.url}")
    print(f"{MAGENTA}Headers:{RESET} {dict(flow.request.headers)}")
    print(f"{RED}Content Length:{RESET} {len(flow.request.content) if flow.request.content else 0} bytes")
    print(f"{DIM}{'-' * 50}{RESET}")


def log_response(flow: http.HTTPFlow):
    """
    Logs details about the intercepted HTTP response with enhanced styling.
    """
    print(f"\n{BOLD}{CYAN}[RESPONSE]{RESET}")
    print(f"{YELLOW}Timestamp:{RESET} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{GREEN}URL:{RESET} {flow.request.url}")
    print(f"{BLUE}Status Code:{RESET} {flow.response.status_code}")
    print(f"{MAGENTA}Headers:{RESET} {dict(flow.response.headers)}")
    print(f"{RED}Content Length:{RESET} {len(flow.response.content) if flow.response.content else 0} bytes")
    print(f"{DIM}{'-' * 50}{RESET}")


# Intercept requests
def request(flow: http.HTTPFlow) -> None:
    log_request(flow)
    # Add custom modifications to the request here if needed

# Intercept responses
def response(flow: http.HTTPFlow) -> None:
    log_response(flow)
    # Add custom modifications to the response here if needed
