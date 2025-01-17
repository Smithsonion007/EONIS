import numpy as np

PLANCK_CONSTANT = 6.626e-34
REDUCED_PLANCK = PLANCK_CONSTANT / (2 * np.pi)
PHI = (1 + np.sqrt(5)) / 2
PI = np.pi

def eonis_encrypt(message, key):
    ascii_values = [ord(char) for char in message]
    scaled_points = [(value * REDUCED_PLANCK * PHI * key, value * REDUCED_PLANCK * PI * key) for value in ascii_values]
    quantum_shifted_points = [(x + REDUCED_PLANCK / PHI, y + REDUCED_PLANCK / PI) for x, y in scaled_points]
    encrypted_message = "".join(chr(int(abs(x + y) % 94) + 33) for x, y in quantum_shifted_points)
    return encrypted_message, quantum_shifted_points
