# This is a sample Python script.
from business.service_d import Service_d
from consola.ui import UI
from interfata.file_repo_divice import FileRepoDivice
from interfata.repo_d import RepoDivice
from validare.validator_d import ValidatorDivice


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__=='__main__':
   calea="fisier.txt"
   repo_d=FileRepoDivice(calea)
   val_d=ValidatorDivice()
   service_d=Service_d(val_d,repo_d)
   consola=UI(service_d)
   consola.run()