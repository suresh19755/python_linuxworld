import http.server
import socketserver
import socket
import os
import sys
import argparse

DEFAULT_PORT = 8000

def resolve_machine_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('10.255.255.255', 1))
        local_address = sock.getsockname()[0]
        sock.close()
    except Exception:
        local_address = '127.0.0.1'
    return local_address

def run_custom_server(port):
    if getattr(sys, 'frozen', False):
        os.chdir(os.path.dirname(sys.executable))

    my_ip = resolve_machine_ip()
    
    print(f"\n[+] Local Share Started successfully.")
    print(f"    Target: http://{my_ip}:{port}")
    print(f"    Source: {os.getcwd()}")
    print("-" * 30)
    print("    CTRL+C to shut down")
    print("-" * 30)

    handler_class = http.server.SimpleHTTPRequestHandler
    
    try:
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(("", port), handler_class) as server_instance:
            server_instance.serve_forever()     
    except KeyboardInterrupt:
        print("\n[!] Shutting down file server. Bye!")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quick Local File Host")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    
    args = parser.parse_args()
    
    run_custom_server(args.port)