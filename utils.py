import openai

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
        print(f"Error: {e}")

if __name__ == "__main__":
    question = input("Enter your question for ChatGPT: ")
    ask_chatgpt(question)
