
from mcpi.minecraft import Minecraft
import os, time

# configurando mundo indestrutivel
m = Minecraft.create()
m.setting("world_immutable",True)

# desenhando o cenario
m.setBlocks(0,3,0,144,3,144,1)
m.setBlocks(0,5,0,144,5,144,0)

# correção do mod
tempo = 0

# barreiras
for i in range(0,11):
	m.setBlocks(0,4,i*14,140,4,(i*14)+4,1)

for i in range(0,11):
	m.setBlocks(i*14,4,0,(i*14)+4,4,144,1)

# Ativadores
for i in range(0,11):
	m.setBlock(4,5,7+i*14,69,5)
	m.setBlock(4,5,9+i*14,69,5)
	m.setBlock(4,5,11+i*14,69,5)

# array do cenario (os circuitos)
cenario = {}
for i in range(1,101):
	cenario[int(i)] = ""

# array das ligações
ligados = []

# variaveis de quest
q = ""

# Lista de Ids:
# 55 - redstone
# 93 - repetidor desligado(94 ligado)
  # 0 - Norte
  # 1 - Leste
  # 2 - Sul
  # 3 - Oeste
# 1  - pedra
# 29 - pistão(aquele que empurra)
  # 0 - Baixo
  # 1 - Cima
  # 2 - Norte
  # 3 - Sul
  # 4 - Oeste
  # 5 - Leste
# 75 - tocha de redstone(76 ligado)
  # 0 - Baixo
  # 1 - Apontada para o Leste
  # 2 - Apontada para o Oeste
  # 3 - Apontada para o Sul
  # 4 - Apontada para o Norte
# 123 - lampada de redstone(124 ligado)
# 152 - bloco de redstone

def escreve(n):
	global m
	m.postToChat(n)
	time.sleep(.1)

def CLEAR(x,z):
	global m
	m.setBlocks(5+x,4,5+z,13+x,4,13+z,0)
	if x > 0:
		m.setBlocks(4+x,5,5+z,14+x,5,13+z,0)
	else:
		m.setBlocks(5+x,5,5+z,14+x,5,13+z,0)

# limpar o cenario quando o mod é iniciado
for i in range(0,11):
	for g in range(0,11):
		CLEAR(i*14,g*14)

def AND(x,z):
	global m
	CLEAR(x,z)
	m.setBlocks(5+x,4,5+z,13+x,4,13+z,41)
	m.setBlock(5+x,5,7+z,93,1)
	m.setBlock(5+x,5,11+z,93,1)
	m.setBlock(6+x,5,7+z,55)
	m.setBlock(6+x,5,8+z,93,2)
	m.setBlock(6+x,5,9+z,55)
	m.setBlock(6+x,5,10+z,93,0)
	m.setBlock(6+x,5,11+z,55)
	m.setBlock(7+x,5,7+z,93,1)
	m.setBlock(7+x,5,9+z,93,1)
	m.setBlock(7+x,5,11+z,93,1)
	m.setBlock(8+x,5,7+z,29,3)
	m.setBlock(8+x,5,8+z,1)
	m.setBlock(8+x,5,11+z,93,1)
	m.setBlock(9+x,5,9+z,93,1)
	m.setBlock(9+x,5,11+z,93,1)
	m.setBlock(10+x,5,10+z,1)
	m.setBlock(10+x,5,11+z,29,2)
	m.setBlock(11+x,5,9+z,93,1)
	m.setBlock(12+x,5,9+z,93,1)
	m.setBlock(13+x,5,9+z,93,1)
	# ligações
	m.setBlock(14+x,5,9+z,123)
	if x > 0:
		m.setBlock(4+x,5,7+z,1)
		m.setBlock(4+x,5,11+z,1)

def OR(x,z):
	global m
	CLEAR(x,z)
	m.setBlocks(5+x,4,5+z,13+x,4,13+z,57)
	m.setBlock(5+x,5,7+z,93,1)
	m.setBlock(5+x,5,11+z,93,1)
	m.setBlocks(6+x,5,7+z,6+x,5,11+z,55)
	m.setBlocks(7+x,5,9+z,12+x,5,9+z,55)
	m.setBlock(13+x,5,9+z,93,1)
	# ligações
	m.setBlock(14+x,5,9+z,123)
	if x > 0:
		m.setBlock(4+x,5,7+z,1)
		m.setBlock(4+x,5,11+z,1)

