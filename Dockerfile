# Base image
FROM ubuntu:latest

# Define environment variable
ENV VERSION=1.2.0

WORKDIR /app

# Install apps and delete package manager metadata
RUN apt-get update && apt-get install -y python3 vim zip unzip && rm -rf /var/lib/apt/lists/*

# Copy zip_job file
COPY zip_job.py /tmp/

# Run command on container startup to print OS type and arch and list /tmp folder
ENTRYPOINT echo "OS type: $(uname -s), Architecture: $(uname -m)" && ls -l /tmp/zip_job.py && /bin/bash
CMD []

