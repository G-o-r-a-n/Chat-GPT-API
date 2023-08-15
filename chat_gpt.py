import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

assistant_type = input("Initialise your assistant: ")
assistant_init = {"role": "system", "content": assistant_type}
messages.append(assistant_init)

while True:
    user_query = input("\n\nEnter your query: ")
    if user_query:
        user_input = {"role": "user", "content": user_query}
        messages.append(user_input)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5
            )

    output = chat.choices[0].message.content
    assistant_output = {"role": "assistant", "content": output}
    print(f"\n\nChat GPT: {output}")
    messages.append(assistant_output)