from sentence_transformers import SentenceTransformer, util
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pickle

class BackendDialogue():
    def __init__(self):
        self.model = SentenceTransformer('roberta-model')
        self.COSINE_THRESHOLD = 0.5
        self.chitchat_bot = ChatBot("PanduBot")
        trainer = ChatterBotCorpusTrainer(self.chitchat_bot)
        trainer.train("chatterbot_corpus/data/english")
    
    def load_trained_model(self):
        encodings = {}
        with open('saved-models/mental.p', 'rb') as fp:
            encodings = pickle.load(fp)
        return encodings

    def get_answer(self, question):
        encodings = {}
        encodings = self.load_trained_model()
        query_encode = self.model.encode(question, convert_to_tensor = True)
        result = {}
        for i in encodings:
            sim = util.pytorch_cos_sim(query_encode, i)
            result[sim.item()] = encodings[i]
        final_result = sorted(result.items(), key=lambda x : x[0], reverse = True)
        confidence = final_result[0][0]
        if confidence > self.COSINE_THRESHOLD:
            answer = final_result[0][1]
        else:
            answer = self.chitchat_bot.get_response(question)
        print('the answer is: ' + str(answer))
        print("confidence: " + str(final_result[0][0]))
        return answer
