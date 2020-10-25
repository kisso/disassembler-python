from src.disassembler import Disassembler
from src.helpers import load_file, load_json


def _main():
    path_to_input = 'src/input.txt'
    mips_configuration = 'src/mips.json'
    configuration = load_json(path=mips_configuration)
    instructions_to_decode = load_file(path=path_to_input)
    disassembler = Disassembler(configuration, instructions_to_decode)
    disassembler.disassemble()


if __name__ == '__main__':
    _main()
