import datetime
import re
import docx2txt
import pandas as pd
import datetime
from .bert_model import BertModelClass
from .translation_model import Translator
import spacy
import re

 
class Document:
    """
    Return a |Document| object loaded from *docx*.
    """

    def __init__(self, file_path):
        self.file_path = file_path    
        
    def read_docx(self):
        text = docx2txt.process(self.file_path)
        return text
    
    def is_sentence_empty(self, sentence):
        return all(char.isspace()  for char in sentence) or all(char=='\n'  for char in sentence)  or sentence is None or len(sentence) == 0
    
    def split_into_sentences(self, nlp, text):
        doc = nlp(text)
        sentences = [sent.text for sent in doc.sents]
        return self.split_text_to_sentences(sentences)
    
    
    def split_text_to_sentences(self, texts):
        r = []
        separators=r'[:：\n]'
        for paragraph in texts:
            a = re.split(separators, paragraph)
            a = [p.strip() for p in a if not self.is_sentence_empty(p)]
            r.extend(a)
        return r
    
def make_same_length(sentences_1, sentences_2):
    max_len = max(len(sentences_1), len(sentences_2))
    # Pad both lists with empty strings to match the length of the longer one
    sentences_1.extend([''] * (max_len - len(sentences_1)))
    sentences_2.extend([''] * (max_len - len(sentences_2)))
    return sentences_1, sentences_2




WINDOW_SIZE = 10
class KFSDocReviewer:
    nlp_en = spacy.load('en_core_web_sm')
    nlp_ch = spacy.load('zh_core_web_sm')

    
    def __init__(self, english_path, chinese_path):
        self.english_path = english_path
        self.chinese_path = chinese_path
        # Paragraph

 
    def validator(self):
        """
        Document Validator
        """
        if self.chinese_path and self.english_path:
            # if the document is 2 documents(one is chinese and another one is english)
            print("[+] Success : Valid Multi Document ")
        else :
            # Exceptional when read path failed
            print("[-] Error : Invalid Documents ")


    def initialize(self):
        """
        Reviewing system initialize
        """
        self.english_doc = Document(self.english_path)
        self.chinese_doc = Document(self.chinese_path)
        self.translator = Translator()
        self.bert = BertModelClass()
        
    
    def treat(self):
        chinese_sentences = self.chinese_doc.split_into_sentences(self.nlp_ch, self.chinese_doc.read_docx())
        english_sentences = self.english_doc.split_into_sentences(self.nlp_en, self.english_doc.read_docx())
        english_sentences, chinese_sentences = make_same_length(english_sentences, chinese_sentences)
        ai_translated_paragraphs = self.translator.translate(english_sentences)
        chinese_sentences = [item for item in chinese_sentences if item is not None]
        ai_translated_paragraphs = [item if item is not None else '' for item in ai_translated_paragraphs]
        english_sentences, ai_translated_paragraphs = make_same_length(english_sentences, ai_translated_paragraphs)
        english_sentences, ai_translated_paragraphs = make_same_length(english_sentences, ai_translated_paragraphs)
        chinise_sorted_paragraphs, translation_accuracy, number_matching_scores = self.bert.sort_paragraphs(chinese_sentences, ai_translated_paragraphs)

        return english_sentences, ai_translated_paragraphs, chinise_sorted_paragraphs, translation_accuracy, number_matching_scores

    