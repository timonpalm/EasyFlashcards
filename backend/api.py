from flask import Flask, request, jsonify, Response, send_file
import langchain
from langchain.llms import openai
from backend.config import API_KEY
from llm_chain import Chain

app = Flask(__name__)
CHAIN = Chain()

def is_valid_api_key(key: str, api_key: str=API_KEY):
    if key == api_key:
        return True
    return False

@app.route("/", methods=["POST"])
def get_all_isins_route(chain=CHAIN):
    # get all keys and their params
    api_key = request.args.get("key")

    # check for valid api key
    if api_key is None:
        return Response("Error 400<br>API key not specified.", status=400)
    if not is_valid_api_key(api_key):
        return Response("Error 403<br>Invalid API key.", status=403)
    try:
        text = request.form.to_dict()["text"]
    except:
        return Response("Error 405<br>No text was given.", status=405)

    flashcards = chain.create_flashcards(text)

    return jsonify({"flashcards": flashcards})

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=False)