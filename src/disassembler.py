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

    def decode_instruction(self, instruction: int):
        opcode = (instruction & self._opcode) >> 26
        print(f'{self._addr:#010x}:', end=' ')

        if opcode not in self._opcodes:
            print('Unsupported instruction!')
            return

        # R-type
        if opcode == 0:
            rs = self._registers.get((self._r_type_format.get('rs') & instruction) >> 21)
            rt = self._registers.get((self._r_type_format.get('rt') & instruction) >> 16)
            rd = self._registers.get((self._r_type_format.get('rd') & instruction) >> 11)
            shift = (self._r_type_format.get('shift') & instruction) >> 6
            func = self._r_type_format.get('func') & instruction
            template = self._instructions.get(opcode).get(func)

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
            rs = self._registers.get((self._i_type_format.get('rs') & instruction) >> 21)
            rt = self._registers.get((self._i_type_format.get('rt') & instruction) >> 16)
            imm = self._i_type_format.get('imm') & instruction
            template = self._instructions.get(opcode)

            decoded_instruction = template.get('syntax').replace('$rs', rs)
            decoded_instruction = decoded_instruction.replace('$rt', rt)
            decoded_instruction = decoded_instruction.replace('$imm', f'{imm:#010x}')

        print(decoded_instruction)

    def disassemble(self):
        for instruction in self.instructions_to_decode:
            self.decode_instruction(int(instruction, 16))
            self._addr += 4
