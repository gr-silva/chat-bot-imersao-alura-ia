import textwrap

from IPython.display import Markdown, display

from GoogleGemini import GoogleGemini

google_ai = GoogleGemini("gemini-1.0-pro")

chat = google_ai.start_chat()

prompt = input("Esperando prompt: ")

while prompt != "exit":
    response = chat.send_message(prompt)
    print("Resposta: ", response.text, "\n")
    prompt = input("Esperando prompt: ")


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


for message in chat.history:
    display(to_markdown(f"**{message.role}**: {message.parts[0].text}"))
    print("--------------------------------------")
