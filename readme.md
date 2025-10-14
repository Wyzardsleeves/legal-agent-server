# Legal Agent Server (Legalese)

### Get Started


initialize venv
```
$ . .venv/bin/activate
```

Run app on localhost:5000 by default
```
$ flask run
```
## Environment variable
Create env file
```
$ touch .env
```

Set OpenAI Key in .env
```
$ echo Enter data here > .env
```

#### or

Paste it in app.py
```
 SECRET_KEY = os.getenv("DEEPSEEK_API_KEY") > SECRET_KEY = "OPENAI_API_KEY here"
```