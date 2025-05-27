console.log("🧠 Brain Rot Translator running...");

async function translateText(text) {
  try {
    console.log("🔄 Translating:", text);
    const res = await fetch('http://127.0.0.1:5000/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    const data = await res.json();
    return data.translated_text;
  } catch (err) {
    console.error("❌ Error translating:", err);
    return text;
  }
}

async function processTextNode(node) {
  if (node.nodeType === Node.TEXT_NODE && node.nodeValue.trim().length > 3) {
    const original = node.nodeValue;
    const translated = await translateText(original);
    if (translated !== original) {
      const span = document.createElement("span");
      span.style.fontStyle = "italic";
      span.textContent = translated;
      node.parentNode.replaceChild(span, node);
    }
  }
}

function walkAndTranslate(root) {
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
  let node;
  while ((node = walker.nextNode())) {
    processTextNode(node);
  }
}

// Watch for new DOM changes
const observer = new MutationObserver(mutations => {
  for (const mutation of mutations) {
    mutation.addedNodes.forEach(node => {
      if (node.nodeType === Node.ELEMENT_NODE) {
        walkAndTranslate(node);
      }
    });
  }
});

observer.observe(document.body, {
  childList: true,
  subtree: true
});

// Initial run
walkAndTranslate(document.body);
