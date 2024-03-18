import csv

# Création d'un fichier CSV
def create_csv_file():
    with open('SystemeScriptSecurite/data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Jean", "25 ans", "Paris"])
        writer.writerow(["Marie", "30 ans", "Lyon"])
        writer.writerow(["Pierre", "22 ans", "Marseille"])
        writer.writerow(["Sophie", "35 ans", "Lille"])

create = create_csv_file()

