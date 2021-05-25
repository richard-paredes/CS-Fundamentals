# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Assignment #7
"""

#This is the plain-text to be encrypted. Do Not delete this!
plain_text = """The quick brown fox jumps over the lazy dog."""

#This is the easy secret message for optional decryption
easy_secret = """S xgjx llvkek, cmwv wsk hvctxbui - jvvx ar Jfyllsp."""

#This is the Full secret message for optional decryption
secret_message = """Gchl kdcey sor fynfb lyssg nag pie zsuvrlk cfboyih sijuv bh liwf 
wgohvhwoh, n hwx bnnapb, pifdsvpwe wa Facsenq, bbq xwewpulfr gi lis clgqcfcljca 
nzbh nfd nsa ujf qeysusq yivoy.

Hgx kr ujf saashsq cf b ueysu qvpam knl, lfggcfh kuylise nzbh auljca, ij bbl hsuwbh 
kp qbhufwiyv bbq mg esqcubhrx, ubb yifh saxmss. Jy sss zyl pb n ajfog vsuhyy-xjsyx 
gg huul xoe. Qw ioiy upar ng esqcubhr u hpfgcgo cs nzbh scwmr, nm s gwaud ssfnaou 
cfsds sij uvbmw xvb bwss tunf huyas zvpwt huul uvnn fbhvif nwtbl mwiy. Au wf uductylise 
zauhvhy bbq jjpdrl liog qw tvbode rb nzvg.

Ool, jb n fssurl kfbfy, of qnh fph qyvjqnnw -- xs puf ocg wgogrwjbhr -- qw doa hgu 
vnfdpk -- gbat ueimor. Gbw cfnpw nsa, fawwaa sor qyse, kui kufhaymsq bwss, uunf 
qbhkfqeulfr vn, xbf nvgws boj qcbl hpkrl lp oqx gs rrnjbqg. Nzf kblde kvfd mwgndf 
bbnw, oce fgou eyefaoyj xvnn of gns zffr, vmu wg wso brpws tblyfh jbsu huyq ewq 
bwss. Vn at tbl mt huy djjvhy, sogbws, hb vw esqcubhrx zffr ng uvr ofgwackisq qgsy 
jbadv gbwz kui xpitbl isey zbjr nzvg suj tc aitmm nxnbbpyv. Jh vm jbhuyj gce ok 
uc oy zffr xwewpulfr gi lis tlwbh gukl frgsjbvhy cssijf if -- nzbh slgn huykf vbhgssq 
xwbr jy lbyr cfdfrukfr qynphvif uc gbsu qnokf tbl oiwpb lisl asws gbw mofn xvzy 
gwbghlw pt qynphvif -- uvnn of vrlw iwtbdz frmgmjr nzbh gbwts qyse guudm bbn zbjr 
xafr vh nbwa -- nzbh gbat bnnapb, hhvff Tiv, tvnfd ioiy s osj vashu ix gfryvpa -- 
nhv uvnn ypjrlfnsan gg huy hfccfw, cm gbw qsbjdf, tbl lis cygqzr, mzbzy hgu drlatv 
slgn huy wbfgb."""

#TO DO:
#1. Ask the user for a code word and store it for use later
def getCodeWord():
    codeWord =  input("Please enter a code word: ")
    print()
    while (not codeWord.isalpha()):
        print("Invalid code word. The ode word must be composed only of letters from the alphabet.")
        codeWord = input("Please enter a code word: ")
        print()
    return codeWord

#2. Call an encryption function with the plainText above and the code word and save the result it gives back (cypher-text)
def encryptPlainText():
    '''
    TEST CASE:
    example = 'A test string, just for practice - here in Houston.'
    codeWord = 'secret'
    '''
    codeWord = getCodeWord()
    cypherText = encrypt(plain_text, codeWord)
    printCypherText(cypherText)
    return cypherText

#3. Print out the cypher-text <-- This is the goal of the assignment!  
def printCypherText(message):
    print(message)

#4. Write the function to encrypt some text with a code word
def encrypt(message, code):
    code = code.upper()
    encryptedMessage = ''
    codeLetterIndex = 0

    for letter in message:
        if (letter.isalpha()):
            codeLetter = code[codeLetterIndex % len(code)]
            encryptedLetter = encryptLetter(letter, codeLetter)
            codeLetterIndex += 1
        else:
            encryptedLetter = letter
        encryptedMessage += encryptedLetter
    
    return encryptedMessage

#5. Write the helper functions needed to do the encryption (encrypt a letter)
def encryptLetter(messageLetter, codeLetter):
    alpha = [chr(letter) for letter in range(65,91)] # instead of importing a package, use ascii-index to char conversion
    
    temp = messageLetter.upper()
    messageLetterIndex = alpha.index(temp)
    codeIndex = alpha.index(codeLetter)

    encryptedAlpha = alpha[codeIndex:] + alpha[:codeIndex]
    encryptedLetter = encryptedAlpha[messageLetterIndex]

    # keep original casing
    if (messageLetter.islower()):
        encryptedLetter = encryptedLetter.lower()
     
    return encryptedLetter

#6. Optional: Write and call a decryption function on the secret message above
def decryptSecretMessage():
    '''
    TEST CASE:
    example = 'S xgjx llvkek, cmwv wsk hvctxbui - jvvx ar Jfyllsp.'
    codeWord = 'secret'
    '''
    codeWord = 'bonus'
    decryptedMessage = decrypt(secret_message, codeWord)
    printCypherText(decryptedMessage)
    return decryptedMessage

def decrypt(message, code):
    code = code.upper()
    decryptedMessage = ''
    codeLetterIndex = 0
    for letter in message:
        if (letter.isalpha()):
            codeLetter = code[codeLetterIndex % len(code)]
            decryptedLetter = decryptLetter(letter, codeLetter)
            codeLetterIndex += 1
        else:
            decryptedLetter = letter
        decryptedMessage += decryptedLetter
    
    return decryptedMessage

def decryptLetter(encryptedMessageLetter, codeLetter):
    alpha = [chr(letter) for letter in range(65,91)]

    temp = encryptedMessageLetter.upper()
    codeIndex = alpha.index(codeLetter)
    encryptedAlpha = alpha[codeIndex:] + alpha[:codeIndex]
    
    encryptedLetterIndex = encryptedAlpha.index(temp)
    decryptedLetter = alpha[encryptedLetterIndex]
    
    # keep original casing
    if (encryptedMessageLetter.islower()):
        decryptedLetter = decryptedLetter.lower()

    return decryptedLetter

def main():
    encryptPlainText()
    print()
    #decryptSecretMessage() # to see secret_message decrypted

main()