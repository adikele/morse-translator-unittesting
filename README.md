# morse-translator-unittesting
This project creates a mode code translator using Python 3.7 and includes unittests to test different input samples.

BACKGROUND 
Initially, when I started programming in Python, I had wondered as to what could be the use for unittests. Since it was possible to run my simple programs with different inputs and tally the outputs with the expected results, I did not see the benefits of creating a separate module for running unittests, particularly so as the module had to be provided with the same input samples as in the manual tests.

As my programs became more complex, data processing steps now included writing to and reading from files, and I found out that I was spending much of my manual testing time opening data files and writing input data to them. Some more time was spent in checking data from output files. But the file-creation process in itself was not my desired test object; the actual intention being to check whether some function in the program worked in the manner that it was designed to work. 

By switching over to the unittests way of testing, I was able to do away with having to write to data files and check the contents of the generated output data files. What was more, a variety of sample inputs and expected outputs for each of the inputs could now all be written in one file and run at one go. No more needless multiple runs of the program for each input, as was happening in the manual testing. 

DESCRIPTION OF THE MAIN PROGRAM AND HOW TO RUN IT
Let me explain how I created the unittests module for testing a program that converts English text to Morse code and vice versa. Before going through the unittests structure, a quick look at how to run the morsetranslator program. The program converts English text to Morse code and vice versa. The input-output operations are performed by asking the user to enter the name of a text input file and by writing the output to another text file. 

Preparations in order to run the morsetranslator.py program:
1. Download and save all the .py python files in this project as well as the accompanying text files in the same directory
2. Create a text file with sample English text of a few characters and store it in the same directory as the python files. (I suggest use 1-10 characters, so it is easy to check the translated code.) Also create a text file with sample Morse code, such that every set of code characters representing one English text character is separated from the next by a whitespace. Alternatively, use the EnglishText.txt or the MorseCode.txt sample input files provided with this project. 

Run the morsetranslator_v1_main.py or the morsetranslator_v2_main.py program files. (The v2 version has more error-checking code than the v1 version; but more of that later.) During the program run, when prompted, provided the name of the appropriate text file. After a successful run of the program, the output data file will contain the results.

CREATING A UNITTEST MODULE
First, run the following test module to test the morsetranslator_v1_main.py program:
test_morsetranslator_v1_main.py 

The test module uses the unittest framework to check whether the encodetomorse and decodemorse functions produce the desired results by testing the functions on sample inputs.

RESULTS
Five tests are run: 
(i) two out of three tests with the encodetomorse function pass and 
(ii) two out of two tests with the decodemorse function pass

Screenshot of expected output of running the morsetranslator_v1_main.py program is provided.

COMMENTS ABOUT THE RESULTS
The tests that pass include inputs with valid as well as invalid one-line strings of: 
(i) English text for the encodetomorse function and 
(ii) Morse code for the decodemorse functions

In the test that fails, the encodetomorse function is given the input parameter of " ". This whitespace character is not in the valid input set of English characters for this program; hence the program should output "<CNF>". As such, in the test function, the following are equated:
(i) encodetomorse function's output for the input parameter " " 
(ii) "<CNF>" 
The test however fails, which means that (i) does not equal (ii)

ANALYSIS OF RESULSTS AND CORRECTIONS REQUIRED
The encodetomorse function in morsetranslator_v1_main.py splits any input string at " " points, so when the function processes the input parameter of " ", the 'encodedmessage' variable has the value "", which is returned. (For more details on the encodetomorse function, refer to its code in morsetranslator_v1_main.py program.) This returned value is not equal to "<CNF>" and so the test fails.

Therefore, the encodetomorse function needs to process the " " input in a different way.

CORRECTIONS DONE:
A new draft of the main program is created: morsetranslator_v2.py
To run this program, main_morsetranslator_v2.py should be run.

In the morsetranslator_v2.py program, the encodetomorse function processes the " " input in a separate 'if' clause, such that the 'encodedmessage' variable takes the value "<CNF>".
NOTE: The new code lines in main_morsetranslator_v2.py file have the inline comments  #NEW in draft v2

Also, a new draft of the test program is created: 
test_morsetranslator_v2.py 
The new test program has the same test functions as the previous one.

All five tests now pass.
Screenshot of expected output of running the morsetranslator_v2_main.py program is provided.

