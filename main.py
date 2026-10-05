from functions import *
from utils import *
import os

def request_name(id_player):
    return input(f"Nom du joueur {id_player} :")

def request_number(question):
    number_question = input(question)
    if not number_question.isdigit() or int(number_question) <= 0:
        return request_number(question)
    
    return int(number_question)


print("=== QUIZ ===")
number_user = request_number("Combien d'utilisateur participe au jeu ?")

all_users = []
for id in range(number_user):
    all_users.append(QuizManagment(request_name(id)))

if is_good_admin(input("Code admin (entrée pour passer) : ")):
    for question in questions:
        print(question[0], "->", question[1])
else:
    print("Mauvais mot de passe")


number_question = request_number("Combien de questions par joueur ? ")

def manage_tour(object_user):
    print(f"--- Tour de {object_user.name} ---")
    anwser = 0
    
    while anwser < number_question:
        object_user.send_question(anwser)
        anwser += 1
        
for user in all_users:
    os.system("clear")
    manage_tour(user)

print("=== RESULTATS ===")
for user in all_users:
    print(f"Réponses de {user.name} : {user.responses}")
    print(f"{user.anwser_quiz} points, {percentage(user.anwser_quiz, number_question)}% de réussite")

save(all_users, number_question)