from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

# default return type is a list
langs_list = GoogleTranslator().get_supported_languages() 
text = "# The ongoing charges figure is based on the total asset management fee and operating expenses in accordance with the interim financial statement for the 6-month period ended 7 September 2021 and is expressed as a percentage of the average net asset value of the share class over the same period. This figure may vary from year to year."
translated = GoogleTranslator(source='auto', target='zh-TW').translate(text=text)
print(translated)

def translate2eng(text):
    pass