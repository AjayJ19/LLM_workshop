"""
Medical system prompt engineering for the Digital Health Assistant.
Contains curated prompts that instruct the AI to behave as a reliable,
simplified medical information guide — NOT a doctor.
"""

SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi (हिन्दी)",
    "ta": "Tamil (தமிழ்)",
    "te": "Telugu (తెలుగు)",
    "kn": "Kannada (ಕನ್ನಡ)",
    "ml": "Malayalam (മലയാളം)",
}

# UI translations for the frontend
UI_TRANSLATIONS = {
    "en": {
        "title": "MedAssist AI",
        "subtitle": "Your Trusted Health Information Guide",
        "placeholder": "Ask a health question...",
        "send": "Send",
        "disclaimer": "⚕️ This assistant provides general health information only. It does not diagnose, treat, or prescribe. Always consult a qualified healthcare professional for medical advice.",
        "welcome": "Hello! I'm **MedAssist AI**, your personal health information guide. 🩺\n\nI can help you understand:\n- 🔍 Common symptoms & conditions\n- 💊 Preventive health measures\n- 🩹 Basic first aid guidance\n- 🏥 When to see a doctor\n\nAsk me anything about your health!",
        "suggestions": [
            "What are the symptoms of diabetes?",
            "How to treat a common cold at home?",
            "What is a balanced diet?",
            "When should I see a doctor for a headache?",
            "What are the benefits of regular exercise?",
            "How to manage stress effectively?"
        ]
    },
    "hi": {
        "title": "मेडअसिस्ट AI",
        "subtitle": "आपका विश्वसनीय स्वास्थ्य जानकारी मार्गदर्शक",
        "placeholder": "स्वास्थ्य से जुड़ा कोई सवाल पूछें...",
        "send": "भेजें",
        "disclaimer": "⚕️ यह सहायक केवल सामान्य स्वास्थ्य जानकारी प्रदान करता है। यह निदान, उपचार या दवा नहीं देता। कृपया चिकित्सा सलाह के लिए योग्य डॉक्टर से परामर्श लें।",
        "welcome": "नमस्ते! मैं **मेडअसिस्ट AI** हूँ, आपका स्वास्थ्य जानकारी मार्गदर्शक। 🩺\n\nमैं आपकी मदद कर सकता हूँ:\n- 🔍 सामान्य लक्षण और बीमारियाँ\n- 💊 स्वास्थ्य सुरक्षा उपाय\n- 🩹 प्राथमिक चिकित्सा\n- 🏥 डॉक्टर से कब मिलें\n\nअपना सवाल पूछें!",
        "suggestions": [
            "मधुमेह के लक्षण क्या हैं?",
            "सर्दी-जुकाम का घरेलू उपचार?",
            "संतुलित आहार क्या है?",
            "सिरदर्द के लिए डॉक्टर कब जाएं?",
            "नियमित व्यायाम के क्या फायदे हैं?",
            "तनाव कैसे कम करें?"
        ]
    },
    "ta": {
        "title": "MedAssist AI",
        "subtitle": "உங்கள் நம்பகமான சுகாதார தகவல் வழிகாட்டி",
        "placeholder": "ஒரு சுகாதார கேள்வி கேளுங்கள்...",
        "send": "அனுப்பு",
        "disclaimer": "⚕️ இந்த உதவியாளர் பொதுவான சுகாதார தகவல்களை மட்டுமே வழங்குகிறது. இது நோய் கண்டறிதல், சிகிச்சை அல்லது மருந்து பரிந்துரைக்காது. மருத்துவ ஆலோசனைக்கு தகுதியான மருத்துவரை அணுகவும்.",
        "welcome": "வணக்கம்! நான் **MedAssist AI**, உங்கள் சுகாதார தகவல் வழிகாட்டி. 🩺\n\nநான் உங்களுக்கு உதவ முடியும்:\n- 🔍 பொதுவான அறிகுறிகள் & நிலைமைகள்\n- 💊 தடுப்பு சுகாதார நடவடிக்கைகள்\n- 🩹 அடிப்படை முதலுதவி\n- 🏥 மருத்துவரை எப்போது அணுக வேண்டும்\n\nஉங்கள் கேள்வியை கேளுங்கள்!",
        "suggestions": [
            "நீரிழிவு நோயின் அறிகுறிகள் என்ன?",
            "சாதாரண சளிக்கு வீட்டு வைத்தியம்?",
            "சமச்சீர் உணவு என்றால் என்ன?",
            "தலைவலிக்கு மருத்துவரிடம் எப்போது செல்ல வேண்டும்?",
            "உடற்பயிற்சியின் நன்மைகள் என்ன?",
            "மன அழுத்தத்தை எப்படி குறைப்பது?"
        ]
    },
    "te": {
        "title": "MedAssist AI",
        "subtitle": "మీ విశ్వసనీయ ఆరోగ్య సమాచార మార్గదర్శి",
        "placeholder": "ఆరోగ్య ప్రశ్న అడగండి...",
        "send": "పంపు",
        "disclaimer": "⚕️ ఈ అసిస్టెంట్ సాధారణ ఆరోగ్య సమాచారాన్ని మాత్రమే అందిస్తుంది. ఇది రోగ నిర్ధారణ, చికిత్స లేదా మందులు సూచించదు. వైద్య సలహా కోసం అర్హత కలిగిన వైద్యుడిని సంప్రదించండి.",
        "welcome": "నమస్కారం! నేను **MedAssist AI**, మీ ఆరోగ్య సమాచార మార్గదర్శి. 🩺\n\nనేను మీకు సహాయం చేయగలను:\n- 🔍 సాధారణ లక్షణాలు & పరిస్థితులు\n- 💊 నివారణ ఆరోగ్య చర్యలు\n- 🩹 ప్రాథమిక చికిత్స\n- 🏥 వైద్యుడిని ఎప్పుడు సంప్రదించాలి\n\nమీ ప్రశ్న అడగండి!",
        "suggestions": [
            "మధుమేహం లక్షణాలు ఏమిటి?",
            "జలుబుకు ఇంటి చిట్కాలు?",
            "సమతుల్య ఆహారం అంటే ఏమిటి?",
            "తలనొప్పికి వైద్యుడిని ఎప్పుడు సంప్రదించాలి?",
            "క్రమం తప్పకుండా వ్యాయామం చేయడం వల్ల ప్రయోజనాలు?",
            "ఒత్తిడిని ఎలా తగ్గించుకోవాలి?"
        ]
    },
    "kn": {
        "title": "MedAssist AI",
        "subtitle": "ನಿಮ್ಮ ವಿಶ್ವಾಸಾರ್ಹ ಆರೋಗ್ಯ ಮಾಹಿತಿ ಮಾರ್ಗದರ್ಶಿ",
        "placeholder": "ಆರೋಗ್ಯ ಪ್ರಶ್ನೆ ಕೇಳಿ...",
        "send": "ಕಳುಹಿಸು",
        "disclaimer": "⚕️ ಈ ಸಹಾಯಕವು ಸಾಮಾನ್ಯ ಆರೋಗ್ಯ ಮಾಹಿತಿಯನ್ನು ಮಾತ್ರ ಒದಗಿಸುತ್ತದೆ. ಇದು ರೋಗ ನಿರ್ಣಯ, ಚಿಕಿತ್ಸೆ ಅಥವಾ ಔಷಧಿ ಸೂಚಿಸುವುದಿಲ್ಲ. ವೈದ್ಯಕೀಯ ಸಲಹೆಗಾಗಿ ಅರ್ಹ ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "welcome": "ನಮಸ್ಕಾರ! ನಾನು **MedAssist AI**, ನಿಮ್ಮ ಆರೋಗ್ಯ ಮಾಹಿತಿ ಮಾರ್ಗದರ್ಶಿ. 🩺\n\nನಾನು ನಿಮಗೆ ಸಹಾಯ ಮಾಡಬಲ್ಲೆ:\n- 🔍 ಸಾಮಾನ್ಯ ರೋಗಲಕ್ಷಣಗಳು & ಪರಿಸ್ಥಿತಿಗಳು\n- 💊 ತಡೆಗಟ್ಟುವ ಆರೋಗ್ಯ ಕ್ರಮಗಳು\n- 🩹 ಮೂಲಭೂತ ಪ್ರಥಮ ಚಿಕಿತ್ಸೆ\n- 🏥 ವೈದ್ಯರನ್ನು ಯಾವಾಗ ಭೇಟಿ ಮಾಡಬೇಕು\n\nನಿಮ್ಮ ಪ್ರಶ್ನೆ ಕೇಳಿ!",
        "suggestions": [
            "ಮಧುಮೇಹದ ಲಕ್ಷಣಗಳು ಯಾವುವು?",
            "ಸಾಮಾನ್ಯ ಶೀತಕ್ಕೆ ಮನೆ ಚಿಕಿತ್ಸೆ?",
            "ಸಮತೋಲಿತ ಆಹಾರ ಎಂದರೇನು?",
            "ತಲೆನೋವಿಗೆ ವೈದ್ಯರನ್ನು ಯಾವಾಗ ಭೇಟಿ ಮಾಡಬೇಕು?",
            "ನಿಯಮಿತ ವ್ಯಾಯಾಮದ ಪ್ರಯೋಜನಗಳು?",
            "ಒತ್ತಡವನ್ನು ಹೇಗೆ ಕಡಿಮೆ ಮಾಡುವುದು?"
        ]
    },
    "ml": {
        "title": "MedAssist AI",
        "subtitle": "നിങ്ങളുടെ വിശ്വസനീയ ആരോഗ്യ വിവര ഗൈഡ്",
        "placeholder": "ഒരു ആരോഗ്യ ചോദ്യം ചോദിക്കൂ...",
        "send": "അയക്കുക",
        "disclaimer": "⚕️ ഈ അസിസ്റ്റന്റ് പൊതുവായ ആരോഗ്യ വിവരങ്ങൾ മാത്രമേ നൽകുന്നുള്ളൂ. ഇത് രോഗനിർണയം, ചികിത്സ അല്ലെങ്കിൽ മരുന്ന് നിർദ്ദേശിക്കുന്നില്ല. വൈദ്യ ഉപദേശത്തിന് യോഗ്യതയുള്ള ഡോക്ടറെ സമീപിക്കുക.",
        "welcome": "നമസ്കാരം! ഞാൻ **MedAssist AI**, നിങ്ങളുടെ ആരോഗ്യ വിവര ഗൈഡ്. 🩺\n\nഎനിക്ക് നിങ്ങളെ സഹായിക്കാൻ കഴിയും:\n- 🔍 സാധാരണ രോഗലക്ഷണങ്ങൾ & അവസ്ഥകൾ\n- 💊 പ്രതിരോധ ആരോഗ്യ നടപടികൾ\n- 🩹 അടിസ്ഥാന പ്രഥമശുശ്രൂഷ\n- 🏥 ഡോക്ടറെ എപ്പോൾ കാണണം\n\nനിങ്ങളുടെ ചോദ്യം ചോദിക്കൂ!",
        "suggestions": [
            "പ്രമേഹത്തിന്റെ ലക്ഷണങ്ങൾ എന്തൊക്കെ?",
            "സാധാരണ ജലദോഷത്തിന് വീട്ടുവൈദ്യം?",
            "സമീകൃത ആഹാരം എന്താണ്?",
            "തലവേദനയ്ക്ക് ഡോക്ടറെ എപ്പോൾ കാണണം?",
            "പതിവ് വ്യായാമത്തിന്റെ ഗുണങ്ങൾ?",
            "മാനസിക സമ്മർദ്ദം എങ്ങനെ കുറയ്ക്കാം?"
        ]
    }
}


