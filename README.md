# disassembler-python
## MIPS32 disassembler

## Supported instructions:

### R-type instructions:

| Type | Keyword | Meaning | Opcode | Funct |
| :---: | :---: | :--- | :---: | :---: |
| R | `sll` | Logical Shift Left | 0x00 | 0x00 |
| R | `srl` | Logical Shift Right (0-extended) | 0x00 | 0x02 |
| R | `sra` | Arithmetic Shift Right (sign-extended) | 0x00 | 0x03 |
| R | `jr` | Jump to Address in Register | 0x00 | 0x08 |
| R | `mfhi` | Move from HI Register | 0x00 | 0x10 |
| R | `mthi` | Move to HI Register | 0x00 | 0x11 |
| R | `mflo` | Move from LO Register | 0x00 | 0x12 |
| R | `mtlo` | Move to LO Register | 0x00 | 0x13 |
| R | `mult` | Multiply | 0x00 | 0x18 |
| R | `multu` | Unsigned Multiply | 0x00 | 0x19 |
| R | `div` | Divide | 0x00 | 0x1A |
| R | `divu` | Unsigned Divide | 0x00 | 0x1B |
| R | `add` | Add | 0x00 | 0x20 |
| R | `addu` | Add Unsigned | 0x00 | 0x21 |
| R | `sub` | Subtract | 0x00 | 0x22 |
| R | `subu` | Unsigned Subtract | 0x00 | 0x23 |
| R | `and` | Bitwise AND | 0x00 | 0x24 |
| R | `or` | Bitwise OR | 0x00 | 0x25 |
| R | `xor` | Bitwise XOR (Exclusive-OR) | 0x00 | 0x26 |
| R | `nor` | Bitwise NOR (NOT-OR) | 0x00 | 0x27 |
| R | `slt` | Set to 1 if Less Than | 0x00 | 0x2A |
| R | `sltu` | Set to 1 if Less Than Unsigned | 0x00 | 0x2B |

### J-type instructions:

| Type | Keyword | Meaning | Opcode |
| :---: | :---: | :--- | :---: |
| J | `j` | Jump to Address | 0x02 |
| J | `jal` | Jump and Link | 0x03 |

### I-type instructions:

| Type | Keyword | Meaning | Opcode |
| :---: | :---: | :--- | :---: |
| I | `beq` | Branch if Equal | 0x04 |
| I | `bne` | Branch if Not Equal | 0x05 |
| I | `blez` | Branch if Less Than or Equal to Zero | 0x06 |
| I | `bgtz` | Branch on Greater Than Zero | 0x07 |
| I | `addi` | Add Immediate | 0x08 |
| I | `addiu` | Add Unsigned Immediate | 0x09 |
| I | `slti` | Set to 1 if Less Than Immediate | 0x0A |
| I | `sltiu` | Set to 1 if Less Than Unsigned Immediate | 0x0B |
| I | `andi` | Bitwise AND Immediate | 0x0C |
| I | `ori` | Bitwise OR Immediate | 0x0D |
| I | `lui` | Load Upper Immediate | 0x0F |
| I | `lb` | Load Byte | 0x20 |
| I | `lw` | Load Word | 0x23 |
| I | `lbu` | Load Byte Unsigned | 0x24 |
| I | `lhu` | Load Halfword Unsigned | 0x25 |
| I | `sb` | Store Byte | 0x28 |
| I | `sh` | Store Halfword | 0x29 |
| I | `sw` | Store Word | 0x2B |