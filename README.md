# fasttext-server

![travis](https://travis-ci.org/dfederschmidt/fasttext-server.svg?branch=master)
[![Documentation Status](https://readthedocs.org/projects/fasttext-server/badge/?version=latest)](http://fasttext-server.readthedocs.io/en/latest/?badge=latest)
[![Docker Automated build](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)](https://hub.docker.com/r/dfederschmidt/fasttext-server)

Deploy your [FastText](https://fasttext.cc/) models as a [microservice](https://www.martinfowler.com/articles/microservices.html) with ease.

## Getting Started

These instructions will get you up and running with fasttext-server.

### Prerequisites

* Python 3 (see [here for instructions](http://docs.python-guide.org/en/latest/starting/installation/))
* FastText for Python (see [here for instructions](https://github.com/facebookresearch/fastText#building-fasttext-for-python))


### Installation 

```bash
pip install fasttext-server
```

**OR**

You can get pre-build images from [hub.docker.com](https://hub.docker.com/r/dfederschmidt/fasttext-server/).

```bash
docker pull dfederschmidt/fasttext-server:latest
```

### Quick Start

```
python -m ft_server $MODEL_PATH
```

where `$MODEL_PATH` is a path to a FastText model (`.bin` or `.ftz`). You can find a 
selection of pre-trained models on the [FastText homepage](https://fasttext.cc/docs/en/english-vectors.html).


## Authors

* **Daniel Federschmidt** - [federschmidt.xyz](https://federschmidt.xyz)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details