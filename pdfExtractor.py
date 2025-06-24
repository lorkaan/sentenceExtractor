from pdfminer.high_level import extract_text
from extractor import SentenceExtractor

class PDFSentenceExtractor(SentenceExtractor):

    valid_ext = ["pdf"]

    @classmethod
    def extractText(cls, filename):
        return extract_text(filename)

if __name__ == '__main__':
    filename = "/home/darthkaan/Documents/CCM_Maintenance_Contract.pdf"

    text = PDFSentenceExtractor.extract(filename)
    for s in text:
        print(s)
    print(len(text))