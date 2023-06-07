import socket
import subprocess
import ipaddress

def scan_port(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	result = sock.connect_ex((ip, port))
	sock.close()
	return result == 0

import socket


def get_local_ip():
    try:
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80)) # 80 (HTTP), 443 (HTTPS), 22 (SSH), 21 (FTP), 25 (SMTP)

        local_ip = temp_socket.getsockname()[0]

        temp_socket.close()

        return local_ip
    except socket.error:
        return None


def main():
	local_ip = get_local_ip()
	network = ipaddress.ip_network(local_ip+'/24', strict=False)

	for ip in network.hosts():
		ip = str(ip)
		if scan_port(ip, 80):  # Change the port number as per your requirement
			print(f"IP Address: {ip} - Port 80 is open.")

if __name__ == '__main__':
	main()
