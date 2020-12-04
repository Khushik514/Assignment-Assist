import PySimpleGUI as sg
import wolframalpha
import wikipedia
import pyttsx3
import requests
import json
from keys import headers, app_id
engine = pyttsx3.init()


voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume',1.0)
engine.setProperty('rate', 150)

sg.theme("dark blue 2")
client = wolframalpha.Client(app_id)
layout = [[sg.Text("What's your query?")],
          [sg.InputText()],
          [sg.Text("Where do you want the result from?"),sg.Combo(['Online Search','Wikipedia', 'Wolfram Alpha'])],
          [sg.Text("Text-To-Speech"),sg.Combo(['Yes','No'])],
          [sg.Button('Search', bind_return_key = 'True'), sg.Button('Quit')]]

window = sg.Window('Assignment Assist', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    result = "Your Query is invalid"
    if values[1] == 'Wikipedia':
        try:
            result = wikipedia.summary(values[0], sentences=5)
        except:
            pass
    elif values[1] == 'Online Search':
        result = ""
        params = (
            ("q",values[0]),
            ("device","desktop"),
            ("location","Manhattan,New York,United States"),
        )
        resp = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
        response = resp.json()
        for res in response["organic"]:
            try:
                result = result + "\n" + res['description']
            except:
                pass
    else:
        try:
            res = client.query(values[0])
            result = next(res.results).text
        except:
            pass
    sg.popup_scrolled(result, title = "Results", non_blocking = True)
    if values[2] == 'Yes':
        engine.say(result)
        engine.runAndWait()

window.close()