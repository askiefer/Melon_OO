"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """Any melon order, globally."""

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_total(self):
        """Calculate price."""
        base_price = 5

        if self.species == "Christmas Melon":
            base_price = base_price * 1.5

        if self.order_type == "international" and self.qty < 10:
            flat_fee = 3.00
            total = ((1 + self.tax) * self.qty * base_price) + flat_fee

        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """U.S. government melon orders, tax exempt and security inspection"""

    def __init__(self, species, qty):
        """"""
        super(GovernmentMelonOrder, self).__init__(species, qty, "government", 0.0)
        self.passed_inspection = False

    def mark_inspection(self):
        """Passed security inspection."""
        self.passed_inspection = True
