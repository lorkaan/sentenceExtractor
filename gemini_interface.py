import requests

from read_env import EnvironVarLoader

class ApiValidationError(Exception):

    def __init__(self, message):
        super().__init__(message)

class GeminiInterface:

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    header_api_key = "X-goog-api-key"

    headers = {
        "Content-Type": "application/json", 
    }

    textResponseKeyArray = ["candidates", "content", "parts"]
    textListKey = "text"

    env_api_key = "API_KEY"

    envloader = EnvironVarLoader()

    @classmethod
    def access_prompt_return(cls, jsonData):
        data = jsonData
        for key in cls.textResponseKeyArray:
            data = data[key]
        textList = []
        for i in range(len(data)):
            textList.append(data[i].get(textList, None))
        return textList

    @classmethod
    def isApiKey(cls, key):
        return type(key) == str and len(key) > 0

    @classmethod
    def send(cls, api_key, prompt):
        if not cls.isApiKey(api_key):
            raise ApiValidationError(f"API Key: {api_key} is not valid")
        cur_headers = {}
        for key, val in cls.headers:
            cur_headers[key] = val
        cur_headers[cls.header_api_key] = api_key
        payload = {
            "contents": [
                {
                    "parts": prompt
                }
            ]
        }
        r = requests.post(cls.url, headers=cur_headers, data=payload)
        return r.json()
    
    @classmethod
    def parse_data(cls, jsonData):
        return cls.access_prompt_return(jsonData)
    
    @classmethod
    def getApiKey(cls):
        return cls.envloader.get(cls.env_api_key)

    @classmethod
    def run(cls, prompt):
        apiKey = cls.getApiKey()
        data = cls.send(apiKey, prompt)
        return cls.parse_data(data)
