class Cliente:
    def __init__(self,nome):
        self.__nome = nome

    @property #chamar o método sem parenteses e com o mesmo nome do atríbuto
    def nome(self):
        return self.__nome.title()

    @nome.setter #nome do atributo em questão e é definido que ele é um setter. É feito isso pois os nomes estão iguais
    def nome(self,nome):
        self.__nome = nome