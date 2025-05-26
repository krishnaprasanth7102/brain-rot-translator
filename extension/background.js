chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: translatePageText,
  });
});

async function translatePageText() {
  // Grab all text nodes from the page (simplified)
  let bodyText = document.body.innerText;

  // Call backend API
  let response = await fetch('http://localhost:5000/translate', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ text: bodyText }),
  });

  let data = await response.json();
  let translatedText = data.translated_text;

  // Replace page text (basic, for demo purposes)
  document.body.innerText = translatedText;
}
