# Flask Microservice Experiment

This miniproject is just a simple experiment to implement microservices using Django and Flask's with RabbitMQ as the broker in a Microservices Architecture.

This repository represents the Flask Backend app of the project.

The project uses mysql database to store the User's info

Prerequisites: 

1.Install Docker and docker-compose

2.Make sure you create the mysql database 'main' (check the docker-compose file)

To run the project :

    $docker-compose build
    $docker-compose up
    
To run db migrations :

    $docker-compose up exec backend sh 
    $python manage.py db init #to initialise 
    $python manage.py db migrate
    $python manage.py db upgrade

Use Postman to call the following endpoints
    
    GET localhost:8001/api/products
    POST localhost:8001/api/products/<id>/like
    

Checkout the [Django App](https://github.com/alza3im/django-microservice-admin)

This project follows this [tutorial](https://www.youtube.com/watch?v=0iB5IPoTDts)
