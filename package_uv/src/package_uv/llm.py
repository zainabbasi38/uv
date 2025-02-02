from litellm import completion
import os

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

# def openai():
#     response = completion(
#         model="openai/gpt-4o",
#         messages=[{ "content": "Hello, how are you?","role": "user"}]
#     )

#     print(response)

def gemini():
    while True:
        question = input("Ask something: ")
        if question == "quit":
            break
        else:
            response = completion(
                model="gemini/gemini-1.5-flash",
                messages=[{ "content": question,"role": "user"}]
            )

            ai_response = response["choices"][0]["message"]["content"]
            print(ai_response)          

def gemini2():
    while True:
        question = input("Ask something: ")
        if question == "quit":
            break
        else:
            response = completion(
                model="gemini/gemini-2.0-flash-exp",
                messages=[{ "content": question,"role": "user"}]
            )

            ai_response = response["choices"][0]["message"]["content"]
            print(ai_response)          