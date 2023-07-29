from sentence_transformers import SentenceTransformer, util

class SBertModelClass:
    def __init__(self):
        self.model = SentenceTransformer("uer/sbert-base-chinese-nli")
    
    def get_sentence_embeddings(self, sentences):
        # Encode sentences to get sentence embeddings
        sentence_embeddings = self.model.encode(sentences, convert_to_tensor=True)
        return sentence_embeddings

    def cosine_similarity(self, embedding1, embedding2):
        cos_sim = util.pytorch_cos_sim(embedding1, embedding2)
        return cos_sim.item()

    def get_best_score_sentence(self, sentences):
        # Get sentence embeddings
        sentence_embeddings = self.get_sentence_embeddings(sentences)

        embedding1 = sentence_embeddings[0].unsqueeze(0)
        embeddings_array = sentence_embeddings[1:]
        scores_similarity = []
        for index, embedding2 in enumerate(embeddings_array):
            similarity_score = self.cosine_similarity(embedding1, embedding2.unsqueeze(0))
            scores_similarity.append(similarity_score)
        return scores_similarity
""" max(scores_similarity), scores_similarity.index(max(scores_similarity))"""
