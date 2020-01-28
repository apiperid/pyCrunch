# pyCrunch

This repository contains two .py files with with you can create a brute force list of passwords given a
specific charset.

# Arguments for crunch.py

Run the .py given file with the command :

<code>python crunch.py arg1 arg2 arg3 arg4</code> 

Where args are :

<ul>
	<li>arg1 = the length of the brute force passwords</li>
	<li>arg2 = the charset of the brute force passwords</li>
	<li>arg3 = the output file in which the programs will save the brute force passwords</li>
	<li>arg4 = the update step (after how many generated password you will be updated)</li>
</ul>

arg1 and arg4 must be integer greater than 0.The others must be string

# Arguments for specificCrunch.py

Run the .py given file with the command :

<code>python specificCrunch.py arg1 arg2 arg3 arg4 arg5</code>

Where args are :

<ul>
	<li>arg1 = the charset of the brute force passwords</li>
	<li>arg2 = the output file in which the programs will save the brute force passwords</li>
	<li>arg3 = the first password from which we will start generating passwords</li>
	<li>arg4 = number of passwords you want to be generated</li>
	<li>arg5 = the update step (same as crunch.py)</li>
</ul>

arg4 and arg5 must be integer greater than 0.The others must be string.The password list will contain<br>
passwords with length same as the first password given by the user.

# Requirements

None
 
