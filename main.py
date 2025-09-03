meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GG": "una expresion de buena partida o buen juego",
            "XD": "es una expresion para decir que gracioso",
            }


Meme = input("Escribe una palabra que no entiendas (¡todo con mayúsculas!): ")


if Meme in meme_dict.keys():
    print(meme_dict[Meme])
else:
    print("esa palabra no la tenemos")
