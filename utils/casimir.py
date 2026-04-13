import numpy as np
from scipy import constants

HBAR = constants.hbar
C = constants.c        # Speed of light (m/s)
PI = np.pi

class CasimirEffect:
    def __init__(self):
        self.prefactor = (PI**2 * HBAR * C) / 240
        
    def force(self, d, area=1e-4):
        return -self.prefactor * area / (d**4)
    
    def pressure(self, d):
        return -(PI**2 * HBAR * C) / (240 * d**4)
    
    def energy(self, d, area=1e-4):
        return -(PI**2 * HBAR * C * area) / (720 * d**3)
    
    def energy_density(self, d):
        return -(PI**2 * HBAR * C) / (720 * d**4)
    
    def naive_sum(self, d, n_max=1000):
        energies = []
        partial_sums = []
        current_sum = 0
        
        for n in range(1, n_max + 1):
            e_n = (n * PI * HBAR * C) / (2 * d)
            energies.append(e_n)
            current_sum += e_n
            partial_sums.append(current_sum)
            
        return np.array(energies), np.array(partial_sums)
    
    def zeta_regularized_energy(self, d):
        zeta_minus_1 = -1/12  # ζ(-1)
        return (PI * HBAR * C / (2 * d)) * zeta_minus_1
    
    def get_force_range(self, d_min=1e-9, d_max=1e-6, num_points=1000):
        distances = np.logspace(np.log10(d_min), np.log10(d_max), num_points)
        forces = self.force(distances)
        return distances, forces
    
    def experimental_comparison(self):
        # Lamoreaux 1997 experiment data
        experiments = {
            'Lamoreaux 1997': {
                'd': 0.6e-6,  # 0.6 microns
                'force_measured': 1.5e-10,  # N
                'force_theoretical': self.force(0.6e-6, area=1e-4)
            },
            'Mohideen 1998': {
                'd': 0.1e-6,  # 0.1 microns
                'force_measured': 6e-7,  # N
                'force_theoretical': self.force(0.1e-6, area=1e-4)
            }
        }
        return experiments