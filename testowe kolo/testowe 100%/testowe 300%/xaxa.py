def file_quest(text):
	# file_name = input("Wprowadź nazwę pliku: ")
	file_name = 'nazwa.txt'

	text = text.lower()

	txt_list = text.replace('.', '').replace(',', '').split(' ')

	with open(file_name, 'w') as f:
		f.write('\n'.join([word for word in txt_list if txt_list.count(word) == 1]))

# text = input("Wprowadź tekst:")
text = 'Ala ma kota. ala'
file_quest(text)