from law_state import LawState

""" Винесення на голосування """
class Voting(LawState):
    name = "Винесення на голосування"
    allowed = ['Підпис спікера ВРУ', 'Розгляд в профільному комітеті']