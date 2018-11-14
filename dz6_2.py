# -*- coding: utf-8 -*-
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", 2: "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

for dicts in documents:
    try:
        print(dicts['number'], dicts['name'])
    except KeyError:
        print('num not found')
