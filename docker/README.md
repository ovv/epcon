Built container
===============

`$ docker build . -t ep2018 -f docker/Dockerfile`

Run container
=============

`$ docker run -it -p 8000:8000 --env DEBUG=True ep2018 dev`
