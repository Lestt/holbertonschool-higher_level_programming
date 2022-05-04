#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return list(
        map(
            lambda element: replace if element == search else element,
            my_list
        )
    )
