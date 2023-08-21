# import PdfFileWriter and PdfFileReader
# class from PyPDF2 library
from PyPDF2 import PdfWriter, PdfReader

# create a PdfFileWriter object
out = PdfWriter()

# Open our PDF file with the PdfFileReader
file = PdfReader("I AM LONEWOLF.pdf")

# Get number of pages in original file
num = len(file.pages)

# Iterate through every page of the original
# file and add it to our new file.
for idx in range(num):
	
	# Get the page at index idx
	page = file.pages[idx]
	
	# Add it to the output file
	out.add_page(page)

# Create a variable password and store
# our password in it.
password = "pass"

# Encrypt the new file with the entered password
out.encrypt(password)

# Open a new file "myfile_encrypted.pdf"
with open("Encrypted.pdf", "wb") as f:
	
	# Write our encrypted PDF to this file
	out.write(f)
