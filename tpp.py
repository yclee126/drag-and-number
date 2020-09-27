# Simple 1D parser for tkDnD

def find_end(string):
    ignore = False
    length = len(string)
    for i, char in enumerate(string):
        if char == '\\':
            ignore = True
        elif char == ' ' and not ignore:
            return i - 1
        else:
            ignore = False
    return length - 1

def parse(t_list):
    t_list = str(t_list)
    t_list_len = len(t_list)
    p_list = []
    
    start_index = 0
    while start_index < t_list_len:
        if t_list[start_index] == '{':
            end_index = t_list.find('}', start_index)
            one_line = t_list[start_index+1:end_index]  # strip {} at the ends
            p_list.append(one_line)
            start_index = end_index + 2
        else:
            end_index = find_end(t_list[start_index:]) + start_index
            one_line = t_list[start_index:end_index+1]
            one_line = one_line.replace('\\', '')
            p_list.append(one_line)
            start_index = end_index + 2
            
    return p_list