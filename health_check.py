import requests

from config import (
    AI_PROVIDER,
    OLLAMA_HOST,
    OLLAMA_MODEL,
    TELEGRAM_BOT_TOKEN,
)


def run_health_check():
    print("\n========================================")
    print("🛡️ JayJay AI Security Assistant")
    print("========================================")

    # Telegram Token
    if TELEGRAM_BOT_TOKEN:
        print("✅ Telegram Bot Token: Loaded")
    else:
        print("❌ Telegram Bot Token: Missing")

    # AI Provider
    print(f"✅ AI Provider: {AI_PROVIDER}")

    # Ollama Check
    if AI_PROVIDER.lower() == "ollama":
        try:
            response = requests.get(
                f"{OLLAMA_HOST}/api/tags",
                timeout=5,
            )

            if response.status_code == 200:
                print("✅ Ollama Server: Online")

                models = response.json().get("models", [])

                installed = any(
                    model.get("name") == OLLAMA_MODEL
                    for model in models
                )

                if installed:
                    print(f"✅ Model Installed: {OLLAMA_MODEL}")
                else:
                    print(f"❌ Model Missing: {OLLAMA_MODEL}")

            else:
                print(
                    f"❌ Ollama Server Responded with Error "
                    f"(HTTP {response.status_code})"
                )

        except requests.RequestException:
            print("❌ Ollama Server: Offline")

    print("========================================")
    print()


if __name__ == "__main__":
    run_health_check()
