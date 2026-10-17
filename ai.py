from openai import OpenAI

def aiProcess(command):
    try:
        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-5.6-luna",
            messages=[
                {
                    "role": "system",
                    "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant. Give short responses"
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        print("AI Error:", e)
        return "Sorry, I couldn't process that request right now."