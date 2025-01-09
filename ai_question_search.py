import os
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

# API anahtarını ortam değişkeninden al
api_key = os.environ.get("AI21_API_KEY")
if not api_key:
    raise ValueError("API key is missing. Ensure AI21_API_KEY is set as an environment variable.")

# AI21Client nesnesi oluştur
client = AI21Client(api_key=api_key)

def main():
    import sys
    if len(sys.argv) < 2:
        print("No input provided.")
        return
    user_input = " ".join(sys.argv[1:])
    try:
        response = client.chat.completions.create(
            model="jamba-instruct-preview",
            messages=[
                ChatMessage(role="user", content=user_input)
            ],
            temperature=0.8,
            max_tokens=100
        )
        for choice in response.choices:
            print(choice.message.content)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
