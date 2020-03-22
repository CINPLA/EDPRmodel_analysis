import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
from EDPRmodel.EDPRmodel import *
from functions.print_initial_values import *
from scipy.integrate import solve_ivp
import pkg_resources

def solve_EDPRmodel_sensitivity_analysis(g_Na_leak, g_K_leak, g_Cl_leak, rho, U_kcc2, U_nkcc1):
    """
    Solves the EDPR model using the solve_ivp function from scipy.

    Arguments:
        g_Na_leak (float): Na leak conductance [S/m**2]
        g_K_leak (float): K leak conductance [S/m**2]
        g_Cl_leak (float): Cl leak conductance [S/m**2]
        rho (float): 3Na/2K pump strength [mol/(m**2 s)]
        U_kcc2 (float): K/Cl cotransporter strength [mol/(m**2 s)]
        U_nkcc1 (float): Na/K/2Cl cotransporter strength [mol/(m**2 s)]

    Returns:
        sol: solution from solve_ivp
    """

    T = 309.14
    alpha = 2.0
    
    filename = pkg_resources.resource_filename('data', 'initial_values/initial_values.npz')
    data = np.load(filename)

    phi_sm = data['phi_sm']
    phi_dm = data['phi_dm']

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
    
    res_si = phi_sm*3e-2*616e-12/(1437e-18*9.648e4)
    res_se = phi_sm*3e-2*616e-12/(718.5e-18*9.648e4)
    res_di = phi_dm*3e-2*616e-12/(1437e-18*9.648e4)
    res_de = phi_dm*3e-2*616e-12/(718.5e-18*9.648e4)
   
    X_si0 = Na_si0 + K_si0 - Cl_si0 + 2*Ca_si0 - res_si
    X_se0 = Na_se0 + K_se0 - Cl_se0 + 2*Ca_se0 + res_se
    X_di0 = Na_di0 + K_di0 - Cl_di0 + 2*Ca_di0 - res_di
    X_de0 = Na_de0 + K_de0 - Cl_de0 + 2*Ca_de0 + res_de
    
    n0 = data['n']
    h0 = data['h']
    s0 = data['s']
    c0 = data['c']
    q0 = data['q']
    z0 = data['z']

    #init_cell = EDPRmodel(T, Na_si0, Na_se0, Na_di0, Na_de0, K_si0, K_se0, K_di0, K_de0, Cl_si0, Cl_se0, Cl_di0, Cl_de0, Ca_si0, Ca_se0, Ca_di0, Ca_de0, X_si0, X_se0, X_di0, X_de0, alpha, 0.01, 0.01, n0, h0, s0, c0, q0, z0)
    #print_initial_values(init_cell)
    
    def dkdt(t,k):

        Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, X_si, X_se, X_di, X_de, n, h, s, c, q, z = k

        my_cell = EDPRmodel(T, Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, X_si, X_se, X_di, X_de, alpha, 0.01, 0.01, n, h, s, c, q, z)

        if t>10:
            my_cell.g_Na_leak = g_Na_leak
            my_cell.g_K_leak = g_K_leak
            my_cell.g_Cl_leak = g_Cl_leak
            my_cell.rho = rho
            my_cell.U_kcc2 = U_kcc2
            my_cell.U_nkcc1 = U_nkcc1

        dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, dCldt_si, dCldt_se, dCldt_di, dCldt_de, \
            dCadt_si, dCadt_se, dCadt_di, dCadt_de, dXdt_si, dXdt_se, dXdt_di, dXdt_de = my_cell.dkdt()
        dndt, dhdt, dsdt, dcdt, dqdt, dzdt = my_cell.dmdt()

        return dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, \
            dCldt_si, dCldt_se, dCldt_di, dCldt_de, dCadt_si, dCadt_se, dCadt_di, dCadt_de, \
            dXdt_si, dXdt_se, dXdt_di, dXdt_de, dndt, dhdt, dsdt, dcdt, dqdt, dzdt

    # solve 
    t_span = (0, 180)

    k0 = [Na_si0, Na_se0, Na_di0, Na_de0, K_si0, K_se0, K_di0, K_de0, Cl_si0, Cl_se0, Cl_di0, Cl_de0, Ca_si0, Ca_se0, Ca_di0, Ca_de0, \
        X_si0, X_se0, X_di0, X_de0, n0, h0, s0, c0, q0, z0]

    sol = solve_ivp(dkdt, t_span, k0, max_step=1e-4)

    return sol
