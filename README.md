# Port Scanner

This is a simple port scanner written in Python. It is a command line tool that can be used to scan for open ports on a given IP address.

## Installation

To install the port scanner,

1. Clone the repository:
2. Highly recommended to create a virtual environment and activate it
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install the dependencies:

```bash
make install
```

## Usage

To use the port scanner, run the following command:

```bash
python main.py --target <target> --range <start_port>-<end_port> --timeout <timeout> --protocol <protocol> --output_file <output_file>
```

## Help

To get help on how to use the port scanner, run the following command:

```bash
python main.py -h
or 
python main.py --help
```

The following options are available:

- `--target` : The target IP address or hostname to scan
- `--range` : The range of ports to scan (e.g. 1-1024)
- `--timeout` : The timeout for the scan in seconds
- `--protocol` : The protocol to use for the scan (e.g. tcp, udp, http)
- `--output_file` : The file to write the results to (e.g. results.txt)

## Example

To scan the first 1024 ports on the IP address `localhost` using the TCP protocol and a timeout of 1 second, run the following command:

```bash
python main.py --target localhost --range 1-1024 --timeout 1 --protocol tcp --output_file results.txt
```

## For Developers

To run the tests, simply run the following command:

```bash
make test
```

To run the linter, simply run the following command:

```bash
make lint
```

To run the formatter, simply run the following command:

```bash
make format
```
