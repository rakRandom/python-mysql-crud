# Python MySQL CRUD

Some notes on how to connect a MySQL database using Python 3.12

## INSTALL
```
pip install mysql-connector-python
```

## IMPORT
```
import mysql.connector
```

## CONNECT
```
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="banco"
)

cursor = connection.cursor()
```

## CREATE
```
nome_produto = "todynho"
valor = 3

command = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(command)
connection.commit()
```

## READ
```
command = 'SELECT * FROM vendas'
cursor.execute(command)
result = cursor.fetchall()
for product in result:
    print(f"{product[0]} - {product[1]} - R${product[2]:.2f}")
```

output example:
```
3 - todynho - R$4.00
3 - todynho - R$6.00
```

## UPDATE
```
nome_produto = "todynho"
valor = 3

command = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(command)
connection.commit()
```

## DELETE
```
nome_produto = "todynho"

command = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(command)
connection.commit()
```

## CLOSE
```
cursor.close()
connection.close()
```
