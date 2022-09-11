FROM python:3.10-slim as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10-alpine

WORKDIR /admin_panel

COPY --from=requirements-stage /tmp/requirements.txt /admin_panel/requirements.txt

RUN pip install --upgrade pip

# https://github.com/python-pillow/Pillow/issues/1763 установка Pillow
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

RUN pip install --no-cache-dir --upgrade -r /admin_panel/requirements.txt

COPY /admin_panel/ /admin_panel
RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "./entrypoint.sh"]
