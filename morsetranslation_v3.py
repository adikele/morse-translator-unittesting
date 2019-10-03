''' 
3.10.2019
By Aditya Kelekar
In this version of the program separation of words in the encoding 
happens as per the standard Morse practice, that is: 
Individual letters are separated by a space while individual 
words are separated by a forward slash (/).

Assumptions: 
1.There is no extra whitespace anywhere in the text.  

Comments:
1. Refer to the following statement in the problem:
"Let's assume that every character is separated from each other 
with a dot and there cannot be two dots in a row."

To my understanding, this assumption is for the English text
to be entered. As an example of a few words:
I c.a.n s.e.e.
However, I could not understand what is the reason for the above assumption.

DESCRIPTION OF THE PROGRAM:
This program converts English text to Morse code and vice versa.

In this program, while converting from English text to Morse code:
(i) a space is used to separate every encoded character 
(ii) a forward slash (/) is used to represent a whitespace in the text

Examples of English text and their converted Morse code
as output in this program:
“SOS” appears as “••• −−− •••”
“SOS SOS” appears as “••• −−− •••/••• −−− •••”

Converter is case insensitive, thus “sos” produces same output
“•••−−−•••” as “SOS” does.

Morse code conversion is carried out only for a limited character set
as specified in the morse_alphabet dictionary in the program,
the characters outside this set are converted to "CNF"

When converting backwards, if there is a non-valid Morse code,
it is converted to "CNF"

Examples of English text and their converted Morse code
as output in this program:
"sos SOS. s-s SO-" appears as
"... --- .../... --- ... .-.-.-/... <CNF> .../... --- <CNF>"
And the above Morse code decoded back to English text
appears as: "SOS SOS. S<CNF>S SO<CNF>"


TYPE OF INPUT EXPECTED:
For this task, text (either English or Morse) is read from a file
and output is written to another file.

Simple command line interface for usage is used which asks for
input and output files and offers a way to do conversion
from either English or Morse.

NEED TO DO:
-- The program needs to be modified to provide for
erroneous/malicious user inputs.
-- The program results are not extensively tested.
'''
import sys
import string

morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "/": "-..-.",
    "@": ".--.-.",
}

inverse_morse_alphabet = dict((v, k) for (k, v) in morse_alphabet.items())

def encodetomorse(message):
    ''' this function encodes English text to Morse code. In the Morse code:
        (i) a space is used to separate every encoded character 
        (ii) foward slash is used to represent a whitespace 
        (iii) <CNF> is used to represent characters for which no corresponding 
        code is found (that is, character not found in the keys of morseAlphabet dict)
    '''
    encodedmessage = ""
    for char in message:
        if char == " ":  # if character is whitespace, add a foward slash
            encodedmessage = encodedmessage[:-1] # strip out the last whitespace from the Morse code
            encodedmessage += "/"
        elif char.upper() in morse_alphabet:  # if valid character, convert to Morse, add a whitespace
            encodedmessage += morse_alphabet[char.upper()] + " "
        else:  # if invalid character, code as <CNF>, add a whitespace
            encodedmessage += "<CNF>" + " "
    encodedmessage = encodedmessage[:-1] # strip out the last whitespace from the Morse code
    return encodedmessage


def decodemorse(message):
    ''' this function decodes a Morse code string to English text.
        Note that the Morse code string fed to this function should have:
        (i) a space between every set of Morse characters
        that represent one keyboard character
        (ii) a foward slash in the Morse code string to represent
        a whitespace in the corresponding text
        If a code sequence between whitespace in the Morse code
        does not map to any character from the given English text
        character set, the sequence is decoded as <CNF>
    '''
    words_separated = message.split("/")
    decodedmessage = ""
    for word in words_separated:
        char_separated = word.split(" ")
        for char in char_separated:
            if char in inverse_morse_alphabet:
                decodedmessage += inverse_morse_alphabet[char]
            else:
                decodedmessage += "<CNF>"
        decodedmessage += " " # for adding the whitespace at the end of every word
    return decodedmessage


def readandwrite():
    ''' this functions invokes three other functions that
    provide interactivity for entering file details
    '''
    user_response = program_interactive()
    while (user_response == "C" or user_response == "D"):
        if user_response == "C":
            print ("prompt:EnglishText.txt")
            content_text = reading_file()
            content_morse = encodetomorse(content_text)
            writing_to_file("MorseOutput.txt", content_morse)
        else:  # user_response == 'D'
            print ("prompt:MorseCode.txt")
            content_morse = reading_file()
            content_text = decodemorse(content_morse)
            writing_to_file("EnglishOutput.txt", content_text)
        user_response = program_interactive()


def program_interactive():
    ''' this functions asks user to select one of the three options
       (code/decode/quit) and returns the user's repsonse
    '''
    print ("NEXT INPUT CYCLE...")
    print ("If you want to code text file to Morse, enter 'C'")
    print ("If you want to decode Morse file to text, enter 'D'")
    print ("If you want to Quit, press any other key.")
    response = input("Enter here:")
    return response


def reading_file():
    ''' this functions asks user to select which file to input,
        reads the file and returns a string containing the file contents
    '''
    filename = input("which file to ip?")
    file = open(filename, "r")
    fileobject = file.read()
    return fileobject


def writing_to_file(filename, content):
    ''' this functions takes in two parameters:
        filename -- name of the file that is to be created and writen to
        content -- the content that is to be writen
        The function writes 'content' to file 'filename'
    '''
    file = open(filename, "w")
    file.write(content)
    print ("Results have been stored in the file:", filename)
    print ("NOTE: File contents appear after user quits the program")


readandwrite()

