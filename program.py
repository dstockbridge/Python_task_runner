import os
import sys

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

# Diff Process
folder_univ = set(os.listdir(udirectory))
folder_mall = set(os.listdir(mdirectory))
missing_from_mall = folder_univ - folder_mall

# CMD
cmd = "cd %s && grunt server --design=%s --company=%s --mall=%s"%(ddirectory,var1,var2,var3)

# Run command
if continue1 == 'Y':
	# print_diff_files(dcmp)
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