from rentomatic.domain.room import Room
from rentomatic.repository.iroomrepo import IRoomRepo


def add_room_use_case(repo: IRoomRepo, room: dict) -> None:
    result = repo.add(Room.from_dict(room))
    print(result)