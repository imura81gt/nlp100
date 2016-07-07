FROM python:3.5-alpine
MAINTAINER imura_takashi <imura_takashi@kakaku.com>

WORKDIR /tmp/mecab

# alpine-update & packages
RUN \
  apk --update add --virtual build-dependencies \
  openssl \
  gcc \
  g++ \
  make \
  file \
  git \
  bash \
  curl \
  perl &&\
  apk add ca-certificates &&\
  update-ca-certificates

# mecab
RUN \
  wget -O mecab-0.996.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE" &&\
  tar xvfp mecab-0.996.tar.gz &&\
  cd mecab-0.996 &&\
  ./configure &&\
  make &&\
  make check &&\
  make install
  

# mecab-ipadic
RUN \
  wget -O mecab-ipadic-2.7.0-20070801.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM" &&\
  tar xvfp mecab-ipadic-2.7.0-20070801.tar.gz &&\
  cd mecab-ipadic-2.7.0-20070801 &&\
  ./configure --with-charset=utf8 &&\
  make &&\
  make install


# mecab-ipadic-neologd 
RUN \
  git clone https://github.com/neologd/mecab-ipadic-neologd.git &&\
  cd mecab-ipadic-neologd/ &&\
  ./bin/install-mecab-ipadic-neologd -y -u

ENTRYPOINT "mecab"

