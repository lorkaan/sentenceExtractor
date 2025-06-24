from docxExtractor import DocxSentenceExtractor
from pdfExtractor import PDFSentenceExtractor
from extractor import SentenceExtractor
import os

class FileRouter:

    router = {
        "docx": DocxSentenceExtractor,
        "pdf": PDFSentenceExtractor
    }

    upload_folder_path = "uploads"
    
    @classmethod
    def getExt(cls, filename):
        filename_parts = filename.split(".")
        if len(filename_parts) > 1:
            ext = filename_parts[-1]
            if type(ext) == str and len(str) > 0:
                return ext
            else:
                return None
        else:
            return None

    @classmethod
    def run(cls, file):
        os.makedirs(cls.upload_folder_path, exist_ok=True)
        fileExt = cls.getExt(file.filename)
        if fileExt == None:
            return []
        else:
            filepath = os.path.join(cls.upload_folder_path, file.filename)
            file.save(filepath)
            extractorCls = cls.router.get(fileExt, None)
            if issubclass(extractorCls, SentenceExtractor):
                return extractorCls.extract(filepath)
            else:
                return []