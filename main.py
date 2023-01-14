import psycopg2
import matplotlib.pyplot as plt
username = 'shramko'
database = 'lab2'
host = 'localhost'
password = '111'
port = '5432'
query1 = '''
CREATE VIEW SpeciesOfEachDinosaur AS 
SELECT species.dino_species, COUNT(dinosaur.species_id) FROM dinosaur
JOIN species ON species.species_id = dinosaur.species_id GROUP BY dino_species

'''
query2 = '''
CREATE VIEW DinosaurDiets AS 
SELECT diet.dino_diet, COUNT(dinosaur.diet_id) FROM dinosaur
JOIN diet ON diet.diet_id = dinosaur.diet_id GROUP BY dino_diet
'''

query3 = '''
CREATE VIEW LengthOfEachDinosaur AS
SELECT dino_name, length_in_meters FROM dinosaur
ORDER BY length_in_meters DESC
'''
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

x = []
y = []


with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    cur.execute('DROP VIEW if exists SpeciesOfEachDinosaur')
    cur.execute(query1)
    cur.execute('SELECT * FROM SpeciesOfEachDinosaur')
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.bar(x, y, width=0.5, alpha=0.6, color='blue')
    plt.ylabel('Кількість особин')
    plt.title('Кількість особин кожного виду')
    plt.show()

    x.clear()
    y.clear()

    cur.execute('DROP VIEW if exists DinosaurDiets')

    cur.execute(query2)
    cur.execute('SELECT * FROM DinosaurDiets')
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.pie(y, labels=x, shadow=True, autopct='%1.1f%%', startangle=180)
    plt.title('Частка способів харчування')
    plt.show()

    x.clear()
    y.clear()
    cur.execute('DROP VIEW if exists LengthOfEachDinosaur')

    cur.execute(query3)
    cur.execute('SELECT * FROM LengthOfEachDinosaur')
    for row in cur:
        y.append(row[1])
        x.append(row[0])
    plt.plot(x, y, 'go-')
    plt.ylabel('Зріст')
    plt.title('Динозаври')
    for x, y in zip(x, y):
        plt.annotate(y, xy=(x, y), xytext=(7, 2), textcoords='offset points')
    plt.show()