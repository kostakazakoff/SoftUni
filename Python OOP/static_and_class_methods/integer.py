class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) is not float:
            return "value is not a float"
        else:
            value = int(float_value)
            return cls(value)

    @classmethod
    def from_roman(cls, value: str):
        integer = 0
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_num = list(value)

        if len(roman_num) < 2:
            return cls(romans[roman_num[0]])
            
        for i in range(len(roman_num)-1):
            current_num = romans[roman_num[i].upper()]
            next_num = romans[roman_num[i+1].upper()]
            if current_num < next_num: integer -= current_num
            else: integer += current_num
        else: integer += next_num

        return cls(integer)

    @classmethod
    def from_string(cls, value: str):
        try:
            if type(value) is not str:
                raise ValueError
            return cls(int(value))
        except ValueError:
            return "wrong type"