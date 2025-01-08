import os
import sys
import openai
from openai import OpenAI


def main():
    # API anahtarını kontrol et
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: API key not found. Set the OPENAI_API_KEY environment variable.", file=sys.stderr)
        sys.exit(2)

    client = OpenAI()

    # openai.api_key = api_key

    # Kullanıcı girdisini al
    if len(sys.argv) < 2:
        print("Error: No input provided. Usage: utils.py '<prompt>'", file=sys.stderr)
        sys.exit(2)

    prompt = " ".join(sys.argv[1:])

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            model="gpt-3.5-turbo",  # e.g. gpt-35-instant,
            stream=True,
        )
        for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="")
    except openai.OpenAIError as e:
        print(f"OpenAI Error: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
