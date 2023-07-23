# Lê as regras GLC de um arquivo texto
arquivo = 'glc1.txt'
#arquivo = 'glc2.txt'
#arquivo = 'glc3.txt'

regras = {}

# Analisa as regras GLC
# Armazena no dicionário, onde os não terminais são as chaves e o resto armazena como listas de strings
with open(arquivo, 'r') as file:
    for line in file:
        line = line.strip() # remove os caracteres de espaço em branco
        if line:
            lado_esq, lado_dir = line.split('->') # divide a linha em duas partes com base no símbolo
            lado_esq = lado_esq.strip() # lado esquerdo
            lado_dir = lado_dir.strip().split('|') # lado direito

            # confere se a chave do lado esquerdo já existe
            if lado_esq not in regras:
                regras[lado_esq] = []

            # itera sobre cada lado direito e a anexa à lista à chave lado_esq correspondente no dicionário
            for prod in lado_dir:
                # Substitui "e" por "ε"
                prod = prod.replace("e", "ε")
                regras[lado_esq].append(prod)


#Inicializa a lista de transições
transitions = []

# Define as transições do APND baseado nas regras do GLC
# Formato (q, a, A) = (p, B) , em que A -> B
for lado_esq in regras: # itera sobre cada símbolo não terminal (lado_esq)
    for lado_dir in regras[lado_esq]: # # itera sobre cada lado direito associado à chave (lado_esq)
        transition = f"(q, ε, {lado_esq}) = (q, {lado_dir})" # formato
        transitions.append(transition) # adiciona a transição na lista

# Armaneza os terminais (símbolos minúsculos) encontrados
terminals = set()
for lado_esq in regras: 
    for lado_dir in regras[lado_esq]:
        for symbol in lado_dir:
            if symbol.islower():
                terminals.add(symbol)

for terminal in terminals: # itera sobre cada símbolo terminal e adiciona uma transição (de "pop")
    transition = f"(q, {terminal}, {terminal}) = (q, ε)"
    transitions.append(transition)

# Imprime
for transition in transitions:
    print(transition)
