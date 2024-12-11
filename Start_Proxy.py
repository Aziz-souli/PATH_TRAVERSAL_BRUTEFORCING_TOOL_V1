import subprocess
import os

def start_mitmdump(proxy_script_path, port=8080):
    """
    Starts the mitmdump process with the given proxy script.
    
    Args:
        proxy_script_path (str): Path to the proxy script file (e.g., proxy.py).
        port (int): The port on which mitmdump will listen (default is 8080).
    
    Returns:
        subprocess.Popen: The Popen object representing the mitmdump process.
    """
    try:
        # Ensure the proxy script exists
        if not os.path.exists(proxy_script_path):
            raise FileNotFoundError(f"Proxy script not found: {proxy_script_path}")
        
        # Construct the mitmdump command
        command = ["mitmdump", "-s", proxy_script_path, "--listen-port", str(port)]
        
        # Start the mitmdump process
        process = subprocess.run(command,shell=True)
        print(f"Started mitmdump on port {port} with script: {proxy_script_path}")
        return process
    except Exception as e:
        print(f"Error starting mitmdump: {e}")
        return None