def NOT(x,z):
	global m
	CLEAR(x,z)
	m.setBlocks(5+x,4,5+z,13+x,4,13+z,49)
	m.setBlock(5+x,5,9+z,93,1)
	m.setBlocks(6+x,5,9+z,12+x,5,9+z,55)
	m.setBlock(11+x,5,9+z,93,1)
	m.setBlock(12+x,5,9+z,1)
	m.setBlock(13+x,5,9+z,76,1)
	# ligações
	m.setBlock(14+x,5,9+z,123)
	if x > 0:
		m.setBlock(4+x,5,9+z,1)

def NAND(x,z):
	global m
	CLEAR(x,z)
	m.setBlocks(5+x,4,5+z,13+x,4,13+z,42)
	m.setBlock(5+x,5,7+z,93,1)
	m.setBlock(5+x,5,11+z,93,1)
	m.setBlock(6+x,5,7+z,55)
	m.setBlock(6+x,5,8+z,93,2)
	m.setBlock(6+x,5,9+z,55)
	m.setBlock(6+x,5,10+z,93,0)
	m.setBlock(6+x,5,11+z,55)
	m.setBlock(7+x,5,7+z,93,1)
	m.setBlock(7+x,5,9+z,93,1)
	m.setBlock(7+x,5,11+z,93,1)
	m.setBlock(8+x,5,7+z,29,3)
	m.setBlock(8+x,5,8+z,1)
	m.setBlock(8+x,5,11+z,93,1)
	m.setBlock(9+x,5,9+z,93,1)
	m.setBlock(9+x,5,11+z,93,1)
	m.setBlock(10+x,5,10+z,1)
	m.setBlock(10+x,5,11+z,29,2)
	m.setBlock(11+x,5,9+z,93,1)
	m.setBlock(12+x,5,9+z,1)
	m.setBlock(13+x,5,9+z,76,1)
	# ligações
	m.setBlock(14+x,5,9+z,123)
	if x > 0:
		m.setBlock(4+x,5,7+z,1)
		m.setBlock(4+x,5,11+z,1)

def NOR(x,z):
	global m
	CLEAR(x,z)
	m.setBlocks(5+x,4,5+z,13+x,4,13+z,45)
	m.setBlock(5+x,5,7+z,93,1)
	m.setBlock(5+x,5,11+z,93,1)
	m.setBlocks(6+x,5,7+z,6+x,5,11+z,55)
	m.setBlocks(7+x,5,9+z,10+x,5,9+z,55)
	m.setBlock(11+x,5,9+z,93,1)
	m.setBlock(12+x,5,9+z,1)
	m.setBlock(13+x,5,9+z,76,1)
	# ligações
	m.setBlock(14+x,5,9+z,123)
	if x > 0:
		m.setBlock(4+x,5,7+z,1)
		m.setBlock(4+x,5,11+z,1)

def XOR(x,z):
	global m
	CLEAR(x,z)
	m.setBlocks(5+x,4,5+z,13+x,4,13+z,5)
	m.setBlock(5+x,5,7+z,29,3)
	m.setBlock(5+x,5,8+z,152)
	m.setBlock(5+x,5,11+z,55)
	m.setBlocks(5+x,5,12+z,13+x,5,12+z,55)
	m.setBlock(6+x,5,8+z,94,1)
	m.setBlock(6+x,5,9+z,93,1)
	m.setBlock(6+x,5,11+z,93,1)
	m.setBlock(7+x,5,11+z,29,2)
	m.setBlock(7+x,5,10+z,1)
	m.setBlock(7+x,5,8+z,1)
	m.setBlock(7+x,5,7+z,75,4)
	m.setBlocks(7+x,5,6+z,13+x,5,6+z,55)
	m.setBlock(8+x,5,9+z,93,1)
	m.setBlock(9+x,5,9+z,1)
	m.setBlock(10+x,5,9+z,75,1)
	m.setBlock(11+x,5,9+z,29,5)
	m.setBlock(13+x,5,9+z,1)
	m.setBlock(13+x,5,8+z,93,2)
	m.setBlock(13+x,5,10+z,93,0)
	m.setBlock(13+x,5,7+z,55)
	m.setBlock(13+x,5,11+z,55)
	# ligações
	m.setBlock(14+x,5,9+z,123)
	if x > 0:
		m.setBlock(4+x,5,7+z,1)
		m.setBlock(4+x,5,11+z,1)

