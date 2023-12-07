from asite import ASite

# Клас Site, що реалізує ASite
class Site(ASite):
    def get_page(self, url: str) -> str:
        return f"Тут вміст сторінки {url}"