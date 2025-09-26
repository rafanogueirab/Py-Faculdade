#Criando uma página HTML usando Python
html_code = '''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Exemplo de Front-end com Python</title>
</head>
<body>
    <h1>Olá, Mundo!</h1>
    <p>Esta é uma página web criada usando Python</p>
</body>
</html>
'''
from IPython.display import HTML
HTML(html_code)