import sys

import dns.resolver

resolver = dns.resolver.Resolver()

try:
	alvo = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print("Está faltando argumentos")
	sys.exit()

try:

	with open(wordlist, "r") as file:
		subdominios = file.read().splitlines()
except:
	print("Erro ao abrir o arquivo")
	sys.exit()

for subdominio in subdominios:
	try:
		sub_alvo = f"{subdominio}.{alvo}"
		resultados = resolver.resolve(sub_alvo, "A")
		for resultado in resultados:
			print(f"{sub_alvo} -> {resultado}")
	except:
		print("Subdominio não existe")
