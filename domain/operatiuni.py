class Operatiune:
    def __init__(self,id_divice,nr_divice,operation):
        #self.__id_operatie=id_operatie
        self.__id_divice=id_divice
        self.__nr_divice=nr_divice
        self.__operation=operation
    def get_nr_divice(self):
        return self.__nr_divice
    def get_operation(self):
        return self.__operation
    def get_id_divice(self):
        return self.__id_divice
    def __str__(self):
        return f"{self.__id_divice},{self.__nr_divice},{self.__operation}"
