from flask import Flask, request, jsonify, Response, send_file
import langchain
from langchain.llms import openai
from config import API_KEY
from llm_chain import Chain

app = Flask(__name__)
CHAIN = Chain()

def is_valid_api_key(key: str, api_key: str=API_KEY):
    if key == api_key:
        return True
    return False

@app.route("/", methods=["GET"])
def get_all_isins_route_get(chain: Chain=CHAIN):
    """Prescesses a GET request to the API. Returns a JSON object with the flashcards.

    Args:
        chain (Chain, optional): Chain that is respnsible for creating the flashcards. Defaults to CHAIN.

    Returns:
        json: created flashcards
    """
    # get all keys and their params
    api_key = request.args.get("key")
    text = request.args.get("text")

    # check for valid api key
    if api_key is None:
        return Response("Error 400<br>API key not specified.", status=400)
    if not is_valid_api_key(api_key):
        return Response("Error 403<br>Invalid API key.", status=403)
    if text is None:
        return Response("Error 405<br>No text was given.", status=405)

    cards = chain.create_flashcards(text)

    response = jsonify({"flashcards": cards})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route("/", methods=["POST"])
def get_all_isins_route_post(chain: Chain=CHAIN):
    """Prescesses a POST request to the API. Returns a JSON object with the flashcards.

    Args:
        chain (Chain, optional): Chain that is respnsible for creating the flashcards. Defaults to CHAIN.

    Returns:
        json: created flashcards
    """
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

    cards = chain.create_flashcards(text)

    response = jsonify({"flashcards": cards})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=False)