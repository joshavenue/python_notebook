## Sending "r" means open in read mode, which is the default. 
## Sending "w" means write mode, for rewriting the contents of a file.
## Sending "a" means append mode, for adding new content to the end of the file.
## 'b' stands for non-binary file type

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")
