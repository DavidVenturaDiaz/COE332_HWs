FROM centos:7.9.2009

RUN yum update -y
RUN yum install -y python3


RUN pip3 install -y --user flask
RUN pip3 install -y --user redis

COPY app.py /code/app.py

RUN docker run -d -p 6379:6435 -v $(pwd)/data:/data:rw --name=david-redis redis:6 --save 1 1

ENV PATH "/code:$PATH"
