# Bulletin board

This work represents the server part of the classifieds site.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have installed:

- Python (version 3.8 and up)
- Pip
- Virtualenv

### Installation

Clone the repository and activate the virtual environment:

git clone https://github.com/RomanKondratiuk/Bulletin_board.git
cd Bulletin_board
virtualenv venv
source venv/bin/activate

Install the dependencies:

pip install -r requirements.txt

### Configuration

Copy the `.env.sample` file to a new `.env` file and configure the environment variables:

cp .env.sample .env

### Running

Start the local server:

python manage.py runserver

## Usage

After starting the server, you can use the API according to the documentation of endpoints. The application provides the following main features:

- User registration and authentication.
- Creating, viewing, editing, and deleting ads and comments.

## Testing

Run tests to ensure the application functions correctly:

python manage.py test

## Deployment

Follow the standard procedure for deploying Django projects for production deployment.

## Built With

- Django & DRF for the backend.
- Docker for containerization and deployment.

