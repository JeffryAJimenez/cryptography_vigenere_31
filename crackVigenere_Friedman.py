INDEX_OF_COINCIDENCE =  0.067;
LOWER_BOUND = 0.0607
HIGHER_BOUND = 0.0777;
englishLetterFreq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,  0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
TEST= 'abcdefghijkmnlopqrstuvwxyz'

def getItemAtIndexOne(x):
    return x[1]

def getFactors(min_num, num):
    
    factors = []
    
    for i in range(min_num, num + 1):
        if (num % i == 0):
            factors.append(i)
    
    return factors

def getSpans(cipher_text, key_length):

    spans = [];

    for i in range(key_length):
        spans.append(breakString(cipher_text, i, key_length));

    return spans;


def getIndexOfCoincedence(span):
    span = span.lower()
    total = 0;
    
    for i in range(26):
        count = span.count(chr(i + 97)) 
        total += count *( count - 1)
    
    return total/((len(span) * (len(span) - 1)))

def getKeyLength(ciphertext, MAX_LENGTH):
    
    ic = []
    
    for i in range(1, MAX_LENGTH + 1):
        indexOfCoincedence = 0.0
        
        spans = getSpans(ciphertext, i)
        
        for span in spans:
            indexOfCoincedence += getIndexOfCoincedence(span)
        
        
        ic.append(indexOfCoincedence/i)
        
    #KEY IS THE LENGHT of the "key"
    #keys are added +2 beacuse the search for IC starts at length 2
    ic_dictionary = {}
    for index in range(len(ic)):
        ic_dictionary[index + 1] = ic[index]
    
    ic_List = list(ic_dictionary.items())
    
    #choose the closest value to INDEX_OF_COINCIDENCE
    ''' if ic_List[i][1] >= INDEX_OF_COINCIDENCE else 1'''
    guessed_lenght = ic_List[min(range(len(ic_List)), key= lambda i: abs(ic_List[i][1] - INDEX_OF_COINCIDENCE) )]
    
    
    factors = getFactors(2, guessed_lenght[0])
    min_key_length = (-1, -999.0)
    posible_factors = []
    for factor in factors:
        if (factor - 1 in ic_dictionary and factor in ic_dictionary and ic_dictionary[factor - 1] < ic_dictionary[factor]):
            if( ic_dictionary[factor] > min_key_length[1]):
                min_key_length = (factor, ic_dictionary[factor])
                posible_factors.append((factor, ic_dictionary[factor]))
    
    # if(min_key_length[0] == factor):
        
    #     # factors4factors = []
    #     # for factor in factors:
    #     #     factors4factors = factors4factors + getFactors(factors[0], factor)
        
    #     factors4factors = []
    #     for factor in posible_factors:
    #         factors4factors = factors4factors + getFactors(posible_factors[0][0], factor[0])
        
    #     factor_count = {}
    #     for factor in factors4factors:
    #         if (not(factor in factor_count)):
    #             factor_count[factor] = 1;
    #         else:
    #             factor_count[factor] += 1
        
    #     factors4factors = list(factor_count.items())
    #     factors4factors.sort(key=getItemAtIndexOne, reverse=True)
        
    #     possible_ans = []
    #     for x in factors4factors:
    #         if (x[1] == factors4factors[0][1]):
    #             possible_ans.append(x[0])
        
    #     if(len(possible_ans) > 1):
    #         answer = -1
    #         for x in possible_ans:
    #             if (answer < x):
    #                 answer = x;
            
    #         min_key_length = (answer, ic_dictionary[answer])
        
    #     else:
    #         min_key_length = (possible_ans[0], ic_dictionary[possible_ans[0]])
    
    
    return min_key_length[0]
    #return ic_List[min(range(len(ic_List)), key= lambda i: abs(ic_List[i][1] - INDEX_OF_COINCIDENCE))][0] if guessed_lenght == 1 else guessed_lenght[0]



'''
IMPORT FROM CRACKVigenenere-Key
'''
def getItemAtIndexZero(x):
    return x[0]

def getSpans(cipher_text, key_length):
    
    spans = [];
    
    for i in range(key_length):
        spans.append(breakString(cipher_text, i, key_length));
        
    return spans;
    

def letterCounter(str):
    letterCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 
        'q': 0,'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    for c in str:
        if(c.lower() in letterCount):
            letterCount[c.lower()] = letterCount[c.lower()] + 1
    
    return letterCount



