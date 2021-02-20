

def generate_table():

    MAX_INDEX = 26;
    colum, index = 0, 0;
    alphabet = [None]*26;

    for x in range(97, 123):
        alphabet[index] = chr(x);
        index += 1

    
    table = [[None for x in range(26)] for y in range(26)];
    
    for x in range(26):
        colum = x;
        for y in range(26):
            if(colum == MAX_INDEX):
                colum = 0;
            table[x][y] = alphabet[colum];
            colum += 1;

    return table;
   

def generate_cypher(plaintext, cipher_key):

    index = 0;
    cypher = '';
    #plaintext = plaintext.lower()
    cipher_key = cipher_key.lower()
    
    while (len(cipher_key) < len(plaintext)):
        cipher_key += cipher_key;

    cipher_key = cipher_key[0:len(plaintext)]
    table = generate_table();

   
    for x in plaintext:
        if(97 <= ord(x.lower()) <=122):
            cypher =   cypher + chr(ord(table[ord(x.lower()) - 97][ord(cipher_key[index]) - 97]) - 32 ) if (65 <= ord(x) <= 90) else cypher + table[ord(x.lower()) - 97][ord(cipher_key[index]) - 97]
            index += 1;
            
        else:
            cypher = cypher + x

    print(cypher)
    



plaintext = input();
ciphertext = input();

generate_cypher(plaintext, ciphertext);