from flask import Flask, request, jsonify, Response, send_file
import langchain
from langchain.llms import openai

API_KEY = "5HA374PKTeDpEf7HXGNAz4qL9Vg9Ay246T4r25qY"

app = Flask(__name__)

def is_valid_api_key(key: str, api_key: str=API_KEY):
    if key == api_key:
        return True
    return False

@app.route("/")
def get_all_isins_route():
    # get all keys and their params
    api_key = request.args.get("key")

    # check for valid api key
    if api_key is None:
        return Response("Error 400<br>API key not specified.", status=400)
    if not is_valid_api_key(api_key):
        return Response("Error 403<br>Invalid API key.", status=403)


    return jsonify({"Hello": "World"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)