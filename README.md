# PsyBot: A question answering FAQ chatbot on mental health 

This is a FAQ chatbot trained on 1000 FAQs automatically extracted from the web on mental health. You can ask any question regarding mental health and psyBot will try to answer. A chit-chat feature is added using Chatterbot.

I have used state of the art sentence transformer models to encode queries and compute similarity. ROBERTA-LARGE is used. Flask is used to write the frontend.

Steps to run the Bot:
1. Install dependencies: You need to have Python 3 installed on your system. Go to the directory of the project and type the following on the shell:
```shell
pip install -r requirements.txt
```
2. Collect FAQs and put them on a CSV file. CSV files format will be like (question, answer). The training FAQs on mental health is uploaded under "training-data". You can collect your own FAQs and put the csv under this directory. Change the corresponding path in "training.py" line 22. To train and save the model run using:
```shell
python3 training.py
```
If you do not want to train, you can use my saved model which is under "saved-model". No steps are required if no training is required.
3. Run the frontend using:
```shell
python3 frontend.py
```
By default it will run on "http://127.0.0.1:5000/". Go to this link using any browser.

Enjoy!
