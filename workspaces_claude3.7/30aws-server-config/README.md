# AWS Server Configuration System

This project provides a server configuration system that initializes various Amazon Web Services (AWS) using access credentials for authentication. The main focus is on managing EC2 instances, S3 buckets, and RDS databases.

## Project Structure

```
aws-server-config
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── config
│   │   ├── __init__.py
│   │   └── credentials.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── ec2.py
│   │   ├── s3.py
│   │   └── rds.py
│   └── utils
│       ├── __init__.py
│       ├── auth.py
│       └── logger.py
├── tests
│   ├── __init__.py
│   ├── test_ec2.py
│   └── test_auth.py
├── config
│   └── aws_config.ini.example
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd aws-server-config
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Make sure to configure your AWS credentials in the `config/aws_config.ini.example` file or set them as environment variables.

## Services

- **EC2Service**: Manage EC2 instances (launch, stop, etc.).
- **S3Service**: Handle file uploads and downloads in S3 buckets.
- **RDSService**: Create and manage RDS instances.

## Testing

To run the tests, use:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.