def breakString(string, start, step):

    result= "";
    index = start;
    string = ''.join(e for e in string if e.isalpha())

    while(index < len(string)):
        if(  ('a' <= string[index] <= 'z') or ('A' <= string[index] <= 'Z') ):
            result += string[index];
            if (index + 1 < len(string) and not('a' <= string[index + 1] <= 'z') and not('A' <= string[index + 1] <= 'Z')):
                index += step + 1;
            else:
                index += step;
                
                counter = 1
        else:
            index+= 1

    return result


            


def shiftLetters(arr, n):
    for i in range(0, n):       
        for j in range(0, len(arr)-1):    
            new_char = ord(arr[j]) - 1;  
            if(new_char < 97):
                new_char += 26
            arr[j] = chr(new_char)   
            

    
    return arr


def getCharFreqs(str):

    frequencies = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0,'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    for c in str:
        frequencies[c] += 1
    

    sortedFreq = list(frequencies.items())
    sortedFreq.sort(key=getItemAtIndexZero)

    spanFrequencis = []
    for v in sortedFreq:
        spanFrequencis.append(v[1]/float(len(str)))

    return spanFrequencis

def getChar(span):
    #span = TEST
    span = span.lower()
    
    #results for chi squares
    chi_squareds = [] 

    for i in range(26):
        chi_squareds.append(0)
        result = 0.0

        
        #shift <code>span<code> letters
        sequence_offset = shiftLetters([c for c in span], i)
        
        #get the frequencies of the span
        sequence_frequencies = getCharFreqs(sequence_offset)
        
        for j in range(26):
            result+=((sequence_frequencies[j] - float(englishLetterFreq[j]))**2)/float(englishLetterFreq[j])


        chi_squareds[i] = result
        
        
    shift = chi_squareds.index(min(chi_squareds))

    return chr(shift + 65)

        



def decodeRemake(cipher_text, key_length):

    key = ''
    #setUp the dictionary

    #breakCipherText 
    spans = getSpans(cipher_text, key_length)

    for x in range(key_length):
        key += getChar(spans[x])
        
    print(key.upper())
    return key

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


