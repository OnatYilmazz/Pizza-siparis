#Mustafa Onat Yılmaz

import datetime
import csv

#Global değişkenler
totdesc = ""
totcost = 0

#Sipariş toplamını veren method
def get_cost(cost):
    global totcost
    totcost = totcost + cost
    return totcost

#Sipariş edilen ürünleri ekleyen method
def get_description(desc):
    global totdesc
    if totdesc == "":
        totdesc = desc
    else:
        totdesc = totdesc + ", " + desc
    return totdesc

#Pizza sınıfı
class Pizza:
  def __init__(self, desc, cost):
        #Alttaki tanımlar program çalışmadığında test etmek için kullanıldı
        self.desc = desc
        self.cost = cost
        get_description(desc)
        get_cost(cost)
        #Pizzanın açıklaması ve fiyatı genel toplama eklendi

#Soslar ve ekleneceklerin sınıfı
class Decorator:
  def __init__(self, desc, cost):
      #Alttaki tanımlar program çalışmadığında test etmek için kullanıldı
      self.desc = desc
      self.cost = cost
      get_description(desc)
      get_cost(cost)
      # Sosun ve ekleneceklerin açıklaması ve fiyatı genel toplama eklendi

#Menü okunmak üzere açıldı
dosya = open("Menu.txt","r",encoding="utf-8")
for i in range(5):
   print(dosya.readline())
    #Pizzalar ekranda gösterildi

#Kullanıcının pizza seçimi yapması
Piz = input("Pizzanız: ")

#Kullanıcının seçimine göre Pizza sınıfında üye oluşturuluyor
if int(Piz) == 1:
    Klasik = Pizza("Klasik Pizza" , 90)
elif int(Piz) == 2:
    Margarita = Pizza("Margarita Pizza" ,60)
elif int(Piz) == 3:
    TurkPizza = Pizza("Türk Pizza",70)
elif int(Piz) == 4:
    SadePizza = Pizza("Sade Pizza",80)


for i in range(7):
   print(dosya.readline())
   #Soslar ve eklenecekler ekranda gösterildi

#Kullanıcının Sos ve eklenecek seçimi yapması
Dec = input("Sosunuz: ")

#Kullanıcının seçimine göre Decorator sınıfında üye oluşturuluyor
if int(Dec) == 11:
    Zeytin = Decorator("Zeytin",5)
elif int(Dec) == 12:
    Mantarlar = Decorator("Mantarlar",7)
elif int(Dec) == 13:
    KeciPeyniri = Decorator("Keçi Peyniri",8)
elif int(Dec) == 14:
    Et = Decorator("Et",9)
elif int(Dec) == 15:
    Sogan = Decorator("Soğan",6)
elif int(Dec) == 16:
    Misir = Decorator("Mısır",4)

#Menü sonundaki teşekkür mesajı ekranda gösterildi
for i in range(1):
   print(dosya.readline())

#Tüm ürünlerin açıklaması ve fiyat toplamı ekranda gösterildi
print("Seçilenler: " + totdesc)
print("Toplam Fiyat: " + str(totcost))

#Kullanıcı adı, TC kimlik numarası, Kredi kartı numarası ve şifresi, kullanıcıdan alındı
name = input("Kullanıcı Adı Giriniz: ")

number = input("TC Kimlik Numarası Giriniz : ")

creditcard = input("Kredi Kartı Giriniz: ")

password = input("Kredi Kartı Şifreniz: ")

#zaman da eklenerek tüm bilgiler csv dosyasına kaydedildi
with open('Orders_Database.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow([ name , number , creditcard, password, totdesc, totcost, datetime.datetime.now()])