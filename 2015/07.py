from collections import defaultdict

import parse


class Circuit:
    def __init__(self, instruction_booklet: list[str]):
        self._wires = []
        self.wire_values = defaultdict(int)
        self.instruction_booklet = instruction_booklet
        self.parse_instructions()

    def parse_instructions(self):
        for i in self.instruction_booklet:
            self._init_booklet(i)

        while self._wires:
            for wire_expr in self._wires:
                if len(self.wire_values) > 18:
                    if (
                        "right" in wire_expr
                        and len(wire_expr["right"]) == 1
                        and len(wire_expr["left"]) == 1
                    ):
                        pass
                if (
                    "right" in wire_expr
                    and (wire_expr["left"] in self.wire_values or wire_expr["left"].isdigit())
                    and (wire_expr["right"] in self.wire_values or wire_expr["right"].isdigit())
                ):
                    if wire_expr["op"] == "AND":
                        if wire_expr["left"].isdigit():
                            _left = int(wire_expr["left"])
                        else:
                            _left = self.wire_values[wire_expr["left"]]
                        self.wire_values[wire_expr["to"]] = (
                            _left & self.wire_values[wire_expr["right"]]
                        )
                    if wire_expr["op"] == "OR":
                        if wire_expr["left"].isdigit():
                            _left = int(wire_expr["left"])
                        else:
                            _left = self.wire_values[wire_expr["left"]]
                        self.wire_values[wire_expr["to"]] = (
                            _left | self.wire_values[wire_expr["right"]]
                        )
                    if wire_expr["op"] == "LSHIFT":
                        self.wire_values[wire_expr["to"]] = self.wire_values[
                            wire_expr["left"]
                        ] << int(wire_expr["right"])
                    if wire_expr["op"] == "RSHIFT":
                        self.wire_values[wire_expr["to"]] = self.wire_values[
                            wire_expr["left"]
                        ] >> int(wire_expr["right"])
                    self._wires.remove(wire_expr)
                if wire_expr["op"] == "NOT" and wire_expr["left"] in self.wire_values:
                    self.wire_values[wire_expr["to"]] = self.wire_values[wire_expr["left"]] ^ 65535
                    self._wires.remove(wire_expr)
                if wire_expr["op"] == "ASSIGNMENT" and wire_expr["left"] in self.wire_values:
                    self.wire_values[wire_expr["to"]] = self.wire_values[wire_expr["left"]]
                    self._wires.remove(wire_expr)

    def _init_booklet(self, instruction: str) -> None:
        value_settings = parse.parse("{value:d} -> {to}", instruction)
        if value_settings:
            self.wire_values[value_settings["to"]] = value_settings["value"]
        else:
            wire_settings = parse.parse("{left} -> {to}", instruction)
            from_to_instr = parse.parse("{left} {command} {right} -> {to}", instruction)
            not_instr = parse.parse("NOT {left} -> {to}", instruction)

            if from_to_instr:
                d = {
                    "to": from_to_instr["to"],
                    "op": from_to_instr["command"],
                    "left": from_to_instr["left"],
                    "right": from_to_instr["right"],
                }

            elif not_instr:
                d = {
                    "to": not_instr["to"],
                    "op": "NOT",
                    "left": not_instr["left"],
                }
            else:
                d = {
                    "to": wire_settings["to"],
                    "op": "ASSIGNMENT",
                    "left": wire_settings["left"],
                }
            self._wires.append(d)


def test_circuit():
    circuit = Circuit(
        [
            "x -> aaa",
            "1 OR x -> p",
            "132 AND x -> pa",
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
        ]
    )
    assert circuit.wire_values == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "aaa": 123,
        "y": 456,
        "p": 123,
        "pa": 0,
    }


def main():
    with open("2015/07_input", "r") as f:
        instructions = f.read().splitlines()
        assert len(instructions) == 339
    circuit = Circuit(instructions)
    print("part1:", circuit.wire_values["a"])

    # part 2
    new_instructions = []
    for i in instructions:
        b_instr = parse.parse("{_} -> b", i)
        if b_instr:
            new_b = f'{circuit.wire_values["a"]} -> b'
            new_instructions.append(new_b)
        else:
            new_instructions.append(i)
    new_circuit = Circuit(new_instructions)
    print("part2:", new_circuit.wire_values["a"])


if __name__ == "__main__":
    main()
