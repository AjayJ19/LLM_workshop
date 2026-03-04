/**
 * MedAssist AI — Frontend Logic
 * Handles chat, language switching, suggestion chips, and markdown rendering.
 */

// ── State ────────────────────────────────────────────────────────
let currentLanguage = 'en';
let isWaitingForReply = false;

// ── DOM refs ─────────────────────────────────────────────────────
const chatMessages = document.getElementById('chat-messages');
const chatContainer = document.getElementById('chat-container');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const languageSelect = document.getElementById('language-select');
const suggestionsScroll = document.getElementById('suggestions-scroll');
const appTitle = document.getElementById('app-title');
const appSubtitle = document.getElementById('app-subtitle');
const disclaimer = document.getElementById('disclaimer');


// ══════════════════════════════════════════════════════════════════
// ── Initialization ───────────────────────────────────────────────
// ══════════════════════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {
    loadTranslations(currentLanguage);
    setupEventListeners();
});


function setupEventListeners() {
    // Send on click
    sendButton.addEventListener('click', handleSend);

    // Send on Enter (Shift+Enter for new line)
    messageInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    });

    // Auto-resize textarea
    messageInput.addEventListener('input', autoResizeTextarea);

    // Language change
    languageSelect.addEventListener('change', (e) => {
        currentLanguage = e.target.value;
        loadTranslations(currentLanguage);
    });
}


// ══════════════════════════════════════════════════════════════════
// ── Language & Translations ──────────────────────────────────────
// ══════════════════════════════════════════════════════════════════

async function loadTranslations(langCode) {
    try {
        const res = await fetch(`/api/translations/${langCode}`);
        if (!res.ok) throw new Error('Failed to load translations');
        const t = await res.json();

        // Update header
        appTitle.textContent = t.title;
        appSubtitle.textContent = t.subtitle;

        // Update input placeholder
        messageInput.placeholder = t.placeholder;

        // Update disclaimer
        disclaimer.textContent = t.disclaimer;

        // Render suggestion chips
        renderSuggestions(t.suggestions);

        // Show welcome message (only if chat is empty)
        if (chatMessages.children.length === 0) {
            addMessageToChat('ai', t.welcome);
        }
    } catch (err) {
        console.error('Translation load error:', err);
        // Fallback — still show English suggestions
        renderSuggestions([
            "What are the symptoms of diabetes?",
            "How to treat a common cold at home?",
            "What is a balanced diet?",
            "When should I see a doctor for a headache?"
        ]);
        if (chatMessages.children.length === 0) {
            addMessageToChat('ai', "Hello! I'm **MedAssist AI**, your personal health information guide. 🩺\n\nAsk me anything about your health!");
        }
    }
}


function renderSuggestions(suggestions) {
    suggestionsScroll.innerHTML = '';
    suggestions.forEach(text => {
        const chip = document.createElement('button');
        chip.className = 'suggestion-chip';
        chip.textContent = text;
        chip.addEventListener('click', () => {
            messageInput.value = text;
            autoResizeTextarea();
            handleSend();
        });
        suggestionsScroll.appendChild(chip);
    });
}


// ══════════════════════════════════════════════════════════════════
// ── Chat Logic ───────────────────────────────────────────────────
// ══════════════════════════════════════════════════════════════════

async function handleSend() {
    const text = messageInput.value.trim();
    if (!text || isWaitingForReply) return;

    // Add user message
    addMessageToChat('user', text);
    messageInput.value = '';
    autoResizeTextarea();

    // Show typing indicator
    isWaitingForReply = true;
    sendButton.disabled = true;
    const typingEl = showTypingIndicator();

    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text, language: currentLanguage })
        });

        if (!res.ok) {
            const err = await res.json().catch(() => ({}));
            throw new Error(err.detail || 'Server error');
        }

        const data = await res.json();
        removeTypingIndicator(typingEl);
        addMessageToChat('ai', data.reply);

    } catch (err) {
        removeTypingIndicator(typingEl);
        addMessageToChat('ai', `❌ **Error:** ${err.message}\n\nPlease check that the server is running and the Gemini API key is configured.`);
    } finally {
        isWaitingForReply = false;
        sendButton.disabled = false;
        messageInput.focus();
    }
}


