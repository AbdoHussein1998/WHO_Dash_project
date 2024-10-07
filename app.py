
import body
import interactions
import socket
import webbrowser
import threading
import time


def find_free_port():
    # Create a new socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to an available port provided by the OS
        s.bind(('', 0))  # '' means all available interfaces, 0 means let the OS choose the port
        # Return the port number assigned by the OS
        return s.getsockname()[1]

free_port=find_free_port()


def open_browser_on_localhost(free_port):
    try:
        # Construct the URL with the provided port
        url = f'http://localhost:{free_port}'
        # Open the URL in the default web browser
        webbrowser.open(url)
        print(f"Opened browser to {url}")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_server():
        app.run(debug=False, port=free_port)



app= body.mainbody()



server = app.server



if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    time.sleep(3)
    open_browser_on_localhost(free_port)