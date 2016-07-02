from __future__ import print_function

# font:
# http://www.globalspec.com/reference/39556/203279/appendix-b-huffman-tables-for-the-dc-and-ac-coefficients-of-the-jpeg-baseline-encoder


huffman_cd = {0: '00',

              1: '010',

              2: '011',

              3: '100',

              4: '101',

              5: '110',

              6: '1110',

              7: '11110',

              8: '111110',

              9: '1111110',

              10: '11111110',

              11: '111111110'}

huffman_luminance = {
    '[0, 0]': '1010',

    '[0, 1]': '00',

    '[0, 2]': '01',

    '[0, 3]': '100',

    '[0, 4]': '1011',

    '[0, 5]': '11010',

    '[0, 6]': '1111000',

    '[0, 7]': '11111000',

    '[0, 8]': '1111110110',

    '[0, 9]': '1111111110000010',

    '[0, 10]': '1111111110000011',

    '[1, 1]': '1100',

    '[1, 2]': '11011',

    '[1, 3]': '1111001',

    '[1, 4]': '111110110',

    '[1, 5]': '11111110110',

    '[1, 6]': '1111111110000100',

    '[1, 7]': '1111111110000101',

    '[1, 8]': '1111111110000110',

    '[1, 9]': '1111111110000111',

    '[1, 10]': '1111111110001000',

    '[2, 1]': '11100',

    '[2, 2]': '11111001',

    '[2, 3]': '1111110111',

    '[2, 4]': '111111110100',

    '[2, 5]': '1111111110001001',

    '[2, 6]': '1111111110001010',

    '[2, 7]': '1111111110001011',

    '[2, 8]': '1111111110001100',

    '[2, 9]': '1111111110001101',

    '[2, 10]': '1111111110001110',

    '[3, 1]': '111010',

    '[3, 2]': '111110111',

    '[3, 3]': '111111110101',

    '[3, 4]': '1111111110001111',

    '[3, 5]': '1111111110010000',

    '[3, 6]': '1111111110010001',

    '[3, 7]': '1111111110010010',

    '[3, 8]': '1111111110010011',

    '[3, 9]': '1111111110010100',

    '[3, 10]': '1111111110010101',

    '[4, 1]': '111011',

    '[4, 2]': '1111111000',

    '[4, 3]': '1111111110010110',

    '[4, 4]': '1111111110010111',

    '[4, 5]': '1111111110011000',

    '[4, 6]': '1111111110011001',

    '[4, 7]': '1111111110011010',

    '[4, 8]': '1111111110011011',

    '[4, 9]': '1111111110011100',

    '[4, 10]': '1111111110011101',

    '[5, 1]': '1111010',

    '[5, 2]': '11111110111',

    '[5, 3]': '1111111110011110',

    '[5, 4]': '1111111110011111',

    '[5, 5]': '1111111110100000',

    '[5, 6]': '1111111110100001',

    '[5, 7]': '1111111110100010',

    '[5, 8]': '1111111110100011',

    '[5, 9]': '1111111110100100',

    '[5, 10]': '1111111110100101',

    '[6, 1]': '1111011',

    '[6, 2]': '111111110110',

    '[6, 3]': '1111111110100110',

    '[6, 4]': '1111111110100111',

    '[6, 5]': '1111111110101000',

    '[6, 6]': '1111111110101001',

    '[6, 7]': '1111111110101010',

    '[6, 8]': '1111111110101011',

    '[6, 9]': '1111111110101100',

    '[6, 10]': '1111111110101101',

    '[7, 1]': '11111010',

    '[7, 2]': '111111110111',

    '[7, 3]': '1111111110101110',

    '[7, 4]': '1111111110101111',

    '[7, 5]': '1111111110110000',

    '[7, 6]': '1111111110110001',

    '[7, 7]': '1111111110110010',

    '[7, 8]': '1111111110110011',

    '[7, 9]': '1111111110110100',

    '[7, 10]': '1111111110110101',

    '[8, 1]': '111111000',

    '[8, 2]': '111111111000000',

    '[8, 3]': '1111111110110110',

    '[8, 4]': '1111111110110111',

    '[8, 5]': '1111111110111000',

    '[8, 6]': '1111111110111001',

    '[8, 7]': '1111111110111010',

    '[8, 8]': '1111111110111011',

    '[8, 9]': '1111111110111100',

    '[8, 10]': '1111111110111101',

    '[9, 1]': '111111001',

    '[9, 2]': '1111111110111110',

    '[9, 3]': '1111111110111111',

    '[9, 4]': '1111111111000000',

    '[9, 5]': '1111111111000001',

    '[9, 6]': '1111111111000010',

    '[9, 7]': '1111111111000011',

    '[9, 8]': '1111111111000100',

    '[9, 9]': '1111111111000101',

    '[9, 10]': '1111111111000110',

    '[10, 1]': '111111010', }