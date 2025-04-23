import re

def parse_line(line):
    # Remove comments and strip whitespace
    line = line.split(';')[0].strip()
    if not line:
        return None, None, None

    # Match label if present
    label_pattern = r"^[A-Za-z][A-Za-z0-9_]*:"
    label_match = re.match(label_pattern, line)
    label = label_match.group(0)[:-1] if label_match else None

    # Remove label from line if it exists
    if label:
        line = line[len(label) + 1:].strip()

    # Split remaining into opcode and operands
    parts = line.split(maxsplit=1)
    opcode = parts[0] if parts else None
    operand = parts[1] if len(parts) > 1 else None

    return label, opcode, operand

def pass_1(assembly_code):
    symbol_table = {}
    location_counter = 0
    address_table = []
    instructions = []

    for line in assembly_code:
        label, opcode, operand = parse_line(line)

        if label:
            if label in symbol_table:
                print(f"Error: Label '{label}' already defined.")
                return None, None, None
            symbol_table[label] = location_counter

        if opcode:
            instructions.append((opcode, operand))
            address_table.append(location_counter)
            location_counter += 1

    return symbol_table, address_table, instructions

# Sample assembly code
assembly_code = [
    "START: LOAD 100",
    "MOV R1, R2",
    "ADD R1, 50",
    "HALT",
    "LOOP: JMP START"
]

symbol_table, address_table, instructions = pass_1(assembly_code)

# Print results
print("Symbol Table:")
print(symbol_table)

print("\nAddress Table:")
print(address_table)

print("\nInstructions (without labels):")
print(instructions)
