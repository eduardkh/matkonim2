ARG Image_Name=python
ARG Image_Tag=slim-buster
FROM $Image_Name:$Image_Tag
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . .
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
