


englishLetterFreq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,  0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]


ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

TEST= 'abcdefghijkmnlopqrstuvwxyz'


def getSpans(cipher_text, key_length):

    spans = [];

    for i in range(key_length):
        spans.append(breakString(cipher_text, i, key_length));

    return spans;
    
def getSpansFrequencies(spans, key_length):

    spamFreqs = [];
    for i in range(key_length):
        spamFreqs.append(findFreqs(spans[i]))

    return spamFreqs

def getItemAtIndexZero(x):
    return x[0]


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


def crack():
    cipher_text = input()
    key_length = int(input())
    
    key = ''

    #breakCipherText 
    spans = getSpans(cipher_text, key_length)

    for x in range(key_length):
        key += getChar(spans[x])
        
    print(key)
    decode_cypher(cipher_text, key.upper())











#cipherText = "CVJTNAFENMCDMKBXFSTKLHGSOJWHOFUISFYFBEXEINFIMAYSSDYYIJNPWTOKFRHWVWTZFXHLUYUMSGVDURBWBIVXFAFMYFYXPIGBHWIFHHOJBEXAUNFIYLJWDKNHGAOVBHHGVINAULZFOFUQCVFBYNFTYGMMSVGXCFZFOKQATUIFUFERQTEWZFOKMWOJYLNZBKSHOEBPNAYTFKNXLBVUAXCXUYYKYTFRHRCFUYCLUKTVGUFQBESWYSSWLBYFEFZVUWTRLLNGIZGBMSZKBTNTSLNNMDPMYMIUBVMTLOBJHHFWTJNAUFIZMBZLIVHMBSUWLBYFEUYFUFENBRVJVKOLLGTVUZUAOJNVUWTRLMBATZMFSSOJQXLFPKNAULJCIOYVDRYLUJMVMLVMUKBTNAMFPXXJPDYFIJFYUWSGVIUMBWSTUXMSSNYKYDJMCGASOUXBYSMCMEUNFJNAUFUYUMWSFJUKQWSVXXUVUFFBPWBCFYLWFDYGUKDRYLUJMFPXXEFZQXYHGFLACEBJBXQSTWIKNMORNXCJFAIBWWBKCMUKIVQTMNBCCTHLJYIGIMSYCFVMURMAYOBJUFVAUZINMATCYPBANKBXLWJJNXUJTWIKBATCIOYBPPZHLZJJZHLLVEYAIFPLLYIJIZMOUDPLLTHVEVUMBXPIBBMSNSCMCGONBHCKIVLXMGCRMXNZBKQHODESYTVGOUGTHAGRHRMHFREYIJIZGAUNFZIYZWOUYWQZPZMAYJFJIKOVFKBTNOPLFWHGUSYTLGNRHBZSOPMIYSLWIKBANYUOYAPWZXHVFUQAIATYYKYKPMCEYLIRNPCDMEIMFGWVBBMUPLHMLQJWUGSKQVUDZGSYCFBSWVCHZXFEXXXAQROLYXPIUKYHMPNAYFOFHXBSWVCHZXFEXXXAIRPXXGOVHHGGSVNHWSFJUKNZBESHOKIRFEXGUFVKOLVJNAYIVVMMCGOFZACKEVUMBATVHKIDMVXBHLIVWTJAUFFACKHCIKSFPKYQNWOLUMYVXYYKYAOYYPUKXFLMBQOFLACKPWZXHUFJYGZGSTYWZGSNBBWZIVMNZXFIYWXWBKBAYJFTIFYKIZMUIVZDINLFFUVRGSSBUGNGOPQAILIFOZBZFYUWHGIRHWCFIZMWYSUYMAUDMIYVYAWVNAYTFEYYCLPWBBMVZZHZUHMRWXCFUYYVIENFHPYSMKBTMOIZWAIXZFOLBSMCHHNOJKBMBATZXXJSSKNAULBJCLFWXDSUYKUCIOYJGFLMBWHFIWIXSFGXCZBMYMBWTRGXXSHXYKZGSDSLYDGNBXHAUJBTFDQCYTMWNPWHOFUISMIFFVXFSVFRNA"
#length = 6

#cipherText = "Zinff ehpdh123!"
#length = 8

#cipherText = "QRBAIUWYOKILBRZXTUWLEGXSNVDXWRXMHXYFCGMWWWSMELSXUZMKMFSBNZIFYEIEGRFZRXWKUFAXQEDXDTTHYNTBRJLHTAIKOCZXQHBNDZIGZGPXARJEDYSJNUMKIFLBTNHWISWNVLFMEGXAIAAWSLFMHXRSGRIGHEQTUMLGLVBRSILAEZSGXCMHTOWHFMLWMRKHPRFBELWGFRUGPBHNBEMKBNVWHHUEAKILBNBMLHKXUGMLYQKHPRFBELEJYNVWSIJBGAXGOTPMXRTXFKIWUALBRGWIEGHWHGAMEWWLTAELNUMREUWTBLSDPRLYVRETLEEDFROBEQUXTHXZYOZBXLKACKSOHNVWXKSMAEPHIYQMMFSECHRFYPBBSQTXTPIWHGPXQDFWTAIKNNBXSIYKETXTLVBTMQALAGHGOTPMXRTXTHXSFYGWMVKHLOIVUALMLDLTSYVWYNVWMQVXPXRVYABLXDLXSMLWSUIOIIMELISOYEBHPHNRWTVUIAKEYGWIETGWWBVMVDUMAEPAUAKXWHKMAUPAMUKHQPWKCXEFXGWWSDDEOMLWLNKMWDFWTAMFAFEAMFZBNWIHYALXRWKMAMIKGNGHJUAZHMHGUALYSULAELYHJBZMSILAILHWWYIKEWAHNPMLBNNBVPJXLBEFWRWGXKWIRHXWWGQHRRXWIOMFYCZHZLVXNVIOYZCMYDDEYIPWXTMMSHSVHHXZYEWNVOAOELSMLSWKXXFXSTRVIHZLEFJXDASFIE"
#length = 12

#cipherText = "Wteer. Xlrta. Qirx. Lir. Ezng tro, tap fonc namtonl wivxo tozpthxc in alrmhyy. Tapn eoprymsinz nhagred psen mse Fbce Nteiog ltttnkew. Znlr ehe Tgattc, maleer hq ale qouk plefpntl , noueo stha thxx. Bum hheg ehe pzrlw yeewpd hbx mole, he olnilsed. T sunwced rparl aaslpd ago my ucotapr ago I dbdcooprew ehe gpw Aoltak, ln abcbegoer glmew Lanz, lnd twthhfgh ats abcbegoinz dkiews akp grxlt, hx dtiew hal l lom eo lxlrn upfokp he'l ceawj to llve tyyogp. Bum T beetevx Lanz nan llve mse whcld"
#length = 4

crack()

