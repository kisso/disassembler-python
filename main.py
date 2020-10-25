import argparse

from disassembler_python.disassembler import Disassembler


def main():
    parser = argparse.ArgumentParser(description='Simple MIPS32 disassembler written in python.')
    required_group = parser.add_mutually_exclusive_group(required=True)
    required_group.add_argument('-f', '--file', nargs=1, help='specify a file to decode')
    required_group.add_argument('-e', '--example', action='store_true', help='use this option to use example program')
    args = parser.parse_args()

    if args.example:
        path_to_input = 'disassembler_python/example_input.txt'
    else:
        path_to_input = args.file[0]

    mips_configuration_path = 'disassembler_python/mips.json'
    disassembler = Disassembler.initialize(path_to_input, mips_configuration_path)
    disassembler.disassemble()


if __name__ == '__main__':
    main()
