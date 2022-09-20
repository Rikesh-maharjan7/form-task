import requests

save ="https://anotepad.com/note/read/y3x6tq9j"
txt = "Hello World"
login = "https://anotepad.com/create_account"

data = {"action": "login",
        "email": "rikeshmhj9@gmail.com",
        "password": "11223344",
        "submit": ""}

# construct the POST request
with requests.session() as s: # Use a Session object.
    s.post(login, data) # Login.

    form_data = {"number": "y3x6tq9j",
                 "notetype": "PlainText",
                 "noteaccess": "2",
                 "notequickedit": "false",
                 "notetitle": "whatever",
                 "notecontent": txt}

    r = s.post(save, data=form_data) # Save note
    print(r.text)

