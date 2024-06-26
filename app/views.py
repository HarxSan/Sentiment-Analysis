from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import json

# Load pre-trained RoBERTa model and tokenizer
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def index(request):
    return render(request, 'index.html')

def sentiment_analysis(request):
    if request.method == 'POST':
        txt = request.POST.get('txt')

        encoded_text = tokenizer(txt, return_tensors='pt')
        
        # Perform sentiment analysis using the pre-trained model
        output = model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        # Create a dictionary to store sentiment scores and input text
        scores_dict = {
            'neg': scores[0],
            'neu': scores[1],
            'pos': scores[2],
            'txt': json.dumps(txt),
        }

        return render(request, 'index.html', scores_dict)