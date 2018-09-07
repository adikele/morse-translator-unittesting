# morse-translator-unittesting
This project creates a mode code translator usign Python3.7 and includes unittests to test different input samples.

BACKGROUND: 
Initially, when I started programming in Python, I had wondered what was the use for unittests. Since it was possible to run my simple programs with different inputs and tally the outputs with the expected results, what could be the benefit of creating a separate class for running the unittests with the same input samples as in the manual tests?

As my programs became more complex and writing to and reading from files, I found out that I was spending much of my manual testing time opening data files and writing input data to them. Some more time was spent in checking data from output files. But the file creation process in itself was not what I wanted to tested every time; the objective of checking was some function in the program that produced the data. 

By switching over to the unittests way of testing, I was able to do away with having to write to data files and check the contents of the generated output data files. What was more, a variety of sample inputs and expected outputs for each of the inputs could now all be written in one file and run at one go. No more needless multiple runs of the program for each input, as was happening in the manual testing. 

DESCRIPTION OF THE MAIN PROGRAM AND HOW TO RUN IT: 
Let me explain how I created the unittests module for testing a program that converts English text to Morse code and vice versa. Before going through the unittests structure, a quick look at how to run the morsetranslator program. The program converts English text to Morse code and vice versa. Input and output are performed by asking the user to enter the name of a text input file and writing the output to another text file. 

Preparations in order to run the morsetranslator.py program:
1. download and save all the python programs and the text files in the same directory
2. create a text file with sample English text of a few characters and store it in the same directory as the python files (I suggest use 1-10 characters, so it is easy to check the translated code.) Alternately, use the EnglishText.txt or the MorseCode.txt sample input files, when prompted once the program is run. 

Run the morsetranslator_v1_main.py or the morsetranslator_v2_main.py program files. (The v2 version has more error-checking code than the v1 version; but more of that later.) After a successful run of the program, the output data file will contain the results.

CREATING A UNITTEST MODULE:
First, run the following test module to test the morsetranslator_v1_main.py program:
test_morsetranslator_v1_main.py 
The test module uses unit test functions to check whether the encodetomorse and decodemorse functions produce the desired results by testing the functions on sample inputs.

RESULTS:
Five tests are run... 
-- two out of three tests with the encodetomorse function pass and 
-- two out of two tests with the decodemorse function pass

Screenshot of expected output is provided.

ANALYSIS OF RESULSTS:
The tests that pass include inputs with valid as well as invalid one-line strings of: 
English text for the encodetomorse function and 
Morse code for the decodemorse functions

In the test that fails, the encodetomorse function is given the input parameter of " ". This whitespace character is not in the valid input set of English characters for this program; hence the program should output "<CNF>". To reiterate, the following (i) and (ii) are equated:
(i) encodetomorse function's output for the input parameter " " 
(ii) "<CNF>" 
The test however fails.

CORRECTION REQUIRED:
The encodetomorse function in morsetranslator_v1_main.py splits any input string at " " points, so when the function processes the input parameter of " ", the 'encodedmessage' variable has the value "", which is returned. Therefore, the encodetomorse function needs to process the " " input in a different way.

CORRECTION DONE:
A new draft of the main program is created: morsetranslator_v2.py
To run this program, main_morsetranslator_v2.py should be run.

In this new draft, which is morsetranslator_v2.py program, the encodetomorse function processes the " " input in a separate 'if' clause, such that the 'encodedmessage' variable takes the value "<CNF>".
NOTE: The new code lines in morsetranslator_v2.py file have the inline comments  #NEW in draft03

Also, a new draft of the test program is created: 
test_morsetranslator_v2.py 
The new test program has the same test functions as the previous one.

All five tests now pass.
Screenshot of expected output is provided.

