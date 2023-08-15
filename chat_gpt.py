import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

assistant_type = input("Initialise your assistant: ")
assistant_init = {"role": "system", "content": assistant_type}
messages.append(assistant_init)

while True:
    user_query = input("Enter your query: ")
    if user_query:
        user_input = {"role": "user", "content": user_query}
        messages.append(user_input)
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.4
            )

    output = chat.choices[0].message.content
    assistant_output = {"role": "assistant", "content": output}
    print(f"Chat GPT: {output}")
    messages.append(assistant_output)