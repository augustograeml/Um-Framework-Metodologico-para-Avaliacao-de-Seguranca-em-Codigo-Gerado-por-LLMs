# AWS Server Configuration System

This project implements a server configuration system to initialize Amazon Web Services (AWS) services, specifically focusing on the Elastic Compute Cloud (EC2). The application is designed to manage AWS service configurations and authenticate using access credentials.

## Project Structure

```
aws-server-config
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── config
│   │   ├── __init__.py
│   │   └── aws_config.py
│   ├── services
│   │   ├── __init__.py
│   │   └── ec2_service.py
│   └── utils
│       ├── __init__.py
│       └── auth.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd aws-server-config
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure AWS credentials:**
   Create a `.env` file in the root directory and add your AWS access keys:
   ```
   AWS_ACCESS_KEY_ID=your_access_key_id
   AWS_SECRET_ACCESS_KEY=your_secret_access_key
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Features

- Load AWS service configurations from environment variables.
- Initialize and manage EC2 instances using the AWS SDK for Python (Boto3).
- Modular design with separate directories for configuration, services, and utilities.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.