#Scrivere un programma che memorizzi N voti e determini la media,il voo maggiore e il voto minore

N = int(input("Inserisci il numero di voti: "))

voti = []
for _ in range(N):
    voto = float(input("Inserisci un voto: "))
    voti.append(voto)

#Inizializziamo le variabili per i calcoli
somma = 0
max_voto = voti[0]
min_voto = voti[0]

#Calcoliamo la somma, il massimo e il minimo manualmente
for voto in voti:
    somma += voto               #uguale a scrivere somma = somma + voto
    if voto > max_voto:
        max_voto = voto
    if voto < min_voto:
        min_voto = voto

#Calcoliamo la media
media = somma / N

#Stampare i risultati
print("La media è:", media)
print("Il voto massimo è:", max_voto)
print("Il voto minimo è:", min_voto)