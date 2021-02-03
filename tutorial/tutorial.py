import python.person_pb2 as person_pb2

person = person_pb2.Person()
person.name = 'Taiki'
person.id = 1
person.email = 'so99ynoodles@gmail.com'

phone_number = person.phones.add()
phone_number.number = '090-8116-4142'
phone_number.type = person_pb2.Person.MOBILE

home_number = person.phones.add()
home_number.number = '03-1234-5678'
home_number.type = person_pb2.Person.HOME

with open('tutorial.bin', 'wb') as f:
    f.write(person.SerializeToString())
    f.close()

with open('tutorial.bin', 'rb') as f:
    person_read = person_pb2.Person()
    person_read.ParseFromString(f.read())
    print(person_read)
    f.close()
