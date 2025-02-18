# flask-and-docker
Hints

Purpose 
1. When ready for the image - run code > docker build -t ml-flask-app . 
    1.1 'docker build' - Will instruct docker to build an image
    1.2 '-t ml-flask-app' - Assign a tag -t to the image, naming it 'ml-flask-app'
    1.3 '.' - Specifies the build context where the Dockerfile is located

2. To run the docker image with a new contain
    2.1 'docker run' - start a new container from an image
    2.2 '-p 5000:5000' - Maps port 5000 on the host to port 5000 in the container
    2.3 'ml-flask-app' - Specifies the DOcker image to use

3. Will be able to access the Flask app by visiting the designated port

