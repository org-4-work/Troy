import langid

def separate_languages(paragraph):
    sentences = paragraph.split('?')
    english_sentences = []
    chinese_sentences = []

    for sentence in sentences:
        lang = langid.classify(sentence)[0]
        if lang == 'en':
            english_sentences.append(sentence.strip())
        elif lang == 'zh':
            chinese_sentences.append(sentence.strip())

    english_text = ' '.join(english_sentences)
    chinese_text = ' '.join(chinese_sentences)

    return english_text, chinese_text


paragraph = "The Fund may invest in fixed income securities issued or guaranteed by governments, government agencies, quasi-government entities, state sponsored enterprises, local or regional governments (including state, provincial, and municipal governments and governmental entities) and supranational bodies of developed or Emerging Markets. 本基金可投資於由已發展或新興市場的政府、政府機構、半政府實體、國家支持企業、當地或地區政府（包括國家、省級及市級政府及政府實體）及超國家組織所發行或擔保的固定收益證券。"


english_text, chinese_text = separate_languages(paragraph)
print(english_text)
print('------')
print(chinese_text)