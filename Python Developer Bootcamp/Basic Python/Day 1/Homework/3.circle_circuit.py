def circle_circuit(diameter):
    pi = 3.14
    radius = diameter / 2
    circuit = 2 * pi * radius
    return circuit


circuit_to_count = circle_circuit(6)
print(circuit_to_count)
