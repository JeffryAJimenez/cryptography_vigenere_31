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

def decode_cypher(cyphertext, cipher_key):

    index = 0;
    plaintext = '';
    #cyphertext = cyphertext.lower()
    cipher_key = cipher_key.lower()
    
    while (len(cipher_key) < len(cyphertext)):
        cipher_key += cipher_key;

    cipher_key = cipher_key[0:len(cyphertext)]
    table = generate_table();

   
    for x in cyphertext:
        if(97 <= ord(x.lower()) <=122):
            for y in range(26):
                if( table[y][ord(cipher_key[index]) - 97] == x.lower()):
                    plaintext =  plaintext + chr(ord(table[y][0]) - 32) if (65 <= ord(x) <= 90)  else plaintext + table[y][0]
                    index += 1;
                    break;
        else:
            plaintext = plaintext + x

    print(plaintext)
    

# cyphertext = "FIIFL VZOZS VPDCA ZVFSL EMRUL BQISC XVQTS NDMFT IDGIZ ILZDM FFLVZ YMHCG DIGSL DSHEZ SIWMM XPNAN TIIRJ SFMWB XIDPS EWHAI XYWQM EXVVV DMRUK XASPF OQTUP JLNTQ WTJYQ OLFOF EOVVW WTURX DIGPT LLMFT INJYF OLKZU FXMVK CZISV AHDQQ VEVDM RTWIR MWYJI GPRFO CFUWK ZYFUQ VGZZU KYLNT MXKZY SDEMW MMXPX SJUZK NAXQQ ZVJSA ZICWN ERSIL BTUWJ HLUFI ZFNTQ GYMLO TARQJ MFLJL ISXMU WUZPA VXUUD MVKNT MXUGL GZFPL BQFVZ HFQTI TSNQE XVSGR DSDLB QBVVK YZOIF XNTQW LFZAX PFOCZ SHRJE ZQWJD CWQEU JYMYR FOUDQ JIGFU ORFLU YAYJW MTMPC VCEFY ITNTU WYSFX AAUZI GEIZS GEQRK OCFTF IGIYN IWGLQ FSJOY QBXYW XGEXS WBUZH KZYPA SI"
# cipherKey = "SUMMER"

cyphertext = input()
cipherKey = input()

decode_cypher(cyphertext, cipherKey);