def get_system_prompt(language_code: str = "en") -> str:
    """
    Build the medical assistant system prompt.
    Instructs the AI to respond in the selected language with simplified medical information.
    """
    language_name = SUPPORTED_LANGUAGES.get(language_code, "English")

    return f"""You are MedAssist AI, a trusted Medical Information Digital Assistant. Your role is to provide simplified, accurate, and easy-to-understand health information to the general public.

## CRITICAL RULES — YOU MUST FOLLOW THESE AT ALL TIMES:

1. **YOU ARE NOT A DOCTOR.** You provide general health INFORMATION only. You do NOT diagnose diseases, prescribe medications, or replace professional medical advice.

2. **ALWAYS include a disclaimer** at the end of your response:
   - In English: "⚠️ *This is general health information only. Please consult a qualified healthcare professional for personalized medical advice.*"
   - Translate this disclaimer into the response language if not English.

3. **RESPOND IN: {language_name}** — The user has selected this language. All your responses must be in {language_name}. If the user writes in a different language, still respond in {language_name}.

4. **USE SIMPLE LANGUAGE** — Avoid complex medical jargon. Explain terms in plain, everyday language that anyone can understand. If you must use a medical term, explain it in parentheses.

5. **STRUCTURE YOUR RESPONSES** clearly using:
   - Short paragraphs
   - Bullet points or numbered lists
   - Bold text for key points
   - Emojis where appropriate to make information friendly and approachable

6. **TOPICS YOU CAN HELP WITH:**
   - Explaining common symptoms and what they might indicate
   - General information about diseases and conditions
   - Preventive health measures and healthy lifestyle tips
   - Basic first aid guidance
   - Nutrition and diet information
   - Mental health awareness and general wellness tips
   - When to seek emergency medical help
   - Understanding common medical tests and procedures (general info)

7. **TOPICS YOU MUST REFUSE:**
   - Specific diagnosis of a user's condition
   - Prescribing or recommending specific medications or dosages
   - Interpreting specific lab results or medical reports
   - Providing second opinions on a doctor's diagnosis
   - Any advice that could delay someone from seeking emergency care
   - For these, politely redirect them to consult a healthcare professional.

8. **WHEN IN DOUBT, RECOMMEND A DOCTOR.** If the user describes symptoms that sound serious or urgent, clearly advise them to seek immediate medical attention. Use phrases like:
   - "Please visit a doctor as soon as possible"
   - "This could require urgent medical attention"
   - "Call emergency services if symptoms worsen"

9. **BE EMPATHETIC AND SUPPORTIVE.** Health concerns can be scary. Be warm, reassuring, and non-judgmental in your tone.

10. **KEEP RESPONSES CONCISE** but comprehensive. Aim for clear, actionable information without overwhelming the user.

Remember: Your goal is to EMPOWER people with knowledge so they can make informed health decisions and know when to seek professional help."""


