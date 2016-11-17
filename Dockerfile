FROM ubuntu:14.04
MAINTAINER chet@chetcarello@hotmail.com
EXPOSE 27017

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list

RUN apt-get update
#RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get install -y mongodb-org

RUN mkdir -p /data/db

ADD . /app
WORKDIR /app
RUN pip install -r  requirements.txt

#CMD ["python", "db_build_v1.py"]

ENTRYPOINT ["/usr/bin/mongod"]
