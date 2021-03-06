# Exemplos de uso:

Você pode abrir ou import todas funções do script utilizando: 
```
from cardspython import *
````
... e usar suas funções da seguinte maneira:


**Criando csv de contatos a partir de uma string**
```
string = """Celia Nicanor, 04111958186100
Celio planalto, 04164984798300
Jarlei Gas, 04177991436700
Julian barra, 04174991945000
Juliane ifba, 04177991746600
Luiz Mariano, 04177991040300
Lurdes Erenilda, 04174999738200
Elenice, 04177981527600
Simone lotérica, 04166984522700"""

users = string
print(create_csv(users))
```

**Criando vcard a partir de um csv na pasta**
```
>>> users = open_file()
 [1] exemplo.csv
 [2] exmplo.txt
    
print(create_vcard(users))
```

**Retornando vcard a partir de um csv**
```
users = open_file("teste.vcf")
print(csv_to_vcard(users))
```

# Outras formas de uso:

**1 - Retornando um csv padrão google/android a partir de uma string, .txt ou .csv**
```
users = open_file()
print(create_csv(users))
```
Obs: O .txt ou .csv deverá estar separado por vírgulas, exemplo -> 
```
"username, number
username2, number2"
```
**2 - Criando um vcard a partir de um .txt ou outro .csv**
```
users = open_file()
print(create_vcard(users))
```

**3 - Para retornar um csv no padrão google/android a partir de um Vcard.**
```
users = open_file()
print(csv_to_vcard(users))
```
 Obs: A função open_file() pode ter como parâmetro o nome do arquivo. Caso seja default, será feita a leitura dos arquivos da pasta e será solicitado que escolha o número respectivo do arquivo
 
**4 - Tranformando vcf em csv.**
```
users = open_file()
print(vcard_to_csv(users))
```

**5 - Para retornar todos contatos de um csv**
```
users = open_file()
print(get_contacts_csv(users))
```

**6 - Para retornar todos os contatos de um vcard**
```
users = open_file()
print(get_contacts_vcard(users))
```

