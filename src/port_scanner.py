"""
Module to scan the ports of a target and write the results to a file
"""

import socket
from src.Job import Job
from src.ScanResults import ScanResults


def scan_ports(job: Job):
    """
    Scan the ports of a target using the specified protocols
    """
    open_ports = []  # Create a list to store the open ports

    for port in range(job.start_port, job.end_port + 1):
        try:
            if job.protocol == "tcp":
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM
                )  # Create a TCP socket
            elif job.protocol == "udp":
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM
                )  # Create a UDP socket
            elif job.protocol == "http":
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM
                )  # Create a TCP socket for HTTP
                sock.sendall(
                    b"GET / HTTP/1.1\r\nHost: " + job.target.encode() + b"\r\n\r\n"
                )  # Send an HTTP GET request
            else:
                raise ValueError(
                    f"Unsupported protocol: {job.protocol}"
                )  # Raise an error for unsupported protocols

            if job.timeout:
                sock.settimeout(job.timeout)  # Set the socket timeout

            result = sock.connect_ex(
                (job.target, port)
            )  # Connect to the target and port
            if result == 0:
                open_ports.append(port)  # Add the open port to the list
            sock.close()  # Close the socket
        except socket.error as e:
            raise ValueError from e
    return open_ports


def write_to_file(scan_results: ScanResults):
    """
    Write the scan results to a file
    """
    with open(scan_results.output_file, "w", encoding="utf-8") as file:
        file.write(f"Port Scanner Results on {scan_results.job.target}\n")
        file.write(f"Protocol: {scan_results.job.protocol}\n")
        file.write(
            f"Port Range: {scan_results.job.start_port}-{scan_results.job.end_port}\n"
        )
        file.write(f"Timeout: {scan_results.job.timeout}\n")
        file.write(f"Start Time: {scan_results.start_time}\n")
        file.write(f"End Time: {scan_results.end_time}\n\n")
        for port in scan_results.data:
            file.write(f"Port {port} is open\n")
        file.write(
            f"\nScan completed in {scan_results.end_time - scan_results.start_time} seconds.\n"
        )
        file.write("========================================\n\n")
