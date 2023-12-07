from law_state import LawState

""" Підпис спікера ВРУ """
class SpeakerSignature(LawState):
    name = "Підпис спікера ВРУ"
    allowed = ['Підпис президента', 'Обговорення на засіданні ВРУ']
