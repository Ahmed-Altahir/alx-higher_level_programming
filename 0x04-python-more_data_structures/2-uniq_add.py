#!/usr/bin/python3
def uniq_add(my_list=[]):
    ui = 0
    for n in set(my_list):
        ui += n
    return ui
