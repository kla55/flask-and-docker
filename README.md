# flask-and-docker
Purpose 
# ML Model Deployment with Flask & Docker

## Overview
This project demonstrates how to deploy a **machine learning model** using **Flask** as an API, containerized with **Docker**.

## Features
- **Flask API** for real-time predictions
- **Dockerized** for easy deployment
- **Scikit-learn model** for inference

## Prerequisites
Ensure you have the following installed:
- [Python 3.9+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)


### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model
Run the training script to generate the model file:
```bash
python train_model.py
```

## Running the Flask App
### 4️⃣ Run Locally (Without Docker)
```bash
python app.py
```
**Access:** [http://localhost:5000](http://localhost:5000)

### 5️⃣ Run with Docker
#### **Build the Docker Image**
```bash
docker build -t ml-flask-app .
```

#### **Run the Docker Container**
```bash
docker run -p 5000:5000 ml-flask-app
```
**Access:** [http://localhost:5000](http://localhost:5000)

<!--
## API Endpoints
### **GET /health**
**Check API status**
```bash
curl http://localhost:5000/health
```
#### **Response**
```json
{"status": "ok"}
```

### **POST /predict**
**Make a prediction**
```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [1.5, 2.3, 3.1]}'
```
#### **Response Example**
```json
{"prediction": 1}
```
-->
## Debugging & Logs
- Check running containers:
  ```bash
  docker ps
  ```
- View container logs:
  ```bash
  docker logs <container_id>
  ```

## Deployment Options
- **Docker Compose:** Scale with `docker-compose.yml`
- **Kubernetes:** Deploy using `kubectl`
- **Cloud Services:** AWS, GCP, Azure


## Hints
1. When ready for the image - run code > docker build -t ml-flask-app . 
    1.1 'docker build' - Will instruct docker to build an image\
    1.2 '-t ml-flask-app' - Assign a tag -t to the image, naming it 'ml-flask-app'\
    1.3 '.' - Specifies the build context where the Dockerfile is located

2. To run the docker image with a new contain
    2.1 'docker run' - start a new container from an image\
    2.2 '-p 5000:5000' - Maps port 5000 on the host to port 5000 in the container\
    2.3 'ml-flask-app' - Specifies the DOcker image to use

3. Will be able to access the Flask app by visiting the designated port

4. Debugging keywords:
    4.1 'docker run -it --rm ml-flask-app /bin/bash' - Run an interactive shell inside the container\
    4.2 'ls -lah /app/' checks inside the container if the file exists

5. Docker-compose --build: - used to build and start the docker container. It combines two operations:
    5.1 '--build': This flag forces Docker Compse to rebuild the image for the services defined in the docker-compose.yml file before starting the container. This is useful if you have made changes to yoru dockerfile and want to make sure the latest changes are reflected in the containers.\
    5.2 'docker-compose up': This command starts all the services defined in your yml file. If the image for hte services don't exist, Docker Compose will build the image before starting the container. \
    5.3 Without --build: If you run docker-compose up without the --build flag, Docker Compose will use existing images (if they exist) and won’t rebuild them. If you’ve made changes to your Dockerfile or application code, you may not see those changes reflected unless you explicitly rebuild the images.

6. To run additional predictions via 'POST' call:
    6.1 - This should be done with 'curl' commands, but on windows PowerShell, the alternative command that must be used is ' Invoke-WebRequest'
    6.2 - The main request used is: "Invoke-WebRequest -Uri http://localhost:5000/predict -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"features": [6.1, 3.5, 5.4, 4.2]}'"
        6.2.1 - 'Invoke-WebRequest': The PowerShell command used to sent HTTP request.
        6.2.2 - '-Uri http://localhost:5000/predict': Specifies the target URL where the prediction request is sent. The Flask API must be running on this address for the request to work.
        6.2.3 - '-Method POST': Specifies that this is a 'POST' request, meaning we are sending data to the server. 
        6.2.4 - '-Headers @{"Content-Type"="application/json"}': Sets the request header to indicate that the data being sent is in JSON format
        6.2.5 - '-Body '{"features": [6.1, 3.5, 5.4, 4.2]}'': The request body containing the input features for the model. This should be formatted as JSON with a key called "features", followed by an array of numeric values representing the input data. 
    6.3 - After providing the request- you can see the results in the Docker logs as well as the run commands.



        

