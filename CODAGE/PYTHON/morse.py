alphabet = {
"a" : ".-",
"b" : "-...",
"c" : "-.-.",
"d" : "-..",
"e" : ".",
"f" : "..-.",
"g" : "--.",
"h" : "....",
"i" : "..",
"j" : ".---",
"k" : "-.-",
"l" : ".-..",
"m" : "--",
"n" : "-.",
"o" : "---",
"p" : ".--.",
"q" : "--.-",
"r" : ".-.",
"s" : "...",
"t" : "-",
"u" : "..-",
"v" : "...-",
"w" : ".--",
"x" : "-..-",
"y" : "-.--", 
"z" : "--..",
" " : "/",
"." : "//",
"," : ",",
"1" : ".----",
"2" : "..---",
"3" : "...--",
"4" : "....-",
"5" : ".....",
"6" : "-....",
"7" : "--...",
"8" : "---..",
"9" : "----.",
"0" : "-----",
"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--", 
"Z" : "--..",
"'" : " ",
"-" : " ",
"(" : " ",
")" : " ",
"!" : "!",
"?" : "?"
}

print("Bonjour, bienenu(e) dans ce traucteur rapide de morse, il te sffit d'ecrire : trad(...)")

#Pour traduire une lettre
def traduire(a):
  return alphabet[a]

#Pour traduire un mot ou des phrases
lettre = []
def trad(b):
  lettre = []
  mot = b
  lettre_actuelle = 0
  while lettre_actuelle < len(mot) :
    lettre.append(traduire(mot[lettre_actuelle]))
    print(traduire(mot[lettre_actuelle]))
    lettre_actuelle = lettre_actuelle + 1
   