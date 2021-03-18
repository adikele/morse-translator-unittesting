# morse-translator-unittesting
This project creates a Morse Code translator using Python 3.7 and includes unittests to test different input samples.

BACKGROUND 
Initially, when I started programming in Python, I had wondered as to what could be the use for unittests. Since it was possible to run my simple programs with different inputs and tally the outputs with the expected results, I did not see the benefits of creating a separate module for running unittests, particularly so as the module had to be provided with the same input samples as in the manual tests.

As my programs became more complex, data processing steps now included writing to and reading from files, and I found out that I was spending much of my manual testing time opening data files and writing input data to them. Some more time was spent in checking data from output files. But the file-creation process in itself was not my desired test object; the actual intention being to check whether some function in the program worked in the manner that it was designed to work. 

By switching over to the unittests way of testing, I was able to do away with having to write to data files and check the contents of the generated output data files. What was more, a variety of sample inputs and expected outputs for each of the inputs could now all be written in one file and run at one go. No more needless multiple runs of the program for each input, as was happening in the manual testing. 

Version 3 - updated 5.10.19:

DESCRIPTION OF THE PROGRAM:
This program converts English text to Morse code and vice versa.

In this program, while converting from English text to Morse code:
(i) a space is used to separate every encoded character 
(ii) a forward slash (/) is used to represent a whitespace in the text
In effect, therefore, individual letters are separated by a space while individual 
words are separated by a forward slash (/).

ADDITIONAL NOTES: 
1. It is assumed that there is no extra whitespace anywhere in the text.  
2. Morse code conversion is carried out only for a limited character set
as specified in the morse_alphabet dictionary in the program,
the characters outside this set are converted to "CNF"
3. When converting backwards, if there is a non-valid Morse code,
it is converted to "CNF"
4. Converter is case insensitive, thus “sos” produces same output
“•••−−−•••” as “SOS” does.

SAMPLES OF EXPECTED OUTPUT:
Examples of English text and their converted Morse code
as output in this program:
“SOS” appears as “••• −−− •••”
“SOS SOS” appears as “••• −−− •••/••• −−− •••”
"sos SOS. s-s SO-" appears as
"... --- .../... --- ... .-.-.-/... <CNF> .../... --- <CNF>"

TYPE OF INPUT EXPECTED:
For this task, text (either English or Morse) is read from a file
and output is written to another file.
Input file is saved in the same directory as the program.

Sample input files are provided.
(Choose input files: EnglishText.txt and MorseCode_v3.txt to run with this version.)
