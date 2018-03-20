# fasttext-server

![travis](https://travis-ci.org/dfederschmidt/fasttext-server.svg?branch=master)
[![Docker Automated build](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)](https://hub.docker.com/r/dfederschmidt/fasttext-server)

Deploy your [FastText](https://fasttext.cc/) models as a [RESTful](https://en.wikipedia.org/wiki/Representational_state_transfer) [Microservice](https://www.martinfowler.com/articles/microservices.html) with ease.

**Disclaimer:** Still very much work in progress. Some things in here might not be implemented yet but I'm abusing this README as a design document for now.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Depending on your setup, you will need a recent version of Python and
You'll need [pipenv](https://github.com/pypa/pipenv) installed. It's the recommended packaging tool
from [python.org](python.org) - it's pretty cool. Otherwise, if you plan on running your service in a containerized
environment you'll need a Docker host.

### Installation 

The server is distributed over pip.

```bash
pip install fasttext-server
```

**OR**

You can get pre-build images from hub.docker.com

```bash
docker pull dfederschmidt/fasttext-server:latest
```

### Quick Start

If you just want to see it running you can run it with a bundled model. 

```
python -m fasttext-server --quickstart
```

If you have your own model ready you could run with

```
python -m fasttext-server $MODEL_PATH
```

where `$MODEL_PATH` is a path to a FastText model (`.bin` or `.ftz`).


## Authors

* **Daniel Federschmidt** - [federschmidt.xyz](https://federschmidt.xyz)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details