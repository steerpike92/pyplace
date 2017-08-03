import numpy as np


def s_to_bytearray(s):
    '''
    >>> s_to_bytearray('a5')
    [97, 53]
    '''
    return list(bytearray(s))


def byte_to_bits(num):
    '''
    >>> n = 5
    >>> byte_to_bits(n)
    [0, 0, 0, 0, 0, 1, 0, 1]
    '''
    bit_list=[]
    for power in range(7,-1,-1):
        if num>=2**power:
            bit_list.append(1)
            num-=2**power
        else:
            bit_list.append(0)
    return bit_list

def bytearray_to_bit_pattern(b_array):
    '''
    >>> bytearray_to_bit_pattern([5,1])
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    '''
    bit_list=[]
    for num in b_array:
        bit_list+=byte_to_bits(num)
    return bit_list


def six_bit_int(bits):
    '''
    >>> six_bit_int([1,0,0,0,0,1])
    33
    '''
    i = 0
    power = 5
    for bit in bits:
        i += bit * 2**power
        power -= 1
    return i


enc64 = {
    0:	'A',	16:	'Q',	32:	'g',	48:	'w',
    1:	'B',	17:	'R',	33:	'h',	49:	'x',
    2:	'C',	18:	'S',	34:	'i',	50:	'y',
    3:	'D',	19:	'T',	35:	'j',	51:	'z',
    4:	'E',	20:	'U',	36:	'k',	52:	'0',
    5:	'F',	21:	'V',	37:	'l',	53:	'1',
    6:	'G',	22:	'W',	38:	'm',	54:	'2',
    7:	'H',	23:	'X',	39:	'n',	55:	'3',
    8:	'I',	24:	'Y',	40:	'o',	56:	'4',
    9:	'J',	25:	'Z',	41:	'p',	57:	'5',
    10:	'K',	26:	'a',	42:	'q',	58:	'6',
    11:	'L',	27:	'b',	43:	'r',	59:	'7',
    12:	'M',	28:	'c',	44:	's',	60:	'8',
    13:	'N',	29:	'd',	45:	't',	61:	'9',
    14:	'O',	30:	'e',	46:	'u',	62:	'+',
    15:	'P',	31:	'f',	47:	'v',	63:	'/'
    }

dec64 = {v: k for k, v in enc64.iteritems()}

def to_base_64(string):
    '''
    >>> s = "this is a string!!"
    >>> e = "dGhpcyBpcyBhIHN0cmluZyEh"
    >>> to_base_64(s)
    'dGhpcyBpcyBhIHN0cmluZyEh'
    '''
    byte_array=s_to_bytearray(string)

    bit_array=bytearray_to_bit_pattern(byte_array)

    #padding
    byte_count=len(byte_array)
    over_chars=byte_count % 3
    if over_chars==1:
        pad_chars=2
    elif over_chars==2:
        pad_chars=1
    else:
        pad_chars=0
    bit_array += [0, 0] * pad_chars

    #reshaping
    bit_array = np.array(bit_array)
    six_bit_arrays=bit_array.reshape(bit_array.size/6,6)
    six_bit_lists = [list(arr) for arr in six_bit_arrays]
    int6s=[six_bit_int(bits) for bits in six_bit_lists]
    out_str=''.join([enc64[int6] for int6 in int6s])
    out_str+='='*pad_chars
    return out_str


def from_base_64(string):
    '''
    >>> s = "this is a string!!"
    >>> e = "dGhpcyBpcyBhIHN0cmluZyEh"
    >>> from_base_64(e)
    'this is a string!!'
    '''
    pass


if __name__ == "__main__":
    s = "this is a string!!!!!"
    print to_base_64(s)
