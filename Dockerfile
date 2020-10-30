#Install condas, setup condas env & install dependencies
#FROM continuumio/miniconda3
FROM python:3.8.0-buster
RUN pip install --upgrade pip

#Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#Activate env
RUN echo "REQUIREMENTS INSTALLED!"

#Copy source code
COPY . .

#Run application
CMD ["python", "application.py"]

RUN echo "DOCKER IMAGE BUILT SUCCESSFULLY"