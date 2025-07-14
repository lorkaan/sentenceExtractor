from dotenv import load_dotenv
import os

class EnvironVarLoader:

    @classmethod
    def isEnvKey(cls, key):
        return type(key) == str and len(key) > 0

    def __init__(self):
        load_dotenv()

    def get(self, key, errorVal=None):
        if self.__class__.isEnvKey(key):
            val = os.getenv(key, default=errorVal)
            if val == errorVal:
                raise KeyError(f"Can not find a value for the given key: {key}")
            else:
                return val
        else:
            raise TypeError(f"The Environment Key: {key} can not be used as a key")
