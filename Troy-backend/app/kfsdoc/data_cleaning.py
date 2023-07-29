
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from translation_model import Translator


class ParagraphComparator:
    def __init__(self, doc1_paragraphs, doc2_paragraphs):
        self.doc1_paragraphs = doc1_paragraphs
        self.doc2_paragraphs = doc2_paragraphs

    def sliding_window_similarity(self, texts1, texts2, window_size):
        model = SentenceTransformer("bert-base-nli-mean-tokens")
        embeddings1 = model.encode(texts1)
        embeddings2 = model.encode(texts2)

        similarity_scores = cosine_similarity(embeddings1, embeddings2)

        sorted_paragraphs = []
        for i in range(len(texts2) - window_size + 1):
            window_similarities = similarity_scores[:, i : i + window_size]
            avg_similarities = window_similarities.mean(axis=1)
            sorted_indices = avg_similarities.argsort()[::-1]
            sorted_paragraphs.extend([texts2[idx + i] for idx in sorted_indices])

        return sorted_paragraphs

    def compare_paragraphs(self, window_size):
        translator = Translator()
        translated_doc1_paragraphs = translator.translate(self.doc1_paragraphs)
        sorted_doc2_paragraphs = self.sliding_window_similarity(translated_doc1_paragraphs, self.doc2_paragraphs, window_size)
        
        result_df = pd.DataFrame({
            'doc1_paragraph': translated_doc1_paragraphs,
            'sorted_doc2_paragraphs': sorted_doc2_paragraphs,
        })

        return result_df
