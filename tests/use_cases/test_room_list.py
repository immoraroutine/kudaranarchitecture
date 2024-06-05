import uuid
from unittest import mock

import pytest

from rentomatic.domain.room import Room
from rentomatic.use_cases.room_list import room_list_use_case, room_price_all_use_case, room_size_all_use_case


@pytest.fixture
def domain_rooms():
    room_1 = Room(
        code=uuid.uuid4(),
        size=215,
        price=39,
        longitude=-0.09998975,
        latitude=51.75436293,
    )
    return [room_1]


def test_room_list_without_parameters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    result = room_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_rooms


def test_room_price_all(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    result = room_price_all_use_case(repo)

    repo.list.assert_called_with()
    assert result == 39


def test_room_size_all_use_case(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    result = room_size_all_use_case(repo)

    repo.list.assert_called_with()
    assert result == 215