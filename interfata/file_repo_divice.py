from domain.operatiuni import Operatiune
from domain.divice import Divice
from interfata.repo_d import RepoDivice


class FileRepoDivice(RepoDivice):
    def __init__(self,calea):
        self.__calea=calea
        RepoDivice.__init__(self)
    def __read_all_from_file(self):
        with open (self.__calea,"r") as f:
            lines=f.readlines()
            self._divice.clear()
            for line in lines:
                line=line.strip()
                if line!="":
                    parts=line.split(",")
                    id_divice=int(parts[0])
                    model_name=parts[1]
                    type=parts[2]
                    brand=parts[3]
                    divice=Divice(id_divice,model_name,type,brand)
                    nr_divices=int(parts[4])
                    operation=parts[5]
                    operatiune=Operatiune(id_divice,nr_divices,operation)
                    self._operatie[id_divice]=operatiune
                    self._divice[id_divice]=divice
    def __write_all_from_file(self):
        with open(self.__calea,"w") as f:
            for divice in  self._divice.values():
                f.write(str(divice)+"\n")
    def get_all(self):
        self.__read_all_from_file()
        return RepoDivice.get_all(self)
    def size(self):
        self.__read_all_from_file()
        return RepoDivice.size(self)
    def adauga(self,divice):
        self.__read_all_from_file()
        return RepoDivice.adauga(self,divice)
        self.__write_all_from_file()
    def get_all_1(self):
        self.__read_all_from_file()
        return RepoDivice.get_all_1(self)
