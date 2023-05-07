import csv
import json

idioms = {}

with open('chineseIdioms.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    # Skip the header line
    headers = next(f) 
    for id, idiom, book1, book2, book3, book4, book5, book6, versatility in reader:
        idioms[idiom] = {'book1': book1, 
                         'book2': book2, 
                         'book3': book3, 
                         'book4': book4, 
                         'book5': book5, 
                         'book6': book6, 
                         'versatility': versatility}

with open('chineseIdioms.json', 'w', encoding='utf-8') as f:
    json_object = f.write(json.dumps(idioms, ensure_ascii=False))
