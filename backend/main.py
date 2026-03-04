"""
MedAssist AI — Medical Information Digital Assistant
FastAPI backend with Mistral AI integration.
Serves both the API and the static frontend.
"""

import os
import asyncio
from pathlib import Path
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

from mistralai import Mistral

from medical_prompt import (
    get_system_prompt,
    SUPPORTED_LANGUAGES,
    UI_TRANSLATIONS,
)

# ── Load environment ──────────────────────────────────────────────
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# ── Mistral client (initialized at startup) ──────────────────────
mistral_client = None


# ── App lifespan ──────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Configure Mistral on startup."""
    global mistral_client
    if MISTRAL_API_KEY and MISTRAL_API_KEY != "your_mistral_api_key_here":
        mistral_client = Mistral(api_key=MISTRAL_API_KEY)
        print("✅ Mistral AI configured successfully")
    else:
        print("⚠️  MISTRAL_API_KEY not set — AI chat will not work.")
        print("   Edit .env file with: MISTRAL_API_KEY=your_key_here")
    yield


# ── FastAPI app ───────────────────────────────────────────────────
app = FastAPI(
    title="MedAssist AI",
    description="Medical Information Digital Assistant",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Request / Response models ─────────────────────────────────────
class ChatRequest(BaseModel):
    message: str
    language: str = "en"


class ChatResponse(BaseModel):
    reply: str
    language: str


# ── API routes ────────────────────────────────────────────────────
@app.get("/api/languages")
async def get_languages():
    """Return list of supported languages."""
    return {
        "languages": [
            {"code": code, "name": name}
            for code, name in SUPPORTED_LANGUAGES.items()
        ]
    }


@app.get("/api/translations/{lang_code}")
async def get_translations(lang_code: str):
    """Return UI translations for the given language."""
    translations = UI_TRANSLATIONS.get(lang_code)
    if not translations:
        raise HTTPException(status_code=404, detail="Language not supported")
    return translations


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Send a medical question to Mistral and return the AI response."""
    if not mistral_client:
        raise HTTPException(
            status_code=503,
            detail="Mistral API key not configured. Please set MISTRAL_API_KEY in the .env file.",
        )

    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    system_prompt = get_system_prompt(request.language)

    # Models to try in order (fallback chain)
    models = ["mistral-small-latest", "mistral-tiny-latest"]
    max_retries = 2
    last_error = None

    for model_name in models:
        for attempt in range(max_retries):
            try:
                response = mistral_client.chat.complete(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": request.message},
                    ],
                )

                reply_text = response.choices[0].message.content
                if reply_text:
                    print(f"✅ Response from {model_name} (attempt {attempt + 1})")
                    return ChatResponse(reply=reply_text, language=request.language)

            except Exception as e:
                last_error = e
                error_str = str(e).lower()
                print(f"⚠️ {model_name} error (attempt {attempt + 1}/{max_retries}): {e}")

                if any(kw in error_str for kw in ["429", "rate", "quota", "limit"]):
                    if attempt < max_retries - 1:
                        await asyncio.sleep(5)
                        continue
                    else:
                        break
                else:
                    break

    # All models and retries exhausted
    error_msg = str(last_error)[:200] if last_error else "Unknown error"
    raise HTTPException(
        status_code=500,
        detail=f"An error occurred: {error_msg}",
    )


# ── Serve frontend static files ──────────────────────────────────
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


@app.get("/")
async def serve_frontend():
    """Serve the frontend index.html."""
    return FileResponse(str(FRONTEND_DIR / "index.html"))


# ── Run with: uvicorn main:app --reload ───────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
