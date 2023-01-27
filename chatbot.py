import toml

class Chatbot:
    def __init__(self, responses_file):
        with open(responses_file) as f:
            data = toml.load(f)
            self.responses = data["responses"]

    def respond(self, message):
        for pattern, response in self.responses.items():
            if message.lower().startswith(pattern.lower()):
                return response

chatbot = Chatbot("responses.toml")
print(chatbot.respond("Hello"))
