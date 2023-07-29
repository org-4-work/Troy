from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F
from .utils.numbers_utils import numbers_matching_score
from .sbert_model import SBertModelClass

class BertModelClass:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('shibing624/text2vec-base-chinese')
        self.model = BertModel.from_pretrained('shibing624/text2vec-base-chinese')
        self.sbert = SBertModelClass()
    
    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    
    def cosine_similarity(self, embedding1, embedding2):
        cos_sim = F.cosine_similarity(embedding1, embedding2)
        return cos_sim.item()

    def get_scores_sentence(self, sentences):
        # Tokenize sentences
        encoded_input = self.tokenizer(sentences, padding=True, truncation=True, max_length=512, return_tensors='pt')


        with torch.no_grad():
            model_output = self.model(**encoded_input)

        sentence_embeddings = self.mean_pooling(model_output, encoded_input['attention_mask'])

        embeddings_array = sentence_embeddings
        embedding1 = embeddings_array[0].unsqueeze(0)
        embeddings_array = embeddings_array[1:]

        similarity_scores =[]
        for index, embedding2 in enumerate(embeddings_array):
            similarity_score = self.cosine_similarity(embedding1, embedding2.unsqueeze(0))
            similarity_scores.append(similarity_score)
        return similarity_scores
            
    
    def sort_paragraphs(self, doc2_paragraphs_chinese, ai_translated_paragraphs, window_size=15):
        
        chinise_sorted_paragraphs = []
        translation_accuracy = []
        number_matching_scores = []
        for i, p in enumerate(ai_translated_paragraphs):
            sentences = [p] + doc2_paragraphs_chinese[i:i+window_size]
            best_scores = self.get_scores_sentence(sentences)
            sbert_best_scores = self.sbert.get_best_score_sentence(sentences)
            sum_scores = list(map(sum, zip(best_scores, sbert_best_scores)))         
            best_score = max(sum_scores)
            index = sum_scores.index(max(sum_scores))
            chinise_sorted_paragraphs.append(doc2_paragraphs_chinese[i+index])
            translation_accuracy.append(best_score)  
            number_matching_scores.append(numbers_matching_score(ai_translated_paragraphs[i], doc2_paragraphs_chinese[i+index]) )
        return chinise_sorted_paragraphs, translation_accuracy, number_matching_scores
