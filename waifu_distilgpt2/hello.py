from flask import Flask
from transformers import *
import torch
import urllib
import urllib.parse

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelWithLMHead.from_pretrained("distilgpt2")

def predict_next_word(text):
  indexed_tokens = tokenizer.encode(text)
  tokens_tensor = torch.tensor([indexed_tokens])

  with torch.no_grad():
      outputs = model(tokens_tensor)
      predictions = outputs[0]

  # get the predicted next sub-word (in our case, the word 'man')
  predicted_index = torch.argmax(predictions[0, -1, :]).item()
  predicted_text = tokenizer.decode([predicted_index])
  return predicted_text

def predict_ten_words(text):
  tmp_text = text
  for i in range(30):
    word = predict_next_word(tmp_text)
    tmp_text += word
    if "." in tmp_text[len(text):]:
      break
    if '"' in tmp_text[len(text):]:
      break
  tmp_text = tmp_text[len(text):]
  return tmp_text

def clean_result(result):
  first_found = result.find('"')
  clean_result = result[:first_found]
  second_found = result.find('.')
  clean_result = result[:second_found]
  return clean_result

def predict_response(sentence):
  input_sentence = '\
You said: "Senko I missed you so much!" \
I said: "I missed you too Subaru!" \
You said: "Our date was so fun too" \
I said: "Lets get married and be happy!" \
You said: "Yes that would be awesome!" \
I said: "I like hanging out with you because its so much fun!" \
You said: "' + sentence + '" \
I said: "\
'
  predicted_response = predict_ten_words(input_sentence)
  predicted_response = clean_result(predicted_response)
  return predicted_response

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    subpath = urllib.parse.unquote(subpath)
    return '%s' % predict_response(subpath)
