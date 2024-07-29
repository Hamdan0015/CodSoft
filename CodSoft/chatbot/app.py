from flask import Flask, request, render_template
import re
import wikipedia
from datetime import datetime

app = Flask(__name__)

class SimpleChatBot:
    def __init__(self):
        wikipedia.set_lang('en')
        self.rules = {
            'hello': self.greet,
            'hi': self.greet,
            'how are you': self.status,
            'your name': self.name,
            'bye': self.goodbye,
            'what time is it': self.time,
            'what is the date': self.date,
            'who is': self.wiki_search,
            'what is': self.wiki_search,
            'tell me about': self.wiki_search,
            'best car': self.best_car,
            'weather': self.weather,
            'sports': self.sports,
            'famous person': self.famous_person,
            'technology': self.technology,
            'current events': self.current_events,
            'joke': self.joke,
            'news': self.news
        }

    def match_rule(self, message):
        for pattern, func in self.rules.items():
            if re.search(pattern, message, re.IGNORECASE):
                return func(message)
        return self.default_response()

    def greet(self, message=None):
        return "Hello! How can I assist you today?"

    def status(self, message=None):
        return "I'm just a bot, but I'm functioning as expected!"

    def name(self, message=None):
        return "I am your friendly chatbot!"

    def goodbye(self, message=None):
        return "Goodbye! Have a great day!"

    def time(self, message=None):
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."

    def date(self, message=None):
        today = datetime.today()
        return f"Today's date is {today.strftime('%Y-%m-%d')}."

    def wiki_search(self, message):
        topic = re.sub(r'(who is|what is|tell me about)', '', message, flags=re.IGNORECASE).strip()
        if not topic:
            return "I'm sorry, I didn't catch the topic. Could you please specify?"
        try:
            summary = wikipedia.summary(topic, sentences=1)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Your query is ambiguous. Please be more specific. Options include: {', '.join(e.options)}"
        except wikipedia.exceptions.PageError:
            return "I couldn't find any information on that topic."

    def best_car(self, message=None):
        return "There are many great cars in the world, and the 'best' car can be subjective. Popular choices include the Tesla Model S, Bugatti Chiron, and Ferrari LaFerrari."

    def weather(self, message=None):
        return "I currently do not have access to live weather data. You can check a weather website or app for the latest updates."

    def sports(self, message=None):
        return "For the latest sports scores and updates, please check a sports news website or app."

    def famous_person(self, message=None):
        return "There are many famous people! If you specify a name or a field (e.g., actors, scientists), I can provide more information."

    def technology(self, message=None):
        return "Technology is rapidly evolving. For the latest tech news, please visit technology news websites or tech blogs."

    def current_events(self, message=None):
        return "For current events and news updates, please refer to a news website or app."

    def joke(self, message=None):
        return "Why don't scientists trust atoms? Because they make up everything!"

    def news(self, message=None):
        return "For the latest news updates, please visit a news website or app."

    def default_response(self, message=None):
        return "I'm sorry, I didn't understand that. Can you please rephrase or provide more details?"

bot = SimpleChatBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = bot.match_rule(user_input.lower())
    return response

if __name__ == "__main__":
    app.run(debug=True)
