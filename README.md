# Port Scanner

This is a simple port scanner written in Python. It is a command line tool that can be used to scan for open ports on a given IP address or a hostname. The tool supports scanning for TCP, UDP, and HTTP ports. It also supports multithreading to speed up the scanning process. The results of the scan can be written to a file and verbose output can be enabled to see the progress of the scan.

## Installation

To install the port scanner,

1. Copy the repository to your local machine and navigate to the directory containing the `main.py` file.
```bash
cd portScanner
```

2. Highly recommended to create a virtual environment and activate it using the following commands:
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
python main.py --target=<target> --range=<start_port>-<end_port> --threads=<number_of_threads> --timeout=<timeout> --protocol=<protocol> --output_file=<output_file> --verbose=<verbose>
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
- `--threads` : The number of threads to use for the scan
- `--protocol` : The protocol to use for the scan (e.g. tcp, udp, http)
- `--output_file` : The file to write the results to (e.g. results.txt)
- `--verbose` : Whether to print verbose output (e.g. True, False)

## Example

To scan the first 1024 ports on the IP address `localhost` using the TCP protocol and a timeout of 1 second, run the following command:

```bash
python main.py --target=localhost --range=1-1024 --threads=10 --timeout=1 --protocol=tcp --output_file=results.txt --verbose=True
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

## Docker version

To build the docker image, run the following command:

```bash
docker build -t port-scanner .
```

To run the docker image, run the following command:

```bash
docker run port_scanner main.py --target <target> --range <start_port>-<end_port> --threads <number_of_threads> --timeout <timeout> --protocol <protocol> --output_file <output_file> --verbose <verbose>
```

For example:

```bash
docker run port_scanner main.py --target 100.115.210.81 --threads 10 --range 1-100 --verbose true
```
make sure to add `--verbose=True` to see the output
