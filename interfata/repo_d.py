class RepoDivice:
    def __init__(self):
        self._divice={}
        self._operatie={}
    def get_all(self):
        return [x for x in self._divice.values()]
    def size(self):
        return len(self._divice)
    def adauga(self,divice):
        self._divice[divice.get_id_divice()]=divice
    def get_all_1(self):
        return [x for x in self._operatie.values()]