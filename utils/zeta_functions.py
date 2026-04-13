import numpy as np
import mpmath as mp

# Set high precision
mp.mp.dps = 50

class RiemannZeta:

    
    def __init__(self):
        # First few non-trivial zeros on critical line
        self.known_zeros = [
            14.13472514173469379045725198356247027078,
            21.022039638771554992628479593896902777,
            25.010857580145688763213790992562821818,
            30.424876125859513210311897530584091320,
            32.935061587739189690662368964074903488,
            37.586178158825671257217763480705332821,
            40.918719012147495187398126914633254395,
            43.327073280914999519496122165406805782,
            48.005150881167159727942472749427516041,
            49.773832477672302181916784678563724057,
            52.970321477714460644147296608880990063,
            56.446247697063394804367759476706127552,
            59.347044002602353079653648674992219031,
            60.831778524609809844259901824245003422,
            65.112544048081606660875054253183705058,
            67.079810529494173714478828896522216770,
            69.546401711173979252926857526554738508,
            72.067157674481907582522101926226159430,
            75.704690699083933168326916762030365466,
            77.144840068874805372682664856304670021,
        ]
        
    def zeta(self, s):

        if isinstance(s, (complex, np.complex128)):
            s_mp = mp.mpc(s.real, s.imag)
        else:
            s_mp = mp.mpc(float(s), 0)
        return complex(mp.zeta(s_mp))
    
    def zeta_critical_line(self, t):

        s = 0.5 + 1j * t
        return self.zeta(s)
    
    def compute_critical_line(self, t_min=0, t_max=100, num_points=1000):

        t_values = np.linspace(t_min, t_max, num_points)
        zeta_values = [self.zeta_critical_line(t) for t in t_values]
        
        return t_values, np.array(zeta_values)
    
    def compute_grid(self, x_min=-2, x_max=2, y_min=-2, y_max=2, resolution=200):
        x = np.linspace(x_min, x_max, resolution)
        y = np.linspace(y_min, y_max, resolution)
        X, Y = np.meshgrid(x, y)
        
        Z = np.zeros((resolution, resolution), dtype=complex)
        magnitude = np.zeros((resolution, resolution))
        phase = np.zeros((resolution, resolution))
        
        for i in range(resolution):
            for j in range(resolution):
                s = complex(X[i, j], Y[i, j])
                try:
                    z = self.zeta(s)
                    Z[i, j] = z
                    magnitude[i, j] = abs(z)
                    phase[i, j] = np.angle(z)
                except:
                    Z[i, j] = np.nan
                    magnitude[i, j] = np.nan
                    phase[i, j] = np.nan
        
        return X, Y, Z, magnitude, phase
    
    def find_zeros_approximate(self, t_max=100, num_points=10000):
        t_values = np.linspace(0, t_max, num_points)
        zeros = []
        
        for i in range(len(t_values) - 1):
            z1 = self.zeta_critical_line(t_values[i])
            z2 = self.zeta_critical_line(t_values[i + 1])
            
            # Check if both real and imaginary parts change sign
            if (z1.real * z2.real < 0) and (z1.imag * z2.imag < 0):
                # Approximate zero location
                t_zero = (t_values[i] + t_values[i + 1]) / 2
                zeros.append(t_zero)
        
        return np.array(zeros)
    
    def prime_connection(self, x_max=100):
        from scipy.special import expi
        
        # Generate primes up to x_max
        def sieve_of_eratosthenes(n):
            primes = []
            sieve = [True] * (n + 1)
            for p in range(2, n + 1):
                if sieve[p]:
                    primes.append(p)
                    for i in range(p * p, n + 1, p):
                        sieve[i] = False
            return primes
        
        x_values = np.arange(2, x_max + 1)
        primes = sieve_of_eratosthenes(x_max)
        
        # Prime counting function π(x)
        pi_x = np.array([sum(1 for p in primes if p <= x) for x in x_values])
        
        # Logarithmic integral approximation (from zeta zeros)
        li_x = np.array([float(mp.li(x)) for x in x_values])
        
        return x_values, pi_x, li_x, primes
    
    def functional_equation_check(self, s):
        from scipy.special import gamma
        
        s = complex(s)
        
        # Left side
        lhs = self.zeta(s)
        
        # Right side
        coeff = (2**s) * (np.pi**(s-1)) * np.sin(np.pi * s / 2) * gamma(1 - s)
        rhs = coeff * self.zeta(1 - s)
        
        return lhs, rhs, abs(lhs - rhs)
    
    def dirichlet_series(self, s, n_terms=1000):
        if isinstance(s, complex):
            s_real = s.real
        else:
            s_real = float(s)
        
        if s_real <= 1:
            return float('inf')  # Diverges
        
        n = np.arange(1, n_terms + 1)
        return np.sum(n**(-s))
    
    def analytic_continuation_demo(self, s):
        if isinstance(s, complex):
            s_real = s.real
        else:
            s_real = float(s)
            s = complex(s, 0)
        
        if s_real > 1:
            # Direct computation works
            return self.zeta(s), "Direct sum"
        elif s_real > 0:
            # Use eta function relation
            eta = self._eta_function(s)
            zeta_from_eta = eta / (1 - 2**(1-s))
            return zeta_from_eta, "Eta function analytic continuation"
        else:
            # Use functional equation
            return self.zeta(s), "Functional equation"
    
    def _eta_function(self, s, n_terms=10000):
        n = np.arange(1, n_terms + 1)
        terms = ((-1)**(n-1)) / (n**s)
        return np.sum(terms)