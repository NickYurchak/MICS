from delivery_service import DeliveryService

# Клас, що розширює базовий алгоритм доставки
class UpgradedDeliveryService(DeliveryService):
    def accept_order(self):
        print("Замовлення прийняте. Ваші побажання будуть опрацьовані перед доставкою.")

    def deliver(self):
        print("Товар доставлений.")

    def additional_service(self):
        if self.wants_technical_support():
            print("Виконується технічна підтримка.")
        if self.wants_large_item_delivery():
            print("Виконується доставка великогабаритної техніки.")
        if self.wants_configure_computer():
            print("Виконується налаштування комп’ютерної техніки.")

    def confirm_delivery(self):
        answer = input("Чи підтверджуєте доставку? (Y/N): ")
        return answer.upper() == 'Y'

    def wants_technical_support(self):
        answer = input("Чи потрібна технічна підтримка? (Y/N): ")
        return answer.upper() == 'Y'

    def wants_large_item_delivery(self):
        answer = input("Чи потрібна доставка великогабаритної техніки? (Y/N): ")
        return answer.upper() == 'Y'

    def wants_configure_computer(self):
        answer = input("Чи потрібне налаштування комп’ютерної техніки? (Y/N): ")
        return answer.upper() == 'Y'
