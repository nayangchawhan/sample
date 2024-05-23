import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class MedicalAssistant:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.responses = {
            'greeting': 'Hello! How can I assist you today?',
            'symptoms': 'Please describe your symptoms in detail.',
            'pain': 'Pain can be caused by various conditions. Can you specify where you are feeling the pain?',
            'fever': 'A fever can be a sign of infection. Have you taken any medication?',
            'cough': 'Coughing can be caused by allergies, infections, or other conditions. Are you experiencing any other symptoms?',
            'headache': 'Headaches can be caused by stress, dehydration, or other factors. Have you tried resting or drinking water?',
            'nausea': 'Nausea can be caused by many things, including food, infection, or motion sickness. Are you experiencing any vomiting?',
            'dizziness': 'Dizziness can be due to low blood pressure, dehydration, or other issues. Are you feeling light-headed or faint?',
            'default': 'I am sorry, I do not understand your request. Can you please rephrase?',
            'No':'Please consult a docter soon',
            'dolo 650' : 'It raises pain threshold, not only used for fevers, it can be used for musculoskeletal pains like neck pains, backache, osteoarthritic, kind of pains as well as headaches like migraine.',
            'diclofinac' : 'Diclofenac is a nonsteroidal anti-inflammatory drug (NSAID) used to treat mild-to-moderate pain, and helps to relieve symptoms of arthritis (eg, osteoarthritis or rheumatoid arthritis), such as inflammation, swelling, stiffness, and joint pain.',
            'cetirizine' : 'Cetirizine is used to temporarily relieve the symptoms of hay fever (allergy to pollen, dust, or other substances in the air) and allergy to other substances (such as dust mites, animal dander, cockroaches, and molds). These symptoms include sneezing; runny nose; itchy, red, watery eyes; and itchy nose or throat.'
        }

    def preprocess(self, sentence):
        tokens = word_tokenize(sentence)
        tokens = [self.lemmatizer.lemmatize(word.lower()) for word in tokens if word.isalpha() and word.lower() not in self.stop_words]
        return tokens

    def classify_intent(self, tokens):
        if any(word in tokens for word in ['hello', 'hi', 'hey']):
            return 'greeting'
        elif any(word in tokens for word in ['pain']):
            return 'pain'
        elif any(word in tokens for word in ['fever']):
            return 'fever'
        elif any(word in tokens for word in ['cough']):
            return 'cough'
        elif any(word in tokens for word in ['headache']):
            return 'headache'
        elif any(word in tokens for word in ['nausea']):
            return 'nausea'
        elif any(word in tokens for word in ['dizziness']):
            return 'dizziness'
        elif any(word in tokens for word in ['No']):
            return 'No'
        elif any(word in tokens for word in ['dolo', '650']):
            return 'Dolo 650'
        elif any(word in tokens for word in ['diclofinac']):
            return 'Diclofinac'
        elif any(word in tokens for word in ['cetirizine']):
            return 'Cetirizine'
        else:
            return 'default'

    def get_response(self, user_input):
        tokens = self.preprocess(user_input)
        intent = self.classify_intent(tokens)
        return self.responses[intent]

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Assistant")
        self.geometry("400x400")
        self.assistant = MedicalAssistant()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Ask me anything about your health:", pady=10)
        self.label.pack()

        self.user_input = tk.Entry(self, width=50)
        self.user_input.pack()

        self.response_box = scrolledtext.ScrolledText(self, width=50, height=15)
        self.response_box.pack()

        self.ask_button = tk.Button(self, text="Ask", command=self.get_assistant_response)
        self.ask_button.pack()

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack()

    def get_assistant_response(self):
        user_input = self.user_input.get()
        if user_input:
            response = self.assistant.get_response(user_input)
            self.response_box.insert(tk.END, "You: " + user_input + "\n")
            self.response_box.insert(tk.END, "Assistant: " + response + "\n\n")
            self.user_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a question.")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
