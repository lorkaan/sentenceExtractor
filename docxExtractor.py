from docx import Document
from extractor import SentenceExtractor

class DocxSentenceExtractor(SentenceExtractor):

    valid_ext = ["docx"]

    @classmethod
    def extractText(cls, filepath):
        try:
            doc = Document(filepath)
            full_text = []
            for para in doc.paragraphs:
                full_text.append(para.text)
            return '\n'.join(full_text)
        except Exception as e:
            return f"Error Reading DOCX file: {e}"
        
if __name__ == '__main__':
    filename = "/home/darthkaan/Documents/legal_whisperer/CCM_Maintenance_Contract_test.docx"

    text = DocxSentenceExtractor.extract(filename)

    for s in text:
        print(s)
    print(len(text))