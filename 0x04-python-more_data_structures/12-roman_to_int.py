#!/usr/bin/python3
<<<<<<< HEAD
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    p = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[c]] >= p:
                res += val[roman_string[c]]
            else:
                res -= val[roman_string[c]]
            p = val[roman_string[c]]
    return res
=======
def complex_delete(a_dictionary, value):
	if value is not None:
		keys = list(a_dictionary.keys())
		for key in keys:
			if a_dictionary[key] == value:
				del a_dictionary[key]
	return a_dictionary
>>>>>>> 88bb34c055fc9ac0627085273404479cd3ca7af8
