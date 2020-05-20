



holding_registers = {
    'dispatch_mw_flag' : [10, 0, 2500],
    'six_sec_raise_flag' : [2, 0, 2600],
    'six_sec_lower_flag' : [4, 77, 2300],
    'sixty_sec_raise_flag' : [51, 0, 3300],
    'sixty_sec_lower_flag' : [6, 0, 4300],
    # 'five_min_raise_flag' : 1
    # 'five_min_lower_flag' : 6
}

def keywithmaxval(d):
     v = list(d.values())
     k = list(d.keys())
     vmax = max(v)
     vmin = min(v)
     # blah=max(v)
     # bLah2=v.index(4)
     return k[v.index(max(v))]


dict_length = len(holding_registers)

# print('{} is the key, {} is the value'.format(holding_registers_floats[0], holding_registers_floats[1]))

maxkey = keywithmaxval(holding_registers)
pass


