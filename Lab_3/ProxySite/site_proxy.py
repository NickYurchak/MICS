import time
from asite import ASite
from typing import Dict

# Клас SiteProxy, що реалізує ASite для кешування
class SiteProxy(ASite):
    def __init__(self, site: ASite):
        self.__site = site
        self.__cache: Dict[str, tuple] = {}

    def get_page(self, url: str) -> str:
        current_time = time.time()

        if url in self.__cache:
            cached_page, timestamp = self.__cache[url]
            if current_time - timestamp <= 10:  # Перевіряємо, чи сторінка ще "жива"
                return f"Отримана сторінка {url} із кешу: {cached_page}"

        page = self.__site.get_page(url)
        self.__cache[url] = (page, current_time)

        # Видалення сторінки з кешу після 10 секунд
        expired_pages = [key for key, (_, timestamp) in self.__cache.items() if current_time - timestamp > 10]
        for expired_page in expired_pages:
            del self.__cache[expired_page]

        return f"Отримана сторінка {url} з сайту: {page}"