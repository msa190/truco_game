import truco_game
import jogador
import baralho

b = baralho.baralho_de_truco()
A = jogador.Jogador('A')
A.mao = baralho.Mao()
B = jogador.Jogador('B')
b.mao = baralho.Mao()

for i in range(3):
	A.mao.add_carta(b.pop())
	B.mao.add_carta(b.pop())
truco_game.jogo_de_truco(A,B)
