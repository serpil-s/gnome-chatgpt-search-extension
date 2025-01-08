import os
import sys
import openai

def main():
    # OpenAI API anahtarını kontrol et
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: API key not found. Please set the OPENAI_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)
    
    # OpenAI istemcisi
    openai.api_key = api_key

    # Kullanıcıdan prompt al
    if len(sys.argv) < 2:
        print("Error: No input provided. Usage: utils.py '<your prompt>'", file=sys.stderr)
        sys.exit(1)
    
    prompt = " ".join(sys.argv[1:])
    
    try:
        # OpenAI'nin en güncel API'sini kullanarak bir istek yap
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Yanıtı yazdır
        print(response.choices[0].message.content)
    except openai.AuthenticationError:
        print("Error: Invalid API key. Please check your API key and try again.", file=sys.stderr)
    except openai.OpenAIError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
