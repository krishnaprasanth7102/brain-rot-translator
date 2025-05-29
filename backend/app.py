from flask_cors import CORS
from flask import Flask, request, jsonify
from textblob import TextBlob
import nltk
nltk.download('punkt')

app = Flask(__name__)
CORS(app)

# Example slang dictionary for replacement
slang_dict = {
    "brb": "be right back",
    "lol": "laughing out loud",
    "idk": "I don't know",
    "u": "you",
    "lol": "laugh out loud",  
"omg": "oh my god",  
"btw": "by the way",  
"idk": "i don't know",  
"tbh": "to be honest",  
"smh": "shaking my head",  
"irl": "in real life",  
"jk": "just kidding",  
"np": "no problem",  
"thx": "thanks",  
"ty": "thank you",  
"yw": "you're welcome",  
"gg": "good game",  
"gl": "good luck",  
"hf": "have fun",  
"imo": "in my opinion",  
"imho": "in my humble opinion",  
"afaik": "as far as i know",  
"icymi": "in case you missed it",  
"fyi": "for your information",  
"tmi": "too much information",  
"nvm": "nevermind",  
"ftw": "for the win",  
"fwiw": "for what it's worth",  
"ama": "ask me anything",  
"tl;dr": "too long; didn't read",  
"dm": "direct message",  
"pm": "private message",  
"nsfw": "not safe for work",  
"sfw": "safe for work",  
"otp": "one true pairing",  
"bff": "best friends forever",  
"rofl": "rolling on the floor laughing",  
"lmao": "laughing my ass off",  
"lmfao": "laughing my fucking ass off",  
"wtf": "what the fuck",  
"stfu": "shut the fuck up",  
"smfh": "shaking my fucking head",  
"fml": "fuck my life",  
"omw": "on my way",  
"rn": "right now",  
"asap": "as soon as possible",  
"eta": "estimated time of arrival",  
"atm": "at the moment",  
"ttyl": "talk to you later",  
"gtg": "got to go",  
"wyd": "what you doing",  
"wbu": "what about you",  
"hbu": "how about you",  
"ily": "i love you",  
"ily2": "i love you too", 
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
