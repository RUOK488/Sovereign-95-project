class TariffCalculator:
    def __init__(self, fixed_charge: float = 50.0):
        self.fixed_charge = fixed_charge

    def calculate_bill(self, units: float) -> dict:
        if units < 0:
            raise ValueError("Units consumed cannot be negative.")
        charge = 0.0
        breakdown = {}
        slab1_units = min(units, 100)
        slab1_cost = slab1_units * 3.50
        charge += slab1_cost
        breakdown["0-100 Units"] = slab1_cost
        if units > 100:
            slab2_units = min(units - 100, 200)
            slab2_cost = slab2_units * 5.50
            charge += slab2_cost
            breakdown["101-300 Units"] = slab2_cost
        if units > 300:
            slab3_units = units - 300
            slab3_cost = slab3_units * 8.00
            charge += slab3_cost
            breakdown[">300 Units"] = slab3_cost
        total_amount = charge + self.fixed_charge
        breakdown["Fixed Charge"] = self.fixed_charge
        breakdown["Total Bill"] = total_amount
        return breakdown
