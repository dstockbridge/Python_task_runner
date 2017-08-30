import os
import sys

design = input('Enter the design name: ')
company = input('Enter the company name: ')
mall = input('Enter the mall name: ')

# Print info to check for typos
print('\nPlease check input information below for accuracy:')
print('Design: ', design,)
print('Company: ', company)
print('Mall: ', mall, "\n")

# EDIT THESE WITH YOUR PATH TO /CoreWebSites/
# Set directory locations
mdirectory = "/Users/danielstockbridge/Documents/PW/CoreWebSites/" + company +"/mall-"+ mall +"/css/vars"
ddirectory = "/Users/danielstockbridge/Documents/PW/CoreWebSites/universal/"+ design +"/design"
udirectory = "/Users/danielstockbridge/Documents/PW/CoreWebSites/universal/universal_base/vars"

# Print Directories - Purely for Debugging - Comment out if not needed
# print('Mall Dir: ', mdirectory)
# print('Design Dir: ', ddirectory)
# print('Universal Dir: ', udirectory, "\n")

# Diff Process
folder_univ = set(os.listdir(udirectory))
folder_mall = set(os.listdir(mdirectory))
missing_from_mall = folder_univ - folder_mall

# Grunt command
cmd = "cd %s && grunt server --design=%s --company=%s --mall=%s"%(ddirectory,design,company,mall)

# Run command
# print_diff_files
print("\n".join(missing_from_mall))

# Post-diff continue check
continue2 = input('Do you want to continue to compile the files?? (Y or N) ')
if continue2 == 'Y':
	os.system(cmd)
else:
	print('Exiting after diff but before compile')
	sys.exit()


print(file=sys.stderr)