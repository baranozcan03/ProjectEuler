'''
Question Id: 89
Question Name: Roman Numerals
The 11K text file, roman.txt (right click and 'Save Link/Target As...'), 
contains one thousand numbers written in valid, but not necessarily minimal, 
Find the number of characters saved by writing each of these in their minimal form.
Note: You can assume that all the Roman numerals in the file contain no 
more than four consecutive identical units.

'''

from timeit import default_timer as timer
import re

#intuitively, we can substitue the non-minimal forms of the roman numerals with their minimal forms
#and calculate the savings in characters.
#this can be done by using a dictionary that maps the non-minimal forms to their minimal forms.
#we can then iterate through the file and use re.subn to replace all occurences of the non-minimal forms with their minimal forms.
#we can then calculate the savings by multiplying the number of replacements 
#made by the difference in the number of characters between the non-minimal and minimal forms.

def calculate_minimal_roman_savings(file_name: str) -> int:
    # Dictionary mapping non-minimal Roman numeral forms to their minimal equivalents
    optimization_map = {
        "VIIII": "IX",  # 'VIIII' (9) is reduced to 'IX'
        "IIII": "IV",   # 'IIII' (4) is reduced to 'IV'
        "LXXXX": "XC",  # 'LXXXX' (90) is reduced to 'XC'
        "XXXX": "XL",   # 'XXXX' (40) is reduced to 'XL'
        "DCCCC": "CM",  # 'DCCCC' (900) is reduced to 'CM'
        "CCCC": "CD"    # 'CCCC' (400) is reduced to 'CD'
    }
    
    savings = 0  # Initialize savings counter to store total character savings

    # Open the file and process each line, each representing a Roman numeral
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()  # Remove any leading/trailing whitespace
            for original, minimal in optimization_map.items():
                # Use re.subn to replace all occurrences of 'original' with 'minimal' in the line
                # re.subn returns a tuple with the modified line and the number of replacements made
                line, substitutions = re.subn(original, minimal, line)
                
                # Calculate the total characters saved for this specific replacement
                # (len(original) - len(minimal)) gives the characters saved per replacement
                # We multiply by 'substitutions' to account for all instances in the line
                savings += substitutions * (len(original) - len(minimal))
    return savings


start = timer()
file_name = "0089_roman.txt"
result = calculate_minimal_roman_savings(file_name)
end = timer()

print(f"Result: {result}")
print(f"Time taken: {end - start} seconds")

#the answer is : 743
#time it took : 0.015357343999767181 seconds