#print usa argumentos
#sep é oq define o que vai ser o separador, o defaul é apenas um espaço
# \r\n (return e linefeed) -> CRLF (Windows)
# \n -> LF (linux e mac)
print(12, 34, sep='-', end='#')
print(56, 78, sep= "-", end= '\r\n')
print(9, 10, sep='-', end= '\n')
#letras maiusculas e minusculas fazem diferença no python
