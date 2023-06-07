# Network Mapper

The Network Mapper is a Python script for Windows that allows you to scan a range of IP addresses and check if a specific port is open on each address. It provides a basic network mapping functionality by establishing TCP connections with the specified port on each IP address to determine if it's open or closed.

## Prerequisites

- Python 3.x
- Windows operating system

## Usage

1. Clone the repository or download the script directly.

2. Open a command prompt or terminal and navigate to the directory where the script is located.

3. Run the following command to execute the script:

   ```shell
   python network_mapper.py
   ```

   The script will scan the IP addresses in the local network and check if port 80 is open on each address.

4. You can modify the port number in the `scan_port` function inside the script to scan for a different port. For example, to scan port 443, change the following line:

   ```python
   if scan_port(ip, 80):
   ```

   to:

   ```python
   if scan_port(ip, 443):
   ```

   Save the script and re-run it to scan the new port.

## Disclaimer

Please note that network scanning can be a sensitive operation. Ensure that you have proper authorization before performing any network scanning activities. Respect the security and privacy policies of the networks you are scanning. The script provided here is for educational and informational purposes only.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
