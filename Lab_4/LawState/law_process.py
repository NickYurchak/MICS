from legislative_initiative import LegislativeInitiative

""" Клас, який представляє законодавчий процес """
class LawProcess(object):
    def __init__(self, title):
        self.title = title
        # Стан закону - за замовчуванням це стан "Створення законодавчої ініціативи".
        self.state = LegislativeInitiative()

    def handle(self, state):
        """ Змінити стан """
        self.state.switch(state)
