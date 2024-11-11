# Fetch Rewards Receipt Processor

## In this ReadMe:

- [About this project](#about-this-project)
- [API Specification](#api-specification)
- [Rules for getting points](#rules-for-getting-points)
- [Tech Stack](#tech-stack)
- [Code snippets](#code-snippets)
- [Structure](#structure)
- [Setup and running instructions](#setup-and-running-instructions)
- [Demo](#demo)
- [About Author](#about-author)

# About this project 

In the US, Fetch Rewards has a large following of over 17 million active users. The platform lets people upload or scan receipts to collect points, which can then be traded in for gift cards or other exciting prizes.

This project aims to build a web service that processes receipts and calculates rewards in line with Fetch Rewards' 'Receipt Processor' task requirements, as specified in their API documentation. The original challenge was hosted on this repository:
[here](https://github.com/fetch-rewards/receipt-processor-challenge)

## API Specification

Endpoint: Process Receipts

- Path: /receipts/process
- Method: POST
- Payload: Receipt JSON
- Response: JSON containing an id for the receipt.

Example Response:
```
{ "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
```

Endpoint: Get Points

- Path: /receipts/{id}/points
- Method: GET
- Response: A JSON object containing the number of points awarded.


Example Response:
```
{ "points": 32 }
```

## Rules for getting points

The points are calculated based on the following rules:

1. One point for every alphanumeric character in the retailer name.
1. 50 points if the total is a round dollar amount with no cents.
1. 25 points if the total is a multiple of 0.25.
1. 5 points for every two items on the receipt.
1. If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
1. 6 points if the day in the purchase date is odd.
1. 10 points if the time of purchase is after 2:00pm and before 4:00pm.

## Example
```
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}
```

```
Expected result: 28 points
```

## Tech Stack

- **Backend**: Python, Flask, Pydantic, Pytest
- **Containerization**: Docker


## Structure

- **requirements.txt**: lists all the necessary Python packages and their versions required to run the Flask application.

- **Dockerfile**: defines the setup for a Docker container to host the Flask application.

## Setup and running instructions

1. Prerequisites:

- Ensure that you have [Docker](https://www.docker.com/) installed on your machine.
- Clone the project repository.

2.Build Docker Image:

- Navigate to the project directory where the Dockerfile and requirements.txt are located.
- Run the following command to build the Docker image:

```
docker build -t my-receipts-app .
```

3. Run Docker Container:

- Once the image is built, run the following command to start the container:

```
docker run -d -p 8080:5000 my-receipts-app
```

4. Accessing the Application:

- The application will now be running in a Docker container and is accessible at http://localhost:8080.
- You can now use the defined routes to process receipts and retrieve points: http://localhost:8080/receipts/process for processing receipts and http://localhost:8080/receipts/{id}/points for retrieving points.

5. Stop and Remove Docker Container:

- To stop the running container, first find the container ID with the following command:

```
docker ps
```

Then stop the container with:

```
docker stop <container-id>
```

6. Viewing Logs:

- To view the logs for the running container, use the following command:

```
docker logs <container-id>
```

## About Author


“Hi, I’m Piyush! As an experienced Software Engineer , I  specialize in functional and object-oriented programming, complex data modeling, and optimizing performance for distributed architectures. Skilled in troubleshooting large-scale production systems and communicating technical solutions effectively to non-technical teams. Proficient with high-level languages (Java, Python), databases (Postgres, MongoDB), and in-memory caching (Redis). Strong foundation in service-oriented and full-stack development, ensuring scalable and efficient solutions in cloud environments (GCP, AWS)."

 My [LinkedIn](https://www.linkedin.com/in/piyush-kanadje/)