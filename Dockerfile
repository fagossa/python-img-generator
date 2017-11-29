FROM python:2.7

VOLUME ["images"]

WORKDIR /images

ADD content/* ./

CMD [ "/bin/bash" ]