def LED(x,z):
	global m
	CLEAR(x,z)
	m.setBlocks(5+x,4,5+z,13+x,4,13+z,123)
	m.setBlocks(6+x,4,6+z,12+x,4,12+z,55)
	# unica ligação
	m.setBlock(5+x,5,9+z,93,1)

def VERIFICAR(i):
	global m, cenario
	i = int(i)
	if cenario[i] != "":
		if m.getBlock((14+int((i-1)/10)*14),5,(9+int(((i-1)%10)*14))) == 124:
			return True
		else:
			return False
	else:
		return False

def TROCAR(i,valor):
	global m, cenario
	i = int(i)
	if cenario[i] != "":
		if int(valor) == 1:
			m.setBlock((14+int((i-1)/10)*14),5,(9+int(((i-1)%10)*14)),152)
		else:
			m.setBlock((14+int((i-1)/10)*14),5,(9+int(((i-1)%10)*14)),123)
		print("TROCADO: "+str(i)+" para "+str(valor))
	else:
		print("SEM CIRCUITO NO LOCAL "+str(i))

def ADMINISTRARLIGACOES():
	global ligados, cenario, m
	# Administrando ligações
	for i in ligados:
		if len(i) == 2:
			if cenario[i[1]] == "not":
				if m.getBlock((14+int((i[0]-1)/10)*14),5,(9+int(((i[0]-1)%10)*14))) == 124 or m.getBlock((14+int((i[0]-1)/10)*14),5,(9+int(((i[0]-1)%10)*14))) == 152:
					if m.getBlock((4+int((i[1]-1)/10)*14),5,(9+int(((i[1]-1)%10)*14))) != 152:
						m.setBlock((4+int((i[1]-1)/10)*14),5,(9+int(((i[1]-1)%10)*14)),152)
				else:
					m.setBlock((4+int((i[1]-1)/10)*14),5,(9+int(((i[1]-1)%10)*14)),1)
			else:
				escreve("CIRCUITO INVALIDO")
				ligados.remove(i)
		elif len(i) == 3:
			if cenario[i[1]] == "not":
				escreve("CIRCUITO INVALIDO")
				ligados.remove(i)
			else:
				if m.getBlock((14+int((i[0]-1)/10)*14),5,(9+int(((i[0]-1)%10)*14))) == 124 or m.getBlock((14+int((i[0]-1)/10)*14),5,(9+int(((i[0]-1)%10)*14))) == 152:
					if i[2] == 1:
						if m.getBlock((4+int((i[1]-1)/10)*14),5,(7+int(((i[1]-1)%10)*14))) != 152:
							m.setBlock((4+int((i[1]-1)/10)*14),5,(7+int(((i[1]-1)%10)*14)),152)
					elif i[2] == 2:
						if m.getBlock((4+int((i[1]-1)/10)*14),5,(11+int(((i[1]-1)%10)*14))) != 152:
							m.setBlock((4+int((i[1]-1)/10)*14),5,(11+int(((i[1]-1)%10)*14)),152)
					else:
						escreve("CIRCUITO INVALIDO")
						ligados.remove(i)
				else:
					if i[2] == 1:
						if m.getBlock((4+int((i[1]-1)/10)*14),5,(7+int(((i[1]-1)%10)*14))) != 1:
							m.setBlock((4+int((i[1]-1)/10)*14),5,(7+int(((i[1]-1)%10)*14)),1)
					elif i[2] == 2:
						if m.getBlock((4+int((i[1]-1)/10)*14),5,(11+int(((i[1]-1)%10)*14))) != 1:
							m.setBlock((4+int((i[1]-1)/10)*14),5,(11+int(((i[1]-1)%10)*14)),1)
					else:
						escreve("CIRCUITO INVALIDO")
						ligados.remove(i)
		else:
			ligados.remove(i)

print("RODANDO")

