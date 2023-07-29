import jieba
import jieba.posseg as pseg
import jieba.analyse

text = "持續費用金額根據截至 2021 年 9 月 7 日止六個月期間的中期財務報表中的年化資產管理費和總運營費用計算，並以佔該股份類別預計平均資產淨值的百分比形式呈現 同期演出。"
# Use jieba to perform word segmentation
seg_list = jieba.cut(text, cut_all=False)

# Convert the segmented text into a list of words
word_list = list(seg_list)
print(word_list)
print(len(word_list))
# Tokenize the text

tokens = jieba.cut(text)
# Perform part-of-speech tagging
pos_tags = pseg.cut(text)

# Extract nouns, verbs, adjectives, and adverbs
nouns = []
verbs = []
adjectives = []
adverbs = []

for word, pos in pos_tags:
    if pos.startswith("n"):  # Noun
        nouns.append(word)
    elif pos.startswith("v"):  # Verb
        verbs.append(word)
    elif pos.startswith("a"):  # Adjective
        adjectives.append(word)
    elif pos.startswith("d"):  # Adverb
        adverbs.append(word)
print('\n')
print("Length",len(text))
print("Nouns:", nouns,(len(nouns)))
print("Verbs:", verbs,(len(verbs)))
print("Adjectives:", adjectives,(len(adjectives)))
print("Adverbs:", adverbs,(len(adverbs)))

# Extract named entities using TF-IDF algorithm
keywords = jieba.analyse.extract_tags(text, topK=5, withWeight=False, allowPOS=("nr", "ns", "nt", "nz"))

print("Named Entities:", keywords)
