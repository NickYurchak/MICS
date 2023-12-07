from law_state import LawState

""" Підпис президента """
class PresidentSignature(LawState):
    name = "Підпис президента"
    allowed = ['Оприлюднення', 'Обговорення на засіданні ВРУ']