def get_safety_disclaimer(language_code: str = "en") -> str:
    """Return a safety disclaimer in the specified language."""
    disclaimers = {
        "en": "⚠️ *This is general health information only. Please consult a qualified healthcare professional for personalized medical advice.*",
        "hi": "⚠️ *यह केवल सामान्य स्वास्थ्य जानकारी है। व्यक्तिगत चिकित्सा सलाह के लिए कृपया योग्य स्वास्थ्य पेशेवर से परामर्श लें।*",
        "ta": "⚠️ *இது பொதுவான சுகாதார தகவல் மட்டுமே. தனிப்பட்ட மருத்துவ ஆலோசனைக்கு தகுதியான சுகாதார நிபுணரை அணுகவும்.*",
        "te": "⚠️ *ఇది సాధారణ ఆరోగ్య సమాచారం మాత్రమే. వ్యక్తిగత వైద్య సలహా కోసం అర్హత కలిగిన ఆరోగ్య నిపుణుడిని సంప్రదించండి.*",
        "kn": "⚠️ *ಇದು ಸಾಮಾನ್ಯ ಆರೋಗ್ಯ ಮಾಹಿತಿ ಮಾತ್ರ. ವೈಯಕ್ತಿಕ ವೈದ್ಯಕೀಯ ಸಲಹೆಗಾಗಿ ಅರ್ಹ ಆರೋಗ್ಯ ವೃತ್ತಿಪರರನ್ನು ಸಂಪರ್ಕಿಸಿ.*",
        "ml": "⚠️ *ഇത് പൊതുവായ ആരോഗ്യ വിവരങ്ങൾ മാത്രമാണ്. വ്യക്തിഗത വൈദ്യ ഉപദേശത്തിന് യോഗ്യതയുള്ള ആരോഗ്യ പ്രൊഫഷണലിനെ സമീപിക്കുക.*",
    }
    return disclaimers.get(language_code, disclaimers["en"])
