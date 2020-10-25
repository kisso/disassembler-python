import json
from sys import exit


class Disassembler:

    def __init__(self, configuration, instructions_to_decode):
        self._addr = 4194304
        self._opcodes = configuration.get('opcodes')
        self._instructions = configuration.get('instructions')
        self._registers = configuration.get('registers')
        self._opcode = configuration.get('opcode')
        self._r_type_format = configuration.get('r_type_format')
        self._j_type_format = configuration.get('j_type_format')
        self._i_type_format = configuration.get('i_type_format')
        self.instructions_to_decode = instructions_to_decode

    @staticmethod
    def _mips_decoder(x):
        if isinstance(x, dict):
            new_dict = {}
            for k, v in x.items():
                try:
                    new_dict[int(k)] = v
                except ValueError:
                    new_dict[k] = v

                    if isinstance(v, str) and v.startswith('0b'):
                        new_dict[k] = int(v, 2)

            return new_dict

        return x

    @classmethod
    def initialize(cls, path_to_input: str, path_to_configuration: str):
        try:
            with open(file=path_to_input) as f:
                input_data = f.read().splitlines()
        except FileNotFoundError:
            print(f'Can not load a file: {path_to_input}')
            print('Try a different file!')
            exit()

        with open(file=path_to_configuration) as json_file:
            configuration = json.load(json_file, object_hook=cls._mips_decoder)

        return cls(configuration, input_data)

    def decode_instruction(self, instruction: int):
        opcode = (instruction & self._opcode) >> 26
        print(f'{self._addr:#010x}:', end=' ')

        if opcode not in self._opcodes:
            print('Unsupported instruction!')
            return

        # R-type
        if opcode == 0:
            try:
                rs = self._registers[(self._r_type_format.get('rs') & instruction) >> 21]
                rt = self._registers[(self._r_type_format.get('rt') & instruction) >> 16]
                rd = self._registers[(self._r_type_format.get('rd') & instruction) >> 11]
                shift = (self._r_type_format.get('shift') & instruction) >> 6
                func = self._r_type_format.get('func') & instruction
                template = self._instructions[opcode][func]
            except KeyError:
                print('Unsupported instruction!')
                return

            decoded_instruction = template.get('syntax').replace('$rs', rs)
            decoded_instruction = decoded_instruction.replace('$rt', rt)
            decoded_instruction = decoded_instruction.replace('$rd', rd)
            decoded_instruction = decoded_instruction.replace('$shift', f'{shift:#010x}')
        # J-type
        elif opcode in [2, 3]:
            offset = self._j_type_format.get('offset') & instruction
            template = self._instructions.get(opcode)
            decoded_instruction = template.get('syntax').replace('$offset', f'{offset:#010x}')
        # I-type
        else:
            try:
                rs = self._registers[(self._i_type_format.get('rs') & instruction) >> 21]
                rt = self._registers[(self._i_type_format.get('rt') & instruction) >> 16]
                imm = self._i_type_format.get('imm') & instruction
                template = self._instructions.get(opcode)
            except KeyError:
                print('Unsupported instruction!')
                return

            decoded_instruction = template.get('syntax').replace('$rs', rs)
            decoded_instruction = decoded_instruction.replace('$rt', rt)
            decoded_instruction = decoded_instruction.replace('$imm', f'{imm:#010x}')

        print(decoded_instruction)

    def disassemble(self):
        for instruction in self.instructions_to_decode:
            self.decode_instruction(int(instruction, 16))
            self._addr += 4
