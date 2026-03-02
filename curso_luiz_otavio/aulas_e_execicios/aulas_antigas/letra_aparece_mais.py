string = "Olá, tudo bem? Seja bem-vindo ao contexto de tudo, aqui não gostamos \
    de panelas e nem chinelos"

i = 0;
letra_popular = string[0]

while i < len(string):
    
    if letra_popular == string[i] or string[i] == " ":
        
        i += 1
        continue
    
    if string.count(letra_popular) < string.count(string[i]):
        
        letra_popular = string[i]
    
    i += 1
    
print(letra_popular)