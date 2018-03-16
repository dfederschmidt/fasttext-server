"""
.. module:: ft_server.server

"""

import json

import fastText
import os
from flask import Flask
from flask import g
from flask import jsonify
from flask import request

app = Flask(__name__)

if os.environ.get('FT_SERVER_ENV') == "development":
    app.config.from_object('config.DevelopmentConfig')
elif os.environ.get('FT_SERVER_ENV') == "test":
    app.config.from_object('config.TestConfig')
else:
    app.config.from_object('config.Config')

if os.environ.get('FT_SERVER_DOCKERIZED') == "True":
    app.config.from_object('config.DockerConfig')

if os.environ.get('FT_SERVER_SETTINGS'):
    app.config.from_envvar('FT_SERVER_SETTINGS')


@app.route("/")
def index():
    """Retrieve information about the deployed model."""
    model_args = g.ft_model.f.getArgs()

    res = {
        "lr": model_args.lr,
        "lrUpdateRate": model_args.lrUpdateRate,
        "epoch": model_args.epoch,
        "dim": model_args.dim,
        "ws": model_args.ws,
        "model": str(model_args.model)[len("model_name."):],
        "loss": str(model_args.loss)[len("loss_name."):],
        "wordNgrams": model_args.wordNgrams,
        "minCountLabel": model_args.minCountLabel,
        "label": model_args.label,
        "thread": model_args.thread,
        "bucket": model_args.bucket,
        "cutoff": model_args.cutoff,
        "t": model_args.t,
        "minn": model_args.minn,
        "maxn": model_args.maxn,
        "isQuant": g.ft_model.f.isQuant()
    }

    return jsonify(res)


@app.route("/words")
def words():
    """
      Get dictionary used for model training.

      Query String:
         * freq (bool):  Whether or not to return frequencies (default: False)

      Returns:
          A json array containing words and optionally their frequencies.
    """
    freq = bool(request.args.get('freq')) if request.args.get('freq') == "True" else False

    words, counts = g.ft_model.get_words(freq)
    res = [{"word": w, "count": int(c)} for w, c in zip(words, counts)]

    return jsonify(res)


@app.route("/predictions", methods=["GET"], endpoint="get_predictions")
def predictions():
    """
       Retrieve predictions for a single word or sentence from the deployed model.

       Query String:
          * q (str):  word or sentence to get a vector representation for.
          * k (int):  Number of most likely classes returned (default: 1)
          * threshold (float): Filter classes with a probability below threshold (default: 0.0)

       Returns:
           A json containing the vector representations.
    """

    k = int(request.args.get('k')) if request.args.get('k') else 1
    threshold = float(request.args.get('threshold')) if request.args.get('threshold') else 0.0

    query = request.args.get('q')
    res = make_prediction(query, k, threshold)

    return jsonify(res)


@app.route("/predictions", methods=["POST"], endpoint="post_predictions")
def predictions():
    """
       Retrieve predictions for words or sentences from the deployed model.

       Query String:
          * k (int):  Number of most likely classes returned (default: 1)
          * threshold (float): Filter classes with a probability below threshold (default: 0.0)
       Body:
          A json array of strings to get classifications.

       Returns:
           A json array containing the vector representations.
       """
    k = int(request.args.get('k')) if request.args.get('k') else 1
    threshold = float(request.args.get('threshold')) if request.args.get('threshold') else 0.0

    queries = json.loads(request.data)
    res = [make_prediction(el, k, threshold) for el in queries]

    return jsonify(res)


@app.route("/representations", methods=["GET"], endpoint="get_representations")
def representations():
    """
    Retrieve vector representations for a single word or sentence from the deployed model.

    Query String:
       q (str):  word or sentence to get a vector representation for.

    Returns:
        A json containing the vector representation and it's dimensionality.
    """
    query = request.args.get('q')
    res = retrieve_representation(query)

    return jsonify(res)


@app.route("/representations", methods=["POST"], endpoint="post_representations")
def representations():
    """
       Retrieve vector representations for a single word or sentence from the deployed model.

       Body:
          A json array of strings.

       Returns:
           A json array containing the vector representations.
       """
    queries = json.loads(request.data)
    res = [retrieve_representation(el) for el in queries]

    return jsonify(res)


@app.before_request
def before_request():
    g.ft_model = fastText.load_model(app.config["FT_SERVER_MODEL_PATH"])


def retrieve_representation(q):
    retrieval_method = g.ft_model.get_word_vector

    if len(q.split(" ")) > 1:
        retrieval_method = g.ft_model.get_sentence_vector

    res = {
        "q": q,
        "representation": retrieval_method(q).tolist(),
        "dim": len(retrieval_method(q))
    }

    return res


def make_prediction(q, k, threshold):
    labels, probas = g.ft_model.predict(q, k, threshold)

    return [{"label": l, "proba": p} for l, p in zip(labels, probas)]


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
