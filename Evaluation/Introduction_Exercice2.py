def remove_spaces(string):
	char_tab=[]
	space=False
	for c in string:
		if c==" ":
			if space==False:
				char_tab.append(c)
				space=True
		else:
			char_tab.append(c)
			space=False

	while char_tab[0] == " ":
		char_tab.pop(0)


	while char_tab[-1] == " ":
		char_tab.pop(-1)
	return "".join(char_tab)

def remove_special(string):
	char_tab=[]
	special=list("!\"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c")
	for c in string:
		if c not in special:
			char_tab.append(c)

	return "".join(char_tab)

def get_domain(string):
	return string[string.find("/")+2:string.find(".")]


print(remove_spaces("  bonjour  je suis Luc!  "))	
print(remove_special("b;o!nj?ou|r+"))
print(get_domain("https://github.com"))
