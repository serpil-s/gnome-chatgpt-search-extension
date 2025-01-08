import openai
import sys

# OpenAI API anahtarınızı buraya ekleyin
openai.api_key = "YOUR_API_KEY"

def ask_chatgpt(question):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            max_tokens=200
        )
        print(response['choices'][0]['text'].strip())
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        ask_chatgpt(question)
    else:
        print("No question provided.", file=sys.stderr)
        sys.exit(2)
