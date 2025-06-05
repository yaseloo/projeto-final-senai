import random

class Pergunta:
    def __init__(self, fase):
        self.num1 = random.randint(1, fase * 10)
        self.num2 = random.randint(1, fase * 10)
        self.operacao = random.choice(["+", "-", "*", "/"])
        
        if self.operacao == "/":
            self.num1 *= self.num2
        
        self.questao = f"{self.num1} {self.operacao} {self.num2}"
        self.resposta = eval(self.questao)

    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.isdigit() and int(resposta_usuario) == self.resposta
