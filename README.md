Here's a clean and helpful `README.md` file for your **Brain Rot Translator** project that explains setup, usage, and troubleshooting:

---

```markdown
# 🧠 Brain Rot Translator

**Brain Rot Translator** is a simple Chrome extension + Flask API that automatically translates internet slang (brain rot text) into formal English on websites you visit.

---

## 🚀 Features

- Detects slang like “brb”, “lol”, “u r” and translates it to formal language.
- Works on any website you visit.
- Translated text appears *italicized* for clarity.
- Built with:
  - 🧠 Python + Flask (backend)
  - 🌐 JavaScript + Chrome Extension (frontend)
  - 🧰 NLTK for text processing

---

## 📁 Project Structure

```

brain-rot-translator/
│
├── backend/
│   ├── app.py               # Flask backend
│   └── requirements.txt     # Dependencies
│
├── extension/
│   ├── manifest.json        # Chrome extension config
│   ├── content.js           # Main logic for replacing slang
│   └── test.html            # Sample HTML page to test locally
│
└── README.md

````

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/brain-rot-translator.git
cd brain-rot-translator
````

---

### 2. Backend Setup (Flask)

```bash
cd backend
pip install -r requirements.txt
```

#### 📦 Requirements (`requirements.txt`)

```
flask
flask-cors
nltk
```

#### 🧠 Start the Flask server

```bash
python app.py
```

The server should now be running at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

✅ Make sure CORS is enabled:

```python
from flask_cors import CORS
CORS(app)
```

---

### 3. Frontend Setup (Chrome Extension)

1. Open **Chrome** and go to `chrome://extensions`
2. Enable **Developer Mode**
3. Click **“Load Unpacked”**
4. Select the `extension/` folder
5. Open any website (or `test.html` from local) to see it in action!

---

## 🌐 Testing on a Sample Page

You can use the included `test.html`:

```bash
cd extension
start test.html
```

Paste slang like:

```html
<p>brb lol u r amazing</p>
```

The extension will translate it to:

```html
<p><i>be right back laugh out loud you are amazing</i></p>
```

---

## 🧪 API Usage (Optional)

You can also call the API manually:

```bash
curl -X POST http://127.0.0.1:5000/translate \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"lol brb u r cool\"}"
```

---

## 🐛 Troubleshooting

* ❌ `CORS policy error`: Make sure you added `CORS(app)` in `app.py`
* ❌ `TypeError: Failed to fetch`: Check if Flask server is running at `localhost:5000`
* ❌ Nothing changes on page: Ensure Chrome extension is loaded and enabled

---

## 📜 License

MIT License. Use, modify, or contribute freely.

---

## 👤 Author

Made with 🧠 by \[Your Name]

```

Let me know if you'd like the markdown exported as a `.md` file or zipped with your project.
```