while True:
	tempo+=1
	if tempo > 200:
		tempo = 0
		m = Minecraft.create()
	# comandos mesmo
	for p in m.events.pollChatPosts():
		u = str(p.entityId).lower() # usuario
		p = str(p.message).lower()  # o que ele disse
		while p.find("  ") != -1:
			p.replace("  "," ")
		print("O JOGADOR \""+u+"\" DISSE \""+p+"\"")
		# comandos de instruções
		if p == "help" or p == "ajuda" or p == "?":
			escreve("LISTA DE COMANDOS : ")
			escreve("\"quest\" - para ver sistema de quests")
			escreve("\"val\" - para ver valores de variaveis")
			escreve("\"reset\" - para resetar o circuito")
			escreve("\"cir\" - para ver lista de circuitos")
			escreve("\"ligar\" - para ligar os circuitos")
			escreve("\"back\" - se teleportar para o ponto 0,0")
		# comando de limpar tudo
		if p.find(" ") != -1:
			if p == "clear all":
				try:
					ligados = []
					for i in range(0,11):
						for g in range(0,11):
							CLEAR(i*14,g*14)
					for i in range(1,101):
						cenario[i] = ""
					escreve("CENARIO LIMPO")
				except:
					escreve("ERRO NO COMANDO \"clear\"")
			# comando de limpar coisa especifica
			elif p[0] == "c" and p[1] == "l" and p[2] == "e" and p[3] == "a" and p[4] == "r" and p[5] == " " and len(p) <= 9 and len(p.split(" ")) == 2:
				try:
					n = int(p.split(" ")[1])
					if n > 0 and n < 101:
						cenario[n] = ""
						CLEAR(int((n-1)/10)*14,int(((n-1)%10)*14))
					else:
						escreve("LOCAL INVALIDO")
				except:
					escreve("COMANDO \"clear\" INVALIDO")
			# portas and
			elif p[0] == "a" and p[1] == "n" and p[2] == "d" and p[3] == " " and len(p) <= 7 and len(p.split(" ")) == 2:
				try:
					n = int(p.split(" ")[1])
					if n > 0 and n < 101:
						cenario[n] = "and"
						AND(int((n-1)/10)*14,int(((n-1)%10)*14))
					else:
						escreve("LOCAL INVALIDO")
				except:
					escreve("COMANDO \"and\" INVALIDO")
			# portas or
			elif p[0] == "o" and p[1] == "r" and p[2] == " " and len(p) <= 6 and len(p.split(" ")) == 2:
				try:
					n = int(p.split(" ")[1])
					if n > 0 and n < 101:
						cenario[n] = "or"
						OR(int((n-1)/10)*14,int(((n-1)%10)*14))
					else:
						escreve("LOCAL INVALIDO")
				except:
					escreve("COMANDO \"or\" INVALIDO")
			# portas not
			elif p[0] == "n" and p[1] == "o" and p[2] == "t" and p[3] == " " and len(p) <= 7 and len(p.split(" ")) == 2:
				try:
					n = int(p.split(" ")[1])
					if n > 0 and n < 101:
						cenario[n] = "not"
						NOT(int((n-1)/10)*14,int(((n-1)%10)*14))
					else:
						escreve("LOCAL INVALIDO")
				except:
					escreve("COMANDO \"not\" INVALIDO")
			# portas nand
			elif p[0] == "n" and p[1] == "a" and p[2] == "n" and p[3] == "d" and p[4] == " " and len(p) <= 8 and len(p.split(" ")) == 2:
				try:
					n = int(p.split(" ")[1])
					if n > 0 and n < 101:
						cenario[n] = "nand"
						NAND(int((n-1)/10)*14,int(((n-1)%10)*14))
					else:
						escreve("LOCAL INVALIDO")
				except:
					escreve("COMANDO \"nand\" INVALIDO")
			# portas nor
			elif p[0] == "n" and p[1] == "o" and p[2] == "r" and p[3] == " " and len(p) <= 7 and len(p.split(" ")) == 2:
				try:
					n = int(p.split(" ")[1])
					if n > 0 and n < 101:
						cenario[n] = "nor"
						NOR(int((n-1)/10)*14,int(((n-1)%10)*14))
					else:
						escreve("LOCAL INVALIDO")
				except:
					escreve("COMANDO \"nor\" INVALIDO")
			# portas xor
			elif p[0] == "x" and p[1] == "o" and p[2] == "r" and p[3] == " " and len(p) <= 7 and len(p.split(" ")) == 2:
				try:
					n = int(p.split(" ")[1])
					escreve("PORTA XOR AINDA INCOMPLETA")
					if n > 0 and n < 101:
						cenario[n] = "xor"
						XOR(int((n-1)/10)*14,int(((n-1)%10)*14))
					else:
						escreve("LOCAL INVALIDO")
				except:
					escreve("COMANDO \"xor\" INVALIDO")
			elif p[0] == "l" and p[1] == "e" and p[2] == "d" and p[3] == " " and len(p) <= 7 and len(p.split(" ")) == 2:
				escreve("LEDS VEM NO FUTURO")
			# sistema de ligações
			elif p[0] == "l" and p[1] == "i" and p[2] == "g" and p[3] == "a" and p[4] == "r" and p[5] == " " and (len(p.split(" ")) == 4 or len(p.split(" ")) == 3 or len(p.split(" ")) == 2):
				try:
					if len(p.split(" ")) == 2:
						if p.split(" ")[1] == "help":
							escreve("COMO USAR O LIGAR:")
							escreve("\"ligar\" <p1> <p2>[ <porta>] - conectar circuitos")
							escreve("\"desligar\" <p1> <p2>[ <porta>] - desconectar circuitos")
							escreve("\"ligar list\" - para visualizar lista de ligacoes")
						elif p.split(" ")[1] == "list":
							if len(ligados) > 0:
								escreve("LISTA DE LIGAS:")
								for i in ligados:
									if len(i) == 2:
										escreve("CIRCUITO "+str(i[0])+" AO CIRCUITO NOT "+str(i[1]))
									elif len(i) == 3:
										escreve("CIRCUITO "+str(i[0])+" AO CIRCUITO "+str(i[1])+" NA PORTA "+str(i[2]))
									else:
										ligados.remove(i)
							else:
								escreve("SEM LIGAS NOS CIRCUITOS")
						else:
							escreve("COMANDO \"ligar\" USADO INCORRETAMENTE")
					elif len(p.split(" ")) == 3:
						try:
							x1 = int(p.split(" ")[1])
							x2 = int(p.split(" ")[2])
							if cenario[x2] == "not":
								if x2 > 10 and x2 < 101:
									if x1 == x2:
										escreve("ISSO NAO FAZ SENTIDO")
									elif x1 > 0 and x1 < 101:
										ligados+=[(x1,x2)]
										escreve("LIGA CONFIRMADA")
									else:
										escreve("VALOR "+str(x1)+" INVALIDO")
								else:
									escreve("VALOR "+str(x2)+" INVALIDO")
							else:
								escreve("DEFINA A PORTA DE : "+str(x2))
						except:
							escreve("VALORES INVALIDOS")
					elif len(p.split(" ")) == 4:
						try:
							x1 = int(p.split(" ")[1])
							x2 = int(p.split(" ")[2])
							porta = int(p.split(" ")[3])
							if cenario[x2] == "not":
								escreve("O CIRCUITO "+str(x2)+" POSSUI APENAS UMA ENTRADA")
							elif cenario[x2] == "":
								escreve("SEM CIRCUITO EM "+str(x2))
							else:
								if x2 > 10 and x2 < 101:
									if x1 > 0 and x1 < 101:
										if porta == 1 or porta == 2:
											ligados+=[(x1,x2,porta)]
											escreve("LIGA CONFIRMADA")
										else:
											escreve("PORTA INVALIDA")
									else:
										escreve("VALOR "+str(x1)+" INVALIDO")
								else:
									escreve("VALOR "+str(x2)+" INVALIDO")
						except:
							escreve("VALORES INVALIDOS")
					else:
						escreve("COMANDO \"ligar\" INVALIDO")
				except:
					# desenhar as ligações no circuito
					if p.split(" ")[1] == "demonstrar":
						# COLOCAR AQUI COMANDO PARA LIMPAR LIGAÇÕES
						for i in ligados:
							if len(i) == 2:
								pass
							elif len(i) == 3:
								pass
							else:
								ligados.remove(i)
					else:
						escreve("COMANDO \"ligar\" USADO DE MANEIRA INCORRETA")
			# sistema para desligar ligações
			elif p[0] == "d" and p[1] == "e" and p[2] == "s" and p[3] == "l" and p[4] == "i" and p[5] == "g" and p[6] == "a" and p[7] == "r" and p[8] == " ":
				if len(p.split(" ")) == 3:
					try:
						n = (int(p.split(" ")[1]),int(p.split(" ")[2]))
						for i in ligados:
							if i == n:
								ligados.remove(i)
								escreve("FIM DA LIGA")
					except:
						escreve("NAO FOI ENCONTRADA LIGACAO")
				elif len(p.split(" ")) == 4:
					try:
						n = (int(p.split(" ")[1]),int(p.split(" ")[2]),int(p.split(" ")[3]))
						for i in ligados:
							if i == n:
								ligados.remove(i)
								escreve("FIM DA LIGA")
					except:
						escreve("NAO FOI ENCONTRADA LIGACAO")
				elif len(p.split(" ")) == 2:
					try:
						if p.split(" ")[1] == "all" or p.split(" ")[1] == "tudo":
							ligados = []
						else:
							escreve("COMANDO INEXISTENTE")
					except:
						escreve("ERRO PARA DELETAR LIGACAO")
				else:
					escreve("COMANDO \"desligar\" INVALIDO")
			# Sistema de Quests
			elif p[0] == "q" and p[1] == "u" and p[2] == "e" and p[3] == "s" and p[4] == "t" and p[5] == " " and len(p.split(" ")) == 2:
				try:
					if p.split(" ")[1] == "help":
						escreve("DIGITE:")
						escreve("quest <alguma_coisa>")
						escreve("")
						escreve("<alguma_coisa> PODE SER:")
						escreve("\"help\" - PARA AJUDA")
						escreve("<nome> - PARA SELECIONAR QUEST")
						escreve("\"out\" - PARA SAIR DA QUEST")
						escreve("\"end\" - PARA ENCERAR QUEST")
						escreve("\"list\" - PARA LISTAR QUESTS")
						escreve("\"status\" - QUEST ATUAL")
					# verificar se quest está encerrada
					elif p.split(" ")[1] == "end":
						if q != "":
							try:
								escreve("CORRIGINDO EXERCICIO...")
								i = open("quests\\"+q+".txt","r").read()
								i = i.replace("\n","")
								i = i.split("\"\"\"")
								resposta = True
								passou = False
								for n in i:
									if n.find(">R: ") == 0:
										passou = True
										if len(n.split(" ")) == 2:
											try:
												k = n.split(" ")[1]
												r = k.split(";")[1]
												p = k.split(";")[0]
												try:
													p = p.split(",")
													# trocar
													for j in p:
														if cenario[int(j.split(":")[0])] == "":
															resposta = False
														TROCAR(int(j.split(":")[0]),int(j.split(":")[1]))
													escreve("CORRIGINDO...")
													for i in range(0,10):
														ADMINISTRARLIGACOES()
														time.sleep(.5)
													# verificar
													if int(r.split(":")[1]) == 1:
														if VERIFICAR(int(r.split(":")[0])):
															pass
														else:
															resposta = False
													else:
														if VERIFICAR(int(r.split(":")[0])):
															resposta = False
														else:
															pass
													# destrocar
													for j in p:
														TROCAR(int(j.split(":")[0]),0)
												except:
													p = p.split(":")
													# trocar
													TROCAR(int(p[0]),int(p[1]))
													escreve("CORRIGINDO...")
													for i in range(0,10):
														ADMINISTRARLIGACOES()
														time.sleep(.5)
													# verificar
													if int(r.split(":")[1]) == 1:
														if VERIFICAR(int(r.split(":")[0])):
															pass
														else:
															resposta = False
													else:
														if VERIFICAR(int(r.split(":")[0])):
															resposta = False
														else:
															pass
													# detrocar
													TROCAR(int(p[0]),0)
												# dando da resposta
												if resposta == False:
													escreve("O CASO "+str(k)+" RESPOSTA ESTA CORRETA")
											except:
												escreve("FALHA PARA CORRIGIR")
								if passou == True:
									if resposta == False:
										escreve("A RESPOSTA ESTA CORRETA")
										q = ""
										escreve("SAINDO DO EXERCICIO")
									else:
										escreve("A RESPOSTA ESTA ERRADA")
							except:
								escreve("ERRO DURANTE A CHECAGEM")
						else:
							escreve("NENHUMA QUEST ATIVA NO MOMENTO")
					elif p.split(" ")[1] == "out":
						if q != "":
							escreve("SAINDO DA QUEST : \""+str(q)+"\"")
							q = ""
						else:
							escreve("NENHUMA QUEST ATIVA NO MOMENTO")
					elif p.split(" ")[1] == "list":
						a = os.listdir("quests/")
						if len(a) > 0:
							escreve("TEMOS "+str(len(a))+" QUESTS NO TOTAL:")
							for i in a:
								escreve(i.rstrip(".txt"))
					elif p.split(" ")[1] == "status":
						if q != "":
							escreve("QUEST ATUAL : "+str(q))
						else:
							escreve("NENHUMA QUEST ATIVA")
					else:
						a = os.listdir("quests/")
						if len(a) > 0:
							for i in a:
								if i.rstrip(".txt") == p.split(" ")[1]:
									q = i
									i = open("quests/"+q,"r").read()
									# correção de quebra de linha
									if i.find("\n") != -1:
										i = i.replace("\n","")
									# agora sim avaliamos:
									try:
										i = i.replace("'''","\"\"\"")
									except:
										pass
									try:
										enunciado = i.split("\"\"\"")[1]
										enunciado = enunciado.split("\n")
										for n in enunciado:
											if n != "":
												escreve(str(n))
									except:
										pass
						else:
							escreve("QUEST INVALIDA")
				except:
					escreve("COMANDO \"quest\" INVALIDO")
		# Comandos de Informação
		if p == "val" or p == "variaveis":
			escreve("LISTA DE VARIAVEIS :")
			# quests
			if q != "":
				escreve("QUEST ATUAL : "+str(q))
			else:
				escreve("SEM QUEST ATIVA")
			# quantidade de circuitos
			n = 0
			for i in cenario:
				if cenario[i] != "":
					n+=1
			if n == 1:
				escreve("UM CIRCUITO NO CENARIO")
			elif n > 1:
				escreve("CIRCUITOS NO CENARIO : "+str(n))
			else:
				escreve("CIRCUITO ESTA LIMPO")
			# ligações
			n = 0
			for i in ligados:
				n+=1
			if n == 0:
				escreve("SEM NENHUMA LIGACAO")
			elif n == 1:
				escreve("UMA UNICA LIGACAO")
			else:
				escreve("TEMOS "+str(n)+" LIGACOES")
		elif p == "back": # teleportar de volta para o cenario
			m.entity.setPos(u,0,6,0)
		elif p == "reset": # Limpar Cenario, Sair de Quests, Teleporte
			q = ""
			for i in range(0,11):
				for g in range(0,11):
					CLEAR(i*14,g*14)
			for i in range(1,101):
				cenario[i] = ""
			ligados = []
			m.entity.setPos(u,0,6,0)
			escreve("CENARIO RESETADO")
		elif p == "cir": # listar circuitos possiveis
			escreve("LISTA DE CIRCUITOS : ")
			escreve("\"and <n>\" - n a posicao do circuito")
			escreve("\"or <n>\" - n a posicao do circuito")
			escreve("\"not <n>\" - n a posicao do circuito")
			escreve("\"nand <n>\" - n a posicao do circuito")
			escreve("\"nor <n>\" - n a posicao do circuito")
			escreve("\"xor <n>\" - n a posicao do circuito")
		elif p == "quest": # só um auxilio
			escreve("Digite \"quest help\" para ver comandos")
		elif p == "ligar":
			escreve("Digite \"ligar help\" para ver comandos")
	# Executando Quests
	if q != "":
		if q.find(".txt") != -1: # executar configurações basicas
			i = open("quests/"+q,"r").read()
			i = i.replace("\n","")
			i = i.split("\"\"\"")
			p = 0
			e = [0,0]
			novidade = {}
			for n in i:
				if n.find("POSICAO: ") == 0:
					if len(n.split(" ")) == 2:
						try:
							p = int(n.split(" ")[1])
						except:
							escreve("ERRO NO VALOR DE POSICAO EM QUESTS")
					else:
						escreve("ERRO NO ARQUIVO QUESTS: "+str(q))
						escreve("ERRO EM POSICAO")
				else:
					pass
				if n.find("CENARIO: ") == 0:
					if len(n.split(" ")) == 2:
						try:
							e = [int(n.split(" ")[1].split("x")[0]),int(n.split(" ")[1].split("x")[1])]
						except:
							escreve("ERRO NO VALOR DE CENARIO EM QUESTS")
					else:
						escreve("ERRO NA VARIAVEL CENARIO DE ARQUIVO QUESTS: "+str(q))
						escreve("ERRO EM CENARIO")
				else:
					pass
				if n.find(">C:") == 0:
					if len(n.split(" ")) == 2:
						if n.find(">C:AND: ") == 0:
							try:
								n = int(n.split(" ")[1])
								novidade[n] = "and"
							except:
								pass
						elif n.find(">C:OR: ") == 0:
							try:
								n = int(n.split(" ")[1])
								novidade[n] = "or"
							except:
								pass
						elif n.find(">C:NOR: ") == 0:
							try:
								n = int(n.split(" ")[1])
								novidade[n] = "nor"
							except:
								pass
						elif n.find(">C:NAND: ") == 0:
							try:
								n = int(n.split(" ")[1])
								novidade[n] = "nand"
							except:
								pass
						elif n.find(">C:XOR: ") == 0:
							try:
								n = int(n.split(" ")[1])
								novidade[n] = "xor"
							except:
								pass
						elif n.find(">C:NOT: ") == 0:
							try:
								n = int(n.split(" ")[1])
								novidade[n] = "not"
							except:
								pass
					else:
						pass
				else:
					pass
			if p == 0 or e[0] == 0 or e[1] == 0:
				escreve("ERRO NO RECONHECIMENTO DE VARIAVEIS DO ARQUIVO QUESTS: "+str(q))
				q = ""
			else:
				if p >= 1 or p <= 100:
					if e[0] >= 1 and e[0] <= 10 and e[1] >= 1 and e[1] <= 10:
						# limpar cenario
						for a in range(p,e[0]+1):
							for b in range(p-1,e[1]+1):
								c = a+b*10
								CLEAR(int((c-1)/10)*14,int(((c-1)%10)*14))
								# limpar ligações
								for d in ligados:
									if d[0] == c or d[1] == c:
										ligados.remove(d)
						if len(novidade) > 0:
							for a in novidade:
								if novidade[a] == "and":
									cenario[a] = "and"
									AND(int((a-1)/10)*14,int(((a-1)%10)*14))
								elif novidade[a] == "or":
									cenario[a] = "or"
									OR(int((a-1)/10)*14,int(((a-1)%10)*14))
								elif novidade[a] == "not":
									cenario[a] = "not"
									NOT(int((a-1)/10)*14,int(((a-1)%10)*14))
								elif novidade[a] == "nor":
									cenario[a] = "nor"
									NOR(int((a-1)/10)*14,int(((a-1)%10)*14))
								elif novidade[a] == "nand":
									cenario[a] = "nand"
									NAND(int((a-1)/10)*14,int(((a-1)%10)*14))
								elif novidade[a] == "xor":
									cenario[a] = "xor"
									XOR(int((a-1)/10)*14,int(((a-1)%10)*14))
						q = q.rstrip(".txt")
						# posicionar coisas
					else:
						escreve("ERRO NO VALOR DE CENARIO: "+str(e))
						q = ""
				else:
					escreve("ERRO NO VALOR DE POSICAO: "+str(p))
					q = ""
	# administrar ligações
	ADMINISTRARLIGACOES()

