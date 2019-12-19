#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on December 2019
# This program finds the average mark from numbers given


def unicode_conversion(single_char):
    # This function converts the character to a hexadecimal

    conversion = {}

    conversion[' '] = "20" 
    conversion['a'] = "61" 
    conversion['b'] = "62" 
    conversion['c'] = "63" 
    conversion['d'] = "64" 
    conversion['e'] = "65" 
    conversion['f'] = "66" 
    conversion['g'] = "67" 
    conversion['h'] = "68" 
    conversion['i'] = "69" 
    conversion['j'] = "6a" 
    conversion['k'] = "6b" 
    conversion['l'] = "6c" 
    conversion['m'] = "6d" 
    conversion['n'] = "6e" 
    conversion['o'] = "6f" 
    conversion['p'] = "70" 
    conversion['q'] = "71" 
    conversion['r'] = "72" 
    conversion['s'] = "73"
    conversion['t'] = "74"
    conversion['u'] = "75"
    conversion['v'] = "76"
    conversion['w'] = "77"
    conversion['x'] = "78"
    conversion['y'] = "79"
    conversion['z'] = "7a"
    conversion['A'] = "41" 
    conversion['B'] = "42" 
    conversion['C'] = "43" 
    conversion['D'] = "44" 
    conversion['E'] = "45" 
    conversion['F'] = "46" 
    conversion['G'] = "47" 
    conversion['H'] = "48" 
    conversion['I'] = "49" 
    conversion['J'] = "4a" 
    conversion['K'] = "4b" 
    conversion['L'] = "4c" 
    conversion['M'] = "4d" 
    conversion['N'] = "4e" 
    conversion['O'] = "4f" 
    conversion['P'] = "50" 
    conversion['Q'] = "51" 
    conversion['R'] = "52" 
    conversion['S'] = "53"
    conversion['T'] = "54"
    conversion['U'] = "55"
    conversion['V'] = "56"
    conversion['W'] = "57"
    conversion['X'] = "58"
    conversion['Y'] = "59"
    conversion['Z'] = "5a"
    
    # return the hex code for the character
    if single_char in conversion.keys():
        return conversion[single_char]
    else:
        return -1


def main():
    # This function takes input from user

    word_string = input("Enter a string: ")
    for single_element in word_string:
        answer = unicode_conversion(single_element)
        print("")
        print(single_element, answer)



if __name__ == "__main__":
    main()
