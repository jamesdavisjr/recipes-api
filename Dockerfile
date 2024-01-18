FROM python:3.10

WORKDIR /usr/src/app

RUN pip install --no-cache-dir fastapi
RUN pip install --no-cache-dir "uvicorn[standard]"

COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]
EXPOSE 8000

# For development, run these commands to:
#
# build: `docker build --pull -t py-fastapi-recipes .`
#
# run: `docker run -d -p 8000:8000 -v `pwd`:/usr/src/app -v recipe_pycache:/usr/src/app/__pycache__  py-fastapi-recipes`
#