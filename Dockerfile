#specify your python version
FROM python:3.10
#define your working dir for the web app
WORKDIR /code
#copy requirements.txt into working dir
COPY ./requirements.txt /code/requirements.txt
#install all the needed and dependency packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#copy main.py into working dir
COPY ./main_app/main.py /code/

#  copy database.py into working dir
COPY ./main_app/database.py /code/

#  copy schema.py into working dir
COPY ./main_app/schema.py /code/

#  copy crud.py into working dir
COPY ./main_app/crud.py /code/

#  copy models.py into working dir
COPY ./main_app/models.py /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]