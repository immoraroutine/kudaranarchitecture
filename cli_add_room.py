from rentomatic.repository.sqliterepo import SqliteRepo
from rentomatic.use_cases.add_room import add_room_use_case

repo = SqliteRepo("rentomatic.db")
code = input("code: ")
size = input("size: ")
price = input("price: ")
longitude = input("longitude: ")
latitude = input("latitude: ")
room = {"code": code, "size": size, "price": price, "longitude": longitude, "latitude": latitude}
result = add_room_use_case(repo, room)