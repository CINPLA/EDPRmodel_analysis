import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
from EDPRmodel.EDPRmodel import *
from scipy.integrate import solve_ivp
from functions.print_initial_values import *
import pkg_resources

def solve_EDPRmodel_without_active_transport(t_dur, alpha):
    """
    Solves the EDPR model using the solve_ivp function from scipy
    when the ATP-dependent mechanisms are turned off.

    Arguments:
        t_dur (float): duration of simulation [s]
        alpha (float): coupling strength

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

    k_res_si0 = data['k_res_si'][-1]
    k_res_se0 = data['k_res_se'][-1]
    k_res_di0 = data['k_res_di'][-1]
    k_res_de0 = data['k_res_de'][-1]

    n0 = data['n']
    h0 = data['h']
    s0 = data['s']
    c0 = data['c']
    q0 = data['q']
    z0 = data['z']
    
    init_cell = EDPRmodel(T, Na_si0, Na_se0, Na_di0, Na_de0, K_si0, K_se0, K_di0, K_de0, Cl_si0, Cl_se0, Cl_di0, Cl_de0, Ca_si0, Ca_se0, Ca_di0, Ca_de0, k_res_si0, k_res_se0, k_res_di0, k_res_de0, alpha, 0.01, 0.01, n0, h0, s0, c0, q0, z0)
    #print_initial_values(init_cell)

    def dkdt(t,k):

        Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, k_res_si, k_res_se, k_res_di, k_res_de, n, h, s, c, q, z = k

        my_cell = EDPRmodel(T, Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, k_res_si, k_res_se, k_res_di, k_res_de, alpha, 0.01, 0.01, n, h, s, c, q, z)
        my_cell.rho = 0.
        my_cell.tau = 0.

        dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, dCldt_si, dCldt_se, dCldt_di, dCldt_de, \
            dCadt_si, dCadt_se, dCadt_di, dCadt_de, dresdt_si, dresdt_se, dresdt_di, dresdt_de = my_cell.dkdt()
        dndt, dhdt, dsdt, dcdt, dqdt, dzdt = my_cell.dmdt()

        return dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, \
            dCldt_si, dCldt_se, dCldt_di, dCldt_de, dCadt_si, dCadt_se, dCadt_di, dCadt_de, \
            dresdt_si, dresdt_se, dresdt_di, dresdt_de, dndt, dhdt, dsdt, dcdt, dqdt, dzdt

    # solve 
    t_span = (0, t_dur)

    k0 = [Na_si0, Na_se0, Na_di0, Na_de0, K_si0, K_se0, K_di0, K_de0, Cl_si0, Cl_se0, Cl_di0, Cl_de0, Ca_si0, Ca_se0, Ca_di0, Ca_de0, \
        k_res_si0, k_res_se0, k_res_di0, k_res_de0, n0, h0, s0, c0, q0, z0]

    sol = solve_ivp(dkdt, t_span, k0, max_step=1e-4)

    return sol
