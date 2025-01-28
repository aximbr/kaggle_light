# Use an official Python runtime as a parent image
FROM python:3.12
#FROM mcr.microsoft.com/azurelinux/base/python:3.12

## Pip dependencies
# Upgrade pip
RUN pip install --upgrade pip
# Install production dependencies

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt && \
  rm /tmp/requirements.txt

# Install Jupyter Notebook
RUN pip install jupyter

# Define environment variable

