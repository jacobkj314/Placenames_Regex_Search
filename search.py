import re
from tqdm import tqdm

places = list()
try:
	with open('placenames.csv') as placenames:
		for place_cc in tqdm(placenames):
			place_cc = place_cc.strip('\n').strip(' ')
			place = place_cc[:-3]
			country_code = place_cc[-2:]
			#print(place_cc)
			#print(country_code, len(country_code))
			places.append((place, country_code))
except FileNotFoundError as e:
	print("Be sure to download and preprocess the placenames list before using search.py! See README.md for instructions.")
	raise e

print("Usage:\nType a regular expression to match a placename. Optionally add a tab and a 2-letter country code (ISO-3166) after the regular expression to filter to places in a particular country.")
print()

while True:
	line = input('> ')
	if line == '':
		continue

	regex_cc = line.split('\t')

	cc_validator = lambda x : True
	regex = regex_cc[0].lower()
	if len(regex_cc) > 1:
		country_code = regex_cc[1]
		cc_validator = lambda x : (x == country_code)


	for place, cc in places:
		cc_match = cc_validator(cc)
		regex_match = re.fullmatch(regex, place)
		#print(f"does {cc} match?: {cc_match}")
		#print(f"does {place} match?: {regex_match}")
		if cc_match and regex_match:
			print(place, end='\t')
	print()

