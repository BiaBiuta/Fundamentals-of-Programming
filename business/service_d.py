class Service_d:
    def __init__(self,val_d,file_repo_d):
        self.__val_d=val_d
        self.__file_repo_d=file_repo_d
    def get_all(self):
        return self.__file_repo_d.get_all()
    def cauta_dupa_tip(self,type):
        divices=self.__file_repo_d.get_all()
        divice_gasit=[]
        for divice in divices:
            if divice.get_type()==type:
                divice_gasit.append(divice)
        return divice_gasit
    def nr_divice_uri(self,type,brand):
        divices=self.__file_repo_d.get_all()
        divices_cu_type=[x for x in divices if x.get_type()==type]
        divices_cu_tip_brand=[x for x in divices_cu_type if x.get_brand()==brand]
        lista_id=[]
        for x in divices_cu_tip_brand:
            lista_id.append(x.get_id_divice())
        operatiuni=self.__file_repo_d.get_all_1()

        operatii_gasite=[]
        for operatiune in operatiuni:
            for id in lista_id:
                if operatiune.get_id_divice()==id:
                    operatii_gasite.append(operatiune)
        lista_numere=[]
        nr=0
        for operatie in operatii_gasite:
            if operatie.get_operation()=="supply":
                nr=nr+operatie.get_nr_divice()
            elif operatie.get_operation()=="sale":
                nr=nr-operatie.get_nr_divice()
        lista_numere.append(nr)

        return lista_numere