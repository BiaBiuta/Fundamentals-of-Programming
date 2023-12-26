import unittest

from business.service_d import Service_d
from domain.divice import Divice
from interfata.file_repo_divice import FileRepoDivice
from validare.validator_d import ValidatorDivice


class Teste(unittest.TestCase):
    def setUp(self):
        self.calea=r"C:\Users\bianc\PycharmProjects\FURTOS BIANCA\teste\teste.txt"
        self.__goleste_fisier(self.calea)
        self.repo=FileRepoDivice(self.calea)
        self.val_d=ValidatorDivice()
        self.service=Service_d(self.val_d,self.repo)
        self.__divice=Divice(1,"Samsung","tv","Lg")
        self.repo.adauga(self.__divice)
    def __goleste_fisier(self,calea):
        with open(calea,"w") as f:
            pass
    def test_get_all(self):
        self.assertEqual(self.repo.size(),0)

    def test_get_id(self):
        self.assertEqual(self.__divice.get_id_divice(),1)
    def test_get_type(self):
        self.assertEqual(self.__divice.get_type(),"tv")
    def test_get_brand(self):
        self.assertEqual(self.__divice.get_brand(),"Lg")
    def test_model_name(self):
        self.assertEqual(self.__divice.get_model_name(),"Samsung")

