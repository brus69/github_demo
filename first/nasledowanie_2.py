class StoreItem:
    def calculate(self, count):
        return self._calculate_tax(count) + (count * 100)

    def _calculate_tax(self, count):
        return 0

class StoreItemInternation(StoreItem)
    def _calculate_tax(self, count):
        return count * 0.5
item = StoreItemInternation()
item.calculate(10)