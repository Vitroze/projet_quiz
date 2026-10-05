def percentage(s, n):
    return s / n * 100

def l():
    f = open("scores.txt")
    t = []
    for x in f.readlines():
        t.append(int(x))
    return t

import os
def save(all_users, number_question):
    fileSystem = None
    
    is_exist = os.path.exists("scores.csv")
    
    fileSystem = open("scores.csv", "a")
    if not is_exist:
        fileSystem.write("User, Score")
    
    for user in all_users:
        fileSystem.write(f"{user.name}, {percentage(user.anwser_quiz, number_question)}")