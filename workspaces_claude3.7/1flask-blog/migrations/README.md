# Database Migrations for Flask Blog Application

This directory contains the migration scripts for the Flask Blog application. Migrations are used to manage changes to the database schema over time.

## Usage

To apply migrations, use the following command:

```
flask db upgrade
```

To create a new migration after making changes to the models, use:

```
flask db migrate -m "Description of changes"
```

## Important Notes

- Ensure that your database is properly configured in the application settings before running migrations.
- Always back up your database before applying migrations, especially in production environments.