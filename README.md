# Como usar:
Você pode abrir ou import todas funções do script utilizando: 
```
from cardspython import *
````
... e usar suas funções da seguinte maneira:

**1 - Retornando um csv padrão google/android a partir de um .txt ou .csv**
```
users = open_file()
print(create_csv(users)):
```
Obs: O .txt ou .csv deverá estar separado por vírgulas, exemplo -> 
```
"username, number
username2, number2"
```
**2 - Criando um vcard a partir de um .txt ou outro .csv**
```
users = open_file()
print(create_vcf(users)):
```

**3 - Para retornar um csv no padrão google/android a partir de um Vcard.**
```
users = open_file()
print(csv_to_vcf(users))
```
 Obs: A função open_file() pode ter como parâmetro o nome do arquivo. Caso seja default, será feita a leitura dos arquivos da pasta e será solicitado que escolha o número respectivo do arquivo
 
**4 - Tranformando vcf em csv.**
```
users = open_file()
print(vcf_to_csv(users))
```

**5 - Para retornar todos contatos de um csv**
```
users = open_file()
print(get_contacts_csv(users)):
```

**6 - Para retornar todos os contatos de um vcard**
```
users = open_file()
print(get_contacts_vcf(users)):
```




