with open('hi.txt') as f:
	print(f.read())             ## An alternative way of doing this is using with statements. 
                              ## This creates a temporary variable (often called f), 
                              ## which is only accessible in the indented block of the with statement.
