# Simple Flask based Web app

A simple "Hello, World!" flask framework based python app. It has been containerised to work independently without having to go through any setup steps.

The `Dockerfile` contains all the configuration steps.

## To build and run the containerised app follow the commands:
- Run `docker build <path to Dockerfile> -t <name for your docker image>`. This will build the image for the web server serving the web app.
- Run `docker run -p 5000:5000 -d <name for your docker image>`. This will run the conatiner in the background and map the servers 5000 port to the host.
- Test by visiting `http://<HOST IP>:5000` to see the app running.
