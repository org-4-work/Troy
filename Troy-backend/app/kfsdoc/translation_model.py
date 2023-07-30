from typing import List
import pandas as pd
from googletrans import Translator as GoogleTranslator
from deep_translator import (GoogleTranslator)
from .utils.text_utils import replace_special_chars_in_list

class Translator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.translator = GoogleTranslator(source='auto', target='zh-TW')

    def translate(self, texts):
        texts = replace_special_chars_in_list(texts, lang='zh')
        translations = []
        for text in texts:
            try:
                translated_text = self.translator.translate(text)
                translations.append(translated_text)
            except Exception as e:
                print(f"Error translating: {e}")
                translations.append("")  # append empty string on exception
        return translations
    
