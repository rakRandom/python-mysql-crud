"""
# CONNECT
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="banco"
)

cursor = connection.cursor()

# CREATE
nome_produto = "todynho"
valor = 3

command = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(command)
connection.commit()

# READ
command = 'SELECT * FROM vendas'
cursor.execute(command)
result = cursor.fetchall()
for product in result:
    print(f"{product[0]} - {product[1]} - R${product[2]:.2f}")

# UPDATE
nome_produto = "todynho"
valor = 3

command = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(command)
connection.commit()

# DELETE
nome_produto = "todynho"

command = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(command)
connection.commit()

# CLOSE
cursor.close()
connection.close()
"""

import mysql.connector


def connect_db():
    # CONNECT
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="banco"
    )
    cursor = connection.cursor()
    return connection, cursor


def create(connection, cursor, nome_produto, valor):
    # CREATE
    command = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(command)
    connection.commit()


def read(cursor):
    # READ
    command = 'SELECT * FROM vendas'
    cursor.execute(command)
    return cursor.fetchall()


def update(connection, cursor, set_cmd, condition):
    # UPDATE
    command = f'UPDATE vendas SET {set_cmd} WHERE {condition}'
    cursor.execute(command)
    connection.commit()


def delete(connection, cursor, condition):
    # DELETE
    command = f'DELETE FROM vendas WHERE {condition}'
    cursor.execute(command)
    connection.commit()


def main():
    connection, cursor = connect_db()

    create(connection, cursor, "todynho", 4)
    table = read(cursor)
    for product in table:
        print(f"{product[0]} - {product[1]} - R${product[2]:.2f}")

    update(connection, cursor, 'valor = 6', 'nome_produto = "todynho"')
    table = read(cursor)
    for product in table:
        print(f"{product[0]} - {product[1]} - R${product[2]:.2f}")
    
    delete(connection, cursor, 'nome_produto = "todynho"')

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
