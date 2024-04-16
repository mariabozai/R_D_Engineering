import math

def encryption(text):
    # Eliminăm spațiile din text
    text = text.replace(" ", "")
    
    # Calculăm lungimea textului modificat
    L = len(text)
    
    # Determinăm numărul de rânduri și coloane pentru grid
    row = math.floor(math.sqrt(L))
    column = math.ceil(math.sqrt(L))
    
    # Ajustăm numărul de rânduri și coloane dacă este necesar
    if row * column < L:
        row += 1
        if row * column < L:
            column += 1
    
    # Cream grid-ul
    grid = []
    index = 0
    for i in range(row):
        end_index = min(index + column, L)
        grid.append(text[index:end_index])
        index = end_index
    
    # Concatenăm fiecare grup de cuvinte pe un rând nou
    encrypted_text = "\n".join(grid)

    return encrypted_text

# Citim textul de la tastatură
text = input("Introduceți textul de criptat: ")

# Aplicăm criptarea și afișăm rezultatul
encrypted_text = encryption(text)
print("Textul criptat:")
print(encrypted_text)
