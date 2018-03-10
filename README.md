This project replicates and modifies Amazon Echo's Alexa feature. Intel Edison is used to respond to questions.  
"speechtext.py" is a python script that records user input, converts it to text, and sends it to the Intel edison.
"New_Midterm.py" is a script that parses the sent text file for certain keywords and then computes the value of the request information and sends it back to the requesting client.
"receive.py" listens for files sent by the Edison and converts the text file contents to audio.

In order to avoid entering login passwords before content is copied from the client to the Edison or vice versa, you need to generate ssh key pairs on both the machines and copy the public key to the other machine. 
