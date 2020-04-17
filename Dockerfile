FROM python:3.6
WORKDIR /opt/promtempl
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . $WORKDIR

ENTRYPOINT ["python3", "src/promtempl/promserverlaunch.py"]
