class ValidatorDivice:
    def __init__(self):
        pass
    def valideaza(self,divice):
        erori=""
        if divice.get_id_divice()<0:
            erori+="id invalid!\n"
        if divice.get_model_name()=="":
            erori += "model invalid!\n"
        if divice.get_type()==0:
            erori += "tip invalid!\n"

