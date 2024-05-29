from tqdm import tqdm

# is_latin_string based on https://stackoverflow.com/a/3308844
import unicodedata as ud
latin_dict = dict()
def is_latin_char(char):
	#print(char)
	#print() ; print()
	if char not in latin_dict:
		latin_dict[char] = ('LATIN' in ud.name(char))	
	return latin_dict[char]
def is_latin_string(string):
	return all(is_latin_char(char) for char in string if char.isalpha())

def remove_accents(input_str):
    # Normalize the string to NFKD form
    nfkd_form = ud.normalize('NFKD', input_str)
    # Encode to ASCII bytes, ignoring non-ASCII characters, then decode back to string
    only_ascii = nfkd_form.encode('ASCII', 'ignore').decode('ASCII')
    return only_ascii

places = set()	

with open("planet-latest_geonames.tsv") as file_in:
	for line in tqdm(file_in):
		name, alternative_names, _, _, _, _, _, _, _, _, _, _, _, _, _, country_code, _, _, _, _, _, _, _, _ = line.split('\t')
		alternative_names = alternative_names.split(',')
		for n in [name, *alternative_names]:
			if is_latin_string(n):
				n = remove_accents(n).lower()
				places.add((n, country_code))

with open("placenames.csv", "w") as file_out:
	for n, country_code in places:
		file_out.write(f"{n},{country_code}\n")

