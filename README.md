
## As a docker compose app

run this to run the API

`docker compose up`

(so much easier...)

## When it was just a fastapi app with docker
run this to build image:

`docker build --pull -t py-fastapi-recipes .`

run this to run image

`docker run -d -p 8000:8000 py-fastapi-recipes`

run this to see logs

`docker logs [HASH OUTPUT FROM PREVIOUS COMMAND]`
