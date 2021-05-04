import csv
import pickle
import string
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

class Training():
    def __init__(self):
        self.model = SentenceTransformer('roberta-model')
    
    def clean_text(self, text):
        #text = text.capitalize()
        text = text.replace('A:', '')
        text = text.replace('Answer:', '')
        text = text.replace('A: ', '')
        text = text.replace('A.', '')
        text = text.replace('\n', '')
        return text
    
    def read_csv(self):
        training_data = {}
        with open('training-data/mental_health_faqs.csv', 'r') as file:
            reader = csv.reader(file)
            print("reading the csv")
            for row in tqdm(reader):
                if row[1]:
                    training_data[row[0]] = self.clean_text(row[1])
        return training_data

    def train(self):
        training_data = {}
        encodings = {}
        training_data = self.read_csv()
        print("training started")
        for i in tqdm(training_data):
            t_encode = self.model.encode(i, convert_to_tensor = True)
            encodings[t_encode] = training_data[i]
        with open('saved-models/mental.p', 'wb') as fp:
             pickle.dump(encodings, fp, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    trainer = Training()
    trainer.train()