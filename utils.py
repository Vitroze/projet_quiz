from dotenv import load_dotenv
import os

questions = [
    ["Quel mot-clé définit une fonction en Python ?", "def"],
    ["Quel port utilise HTTPS ?", "443"],
    ["Quel protocole permet de se connecter à distance de façon sécurisée ?", "SSH"],
    ["Combien de bits dans un octet ?", "8"],
    ["Quel type Python représente vrai ou faux ?", "bool"],
    ["Quelle est la capitale de la France ?", "Paris"],
]
        
class QuizManagment:
    def __init__(self, name_user):
        self.name = name_user
        self.anwser_quiz = 0
        self.responses = []
        
    def good(self):
        self.anwser_quiz = (self.anwser_quiz or 0) + 1
    
    def bad(self):
        self.anwser_quiz = max((self.anwser_quiz or 0) - 1, 0)
        
    def add(self, r):
        self.responses.append(r)
        
    def send_question(self, id):
        response = input(f"Question n°{id} : {questions[id][0]}")
        self.add(response)
        if questions[id] and questions[id][1] == response:
            self.good()
        else:
            self.bad()
       
load_dotenv()

def is_good_admin(response):
    return response == os.getenv("admin_mdp")
    