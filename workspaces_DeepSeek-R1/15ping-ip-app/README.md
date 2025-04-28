# Ping IP Application

This project is a simple Python application that accepts an IP address as input and returns the result of the ping command for that IP address.

## Project Structure

```
ping-ip-app
├── src
│   └── ping_script.py       # Main script for pinging an IP address
├── tests
│   └── test_ping_script.py   # Unit tests for the ping script
├── requirements.txt          # Dependencies for the project
├── README.md                 # Project documentation
└── .gitignore                # Files to ignore in Git
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ping-ip-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the ping script, execute the following command in your terminal:

```
python src/ping_script.py <IP_ADDRESS>
```

Replace `<IP_ADDRESS>` with the actual IP address you want to ping.

## Running Tests

To run the unit tests for the ping script, use the following command:

```
python -m unittest discover -s tests
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.