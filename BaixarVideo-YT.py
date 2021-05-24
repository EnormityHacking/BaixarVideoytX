try:
      from pytube import YouTube as youtube
except:
      print('Módulo não encontrado! instale-o ! ')

# Digite o link do vídeo e o local que deseja salvar o video  #
print("	\033[1;97mDOWNLOADER VIDEO YOUTUBE")
print("Cole o Link, Depois, Escolha o Local Para Salva-lo")
print("	\033[1;92m")
print("║█║▌║█║▌│║▌█║▌║║█║▌║█║║▌█║▌║▌│║▌█║║▌█║▌║║▌█▌║")
print()			
print("DESENVOLVIDO PELA ENORMITY HACKING")
print("© PYCODE, KRIPTUZ SEC, SPEATEC SYSTEM")
print("INSTAGRAM: https://instagram.com/enormityhacking_org")
print("CONTACT: (92) 99965-2961")
print()
print("║█║▌║█║▌│║▌█║▌║║█║▌║█║▌│║▌█║║█║▌║█║▌│║▌█║▌║▌║")

print()

print("	\033[1;41m")
print("	\033[1;97m")
link = input("➡Digite o link do vídeo:  ")
path = input("➡Digite o diretório que deseja salvar o vídeo:  ")
yt = youtube (link)

# Mostra os detalhes do video #
print("🔷Informacoes do video🔷")
print("Título: ", yt.title)
print("Número de views: ", yt.views)
print("Tamanho do vídeo: ", yt.length, "segundos")
print("Avaliação do vídeo: ", yt.rating)

print()

# Usa a maior resolucao #
ys = yt.streams.get_highest_resolution()

# Começa o Download do vídeo #
print("Baixando Aguarde...")
ys.download(path)
print("Seu Download foi Concluido!")

print ()
print("Desenvolvida Pela Enormity Hacking")
print("Instagram:  https://instagram.com/enormityhacking_org")
print("Criador 92 999652961")

