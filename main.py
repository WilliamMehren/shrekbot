import chatterbot as cb
from chatterbot.trainers import ListTrainer
#initiation
chatbot = cb.ChatBot("shrekbot")
#fil spor
paths=["data\shrek.txt","data\shrek2.txt","data\shrek3.txt","data\shrek4.txt","data\shrekmeta.txt"]

def Train():
    global chatbot
    global paths
    data = []
    #åpner hver fil, henter data
    for path in paths:
        file = open(path,"r")
        data+=file.readlines()
        file.close()
    #trener med dataen
    ListTrainer(chatbot).train(data)
        
Train()
#loop med enkel quit funksjon
exit_conditions = ("quit", "exit")
while True:
    query = input(": ")
    if query in exit_conditions:
        break
    else:
        print(f"🧅 {chatbot.get_response(query)}")