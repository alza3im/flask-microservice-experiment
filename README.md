# Flask Microservice Experiment

This miniproject is just a simple experiment to implement microservices using Django and Flask's with RabbitMQ as the broker in a Microservices Architecture.

This repository represents the Flask Backend app of the project.

The project uses mysql database to store the User's info

Prerequisites: 

1.Install Docker and docker-compose
2.Make sure you create the databases (check the docker-compose file)

To run the project :

    $docker-compose build
    $docker-compose up

Use Postman to call the following endpoints
    
    localhost:8000/api/products
    localhost:8000/api/products/<id>
    localhost:8000/api/user
    
This project follows this \href{https://www.youtube.com/watch?v=0iB5IPoTDts}{tutorial} 
