import os
import sys
import filecmp

design = input('Enter the design name: ')
company = input('Enter the company name: ')
mall = input('Enter the mall name: ')

print('Design: ', design,)
print('Company: ', company)
print('Mall: ', mall)

# Set string variables
var1 = design
var2 = company
var3 = mall

# EDIT THESE WITH YOUR PATH TO /CoreWebSites/
# Set directory locations
mdirectory = "/Users/danielstockbridge/Documents/PW/CoreWebSites/" + company +"/mall-"+ mall +"/css/vars"
ddirectory = "/Users/danielstockbridge/Documents/PW/CoreWebSites/universal/"+ design +"/design"
udirectory = "/Users/danielstockbridge/Documents/PW/CoreWebSites/universal/universal_base/vars"

# Print Directories - Purely for Debugging - Comment out if not needed
print('Mall Dir: ', mdirectory)
print('Design Dir: ', ddirectory)
print('Universal Dir: ', udirectory)

# Continue Question
continue1 = input('Do you want to continue to diff the files?? (Y or N) ')

# CMD
cmd = "cd %s && grunt server --design=%s --company=%s --mall=%s"%(ddirectory,var1,var2,var3)

Dif Command
from filecmp import dircmp

def print_diff_files(dcmp):
	for name in dcmp.diff_files:
		print("diff_file %s found in %s and %s"%(name, dcmp.left, dcmp.right))
	for sub_dcmp in dcmp.subdirs.values():
		print_diff_files(sub_dcmp)

dcmp = dircmp(udirectory, mdirectory)

# Run command
if continue1 == 'Y':
	print_diff_files(dcmp)
	print(missing_from_mall)
	continue2 = input('Do you want to continue to compile the files?? (Y or N) ')
	if continue2 == 'Y':
		os.system(cmd)
	else:
		print('Exiting after cmp but before compile')
		sys.exit()
else:
	print('Exiting before cmp and compile')
	sys.exit()

print(file=sys.stderr)