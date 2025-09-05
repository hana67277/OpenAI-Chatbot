from openai import OpenAI

# Initialize the client (reads key from env var OPENAI_API_KEY automatically)
client = OpenAI(api_key="")

def chat_with_gpt(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # use "gpt-5" if your account has access
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye 👋")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
    