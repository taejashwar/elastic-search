from elasticsearch import Elasticsearch

es = Elasticsearch([{'host':'localhost','port':'9200'}])

es.indices.create(index="cities",ignore=400)

delhi = {"Delhi":['Kebabs','Chaat','Nihari','Chole Bhature','Rolls']}
beng = {"Bengaluru":['Bhajji','Momos','Obbattu','Mangalore Buns','Fresh Juice']}
mumbai = {"Mumbai":['Akuri','Batata Vada','Ragda pattice','Bhel puri','Faluda']}
kolk = {"Kolkata":['Macher Jhol','Shukto','Kosha Mangsho','Mochar Ghonto','Roshogulla']}
chennai = {"Chennai":['Uthappam','Puttu','Sundal','Murukku','Payasam']}
punjab = {"Punjab":['Naan','Aloo paratha','Lassi','Khoa','Kulche']}
hydra = {"Hyderabad":['Haleem','Hyderabadi Biryani','Phirni','Mutton Dalcha','Keema samosa']}
pune = {"Pune":['Poha','Dabeli','Sabudana Vada','Street Dosa','Dahi puri']}
kera = {"Kerala":['Appam','Fish moilee','Palada payasam','Erissery','Idiyappam']}
guja = {"Gujarat":['Gujarati Thali','Thepla','Aam Ras','Dhokla','Basundi']}

es.index(index="cities",doc_type="food",id=1,body=delhi)
es.index(index="cities",doc_type="food",id=2,body=beng)
es.index(index="cities",doc_type="food",id=3,body=mumbai)
es.index(index="cities",doc_type="food",id=4,body=kolk)
es.index(index="cities",doc_type="food",id=5,body=chennai)
es.index(index="cities",doc_type="food",id=6,body=punjab)
es.index(index="cities",doc_type="food",id=7,body=hydra)
es.index(index="cities",doc_type="food",id=8,body=pune)
es.index(index="cities",doc_type="food",id=9,body=kera)
es.index(index="cities",doc_type="food",id=10,body=guja)

if __name__ == '__main__':
    print("INDIAN CITIES")
    print("Select the city:\n1.Delhi\n2.Bengaluru\n3.Mumbai\n4.Kolkata\n5.Chennai\n6.Punjab\n7.Hyderabad\n8.Pune\n9.Kerala\n10.Gujarat\n")
    choice = int(input("Enter your choice:"))
    res = es.get(index="cities",doc_type="food",id=choice)
    print(res['_source'])