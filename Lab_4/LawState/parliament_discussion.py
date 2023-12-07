from law_state import LawState

""" Обговорення на засіданні ВРУ """
class ParliamentDiscussion(LawState):
    name = "Обговорення на засіданні ВРУ"
    allowed = ['Винесення на голосування', 'Розгляд в профільному комітеті']