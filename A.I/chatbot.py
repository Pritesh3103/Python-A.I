import re

class RuleBasedChatbot:
    
    def __init__(self):
        
        self.greetings = ['hello', 'hi', 'hey', 'greetings', 'what\'s up']
        
        self.questions = {
            'how are you': 'I am just a program, but I\'m doing well. How can I help you?',
            'what is your name': 'I am A . T . O . M .(A.I) created to assist you.',
            'what can you do': 'I can answer some basic questions and have a chat with you.',
        }
        
        self.farewells = ['bye', 'goodbye', 'see you', 'take care']
        
    
    def respond_to_greeting(self, message):
        
        for greeting in self.greetings:
        
            if re.search(r'\b' + greeting + r'\b', message.lower()):
        
                return 'Hello! How can I assist you today?'
        
        return None

    def respond_to_question(self, message):
        
        for question, response in self.questions.items():
        
            if re.search(r'\b' + question + r'\b', message.lower()):
        
                return response
        
        return None

    def respond_to_farewell(self, message):
        
        for farewell in self.farewells:
        
            if re.search(r'\b' + farewell + r'\b', message.lower()):
        
                return 'Goodbye! Have a great day!'
        
        return None

    def get_bot_response(self, message):
        
        response = (self.respond_to_greeting(message) or
        
                    self.respond_to_question(message) or
        
                    self.respond_to_farewell(message) or
        
                    'Sorry, I don\'t understand that.')
        
        return response

    def run(self):
        
        print("Hello! I am your rule-based chatbot. Type 'QUIT' to end the conversation.")
        
        while True:
        
            user_input = input('PRITESH: ')
        
            if user_input.lower() == 'QUIT':
        
                print('Chatbot: Goodbye!')
        
                break
        
            response = self.get_bot_response(user_input)
        
            print(f'Chatbot: {response}')

if __name__ == '__main__':
    
    chatbot = RuleBasedChatbot()
    
    chatbot.run()
