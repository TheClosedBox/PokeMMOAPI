# Use an official Python runtime as the base image
FROM python:3.9-alpine3.15

# Set the working directory in the container
WORKDIR /app

# Copy the entire project to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --disable-pip-version-check -q -r requirements.txt

EXPOSE 5000
COPY . .
# Set the command to run when the container starts
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]