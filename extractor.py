import re

class SentenceExtractor:
    """
        Class for handling sentence extraction from text
    """

    sentence_regex = r"[^.!?]+[.!?]"

    valid_ext = []

    @classmethod
    def check_file_type(cls, ext, filepath):
        return filepath.endswith(f".{ext}")

    @classmethod
    def getSentenceArray(cls, text):
        sentences = re.findall(cls.sentence_regex, text)
        sentences = [s.strip() for s in sentences]
        return sentences
    
    @classmethod
    def extractText(cls, filepath):
        return ""

    @classmethod
    def extractSentenceArray(cls, filepath):
        try:
            foundText = cls.extractText(filepath)
        except Exception as e:
            print(f"Exception Exctracting Text: {e}")
            foundText = None
        finally:
            if type(foundText) == str and len(foundText) > 0:
                return cls.getSentenceArray(foundText)
            else:
                return []
        
    @classmethod
    def extract(cls, filepath):
        for ext in cls.valid_ext:
            if cls.check_file_type(ext, filepath):
                return cls.extractSentenceArray(filepath)
            else:
                continue
        return []
