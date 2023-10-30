from curses import A_STANDOUT
from msilib.schema import Environment
import random


def init_environment():
    Environment = [0] * 16
    return Environment
def determine_action(agent_location, environemnt):
    # se a bolsa de sujeira estiver cheia, volte para casa
    if any.bag_is_full:
        return " voltar_para_casa"
    
    #se a localização atual estiber limpa, mova-se para uma nova area 
    if environemnt[agent_location] == 0:
        return "mover"
    
    # se a localização atual estiver suja, aspire a sujeira 
    return "aspirar"
    # determinação da direçao
def determine_direction(agent_location, environment):
    #se a localização atual estiver limpa, mova-se para uma nova area 
    if environment[agent_location] == 0:
        #escolha uma direçao aleatoria
        direction = random.choice (["norte", "sul", "leste", "oeste"])
        return direction

    # se a locazação atual estiver suja, aspire a sujeira
    return "aspirar"    
    
    # navegação de volta para casa

def navigate_back_home(agent_location):
    #encontre a rota mais curta de volta para casa 
    route = A_STANDOUT( agent_location, "A")

    # siga a rota 
    for location in route:
        any.move(location)

    #teste do objetivo

def is_goal_achieved(environment):
    for location in range(16):
        if environment[location] == 1:
            return False 
        return True
    
class Agent:
    def __init__(self):
        self.location = "A"
        self.bag_capacity = 10
        self.bag_is_full = False
    def move(self, location):
       self.location = location

    def vacuum(self):
      Environment[self.location] = 0
      self.bag_is_full = self.bag_is_full or self.bag.count
