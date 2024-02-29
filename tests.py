"""
This file contains the tests for the portScanner.py file.
"""

import os
from src.port_scanner import scan_ports, write_to_file


def test_scan_ports():
    target = "localhost"
    start_port = 80
    end_port = 80
    timeout = 1
    protocols = ["tcp"]

    result = scan_ports(target, start_port, end_port, timeout, protocols)
    assert isinstance(result, list)
    if result:
        port, protocol = result[0]
        assert port == 80
        assert protocol == "tcp"


def test_write_to_file():
    target = "localhost"
    start_port = 80
    end_port = 80
    timeout = 1
    num_threads = 1
    start_time = 0
    end_time = 1

    data = [(target, start_port, "tcp")]
    write_to_file(
        data,
        output_file,
        target,
        "tcp",
        start_port,
        end_port,
        timeout,
        start_time,
        end_time,
    )
    assert os.path.exists(output_file)
    with open(output_file, "r", encoding="utf-8") as file:
        content = file.read()
        assert "Port Scanner Results on localhost" in content


def cleanup(file):
    if os.path.exists(file):
        os.remove(file)


output_file = "test_output.txt"
test_scan_ports()
test_write_to_file()
cleanup(output_file)
