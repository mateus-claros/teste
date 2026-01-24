import random
import os
import time

class Carta:
    def __init__(self, simbolo: str):
        self.simbolo = simbolo
        self.virada = False
        self.encontrada = False

    def revelar(self):
        if not self.encontrada:
            self.virada = True

    def esconder(self):
        if not self.encontrada:
            self.virada = False

    def marcar_encontrada(self):
        self.encontrada = True
        self.virada = True


class JogoDaMemoria:
    def __init__(self, pares=8):
        # escolha de símbolos (pode aumentar)
        simbolos = ["🍕", "🍔", "🍟", "🍩", "🍎", "🍇", "🐶", "🐱", "⚽", "🎮", "🚗", "🎧"]
        if pares > len(simbolos):
            raise ValueError("Aumente a lista de símbolos ou diminua a quantidade de pares.")

        escolhidos = simbolos[:pares]
        baralho = escolhidos + escolhidos  # duplica para formar pares
        random.shuffle(baralho)

        self.cartas = [Carta(s) for s in baralho]  # objetos Carta
        self.tentativas = 0
        self.acertos = 0

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_tabuleiro(self):
        print("=== JOGO DA MEMÓRIA (Terminal) ===")
        print(f"Tentativas: {self.tentativas} | Pares encontrados: {self.acertos}\n")

        # Mostrar como grade de 4 colunas
        cols = 4
        for i, carta in enumerate(self.cartas):
            if carta.virada or carta.encontrada:
                conteudo = carta.simbolo
            else:
                conteudo = "❓"

            print(f"{i:02d}:{conteudo}", end="   ")

            if (i + 1) % cols == 0:
                print()
        print("\n")

    def escolher_posicao(self, msg: str) -> int:
        while True:
            valor = input(msg).strip()
            if not valor.isdigit():
                print("Digite um número válido (ex: 0, 1, 2...).")
                continue

            pos = int(valor)
            if pos < 0 or pos >= len(self.cartas):
                print("Posição fora do tabuleiro.")
                continue

            carta = self.cartas[pos]
            if carta.encontrada:
                print("Essa carta já foi encontrada. Escolha outra.")
                continue

            return pos

    def terminou(self) -> bool:
        return self.acertos == len(self.cartas) // 2

    def jogar(self):
        while not self.terminou():
            self.limpar_tela()
            self.mostrar_tabuleiro()

            p1 = self.escolher_posicao("Escolha a 1ª carta (índice): ")
            self.cartas[p1].revelar()

            self.limpar_tela()
            self.mostrar_tabuleiro()

            p2 = self.escolher_posicao("Escolha a 2ª carta (índice): ")
            if p2 == p1:
                print("Você escolheu a mesma carta. Tente de novo.")
                time.sleep(1)
                self.cartas[p1].esconder()
                continue

            self.cartas[p2].revelar()
            self.tentativas += 1

            self.limpar_tela()
            self.mostrar_tabuleiro()

            c1 = self.cartas[p1]
            c2 = self.cartas[p2]

            if c1.simbolo == c2.simbolo:
                print("✅ Par encontrado!")
                c1.marcar_encontrada()
                c2.marcar_encontrada()
                self.acertos += 1
                time.sleep(1)
            else:
                print("❌ Não foi dessa vez...")
                time.sleep(1.2)
                c1.esconder()
                c2.esconder()

        self.limpar_tela()
        self.mostrar_tabuleiro()
        print("🎉 Você terminou o jogo!")
        print(f"Total de tentativas: {self.tentativas}")


if __name__ == "__main__":
    jogo = JogoDaMemoria(pares=8)  # mude para 4, 6, 10...
    jogo.jogar()
