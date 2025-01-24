import socket
import time

import socket
import time


def connect_to_server(host, port=12345):
  while True:
    try:
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client_socket.settimeout(5)  # Setting timeout to 5 seconds
      client_socket.connect((host, port))

      try:
        message = client_socket.recv(1024)
        print(
            f"Connection successful! Message from server: {message.decode()}")
        client_socket.close()
        break  # Exit the loop after successful connection
      except socket.timeout:
        print("Timed out waiting for a response from the server.")
        break  # Exit the loop on timeout

    except ConnectionRefusedError:
      print("Server is unavailable, retrying in 1 second...")
      time.sleep(1)
    except Exception as e:
      print(f"An error occurred: {e}")
      break  # Exit the loop on general exceptions


if __name__ == "__main__":
  server_ip = '10.0.0.102'  # Replace with your server's IP address
  connect_to_server(server_ip, 60000)
