import urllib.parse
import urllib.request

def get_response(sentence):
  sentence_quoted = urllib.parse.quote(sentence)
  request_url = "http://127.0.0.1:5000/path/" + sentence_quoted
  result = ""
  with urllib.request.urlopen(request_url) as f:
    result = f.read(300)
  return result

