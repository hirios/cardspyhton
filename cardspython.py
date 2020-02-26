import os
from pprint import pprint


def locate_file():
    # Mostra os arquivos permitidos e pede para escolher um deles,
    # caso haja somente um, este será escolhido automaticamente
    path = os.listdir()
    path = [x for x in path if x[-4:] in [".txt", ".csv", ".vcf"]]

    contador = 1
    if len(path) == 1:
        print("[1]", path[0])
    else:
        for c in path:
            print([contador], c)
            contador += 1

    print()
    n = int(input('Digite o número do arquivo: ')) - 1
    return path[n]


def open_file(default='locate_file()'):
    # Aceita o nome do arquivo como paramêtro. O default mostra os arquivos
    # e pede pra escolher o número dele a partir da função locate_file()
    if default == 'locate_file()':
        default = str(locate_file())

    users = open(default, "r").read()
    try:
        users = users.replace(";;;;;;", "")
    except:
        pass

    users = users.replace(";", ",")
    return users


class Pyvcard():
    # Recebe uma string contendo os contatos e seus números, separados por vírgulos ("username, number\n")
    def __init__(self, users):
        self.users = users


    def read_string_contacts(self):
        # Lê .csv, .txt ou string que estes estejam separados por virgula (username, number)
        self.users = self.users.strip().split("\n")
        self.users = [x.split(",") for x in self.users]
        self.username, self.number = [[x[0] for x in self.users], [x[1] for x in self.users]]


    def read_vcard(self):
        # Lê apenas arquivo vcard
        self.users = self.users.strip().replace(",", ";").split("\n")
        self.username, self.number = [[x.split("FN:")[1] for x in self.users if "FN" in x],[x.split(":")[-1] for x in self.users if "TEL;" in x]]


    def shape_vcard(self, username, number):
        # Encorpora dados num modelo vcard

        username_split = username.split()[::-1]
        username_split = list(filter(None, username_split))
        username_split = [x for x in username_split if x != []]
        
        
        if len(username_split) == 1:
            username_join = ";" + username_split[0] + ";;;"

        elif len(username_split) > 1 < 5:
            username_join = ";".join(username_split) + ";" * (4 - (len(username_split) -1))

        elif len(username_split) == 0:
            username_join = ";" + " " + ";;;"

        elif len(username_split) <= 5:
            username_join = ";" + "ERRRRRRRRROOOOOOO" + ";;;"


        return f"""BEGIN:VCARD
VERSION:3.0
FN:{username}
N:{username_join}
TEL;TYPE=CELL:{number}
END:VCARD
"""


    def get_contacts_vcard(self):
        # Obtem o nome e o número de cada contato em self.username e self.number do csv selecionado
        username1 = self.username
        number1 = self.number

        contacts_of_vcard = ""
        for c in range(0, len(username1)):
            contacts_of_vcard += username1[c] + "," + number1[c] + "\n"

        return contacts_of_vcard


    # Retorna uma string com o vcard
    def vcard_finale(self):
        username = self.username
        number = self.number
        string = ''
        for c in range(0, len(username)):
            try:
                string += str(self.shape_vcard(username[c], number[c]))
            except:
                pass
        return string


class Pycsv():
    def __init__(self,users):
        self.users = users


    def read_string_contacts(self):
        # Lerá .csv, .txt ou string separados por vírgula: "username, number\n")
        self.users = self.users.strip().split("\n")
        self.users = [x.split(",") for x in self.users]
        self.username, self.number = [[x[0] for x in self.users], [x[1] for x in self.users]]


    def read_csv_google(self):
        # Lê csv somente se estiver na mesma padronização da google
        self.users = self.users.strip().split("\n")
        [x for x in self.users]
        self.users = [x.split(",") for x in self.users]
        self.username, self.number = [[x[0]][0] for x in self.users if [x[0]][0] != 'Name'], [[x[30]][0] for x in self.users if [x[30]][0] != 'Phone 1 - Value']


    def get_contacts_csv(self):
        # Obtem o nome e o número de cada contato em self.username e self.number do csv selecionado
        username = self.username
        number = self.number

        contacts_of_csv = ""
        for c in range(0, len(username)):
            contacts_of_csv += (username[c] + "," + number[c] + "\n")

        return contacts_of_csv


    def check_csv(self):
        if self.users.split("\n")[2].count(",") > 1:
            return self.read_csv_google()
        else:
            return self.read_string_contacts()


    def csv_finale(self):
        # Retorna uma string com o csv final
        username = self.username
        number = self.number

        csv_finale = """Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,Phone 1 - Type,Phone 1 - Value,Phone 2 - Type,Phone 2 - Value;\n"""
        for c in range(0, len(username)):
            csv_finale += (username[c] + ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,," + number[c] + "\n")

        return csv_finale


def get_contacts_vcard(users):
    # Pega os contatos no vcard e retorna no padrão -> "name-exemplo, 40028922"
    start = Pyvcard(users)
    start.read_vcard()
    string = start.get_contacts_vcard()
    return string


def get_contacts_csv(users):
    # Pega os contatos de um csv da google e retorna no padrão -> "name-exemplo, 40028922"
    start = Pycsv(users)
    start.check_csv()
    string = start.get_contacts_csv()
    return string


def create_csv(users):
    # Cria um csv a partir de um .txt, .csv, .vcf ou string se estiverem no padão -> "name-exemplo, 40028922",
    # ou no padrão da google
    start = Pycsv(users)
    start.check_csv()
    string = start.csv_finale()
    return string


def create_vcard(users):
    # Cria um Vcard a partir de um .txt, .csv ou string se estiverem assim -> "name-exemplo, 40028922"
    start = Pyvcard(users)
    start.read_string_contacts()
    string = start.vcard_finale()
    return string


def csv_to_vcard(users):
    # Transforma csv em vcard
    csv = get_contacts_csv(users)
    return create_vcard(csv)


def vcard_to_csv(users):
    # Transforma vcard em csv
    vcard = get_contacts_vcard(users)
    return create_csv(vcard)



