def mostrar_capitais(paises_e_capitais):
	for chave,valor in paises_e_capitais.items():
		print(f"A capital de {chave} eh: {valor}")


paises_e_capitais={"Mozambique":"Maputo",
				"Angola":"Luanda",
				"EUA":"Washington DC",
				"Russia":"Moscovo"}
mostrar_capitais(paises_e_capitais)