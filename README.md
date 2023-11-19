EasyFlashcards is an easy to use web application that creates usable flashcards from a given text. The flashcards are then provided as txt-file that you can import to your local Anki-App and you can start learning!

The project is split up into a python backend part (folder: backend) and a Next.js web interface (easy-flashcards).

## Run the Project

To run the project, you need to setup the backend api and run the web app.

### Backend

Go to ``backend/config.py`` and specify your api tokens:

```python
os.environ["HUGGINGFACEHUB_API_TOKEN"] = # Your Token
os.environ["OPENAI_API_KEY"] = # Your Token
```

Next, open the project in a terminal and go to the ``backend``-folder. 
Create a virtual environment and install all the necessary dependencies.

```bash
# create environment
python3 -m venv .env
# start environment
source .env/bin/activate
# install dependancies
pip install -r requirements.py
```

Now the backend is ready and you can simply run ``python api.py``. The backend api should start on your [http://localhost:5000](http://localhost:5000)

For a test, you can send an example request:

```bash
curl --request GET \
  --url 'http://localhost:5000/?key=5HA374PKTeDpEf7HXGNAz4qL9Vg9Ay246T4r25qY&text=A%20flashcard%20or%20flash%20card%20(also%20known%20as%20an%20index%20card)%20is%20a%20card%20bearing%20information%20on%20both%20sides%2C%20which%20is%20intended%20to%20be%20used%20as%20an%20aid%20in%20memorization.'
```

### Frontend

Got into the directory ``easy-flashcards`` and run ```npm run dev```

Open [http://localhost:5000](http://localhost:5000) with your browser to see the result.

