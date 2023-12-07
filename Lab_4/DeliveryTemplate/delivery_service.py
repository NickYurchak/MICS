from abc import ABC, abstractmethod

# Базовий клас для доставки
class DeliveryService(ABC):
    def deliver_order(self):
        self.accept_order()
        confirmation = self.confirm_delivery()
        if confirmation:
            self.process_delivery()
            print("Доставка підтверджена. Замовлення закрите.")
        else:
            print("Доставка не підтверджена. Замовлення не закрите.")

    @abstractmethod
    def accept_order(self):
        pass

    def process_delivery(self):
        self.deliver()
        self.additional_service()

    @abstractmethod
    def deliver(self):
        pass

    def additional_service(self):
        pass

    @abstractmethod
    def confirm_delivery(self):
        pass
