class Company:
    def __init__(self, name, budget):
        self.name = name
        self._annual_budget = budget

    def get_budget(self):
        return self._annual_budget

    def set_budget(self, updated_budget):
        self._annual_budget = updated_budget

    def _internal_audit(self):
        print(f"Performing internal audit for {self.name}...")


miftahcoding = Company("MiftahCoding", 1000000)
print(miftahcoding.get_budget())
# print(miftahcoding._annual_budget) # discouraged
miftahcoding.name = "MiftahCoding Inc."
miftahcoding.set_budget(200000000)
print(miftahcoding.get_budget())
# miftahcoding._annual_budget = 20000000 # discouraged
