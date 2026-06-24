# Flatiron Cars - Flask Routes Lab

A Flask web application for managing car model information with dynamic routing.

## Description

This application provides a simple API for querying car models in the Flatiron Cars fleet. It demonstrates Flask routing fundamentals including default routes and dynamic URL parameters.

## Features

- Welcome page at root route
- Dynamic model lookup by URL parameter
- Model availability checking against existing inventory

## Installation

```bash
pipenv install
pipenv shell
```

## Usage

Run the application:

```bash
python server/app.py
```

The server starts on `http://127.0.0.1:5000/` in debug mode.

### Available Routes

**GET /**
- Returns welcome message
- Response: `"Welcome to Flatiron Cars"`

**GET /<model>**
- Checks if model exists in fleet
- Response (if found): `"Flatiron {model} is in our fleet!"`
- Response (if not found): `"No models called {model} exists in our catalog"`

### Examples

```bash
curl http://127.0.0.1:5000/
# Welcome to Flatiron Cars

curl http://127.0.0.1:5000/Beedle
# Flatiron Beedle is in our fleet!

curl http://127.0.0.1:5000/Tesla
# No models called Tesla exists in our catalog
```

## Available Models

- Beedle
- Crossroads
- M2
- Panique

## Testing

Run the test suite:

```bash
pytest --disable-warnings -q
```

## Technologies

- Python 3.x
- Flask

## License

MIT