def main():
    '''
    cipherText = "Lb hth twdvh osh, wb fks tuugh ndhhxh, kvqq hvq vvoprkg rlfgf osbswvszhr, czh gharr. Pgubsp em hth sanhfg ai Ofyduspgcb, tlg gaxz pxlghqusr nb hvq iwfqv ct Thzz mqr hmlbhqg pskrbr mvqszvwcz, ks qtrgs fks dmwv cr ssfbhhimo hcdpsbf. Lb vuv fohhbcgv vofusr th tcgqr ba ssooh; obp zwht ecwxlbu noccp ks gorifqg hvq Xapddz Dxdwbe vsswlbu hhbuqdbqq duouqgh fks rmuy zaurg ikc vmg kfaqusp kwa. Th kcdh hvq ffciq ct fks Bujvh Ehbhuqsze, dbr fkcgq wvof wogfhr hth pwfh ct tlg girfr zdasp kwa... fks Rara Gxdmsd"
    key = "UNITEDSTATES"
    '''
    
    
    '''
    cipherText = "QRBAIUWYOKILBRZXTUWLEGXSNVDXWRXMHXYFCGMWWWSMELSXUZMKMFSBNZIFYEIEGRFZRXWKUFAXQEDXDTTHYNTBRJLHTAIKOCZXQHBNDZIGZGPXARJEDYSJNUMKIFLBTNHWISWNVLFMEGXAIAAWSLFMHXRSGRIGHEQTUMLGLVBRSILAEZSGXCMHTOWHFMLWMRKHPRFBELWGFRUGPBHNBEMKBNVWHHUEAKILBNBMLHKXUGMLYQKHPRFBELEJYNVWSIJBGAXGOTPMXRTXFKIWUALBRGWIEGHWHGAMEWWLTAELNUMREUWTBLSDPRLYVRETLEEDFROBEQUXTHXZYOZBXLKACKSOHNVWXKSMAEPHIYQMMFSECHRFYPBBSQTXTPIWHGPXQDFWTAIKNNBXSIYKETXTLVBTMQALAGHGOTPMXRTXTHXSFYGWMVKHLOIVUALMLDLTSYVWYNVWMQVXPXRVYABLXDLXSMLWSUIOIIMELISOYEBHPHNRWTVUIAKEYGWIETGWWBVMVDUMAEPAUAKXWHKMAUPAMUKHQPWKCXEFXGWWSDDEOMLWLNKMWDFWTAMFAFEAMFZBNWIHYALXRWKMAMIKGNGHJUAZHMHGUALYSULAELYHJBZMSILAILHWWYIKEWAHNPMLBNNBVPJXLBEFWRWGXKWIRHXWWGQHRRXWIOMFYCZHZLVXNVIOYZCMYDDEYIPWXTMMSHSVHHXZYEWNVOAOELSMLSWKXXFXSTRVIHZLEFJXDASFIE"
    key = "UNITEDSTATES"
    '''
    #cipherText = "FIIFL VZOZS VPDCA ZVFSL EMRUL BQISC XVQTS NDMFT IDGIZ ILZDM FFLVZ YMHCG DIGSL DSHEZ SIWMM XPNAN TIIRJ SFMWB XIDPS EWHAI XYWQM EXVVV DMRUK XASPF OQTUP JLNTQ WTJYQ OLFOF EOVVW WTURX DIGPT LLMFT INJYF OLKZU FXMVK CZISV AHDQQ VEVDM RTWIR MWYJI GPRFO CFUWK ZYFUQ VGZZU KYLNT MXKZY SDEMW MMXPX SJUZK NAXQQ ZVJSA ZICWN ERSIL BTUWJ HLUFI ZFNTQ GYMLO TARQJ MFLJL ISXMU WUZPA VXUUD MVKNT MXUGL GZFPL BQFVZ HFQTI TSNQE XVSGR DSDLB QBVVK YZOIF XNTQW LFZAX PFOCZ SHRJE ZQWJD CWQEU JYMYR FOUDQ JIGFU ORFLU YAYJW MTMPC VCEFY ITNTU WYSFX AAUZI GEIZS GEQRK OCFTF IGIYN IWGLQ FSJOY QBXYW XGEXS WBUZH KZYPA SIFIIFL VZOZS VPDCA ZVFSL EMRUL BQISC XVQTS NDMFT IDGIZ ILZDM FFLVZ YMHCG DIGSL DSHEZ SIWMM XPNAN TIIRJ SFMWB XIDPS EWHAI XYWQM EXVVV DMRUK XASPF OQTUP JLNTQ WTJYQ OLFOF EOVVW WTURX DIGPT LLMFT INJYF OLKZU FXMVK CZISV AHDQQ VEVDM RTWIR MWYJI GPRFO CFUWK ZYFUQ VGZZU KYLNT MXKZY SDEMW MMXPX SJUZK NAXQQ ZVJSA ZICWN ERSIL BTUWJ HLUFI ZFNTQ GYMLO TARQJ MFLJL ISXMU WUZPA VXUUD MVKNT MXUGL GZFPL BQFVZ HFQTI TSNQE XVSGR DSDLB QBVVK YZOIF XNTQW LFZAX PFOCZ SHRJE ZQWJD CWQEU JYMYR FOUDQ JIGFU ORFLU YAYJW MTMPC VCEFY ITNTU WYSFX AAUZI GEIZS GEQRK OCFTF IGIYN IWGLQ FSJOY QBXYW XGEXS WBUZH KZYPA SI"
    
    cipherText = input()
    
    decode_cypher(cipherText,decodeRemake(cipherText, getKeyLength(cipherText,  100)).upper())



#keyLen 4
#cipherText = "CDGAVNNANXDOKVZXDGVGOBMXGHVLOLQFZIAPJAXBOAGTZFBTGAIBVUKLOBZTSMDNVGKSIIOAGJOBJLGOCIDGVZZCMHYFGUIZWSBYVKGUVFGXFUZFOLKFJOMZCMGMOAGLCCMWCDGNCXUWYCAYGJALJFGSXBJMJWMCIECFBOVZGUPMOHOKVHYECONNCXTAQYMZCJJHIXUWKUMTVWNNCXISPFNYTGHNCXCIPCOTPAOBZFCJIYVGFLCYNXKFZMZICJVNZMJWHZMHOLCYWX"

#keylen = 11
#amirrahmatt
#cipherText = "Wdqkv a wdozzay bf trhok tv izxlk euorrxtql ljius tam Vuoveeyq cbxhqz, xzvlz ima kqg cvnnfh. Bv ttm wzrzf lbve, fpv lsld sailx xifvppe mpe oqgyeyfeqb. Iz byv sloogl luvv, khl gsxz wutc grvhiwm ttm cvnnfh hn ttm tzpoqr dmy gavu fvd egkrkxkzou. Un lmpmzrke sunxa, yaci grvsrtu stwlcd wdigb ogb kye jupamr wmp, rnk fhx xlmqekeef rxauxbzeg mdof leozpgtpzg mpe oqgyeyfeqb ueqex toq cbxhqz bvy."

main()

