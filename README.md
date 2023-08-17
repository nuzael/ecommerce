# Ecommerce
This repository contains an ecommerce project built in Django. The process to run the project on your local machine is detailed below.

## Project Description
The project is an ecommerce system developed using the Django backend framework to manage system logic and data manipulation. The frontend is developed using the Bootstrap framework, providing an attractive and responsive interface. Whitenoise is used to serve static files, enhancing the efficiency and performance of the application. Additionally, the use of Docker simplifies the setup and deployment process of the project.

## Configuration
Follow the steps below to configure and run the project locally:

### Clone the repository:
```bash
git clone https://github.com/nuzael/ecommerce.git
cd ecommerce
```

### Install Docker:
Ensure you have Docker installed on your machine. You can download it from: https://www.docker.com/get-started

### Configure environment variables:
Rename the `.env.example` file to `.env`, the `.env.dev.example` file to `.env.dev`, and fill in the required information.

### Build and run the containers:
```bash
docker compose -f docker-compose.yml up -d --build
```

### Collect the static files:
```bash
docker compose exec web python collectstatic
```

### Apply database migrations:
```bash
docker compose exec web python manage.py migrate --noinput
```

### Access the application:
Open your web browser and navigate to http://127.0.0.1:8000/ to see the application in action.

## Contribution
If you wish to contribute improvements to this project, feel free to create a pull request. Make sure to follow development best practices and document the changes you make.

## License
This project is under the MIT license. Refer to the LICENSE file for more information.
