import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
from EDPRmodel.EDPRmodel import *
from EDPRmodel.somatic_injection_current import *
from scipy.integrate import solve_ivp
from functions.print_initial_values import *
import pkg_resources

def solve_EDPRmodel(t_dur, alpha, I_stim, stim_start, stim_end):
    """
    Solves the EDPR model using the solve_ivp function from scipy.

    Arguments:
        t_dur (float): duration of simulation [s]
        alpha (float): coupling strength
        I_stim (float): stimulus current [s]
        stim_start (float): time of stimulus onset [s]
        stim_end (float): time of stimulus offset [s]

    Returns:
        sol: solution from solve_ivp
    """

    T = 309.14
    
    filename = pkg_resources.resource_filename('data', 'initial_values/initial_values.npz')
    data = np.load(filename)

    Na_si0 = data['Na_si']
    Na_se0 = data['Na_se']
    K_si0 = data['K_si']
    K_se0 = data['K_se']
    Cl_si0 = data['Cl_si']
    Cl_se0 = data['Cl_se']
    Ca_si0 = data['Ca_si']
    Ca_se0 = data['Ca_se']

    Na_di0 = data['Na_di']
    Na_de0 = data['Na_de']
    K_di0 = data['K_di'] 
    K_de0 = data['K_de']
    Cl_di0 = data['Cl_di']
    Cl_de0 = data['Cl_de']
    Ca_di0 = data['Ca_di']
    Ca_de0 = data['Ca_de']

    X_si0 = data['X_si']
    X_se0 = data['X_se']
    X_di0 = data['X_di']
    X_de0 = data['X_de']

    n0 = data['n']
    h0 = data['h']
    s0 = data['s']
    c0 = data['c']
    q0 = data['q']
    z0 = data['z']
    
    init_cell = EDPRmodel(T, Na_si0, Na_se0, Na_di0, Na_de0, K_si0, K_se0, K_di0, K_de0, Cl_si0, Cl_se0, Cl_di0, Cl_de0, Ca_si0, Ca_se0, Ca_di0, Ca_de0, X_si0, X_se0, X_di0, X_de0, alpha, 0.01, 0.01, n0, h0, s0, c0, q0, z0)
    #print_initial_values(init_cell)

    def dkdt(t,k):

        Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, X_si, X_se, X_di, X_de, n, h, s, c, q, z = k

        my_cell = EDPRmodel(T, Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, X_si, X_se, X_di, X_de, alpha, 0.01, 0.01, n, h, s, c, q, z)

        dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, dCldt_si, dCldt_se, dCldt_di, dCldt_de, \
            dCadt_si, dCadt_se, dCadt_di, dCadt_de, dXdt_si, dXdt_se, dXdt_di, dXdt_de = my_cell.dkdt()
        dndt, dhdt, dsdt, dcdt, dqdt, dzdt = my_cell.dmdt()

        if t > stim_start and t < stim_end:
            dKdt_si, dKdt_se = somatic_injection_current(my_cell, dKdt_si, dKdt_se, 1.0, I_stim)

        return dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, \
            dCldt_si, dCldt_se, dCldt_di, dCldt_de, dCadt_si, dCadt_se, dCadt_di, dCadt_de, \
            dXdt_si, dXdt_se, dXdt_di, dXdt_de, dndt, dhdt, dsdt, dcdt, dqdt, dzdt

    # solve 
    t_span = (0, t_dur)

    k0 = [Na_si0, Na_se0, Na_di0, Na_de0, K_si0, K_se0, K_di0, K_de0, Cl_si0, Cl_se0, Cl_di0, Cl_de0, Ca_si0, Ca_se0, Ca_di0, Ca_de0, \
        X_si0, X_se0, X_di0, X_de0, n0, h0, s0, c0, q0, z0]

    sol = solve_ivp(dkdt, t_span, k0, max_step=1e-4)

    return sol
