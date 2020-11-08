# disassembler-python

Author: Kryštof Kiss

Simple MIPS32 disassembler written in python.

## Prerequisites

Project was developed in Python. We used PyCharm as IDE.

| Library | Version |
| ------ | ------ |
| [Python] | 3.8+ |

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
0x23bdfffc -> addi $sp, $sp, 0x0000fffc
0xafbf0000 -> sw $ra, 0x00000000($sp)
0x20040002 -> addi $a0, $zero, 0x00000002
0xaf848000 -> sw $a0, 0x00008000($gp)
0x20050003 -> addi $a1, $zero, 0x00000003
0xaf858004 -> sw $a1, 0x00008004($gp)
0x0c10000b -> jal 0x0010000b
0xaf828008 -> sw $v0, 0x00008008($gp)
0x8fbf0000 -> lw $ra, 0x00000000($sp)
0x23bd0004 -> addi $sp, $sp, 0x00000004
0x03e00008 -> jr $ra
0x00851020 -> add $v0, $a0, $a1
0x03e00008 -> jr $ra
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

## Implementation

Disassembler translates machine code to language of symbolic instructions.

### Project structure

```
disassembler-python/
│
├── disassembler_python/
│   ├── __init__.py
│   ├── disassembler.py
│   ├── example_input.txt
│   └── mips.json
│
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```

- **disassembler-python/** - project root
- **.gitignore** - gitignore for git
- **main.py** - entry point for starting application
- **README.md** - this file
- **disassembler_python/** - package containing logic of disassembler
- **__init__.py** - package file
- **disassembler.py** - defines Disassembler class with methods
- **example_input.txt** - example text for input
- **mips.json** - mips configuration

### Instruction file

Disassembler uses `mips.json` file to initialize it's configuration.
Initialization includes: MIPS registers, MIPS instructions, templates for parsing instructions.

#### mips.json

Structure of file is following:

```json
{
  "registers": {
    "0": "$zero",
    "1": "$at",
    "2": "$v0"
  },
  "opcodes": [
    0,
    2,
    3
  ],
  "instructions": {
    "0": {
      "0": {
        "type": "R",
        "opcode": 0,
        "func": 0,
        "syntax": "sll $rd, $rt, $shift"
      }
    },
    "2": {
      "type": "J",
      "opcode": "0x02",
      "syntax": "j $offset"
    }
  },
  "opcode": "0b11111100000000000000000000000000",
  "r_type_format": {
    "rs": "0b00000011111000000000000000000000",
    "rt": "0b00000000000111110000000000000000",
    "rd": "0b00000000000000001111100000000000",
    "shift": "0b00000000000000000000011111000000",
    "func": "0b00000000000000000000000000111111"
  },
  "j_type_format": {
    "offset": "0b00000011111111111111111111111111"
  },
  "i_type_format": {
    "rs": "0b00000011111000000000000000000000",
    "rt": "0b00000000000111110000000000000000",
    "imm": "0b00000000000000001111111111111111"
  }
}
```

- **registers:** registers array
- **instructions:** instructions array, each instruction has it's type, opcode, syntax and optionally function code
- **opcode/(r/j/i_type_format):** templates for parsing different part of instruction

[Python]: <https://www.python.org/>