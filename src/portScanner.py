import socket


def scan_ports(target, start_port, end_port, timeout, protocols):
    """
    Scan the ports of a target using the specified protocols
    """
    open_ports = []
    for port in range(start_port, end_port + 1):
        for protocol in protocols:
            try:
                if protocol == "tcp":
                    sock = socket.socket(
                        socket.AF_INET, socket.SOCK_STREAM
                    )  # Create a TCP socket
                elif protocol == "udp":
                    sock = socket.socket(
                        socket.AF_INET, socket.SOCK_DGRAM
                    )  # Create a UDP socket
                elif protocol == "http":
                    sock = socket.socket(
                        socket.AF_INET, socket.SOCK_STREAM
                    )  # Create a TCP socket for HTTP
                    sock.sendall(
                        b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n"
                    )  # Send an HTTP GET request
                else:
                    raise ValueError(
                        f"Unsupported protocol: {protocol}"
                    )  # Raise an error for unsupported protocols

                sock.settimeout(timeout)  # Set the socket timeout
                result = sock.connect_ex(
                    (target, port)
                )  # Connect to the target and port
                if result == 0:
                    open_ports.append((port, protocol))  # Add the open port to the list
                sock.close()  # Close the socket
            except socket.error:
                pass
    return open_ports


def write_to_file(
    data,
    output_file,
    target,
    protocol,
    start_port,
    end_port,
    timeout,
    num_threads,
    start_time,
    end_time,
):
    """
    Write the scan results to a file
    """
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Port Scanner Results on {target}\n")
        file.write(f"Protocol: {protocol}\n")
        file.write(f"Port Range: {start_port}-{end_port}\n")
        file.write(f"Timeout: {timeout}\n")
        file.write(f"Number of Threads: {num_threads}\n")
        file.write(f"Start Time: {start_time}\n")
        file.write(f"End Time: {end_time}\n\n")
        for ip, port, protocol in data:
            file.write(f"IP: {ip} - Port {port} is open ({protocol.upper()})\n")
        file.write(f"\nScan completed in {end_time - start_time} seconds.\n")
        file.write("========================================\n\n")