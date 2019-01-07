# If necessary, change the tag from :py3 to :py3-cuda for cuda support
FROM ubuntu:18.04

# Install javascript dependencies
RUN apt-get update && apt-get install -y \
    npm python3-dev python3-pip

# Install openCV dependencies
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev

# Set up the app directory and install python dependencies
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Create the static directory and install js dependencies
WORKDIR /usr/src/app/static
COPY static/package.json /usr/src/app/static
RUN npm install

# Copy over the code and run build
COPY . /usr/src/app
RUN npm run build

# Run the app
WORKDIR /usr/src/app
EXPOSE 5000
CMD [ "python3", "./app.py" ]