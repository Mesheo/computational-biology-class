dna = "TTGGACCGGATTCAAAGATAGGGATCATAGTGGCGAATGGGGTCAACGGCGGACTACACAGAGAAGCTGCGTATGGCCGATCTGCGCGTCACCCGGCCGAGGCTTGCTGTGCTCGAGGCCGTGGGCGATCACCCACACGCCGACACCGAAACGATCTACTCGGCGGTTCGCGAAATCCTGCCCGACGTGTCCCGGCAGGCCGTATATGACGTGCTCGGCGCACTTACCTCGGTGGGCCTGGTCCGTGCGATCCAGCCGTCGGGATCGGTCGCCCGCTACGAATCCCGCGTCGGCGACAACCACCACCATGTCGTCTGCCGATCCTGCGGAGCGATTGCCGACATCGATTGTCCCGTCGGTGAGGCTCCGTGTCTGGCCCCCTCGGACGACAGCAATGTGCTGGATGGCTTCGTTGTCGACGAGGCCGAAGTCATTTATTGGGGCATCTGCCCCGATTGTTCAACCGCAATGCCCCGGTCACAGCCGTGATCGCAGCCCGATTCACCCACCCCTGGAAGGAATGCTGTGTCATCCGATAGCCGCCCACCTCAACCCGGCACCTGACCCAGAGCAATACGGAAACGGAAAGCCCGAATCTCTCCCACCCGAGGATCACGCGCGCCGATGACAACCGGAGGTGTGCCCAACCAGATCGACGTGTCGATGCTGCACCCGCACCCGTCTCTCAGCCAGCCCGCTCGGTGCTGATTTCGACTACCCCGAAAGAGTTCGCCAAGCTCGACGTCGATGCGCTCAAGGCCGACGTCATGTCGGTGATGACCACCTCGCAGGACTGGTGGCCCGCCGAGACTATGCCACTACGGTGGCCTGTTCATCCGGATGAGCTGGCACGCCGCCGGTACCTACCGCATCCAAGGATGGTCGCGGCGGCGGTGGCCAGGGCATGCAGCGATCTCTCCGGCTCAACAGGCTGG"

letters_mapping = {
    "T" : "A",
    "C" : "G",
    "A" : "T",
    "G": "C"
} 

def fita_complementar(dna_string):
    fita = []
    for letter in dna_string:
        fita.append(letters_mapping[letter])

    return "".join(fita)  

def verifica_palindromo(dna_string):
    if fita_complementar(dna_string)[::-1] == dna_string:
        return True
    return False

def find_substring_positions(main_str, substring):
    positions = []
    substring_length = len(substring)

    for i in range(len(main_str)):
        if main_str[i:i+substring_length] == substring:
            positions.append(i)

    return positions       

 
def verifica_sub_palindromos(dna):
    substrings = set()
    max_length=0
    max_palindrome="" 
    
    # 1. Verifica todas as substrings de no minimo i:j em que J > 2 vulgo 3
    for i in range(len(dna)):
        min_substring_size = 3
        for j in range(i+min_substring_size, len(dna)+1):
            substring = dna[i:j]

            # 2. Verifica se essa substring é um palindromo de dna
            if verifica_palindromo(substring):

                # 3. Guarda essa substring e atualiza o valor da maior substring
                substrings.add(substring)
                if len(substring) > max_length:
                    max_length = len(substring)
                    max_palindrome = substring

    # 4. Encontra a posicao inicial da maior substring
    max_palindrome_position = find_substring_positions(dna, max_palindrome)
    print(
        f"O maior palindromo encontrado foi {max_palindrome} e ele apareceu nas posicões {max_palindrome_position}")
    
    return substrings

sub_palindromos = verifica_sub_palindromos(dna)
print("\nLista dos palindromos : ", sub_palindromos)
 