// ══════════════════════════════════════════════════════════════════
// ── Message Rendering ────────────────────────────────────────────
// ══════════════════════════════════════════════════════════════════

function addMessageToChat(role, text) {
    const wrapper = document.createElement('div');
    wrapper.className = `message ${role === 'user' ? 'user-message' : 'ai-message'}`;

    // Avatar
    const avatar = document.createElement('div');
    avatar.className = `message-avatar ${role === 'user' ? 'user-avatar' : 'ai-avatar'}`;

    if (role === 'user') {
        avatar.textContent = '👤';
    } else {
        avatar.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
                 stroke="currentColor" stroke-width="2">
                <path d="M12 2L12 22"/><path d="M2 12L22 12"/>
                <circle cx="12" cy="12" r="10"/>
            </svg>`;
    }

    // Content
    const content = document.createElement('div');
    content.className = 'message-content';

    if (role === 'ai') {
        content.innerHTML = renderMarkdown(text);
    } else {
        content.textContent = text;
    }

    wrapper.appendChild(avatar);
    wrapper.appendChild(content);
    chatMessages.appendChild(wrapper);

    scrollToBottom();
}


// ══════════════════════════════════════════════════════════════════
// ── Typing Indicator ─────────────────────────────────────────────
// ══════════════════════════════════════════════════════════════════

function showTypingIndicator() {
    const template = document.getElementById('typing-template');
    const clone = template.content.cloneNode(true);
    const el = clone.querySelector('.message');
    el.id = 'typing-msg';
    chatMessages.appendChild(clone);
    scrollToBottom();
    return document.getElementById('typing-msg');
}

function removeTypingIndicator(el) {
    if (el && el.parentNode) {
        el.parentNode.removeChild(el);
    }
}


// ══════════════════════════════════════════════════════════════════
// ── Markdown Renderer (lightweight) ──────────────────────────────
// ══════════════════════════════════════════════════════════════════

function renderMarkdown(text) {
    if (!text) return '';

    let html = escapeHtml(text);

    // Headers
    html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
    html = html.replace(/^# (.+)$/gm, '<h1>$1</h1>');

    // Bold
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');

    // Italic
    html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');

    // Inline code
    html = html.replace(/`(.+?)`/g, '<code>$1</code>');

    // Horizontal rule
    html = html.replace(/^---$/gm, '<hr>');

    // Unordered lists  (- item or * item)
    html = html.replace(/^[\-\*] (.+)$/gm, '<li>$1</li>');
    html = html.replace(/((?:<li>.*<\/li>\n?)+)/g, '<ul>$1</ul>');

    // Ordered lists  (1. item)
    html = html.replace(/^\d+\. (.+)$/gm, '<li>$1</li>');
    // Wrap consecutive <li> not already in <ul>
    html = html.replace(/(?<!<\/ul>)((?:<li>.*<\/li>\n?)+)/g, (match, p1) => {
        if (match.includes('<ul>')) return match;
        return '<ol>' + p1 + '</ol>';
    });

    // Paragraphs — split on double newlines
    html = html.split(/\n{2,}/).map(block => {
        block = block.trim();
        if (!block) return '';
        // Don't wrap block-level elements
        if (/^<(h[1-6]|ul|ol|li|hr|blockquote)/.test(block)) return block;
        return `<p>${block}</p>`;
    }).join('');

    // Single newlines → <br> inside <p>
    html = html.replace(/(<p>.*?<\/p>)/gs, (match) => {
        return match.replace(/\n/g, '<br>');
    });

    return html;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}


// ══════════════════════════════════════════════════════════════════
// ── Utilities ────────────────────────────────────────────────────
// ══════════════════════════════════════════════════════════════════

function scrollToBottom() {
    requestAnimationFrame(() => {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    });
}

function autoResizeTextarea() {
    messageInput.style.height = 'auto';
    messageInput.style.height = Math.min(messageInput.scrollHeight, 120) + 'px';
}
