import re

# Open file and split into passport segments
passports = open('2020\Day04\input.txt').read().strip().split('\n\n')

# Create dictionary for each field and a validator for that field
fields = {
    'byr': lambda x: len(x) <= 4 and 2002 >= int(x) >= 1920,
    'iyr': lambda x: len(x) <= 4 and 2020 >= int(x) >= 2010,
    'eyr': lambda x: len(x) <= 4 and 2030 >= int(x) >= 2020,
    'hgt': lambda x: (x.endswith('cm') and 193 >= int(x[:-2]) >= 150) or (x.endswith('in') and 76 >= int(x[:-2]) >= 59),
    'hcl': lambda x: re.match('^#[a-f\d]{6}$', x) != None,
    'ecl': lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda x: len(x) == 9  and x.isdigit(),
}

p1 = p2 = 0
 # Iterate over each passport and restructure it into a dictionary
for passport in passports:
    parts = re.split('\s', passport)
    passport_dict = dict(part.split(':') for part in parts)

    # Check if all keys from fields dictionary are in the passport dictionary
    if all(key in passport_dict for key in fields):
        p1 += 1

        #Check if all functions from our fields dictionary return True
        if all(fields[key](passport_dict[key]) for key in fields):
            p2 += 1
print("Part 1:", p1)
print("Part 2:", p2)