from typing import Self


class AgenteAspirador:
    def __init__(self):
        self.localizacao = "A"
        self.energia = 100
        self.bolsa_sujeira = 0

    def decidir_acao(self, ambiente):
        if self.bolsa_sujeira == 10 or self.energia == 0:
            return 'voltar para casa'
        elif ambiente.tem_sujeira(self.localizacao):
            return 'aspirar'
        else:
            return 'mover'
    def mover (self, ambiente):
        if self.localizacao in ambiente.localizacoes:

            indice_atual =  ambiente.localizacoes.index(self.localizacao)
        if indice_atual < len(ambiente.localizacoes) - 1:
            self.localizacao = ambiente.localizacoes[indice_atual + 1]
            self.energia -= 1
        else:
            self.localizacao = ambiente.localizacoes[0]
            self.energia -= 1 
            
        print("erro: Localizacao atual nao encontrada na lista de localizaçoes.")

    def voltar_para_casa(self):
        self.energia -= 1
        self.localizacao = 'A'
        self.bolsa_sujeira = 0

    def aspirar(self, ambiente):
        self.energia -= 1 
        ambiente.remover_sujeira(self.localizacao)
        self.bolsa_sujeira += 2

class ambiente:
    def __init__(self):
        self.localizacoes = [
            'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P',
        ]
        self.sujeira = {'D', 'H', 'J', 'L', 'N', 'P'}

    def tem_sujeira(self):
        return any in self.sujeira
    
    def remover_sujeira(self, localizacao):
        if any in self.sujeira:
            if any == 'voltarparacasa':
                AgenteAspirador.voltar_para_casa()
            elif any == 'aspirar':
                AgenteAspirador(ambiente)
            elif any == 'mover':
                any.mover(ambiente)

            print(f"localizaçao:{any.localizacao}, Energia: {any.energia}, bolsa de sujeira:{any.bolsa_suejeira}")