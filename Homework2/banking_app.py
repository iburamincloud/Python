import sqlite3

def mainMenu():
    while True:
        print("1-> Giriş\n2-> Kayıt Ol\n0-> Çıkış")
        try:
            selectedAction = int(input("lütfen yapmak istediğiniz işlemi seçiniz: "))
            if selectedAction == 1:
                signIn()
            elif selectedAction == 2:
                signUp()
            elif selectedAction == 0:
                break
            else:
                print("Hatalı tuşlama yaptınız lütfen tekrar deneyin!")
                continue
        except:
            print("Hatalı tuşlama yaptınız lütfen tekrar deneyin!")


def customerMenu(customerTC):
    while True:
        print("1-> Göster\n2-> Nakit Ekle\n3-> Nakit Çek\n4-> Nakit Gönder\n0-> Çıkış")
        try:
            selectedAction = int(input("Lütfen yapmak istediğiniz işlemi seçiniz: "))
            if selectedAction == 1:
                showBalance(customerTC)
            elif selectedAction == 2:
                try:
                    cash = float(input("Eklenecek bakiyeyi giriniz: "))
                    addBalance(customerTC,cash)
                except:
                    print("Geçersiz bakiye lütfen yeni bir işlem yapın!!!")
            elif selectedAction == 3:
                try:
                    cash = float(input("Çekilecek tutarı giriniz: "))
                    pullBalance(customerTC,cash)
                except:
                    print("Geçersiz bakiye lütfen yeni bir işlem yapın!!!")
            elif selectedAction == 4:
                try:
                    cash = float(input("Gönderilecek tutarı giriniz: "))
                    tc = input("Gönderilecek kişinin TC sini giriniz: ")
                    dataBaseCursor.execute(f"SELECT * FROM customers WHERE TC={tc}")
                    for data in dataBaseCursor:
                        if data :
                            if pullBalance(customerTC,cash):
                                addBalance(tc,cash)
                    
                except:
                    print("Geçersiz tuşlama yaptınız yeni bir işlem yapın!!!")
            elif selectedAction == 0:
                print("Çıkış Başarılı!")
                break
            else:
                print("Hatalı tuşlama yaptınız lütfen tekrar deneyin!")
                continue
        except:
            print("Hatalı tuşlama yaptınız lütfen tekrar deneyin!")


def signUp():
    try:
        tc = input("TC girin: ")
        password = input("Parola girin: ")
        balance = float(input("Bakiye giriniz: "))
        dataBaseCursor.execute("SELECT * FROM customers")
        for data in dataBaseCursor: 
            if data[0] == tc:
                print("Bu kullanıcı zaten var! Farklı bir işlem yapınız.")
                return
        dataBaseCursor.execute(f"INSERT INTO customers VALUES( '{tc}', '{password}', {balance})")
        dataBase.commit()
        print("Kayıt başarılı!")
        customerMenu(tc)
    except:
        print("Hatalı bakiye girişi yaptınız tekrar deneyin!!!!!")
        signUp()

def signIn():
    tc = input("TC giriniz: ")
    pasword = input("Şifre giriniz: ")
    if dataBaseCursor.execute(f"SELECT * FROM customers WHERE TC={tc}"):
        for data in dataBaseCursor:
            if data[1]==pasword:
                print("giriş başarılı!")
                customerMenu(tc)
                return
            else:
                print("Hatalı giriş yaptınız!!!!")
                return
        print("Kullanıcı bulunamadı!!!")
    


def showBalance(customerTC):
    dataBaseCursor.execute(f"SELECT * FROM customers WHERE TC={customerTC}")
    for data in dataBaseCursor:
        print(f"Bakiye-> {data[2]}")

def addBalance(customerTC,cash):
    dataBaseCursor.execute(f"SELECT * FROM customers WHERE TC={customerTC}")
    for data in dataBaseCursor:
        temp = data
    dataBaseCursor.execute (f"DELETE FROM customers WHERE TC={customerTC}")
    dataBaseCursor.execute(f"INSERT INTO customers VALUES( '{temp[0]}', '{temp[1]}', {temp[2]+cash})")
    dataBase.commit()
    print("Başarıyla yüklendi")

def pullBalance(customerTC,cash):
    dataBaseCursor.execute(f"SELECT * FROM customers WHERE TC={customerTC}")
    for data in dataBaseCursor:
        temp = data
    if temp[2]>=cash:
        dataBaseCursor.execute (f"DELETE FROM customers WHERE TC={customerTC}")
        dataBaseCursor.execute(f"INSERT INTO customers VALUES( '{temp[0]}', '{temp[1]}', {temp[2]-cash})")
        dataBase.commit()
        print("Para çekme işlemi tamamlandı.")
        return True
    else:
        print(f"Para çekme başarısız. Maximum çekilebilecek tutar-> {temp[2]}")
        return False
    
                


dataBase = sqlite3.connect("customers.db")
dataBaseCursor = dataBase.cursor()
dataBaseCursor.execute("CREATE TABLE IF NOT EXISTS customers(TC TEXT, Password TEXT, Balance REAL)")
mainMenu()
dataBase.commit()
dataBase.close()