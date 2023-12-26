from erori.repoerror import RepoError
from erori.validationerror import ValidError


class UI:
    def __init__(self,service):
        self.__service=service
        self.__comenzi={"get_all":self.get_all,
                        "divice_gasit":self.__divice_gasit,
                        "nr_divice":self.__nr_divice}

   # the function brings all the elements from the file
    def get_all(self):
        divices=self.__service.get_all()
        for divice in divices:
            print(divice)
    #the function finds a device of a certain type
    #params->type
    def __divice_gasit(self):
        type=self.__params[0]
        divice_gasit=self.__service.cauta_dupa_tip(type)
        for divice in divice_gasit:
            print(divice)
    # the function checks how many items of a certain type we have in the warehouse at the end
    # of the day after the sale and addition
    #params ->type and brand
    def __nr_divice(self):
        type=self.__params[0]
        brand=self.__params[1]
        lista_numere=self.__service.nr_divice_uri(type,brand)

        for nr in lista_numere:
            print(nr)
    #the commands are given with their names saved in a dictionary
    # separated by commas from the parameters
    def run(self):
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == " ":
                continue
            if comanda == "exit":
                return
            parti = comanda.split(",")
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("Eroare UI :tip numeric invalid!")
                except ValidError as ve:
                    print(f"ValidError{ve}")
                except RepoError as re:
                    print(f"RepoError:{re}")
            else:
                print("comanda invalida!")