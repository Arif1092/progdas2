import mysql.connector as conn

def koneksi():
    return conn.connect(
        host="localhost",
        user="root",
        password="",
        database="sisfo"
    )

def tambah_data(cursor,nama,username,password):
    sql = "INSERT INTO user (nama,username,password) VALUES (%s,%s,%s)"
    var = (nama,username,password)
    cursor.execute(sql,var)
    db.commit()
    print("Data telah di tambah")

def tampil_data(cursor):
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    for row in result:
        print(row)

def update_data(cursor,id,nama,username,password):
    sql = "UPDATE user SET nama = %s,username=%s,password= %s WHERE id = %s"
    val = (nama,username,password,id)
    cursor.execute(sql,val)
    db.commit()
    print("Data telah di update.")

def delete_data(cursor,id):
    sql = "DELETE FROM `user` WHERE id = %s"
    val = (id,)
    cursor.execute(sql,val)
    db.commit()
    print("Data telah Di hapus")


def display_data():
    print("======== Data User ========")
    tampil_data(cursor)
    print("===========================")
    

##membuat koneksi ke database
db = koneksi()
cursor = db.cursor()

while True:
    display_data()
    print("1. Tambah Data")
    print("2. Edit Data")
    print("3. Delete Data")
    print("4. Keluar Aplikasi")
    menu = input("masukan Nomor menu: ")
    if menu == "1":
        nama = input("masukan nama: ")
        username = input("masukan username: ")
        password = input("masukan password: ")
        tambah_data(cursor,nama,username,password)
    elif menu == "2":
        id = input("masukan id")
        nama = input("masukan nama: ")
        username = input("masukan username: ")
        password = input("masukan password: ")
        update_data(cursor,id,nama,username,password)
    elif menu == "3":
        id = input("Masukan id yang ingin di hapus: ")
        delete_data(cursor,id)
    elif menu == "4":
        print("terimakasih sudah mencoba,anda telah keluar")
        break
    else:
        print("input tidak valid. silakan pilihan nomer menu yang benar")

cursor.close()
db.close()

        



