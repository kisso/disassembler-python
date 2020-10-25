# disassembler-python
## MIPS32 disassembler

## Supported instructions:

### R-type instructions:

| Type | Keyword | Meaning | Opcode (int) | Func (int) |
| :---: | :---: | :--- | :---: | :---: |
| R | `sll` | Logical Shift Left | 0x00 (0) | 0x00 (0) |
| R | `srl` | Logical Shift Right (0-extended) | 0x00 (0) | 0x02 (2) |
| R | `sra` | Arithmetic Shift Right (sign-extended) | 0x00 (0) | 0x03 (3) |
| R | `jr` | Jump to Address in Register | 0x00 (0) | 0x08 (8) |
| R | `syscall` | System Call | 0x00 (0) | 0x0C (12) |
| R | `mfhi` | Move from HI Register | 0x00 (0) | 0x10 (16) |
| R | `mthi` | Move to HI Register | 0x00 (0) | 0x11 (17) |
| R | `mflo` | Move from LO Register | 0x00 (0) | 0x12 (18) |
| R | `mtlo` | Move to LO Register | 0x00 (0) | 0x13 (19) |
| R | `mult` | Multiply | 0x00 (0) | 0x18 (24) |
| R | `multu` | Unsigned Multiply | 0x00 (0) | 0x19 (25) |
| R | `div` | Divide | 0x00 (0) | 0x1A (26) |
| R | `divu` | Unsigned Divide | 0x00 (0) | 0x1B (27) |
| R | `add` | Add | 0x00 (0) | 0x20 (32) |
| R | `addu` | Add Unsigned | 0x00 (0) | 0x21 (33) |
| R | `sub` | Subtract | 0x00 (0) | 0x22 (34) |
| R | `subu` | Unsigned Subtract | 0x00 (0) | 0x23 (35) |
| R | `and` | Bitwise AND | 0x00 (0) | 0x24 (36) |
| R | `or` | Bitwise OR | 0x00 (0) | 0x25 (37) |
| R | `xor` | Bitwise XOR (Exclusive-OR) | 0x00 (0) | 0x26 (38) |
| R | `nor` | Bitwise NOR (NOT-OR) | 0x00 (0) | 0x27 (39) |
| R | `slt` | Set to 1 if Less Than | 0x00 (0) | 0x2A (42) |
| R | `sltu` | Set to 1 if Less Than Unsigned | 0x00 (0) | 0x2B (43) |

### J-type instructions:

| Type | Keyword | Meaning | Opcode (int) |
| :---: | :---: | :--- | :---: |
| J | `j` | Jump to Address | 0x02 (2) |
| J | `jal` | Jump and Link | 0x03 (3) |

### I-type instructions:

| Type | Keyword | Meaning | Opcode (int) |
| :---: | :---: | :--- | :---: |
| I | `beq` | Branch if Equal | 0x04 (4) |
| I | `bne` | Branch if Not Equal | 0x05 (5) |
| I | `blez` | Branch if Less Than or Equal to Zero | 0x06 (6) |
| I | `bgtz` | Branch on Greater Than Zero | 0x07 (7) |
| I | `addi` | Add Immediate | 0x08 (8) |
| I | `addiu` | Add Unsigned Immediate | 0x09 (9) |
| I | `slti` | Set to 1 if Less Than Immediate | 0x0A (10) |
| I | `sltiu` | Set to 1 if Less Than Unsigned Immediate | 0x0B (11) |
| I | `andi` | Bitwise AND Immediate | 0x0C (12) |
| I | `ori` | Bitwise OR Immediate | 0x0D (13) |
| I | `lui` | Load Upper Immediate | 0x0F (15) |
| I | `lb` | Load Byte | 0x20 (32) |
| I | `lw` | Load Word | 0x23 (35) |
| I | `lbu` | Load Byte Unsigned | 0x24 (36) |
| I | `lhu` | Load Halfword Unsigned | 0x25 (37) |
| I | `sb` | Store Byte | 0x28 (40) |
| I | `sh` | Store Halfword | 0x29 (41) |
| I | `sw` | Store Word | 0x2B (43) |