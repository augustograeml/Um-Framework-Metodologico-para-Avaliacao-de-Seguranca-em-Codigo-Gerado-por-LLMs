# IP Ping Tool

This project is a simple command-line tool that allows users to ping an IP address and receive the results. It is designed to validate the IP address input and execute the ping command using Python.

## Project Structure

```
ip-ping-tool
├── src
│   ├── main.py          # Entry point of the application
│   ├── ping_utils.py    # Contains the ping functionality
│   └── validators.py     # Validates IP addresses
├── tests
│   ├── test_main.py     # Unit tests for main.py
│   └── test_validators.py # Unit tests for validators.py
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To use the IP Ping Tool, run the following command in your terminal:

```
python src/main.py <IP_ADDRESS>
```

Replace `<IP_ADDRESS>` with the IP address you want to ping.

## Running Tests

To run the tests for this project, use the following command:

```
pytest
```

Make sure you have `pytest` installed, which can be added to your `requirements.txt` if not already included.

## License

This project is open-source and available under the MIT License.