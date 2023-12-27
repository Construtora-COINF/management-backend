FROM python:3.11-alpine

RUN apk update && apk add postgresql-dev tzdata && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
      apk add --no-cache \
      --virtual=.build-dependencies \
      gcc \
      g++ \
      musl-dev \
      git \
      python3-dev \
      jpeg-dev \
      zlib-dev \
      freetype-dev \
      lcms2-dev \
      openjpeg-dev \
      tiff-dev \
      tk-dev \
      tcl-dev \
      harfbuzz-dev \
      harfbuzz-dev \
      fribidi-dev && \
    apk del --purge .build-dependencies

ADD Pipfile Pipfile.lock ./

RUN pip install pipenv  &&\
    pipenv install --system --deploy --ignore-pipfile

ADD . .

RUN chmod +x ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]