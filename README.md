# disassembler-python

Author: Kryštof Kiss

Simple MIPS32 disassembler written in python.

## Prerequisites

Project was developed in Python. We used PyCharm as IDE.

| Library | Version |
| ------ | ------ |
| [Python] | 3.7+ |

## Getting started

To run the application use one of the following commands:
```
python main.py -h, --help            show this help message and exit
python main.py -f FILE, --file FILE  specify a file to decode
python main.py -e, --example         use this option to use example program
```

## Example

**Example input**

```text
0x23bdfffc
0xafbf0000
0x20040002
0xaf848000
0x20050003
0xaf858004
0x0c10000b
0xaf828008
0x8fbf0000
0x23bd0004
0x03e00008
0x00851020
0x03e00008
```

**Example output**

```text
addi $sp, $sp, 0x0000fffc
sw $ra, 0x00000000($sp)
addi $a0, $zero, 0x00000002
sw $a0, 0x00008000($gp)
addi $a1, $zero, 0x00000003
sw $a1, 0x00008004($gp)
jal 0x0010000b
sw $v0, 0x00008008($gp)
lw $ra, 0x00000000($sp)
addi $sp, $sp, 0x00000004
jr $ra
add $v0, $a0, $a1
jr $ra
```

## Supported instructions:

### R-type instructions:

| Type | Keyword | Purpose | Opcode (int) | Func (int) |
| :---: | :---: | :--- | :---: | :---: |
| R | `sll` | Shift Word Left Logical | 0x00 (0) | 0x00 (0) |
| R | `srl` | Shift Word Right Logical | 0x00 (0) | 0x02 (2) |
| R | `sra` | Shift Word Right Arithmetic | 0x00 (0) | 0x03 (3) |
| R | `sllv` | Shift Word Left Logical Variable | 0x00 (0) | 0x04 (4) |
| R | `srlv` | Shift Word Right Logical Variable | 0x00 (0) | 0x07 (6) |
| R | `srav` | Shift Word Right Arithmetic Variable | 0x00 (0) | 0x07 (7) |
| R | `jr` | Jump Register | 0x00 (0) | 0x08 (8) |
| R | `jalr` | Jump and Link Register | 0x00 (0) | 0x09 (9) |
| R | `syscall` | System Call | 0x00 (0) | 0x0C (12) |
| R | `mfhi` | Move From HI Register | 0x00 (0) | 0x10 (16) |
| R | `mthi` | Move to HI Register | 0x00 (0) | 0x11 (17) |
| R | `mflo` | Move From LO Register | 0x00 (0) | 0x12 (18) |
| R | `mtlo` | Move to LO Register | 0x00 (0) | 0x13 (19) |
| R | `mult` | Multiply Word | 0x00 (0) | 0x18 (24) |
| R | `multu` | Multiply Unsigned Word | 0x00 (0) | 0x19 (25) |
| R | `div` | Divide Word | 0x00 (0) | 0x1A (26) |
| R | `divu` | Divide Unsigned Word | 0x00 (0) | 0x1B (27) |
| R | `add` | Add Word | 0x00 (0) | 0x20 (32) |
| R | `addu` | Add Unsigned Word | 0x00 (0) | 0x21 (33) |
| R | `sub` | Subtract Word | 0x00 (0) | 0x22 (34) |
| R | `subu` | Subtract Unsigned Word | 0x00 (0) | 0x23 (35) |
| R | `and` | Bitwise AND | 0x00 (0) | 0x24 (36) |
| R | `or` | Bitwise OR | 0x00 (0) | 0x25 (37) |
| R | `xor` | Bitwise XOR | 0x00 (0) | 0x26 (38) |
| R | `nor` | Bitwise NOR | 0x00 (0) | 0x27 (39) |
| R | `slt` | Set on Less Than | 0x00 (0) | 0x2A (42) |
| R | `sltu` | Set on Less Than Unsigned | 0x00 (0) | 0x2B (43) |

### J-type instructions:

| Type | Keyword | Purpose | Opcode (int) |
| :---: | :---: | :--- | :---: |
| J | `j` | Jump | 0x02 (2) |
| J | `jal` | Jump and Link | 0x03 (3) |

### I-type instructions:

| Type | Keyword | Purpose | Opcode (int) |
| :---: | :---: | :--- | :---: |
| I | `beq` | Branch on Equal | 0x04 (4) |
| I | `bne` | Branch on Not Equal | 0x05 (5) |
| I | `blez` | Branch on Less Than or Equal to Zero | 0x06 (6) |
| I | `bgtz` | Branch on Greater Than Zero | 0x07 (7) |
| I | `addi` | Add Immediate Word | 0x08 (8) |
| I | `addiu` | Add Immediate Unsigned Word | 0x09 (9) |
| I | `slti` | Set on Less Than Immediate | 0x0A (10) |
| I | `sltiu` | Set on Less Than Immediate Unsigned | 0x0B (11) |
| I | `andi` | Bitwise AND Immediate | 0x0C (12) |
| I | `ori` | Bitwise OR Immediate | 0x0D (13) |
| I | `xori` | Bitwise XOR Immediate | 0x0E (14) |
| I | `lui` | Load Upper Immediate | 0x0F (15) |
| I | `lb` | Load Byte | 0x20 (32) |
| I | `lh` | Load Halfword | 0x21 (33) |
| I | `lw` | Load Word | 0x23 (35) |
| I | `lbu` | Load Byte Unsigned | 0x24 (36) |
| I | `lhu` | Load Halfword Unsigned | 0x25 (37) |
| I | `sb` | Store Byte | 0x28 (40) |
| I | `sh` | Store Halfword | 0x29 (41) |
| I | `sw` | Store Word | 0x2B (43) |

[Python]: <https://www.python.org/>