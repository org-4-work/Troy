import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def get_tokenized(text):
    # Function to check if a word is a named entity
    def is_named_entity(pos):
        return pos[:2] == 'NNP'  # NNP represents proper nouns
    # Function to check if a word is a noun
    def is_noun(pos):
        return pos[:2] == 'NN'
    # Function to check if a word is a verb
    def is_verb(pos):
        return pos[:2] == 'VB'
    # Function to check if a word is an adjective
    def is_adjective(pos):
        return pos[:2] == 'JJ'

    # Function to check if a word is an adverb
    def is_adverb(pos):
        return pos[:2] == 'RB'
    # Tokenize the sentences
    sentences = nltk.sent_tokenize(text)

    # Tokenize each sentence into words and flatten the list
    tokens = [word for sent in sentences for word in nltk.tokenize.word_tokenize(sent)]

    # Perform part-of-speech tagging
    pos_tags = nltk.pos_tag(tokens)

    # Perform named entity recognition
    ne_chunks = nltk.ne_chunk(pos_tags)
    named_entities = [chunk.leaves()[0][0] for chunk in ne_chunks if isinstance(chunk, nltk.Tree) and is_named_entity(chunk.label())]

    print("Named Entities:", named_entities)
    # Extract nouns and verbs from the tagged tokens
    nouns = [word for (word, pos) in pos_tags if is_noun(pos)]
    verbs = [word for (word, pos) in pos_tags if is_verb(pos)]
    adjectives = [word for (word, pos) in pos_tags if is_adjective(pos)]
    adverbs = [word for (word, pos) in pos_tags if is_adverb(pos)]
    print("Nouns:", nouns,len(nouns))
    print("Verbs:", verbs,len(verbs))
    print("Adjectives:", adjectives,len(adjectives))
    print("Adverbs:", adverbs,len(adverbs))



text = "# Ongoing fee amounts are calculated based on annualized asset management fees and total operating expenses in the interim financial statements for the six-month period ended September 7, 2021, and are presented as a percentage of the share class's estimated average net asset value for the same period Show."
get_tokenized(text)