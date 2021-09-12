

"""
Ova funkcija sabira dva broja uz 
neke modifikacije:
1) AKO SE PROSLEDI NEGATIVNI BROJ, BILO 
KOJI OD ARGUMENATA, FUNKCIJA MORA VRAITIT 
-1
2) AKO SE prosledi 0 kao bilo koji od 
argumenata, FUNKCIJA MORA VRAITIT -2
3) Ako su arugmenti veci od nule, 
vraca njihov zbir
"""
def poslovna_logika(prvi, drugi):
    if prvi < 0 or drugi < 0:
        return -5
    
    if prvi == 0 or drugi == 0:
        return -2
    
    return prvi + drugi







# def zbir(a, b):

#     return a + b

# rezultat = zbir("zddravo", "svete")
# print(rezultat)
# rezultat = zbir(2,2)
# print(rezultat)