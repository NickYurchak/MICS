from law_state import LawState

""" Стан: Створення законодавчої ініціативи """
class LegislativeInitiative(LawState):
    name = "Створення законодавчої ініціативи"
    allowed = ['Розгляд в профільному комітеті']
