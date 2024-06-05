from rentomatic.repository.memrepo import MemRepo
from rentomatic.use_cases.room_list import room_list_use_case, room_price_all_use_case

rooms = [
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 215,
        "price": 39,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    },
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 215,
        "price": 39,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    },
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 215,
        "price": 39,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    },
]

repo = MemRepo(rooms)
result = room_list_use_case(repo)
print([room.to_dict() for room in result])

total_price = room_price_all_use_case(repo)
print(f"total: {total_price}")