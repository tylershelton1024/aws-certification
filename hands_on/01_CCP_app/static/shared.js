// Shared helpers used by more than one page's inline script (flashcards,
// practice). Loaded once via <script src="/static/shared.js"> before each
// page's own script, so this logic has exactly one copy instead of being
// redefined per page.

function shuffleArray(array) {
    const arr = array.slice();
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
    return arr;
}

// Given a topic ({ core: [...], deeper: [...] }) and a deck name of
// "core", "deeper", or "both", returns the requested list - "both" merges
// core and deeper into one combined list.
function combineDecks(topic, deckName) {
    if (deckName === "both") {
        return topic.core.concat(topic.deeper);
    }
    return topic[deckName];
}
