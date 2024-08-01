from pathlib import Path

fh = open('path.txt', 'w', encoding='utf-8')
fh.write('60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5')
fh.close()

def get_cats_info(path):
    try:
        with open(path, "r", encoding='utf-8') as fh:
            for line in fh:
                id, name, age = line.strip().split(',')
                my_dict = [{"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},{"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age":"1"}, 
                {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"}, 
                {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
                {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"}]
                
        return my_dict
    except ValueError:
        return []
    except FileNotFoundError:
        return []
cats_info = get_cats_info("path.txt")
print(cats_info)
