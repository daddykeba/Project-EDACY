import csv
from faker import Faker

record_count = 500
fake = Faker()

def create_csv_file():
    with open('D:/Django-Tutoriel/talents.csv', 'w', newline='') as csvfile:
        fiednames = ['id', 'prenom', 'nom', 'genre', 'age', 'background', 'cohorte', 'tauxPart',
                     'visiPlat', 'discussion', 'noteTalent', 'noteInst', 'retards', 'absences', 'parti']
        writer = csv.DictWriter(csvfile, fieldnames=fiednames)
        writer.writeheader()

        for i in range(record_count):
            writer.writerow({
                'id': fake.random_int(min=1, max=10000),
                'prenom': fake.first_name(),
                'nom': fake.last_name(),
                'genre': fake.random_element(elements=('F', 'M')),
                'age': fake.random_int(min=18, max=30),
                'background': fake.random_element(elements=('Licence 3', 'Master 1', 'Master 2')),
                'cohorte': fake.random_element(elements=('cohorte 7', 'cohorte 6', 'cohorte 5')),
                'tauxPart': fake.random_int(min=1, max=50),
                'visiPlat': fake.random_int(min=1, max=30),
                'discussion': fake.random_int(min=1, max=50),
                'noteTalent': fake.random_int(min=0, max=20),
                'noteInst': fake.random_int(min=0, max=20),
                'retards': fake.random_int(min=0, max=20),
                'absences': fake.random_int(min=0, max=4),
                'parti': fake.random_element(elements=('Oui', 'Non'))
            })


if __name__=='__main__':
    create_csv_file()