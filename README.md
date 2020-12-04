# Assignment-Assist
Built to help student with assignments. A python based system that asks your query and its type(Wikipedia, Wolfram Alpha or Online Search) and returns the result. An option of text-to-speech is also provided. 
### Before using please install the following python libraries-
```PySimpleGUI```

```wolframalpha```

```wikipedia```

```pyttsx3```


### Make sure to make a file named as ```keys.py``` in the same directory as the project and store these api-keys in that file.

1. Sign Up on [Wolfram Alpha](https://www.wolframalpha.com/) and head to the [API Section](https://products.wolframalpha.com/api/) and click on **Get API Access**. Create an app and get your app id. Store it as -

```app_id = 'your_api_key'```

2. Create account on [Zenserp](https://zenserp.com/) and get your api-key from there and store it as -

```headers = { 'apikey': 'your_api_key' }```

Run your assistant by using the following command-

```python AssignmentAssist.py```

or by just saying-

```AssignmentAssist.py```
