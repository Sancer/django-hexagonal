class Criteria:
    def __init__(self, filters, order=None, offset=None, limit=None):
        self.filters = filters
        self.order = order
        self.offset = offset
        self.limit = limit

    @staticmethod
    def create_empty():
        return Criteria(Filters.from_values([]), None, None, None)

    def has_filters(self):
        return not self.filters.is_empty()

    def filters(self):
        return self.filters

    def order(self):
        return self.order

    def offset(self):
        return self.offset

    def limit(self):
        return self.limit

    def has_order(self):
        return self.order is not None
