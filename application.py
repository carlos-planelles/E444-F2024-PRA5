from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)


@application.route("/")
def index():
    return "Your Flask App Works! V1.0"


@application.route("/is-fake", methods=["POST"])
def is_fake():
    data = request.get_json()

    docs = data["documents"]

    model, vectorizer = load_model()
    prediction = model.predict(vectorizer.transform(docs))

    return jsonify({"results": prediction})


def load_model():
    loaded_model = None
    with open("basic_classifier.pkl", "rb") as fid:
        loaded_model = pickle.load(fid)

    vectorizer = None
    with open("count_vectorizer.pkl", "rb") as vd:
        vectorizer = pickle.load(vd)

    return loaded_model, vectorizer


if __name__ == "__main__":
    application.run(port=5000, debug=True)
