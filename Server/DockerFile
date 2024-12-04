FROM python:3.12-bullseye
RUN apt update
RUN apt upgrade -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r req.txt
EXPOSE 8080
EXPOSE 8000
CMD [ "python", "server.py"]