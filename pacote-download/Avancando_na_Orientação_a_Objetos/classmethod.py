class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'


f1 = Funcionario()
print(f1.info())


class FolhaDePagamento:
    @staticmethod
    def log():
        return f'Isso é um log qualquer'
