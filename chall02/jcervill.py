import sys

i = 0
morse = {
	'a':'.-',
	'A':'.-',
	'b':'-...',
	'B':'-...',
	'c':'-.-.',
	'C':'-.-.',
	'd':'-..',
	'D':'-..',
	'e':'.',
	'E':'.',
	'f':'..-.',
	'F':'..-.',
	'g':'--.',
	'G':'--.',
	'h':'....',
	'H':'....',
	'i':'..',
	'I':'..',
	'j':'.---',
	'J':'.---',
	'k':'-.-',
	'K':'-.-',
	'l':'.-..',
	'L':'.-..',
	'm':'--',
	'M':'--',
	'n':'-.',
	'N':'-.',
	'o':'---',
	'O':'---',
	'p':'.--.',
	'P':'.--.',
	'q':'--.-',
	'Q':'--.-',
	'r':'.-.',
	'R':'.-.',
	's':'...',
	'S':'...',
	't':'-',
	'T':'-',
	'u':'..-',
	'U':'..-',
	'v':'...-',
	'V':'...-',
	'w':'.--',
	'W':'.--',
	'x':'-..-',
	'X':'-..-',
	'y':'-.--',
	'Y':'-.--',
	'z':'--..',
	'Z':'--..',
	' ':' '
}
if (len(sys.argv) == 2):
	str = ''
	if (sys.argv[1].isalpha()):
		while (i < len(sys.argv[1])):
			str = str + (morse[sys.argv[1][i]])
			i = i + 1
		print (str)
	else:
		print("usage:" + sys.argv[0] + "<a-zA-Z string>")
		exit(1)
else:
	print("usage: " + sys.argv[0] + " <a-zA-Z string>")
	exit(1)
