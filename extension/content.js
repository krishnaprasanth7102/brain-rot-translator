async function translateText(text) {
  try {
    const res = await fetch('http://localhost:5000/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    const data = await res.json();
    return data.translated_text;
  } catch (err) {
    console.error("Translation failed:", err);
    return text;
  }
}

function walkAndTranslate(node) {
  const skipTags = ['SCRIPT', 'STYLE', 'NOSCRIPT', 'IFRAME'];
  if (node.nodeType === Node.TEXT_NODE) {
    if (node.nodeValue.trim().length > 3) {
      translateText(node.nodeValue).then(translated => {
        if (translated && translated !== node.nodeValue) {
          node.nodeValue = translated;
        }
      });
    }
  } else if (node.nodeType === Node.ELEMENT_NODE && !skipTags.includes(node.tagName)) {
    node.childNodes.forEach(walkAndTranslate);
  }
}

walkAndTranslate(document.body);
