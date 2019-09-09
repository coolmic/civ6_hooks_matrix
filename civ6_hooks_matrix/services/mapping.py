import json

rooms_mapping = {}

users_mapping = {}


def set_rooms_mapping(m):
    global rooms_mapping
    rooms_mapping = m


def set_users_mapping(m):
    global users_mapping
    users_mapping = m


def parse_mapping_file(file):
    with open(file) as f:
        parsed = json.load(f)
        set_rooms_mapping(parsed['rooms'])
        set_users_mapping(parsed['users'])


def get_rooms_mapping():
    return rooms_mapping


def get_users_mapping():
    return users_mapping


__all__ = ['parse_mapping_file', 'get_rooms_mapping', get_users_mapping]
