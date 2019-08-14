import json

mapping = {}

def set_room_mapping(m):
    global mapping
    mapping = m


def parse_room_mapping_file(file):
    with open(file) as f:
        set_room_mapping(json.load(f))


def get_room_mapping():
    return mapping


__all__ = ['get_room_mapping', 'parse_room_mapping_file']