print("MOD FOI FINALIZADO")

'''

PROBLEMAS:
- Ainda não é possivel saber visualmente quais circuitos estão
conectados e isso acaba deixando dificil pra certas pessoas como
esta a situação do circuito no momento.
- Deixar as respostas de exercicios mais escandalosas, como o
titulo de que ele acertou a resposta e coisas assim.
- Otimizar a leitura de arquivos do sistema de quests a fim de
diminuir ao maximo o numero de erros numa leitura.

BUGS AINDA PRESENTES:
- Durante a correção de exercicios, não é possivel realizar
comandos por parte dos jogadores.

PROBLEMAS/BUGS RESOLVIDOS:
- Antes o principal problema era que depois de alguns comandos o
codigo simplesmente parava de receber informações do jogador, mas
isso foi resolvido tirando a parte da redefinição da variavel 'm'
de dentro do Loop. Eu resolvi isso resetando a variavel apenas a
cada 200 execuções não sobrecarregando mais o mod.
- Antes o sistema de correção de quests não funcionava, por duas
causas principais, primeiro era a necessidade de um temporizador
para dar tempo para os circuitos se modificarem dependendo das
entradas, e o outro era que, já que o sistema de ligações atual
foi feito apenas com programação e era executado no final de cada
loop, os circuitos não eram modificados por causa que o código na
correção ficava travado na mesma parte, então eu transformei a
parte de ligações numa função para chamar ela antes de conferir
as respostas.
- Houve alguns problemas no sistema de verificação de blocos do
circuito que comprometeram o mod durante a limpeza de circuitos
de cada posição. Já resolvidos.
- Concluir o circuito XOR.

'''
