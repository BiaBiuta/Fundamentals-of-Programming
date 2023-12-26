class Divice:
    def __init__(self,id_divice,model_name,type,brand):
        self.__id_divice=id_divice
        self.__model_name=model_name
        self.__type=type
        self.__brand=brand
       #self.__nr_divice=nr_divice
        #self.__operation=operation
    def get_id_divice(self):
        return self.__id_divice
    def get_model_name(self):
        return self.__model_name
    def get_type(self):
        return self.__type
    def get_brand(self):
        return self.__brand
    '''def get_nr_divice(self):
        return self.__nr_divice
    def get_operation(self):
        return self.__operation
    def set_operation(self,operation):
        self.__operation=operation
        return self'''
    def __str__(self):
        return f"{self.__id_divice},{self.__model_name},{self.__type},{self.__brand}"