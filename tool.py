import argparse
from request import DIRECTORY_BRUTEFORCE
from Start_Proxy import start_mitmdump
import threading
import time


# Argument parser setup
parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", type=str, nargs=1, 
                    help="Target URL to perform a brute-force path traversal attack.")

parser.add_argument("-p", "--PATH", type=str, nargs=1, 
                    help="Specify a file or path to test for path traversal vulnerabilities. Provide the path as a string.")

parser.add_argument("-l", "--log", type=str, nargs=1, 
                    help="Specify the path to a log file where attack results and information will be stored.")

parser.add_argument("-v", "--verbose", type=int, choices=[1, 2, 3],
                    help="Set the verbosity level. Use 1 for basic info, 2 for detailed info, and 3 for debug-level output.")

parser.add_argument("-CA", "--cert_path", type=str, nargs=1, 
                    help="Specify the path to the certificate authority (CA) certificate file for proxy verification.")

parser.add_argument("-A", "--ALL", action='store_true',
                    help="If provided, the tool will attempt all possible combinations. Without this argument, it will stop at the first successful 200 status code.")

parser.add_argument('-Pr', '--PROXY', action='store_true', 
                    help="Enable proxy support for the tool. If this flag is provided, the tool will route requests through the specified proxy settings.")

args = parser.parse_args()





# Run the proxy in a separate thread if the --PROXY flag is set

if args.PROXY:
    print("[INFO] Proxy flag is enabled.")
    proxy_thread = threading.Thread(target=start_mitmdump, args=("./proxy_config.py",), daemon=True)
    proxy_thread.start()

    # Allow some time for the proxy to initialize
    time.sleep(2)

# Run the directory brute force with or without proxy
print("[INFO] Starting directory brute force...")
DIRECTORY_BRUTEFORCE(
    args.PROXY,
    cert_path=args.cert_path,
    file=args.PATH[0], 
    url=args.url[0], 
    ALL=args.ALL
)

# Wait for the proxy thread
