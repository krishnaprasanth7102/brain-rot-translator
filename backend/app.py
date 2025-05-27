from flask import Flask, request, jsonify
from textblob import TextBlob
import nltk
nltk.download('punkt')

app = Flask(__name__)

# Example slang dictionary for replacement
slang_dict = {
    "brb": "be right back",
    "lol": "laughing out loud",
    "idk": "I don't know",
    "u": "you",
    "r": "are",
    "btw": "by the way",
    # add more slang mappings here
}

def replace_slang(text):
    words = text.split()
    replaced = [slang_dict.get(w.lower(), w) for w in words]
    return " ".join(replaced)

def correct_spelling(text):
    blob = TextBlob(text)
    corrected = str(blob.correct())
    return corrected

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    input_text = data.get('text', '')
    
    # Step 1: Replace slang
    slang_replaced = replace_slang(input_text)
    
    # Step 2: Correct spelling
    corrected_text = correct_spelling(slang_replaced)
    
    # TODO: Add more NLP steps like grammar fixing here
    
    return jsonify({'translated_text': corrected_text})

if __name__ == "__main__":
    app.run(debug=True)