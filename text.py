def convert_to_roman(arabic_num):
    num_table = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_table = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90:"XC", 50: "L", 40: "XL",10: "X", 9: "IX", 5: "V", 4: "IX", 1: "I"} 
    roman_num = ""
    if arabic_num > 3999:
        return roman_num
    for i in num_table:
        num_digits = arabic_num // i
        arabic_num = arabic_num % i
        print("{},' '{},' ',{}".format(i, num_digits, arabic_num))
        if num_digits == 0:
            continue
        else:
            roman_num = roman_num + (roman_table[i] * num_digits)
            if arabic_num == 0:
                return roman_num

        
print(convert_to_roman(1204))