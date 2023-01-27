# Chatbot in Python

A chatbot is a computer program designed to simulate conversation with human users.

 This chatbot is implemented in Python, and it uses .toml files to store its responses. The .toml file contains a dictionary of patterns and their corresponding responses. When the chatbot receives a message from the user, it checks if the message matches one of the patterns in the .toml file and returns the corresponding response.

```
[responses]
"pattern1" = "response1"
"pattern2" = "response2"
...
```

 - The patterns are case-insensitive, so the chatbot will match "Hello" and "hello" as the same pattern.
 - The chatbot will only return the first matching pattern it finds in the .toml file.

#### How to use ####

Step 1: Install toml package

```
pip install toml
```

Step 2: Create a file responses.toml and put your response patterns and corresponding responses in the following format

```
[responses]
"hello" = "Hello, how can I help you?"
"how are you" = "I'm doing well, thank you for asking!"
"goodbye" = "Goodbye! Have a great day."
```

Step 3: Create a new python file and import the toml package and the Chatbot class

```
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
```
Step 4: Create an instance of the Chatbot class, passing the path of the .toml file containing the responses as an argument

```
chatbot = Chatbot("responses.toml")
```

Step 5: Use the respond method of the Chatbot class to get the response of the bot

```
print(chatbot.respond("Hello"))
```

Step 6: Run the python file and test the bot with different messages.

* Note that this is a very basic example of a chatbot using .toml files. You can further improve this chatbot by adding more patterns, keeping the history of conversation, and providing more intelligent responses. *
