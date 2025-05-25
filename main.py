from llm import chat
from speech_to_text import listen
from text_to_speech import speak



if __name__ == "__main__":
    while True:
        try:
            # Listen for user input
            user_input = listen()
            print(f"You said: {user_input}")

            # Generate response using LLM
            response = chat(user_input)
            print(f"LLM response: {response}")

            # Speak the response
            speak(response)

        except Exception as e:
            print(f"An error occurred: {e}")