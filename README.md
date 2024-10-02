# Project Title

A fully functional website for a band built using Django. It features a homepage showcasing the band’s latest news, an about section, a contact page, a blog for posts, and user authentication for fans to log in and register.

## Table of Contents

- [Installation](#installation)
- [Running the Project with Docker](#running-the-project-with-docker)
- [Usage](#usage)
- [Credits](#credits)

## Installation

1. Clone the repository:
   git clone https://github.com/w0ngky/Consolidation/

2. Navigate to the project directory:
    cd Consolidation

3. Set up a virtual environment:
    python -m venv venv

4. Activate the virtual environment:
    venv\Scripts\activate

5. Install the required packages:
    pip install -r requirements.txt

## Running the Project with Docker

1. Ensure you have Docker installed.

2. Clone the repository:
    git clone https://github.com/w0ngky/Consolidation/
    cd Consolidation

3. Build the Docker image:
    docker build -t band-website .

4. Run the Docker container:
    docker run -p 8000:8000 band-website

5. Open your web browser and navigate to http://127.0.0.1:8000/ to access the website.

## Usage

This Django website is designed for a band and includes the following features:

- **Home**: The main landing page that showcases the band’s latest news and upcoming shows.
- **About**: A section that provides information about the band.
- **Contact**: A page where fans can reach out to the band for inquiries or bookings.
- **Blog**: A blog section to keep fans updated with the latest posts and news.
- **Login**: A feature that allows users to log into their accounts.
- **Register**: A page for new users to create an account and stay connected with the band.

To run the project locally:

1. Start the development server:
   python manage.py runserver

2. Open your web browser and navigate to http://127.0.0.1:8000/ to access the website.

## Credits
Contributor: Kyle Wong
