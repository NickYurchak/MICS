from law_state import LawState

""" Стан: Розгляд в профільному комітеті """
class CommitteeConsideration(LawState):
    name = "Розгляд в профільному комітеті"
    allowed = ['Обговорення на засіданні ВРУ']
