# AWS Server Configuration System

This project implements a server configuration system to initialize Amazon Web Services (AWS) services, specifically focusing on EC2 (Elastic Compute Cloud). The application uses access credentials for authentication, which are loaded from a configuration file.

## Project Structure

```
aws-server-config
├── src
│   ├── main.py                # Entry point of the application
│   ├── aws_services           # Module for AWS services
│   │   ├── __init__.py        # Package initialization
│   │   └── ec2.py             # EC2 service management
│   └── utils                  # Utility functions
│       ├── __init__.py        # Package initialization
│       └── config_loader.py    # Load AWS credentials
├── config
│   └── aws_credentials.json    # AWS access credentials
├── tests
│   ├── __init__.py            # Package for test suite
│   ├── test_ec2.py            # Unit tests for EC2Service
│   └── test_config_loader.py   # Unit tests for config loader
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Files to ignore in version control
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd aws-server-config
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your AWS credentials:
   - Create a file named `aws_credentials.json` in the `config` directory with the following structure:
     ```json
     {
       "access_key": "YOUR_ACCESS_KEY",
       "secret_key": "YOUR_SECRET_KEY",
       "region": "YOUR_AWS_REGION"
     }
     ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Testing

To run the tests, use:
```
pytest
```

This will execute all unit tests in the `tests` directory.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.