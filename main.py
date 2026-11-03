"""
SOVEREIGN 66 - HIGH-PERFORMANCE QUANTUM & ENERGY SUITE
Developers:
1. YAMISH PAL (Roll No: BTEE24O2091)
2. TUMCHOBEMO C YANTHAN (Roll No: BTEE24O1084)
"""

import sys
import time
import os
import http.server
import socketserver
import webbrowser

PORT = 8000

def launch_sovereign_core():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[96m") # Cyan text
    banner = [
        "   _____  ______   _____   ______ _____  ______ _____ _____ _   _    ______ _____ ",
        "  / ____|/ ____ \\ / ____| / ____/  __ \\|  ____|_   _/ ____| \\ | |  / /____|  ___|",
        " | (___ | |    | | (___  | |   |  /  \\/ | |__    | || |    |  \\| | / /_   | |__  ",
        "  \\___ \\| |    | |\\___ \\ | |   | | __ |  __|   | || |    | . ` |/ /_ \\ |  __| ",
        "  ____) | |____| |____) || |___|  \\__/ /| |____ _| || |____| |\\  | |__) || |___ ",
        " |_____/ \\______/|_____/  \\____\\____/\\/ |______|_____\\_____|_| \\_|\\____/ \\____/",
        "  ==========================================================================",
        "     [!] SOVEREIGN 66: HYPER-CYAN & ULTRAVIOLET QUANTUM WEB SUITE [!]",
        "  ==========================================================================",
        "     Developers: YAMISH PAL (BTEE24O2091) | TUMCHOBEMO C YANTHAN (BTEE24O1084)",
        "  =========================================================================="
    ]
    for line in banner:
        print(line)
        time.sleep(0.08)
        
    print("\n[+] Launching local web server for Sovereign 66...")
    print(f"[+] Hosted at: http://localhost:{PORT}")
    
    # Open local browser automatically
    webbrowser.open(f"http://localhost:{PORT}")
    
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n[+] SOVEREIGN 66 CORE LIVE ON PORT {PORT}. Press Ctrl+C to terminate.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Sovereign 66 Server Shutdown Successfully.")

if __name__ == "__main__":
    launch_sovereign_core()
