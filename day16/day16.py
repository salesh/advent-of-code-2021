
from functools import reduce
import operator

digit_to_binary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def convertHexInputToBinary():
    with open('input.txt') as f:
        return ''.join([digit_to_binary[digit] for digit in f.read().strip()])


class Parser():
    def __init__(self, bits):
        self.bits = bits
        self.counter = 0
        self.sum_of_packet_versions = 0

    def read(self, n):
        ch = 0
        for _ in range(n):
            ch <<= 1
            if self.counter < len(self.bits):
                if self.bits[self.counter] == '1':
                    ch |= 1
                self.counter += 1
        return ch

    def parse(self):
        packet_version = self.read(3)
        type_id = self.read(3)

        self.sum_of_packet_versions += packet_version

        operator_ref = None
        if type_id == 4:
            return self.parse_literal()
        # Part 2
        else:
            if type_id == 0:
                operator_ref = sum
            elif type_id == 1:
                def operator_ref(value): return reduce(operator.mul, value, 1)
            elif type_id == 2:
                operator_ref = min
            elif type_id == 3:
                operator_ref = max
            elif type_id == 5:
                def operator_ref(value): return 1 if value[0] > value[1] else 0
            elif type_id == 6:
                def operator_ref(value): return 1 if value[0] < value[1] else 0
            elif type_id == 7:
                def operator_ref(
                    value): return 1 if value[0] == value[1] else 0

            return self.parse_operator(operator_ref)

    def parse_literal(self):
        value = 0
        while True:
            one = self.read(1)
            two = self.read(4)
            value = (value << 4) | two
            if one == 0:
                return value

    def parse_operator(self, operator_ref):
        if self.read(1) == 0:
            return self.parse_subpackets(operator_ref, total_length=self.read(15))
        else:
            return self.parse_subpackets(operator_ref, num_packets=self.read(11))

    def parse_subpackets(self, operator_ref, total_length=None, num_packets=None):
        if total_length is not None:
            one = self.counter + total_length
            value = []
            while self.counter < one:
                value.append(self.parse())

        elif num_packets is not None:
            value = [self.parse() for _ in range(num_packets)]

        return operator_ref(value)


if __name__ == '__main__':

    binary_data = convertHexInputToBinary()

    parser = Parser(binary_data)
    parsed = parser.parse()

    print(f'Part1: {parser.sum_of_packet_versions}')
    print(f'Part2: {parsed}')
