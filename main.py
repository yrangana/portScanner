"""
This is the main file for the port scanner. It is used to run the port scanner from the command line.
"""

import argparse
import re
from src.port_scanner import scan_ports, write_to_file
from src.Job import Job
from src.ScanResults import ScanResults

protocols = ["tcp", "udp", "http"]
min_port = 1
max_port = 65535
default_timeout = 1


def main():
    """
    run the port scanner from the command line

    usage: main.py -h or --help for help
    main.py --target <target> --range <start_port> - <end_port> --timeout <timeout> --protocol <protocol> --output_file <output_file>

    example:
    main.py --target localhost --range 1-1024 --timeout 1 --protocol tcp --output_file output.txt

    """
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument(
        "--target",
        help="The target url or ip to scan",
        metavar="target",
        required=True,
    )

    parser.add_argument(
        "--range",
        help="The range of ports to scan in the format start_port-end_port",
        required=False,
        metavar="start_port-end_port",
        default=f"{min_port}-{max_port}",
    )

    parser.add_argument(
        "--timeout",
        help="The timeout for the scan in seconds",
        required=False,
        metavar="timeout",
        type=int,
        default=default_timeout,
    )

    parser.add_argument(
        "--protocol",
        help="The protocol to use for the scan. Options are tcp, udp, http",
        required=False,
        metavar="protocol",
        default="tcp",
    )

    parser.add_argument(
        "--output_file",
        help="The path of the file to write the results to",
        required=False,
        metavar="file path",
        default="output.txt",
    )

    args = parser.parse_args()

    if not re.match(r"\d+-\d+", args.range):
        raise ValueError("Invalid port range")

    start_port, end_port = args.range.split("-")

    if int(start_port) < min_port or int(end_port) > max_port:
        raise ValueError(f"Port range must be between {min_port} and {max_port}")

    if start_port > end_port:
        raise ValueError("Start port must be less than or equal to end port")

    args.start_port = int(start_port)
    args.end_port = int(end_port)
    args.timeout = int(args.timeout)
    args.protocols = args.protocol

    job = Job(
        args.target,
        args.start_port,
        args.end_port,
        args.timeout,
        args.protocols,
    )

    open_ports = scan_ports(job=job)

    scan_results = ScanResults(
        data=open_ports,
        output_file=args.output_file,
        job=job,
        start_time=0,
        end_time=1,
    )

    write_to_file(scan_results=scan_results)


if __name__ == "__main__":
    main()
