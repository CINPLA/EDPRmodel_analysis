import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
from ICPRmodel.ICPRmodel import *
from ICPRmodel.somatic_injection_current import *
from scipy.integrate import solve_ivp
from functions.print_initial_values import *

def solve_ICPRmodel(t_dur, alpha, I_stim, stim_start, stim_end):
    """
    Solves the ICPR model using the solve_ivp function from scipy.

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

    Na_si0 = 18.
    Na_se0 = 140.
    K_si0 = 99.
    K_se0 = 4.3
    Cl_si0 = 7.
    Cl_se0 = 134.
    Ca_si0 = 0.01
    Ca_se0 = 1.1

    Na_di0 = 18.
    Na_de0 = 140.
    K_di0 = 99.
    K_de0 = 4.3
    Cl_di0 = 7.
    Cl_de0 = 134.
    Ca_di0 = 0.01
    Ca_de0 = 1.1

    res_i = -68e-3*3e-2*616e-12/(1437e-18*9.648e4)
    res_e = -68e-3*3e-2*616e-12/(718.5e-18*9.648e4)

    k_res_si0 = Cl_si0 - Na_si0 - K_si0 - 2*Ca_si0 + res_i
    k_res_se0 = Cl_se0 - Na_se0 - K_se0 - 2*Ca_se0 - res_e
    k_res_di0 = Cl_di0 - Na_di0 - K_di0 - 2*Ca_di0 + res_i
    k_res_de0 = Cl_de0 - Na_de0 - K_de0 - 2*Ca_de0 - res_e

    n0 = 0.0003
    h0 = 0.999
    s0 = 0.007
    c0 = 0.006
    q0 = 0.011
    z0 = 1.0

    def calibrate(t,k):

        Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, k_res_si, k_res_se, k_res_di, k_res_de, n, h, s, c, q, z = k

        my_cell = ICPRmodel(T, Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, k_res_si, k_res_se, k_res_di, k_res_de, alpha, Ca_si0, Ca_di0, n, h, s, c, q, z)

        dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, dCldt_si, dCldt_se, dCldt_di, dCldt_de, \
            dCadt_si, dCadt_se, dCadt_di, dCadt_de, dresdt_si, dresdt_se, dresdt_di, dresdt_de = my_cell.dkdt()
        dndt, dhdt, dsdt, dcdt, dqdt, dzdt = my_cell.dmdt()

        return dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, \
            dCldt_si, dCldt_se, dCldt_di, dCldt_de, dCadt_si, dCadt_se, dCadt_di, dCadt_de, \
            dresdt_si, dresdt_se, dresdt_di, dresdt_de, dndt, dhdt, dsdt, dcdt, dqdt, dzdt

    def dkdt(t,k):

        Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, k_res_si, k_res_se, k_res_di, k_res_de, n, h, s, c, q, z = k

        my_cell = ICPRmodel(T, Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, k_res_si, k_res_se, k_res_di, k_res_de, alpha, Ca_si0, Ca_di0, n, h, s, c, q, z)

        dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, dCldt_si, dCldt_se, dCldt_di, dCldt_de, \
            dCadt_si, dCadt_se, dCadt_di, dCadt_de, dresdt_si, dresdt_se, dresdt_di, dresdt_de = my_cell.dkdt()
        dndt, dhdt, dsdt, dcdt, dqdt, dzdt = my_cell.dmdt()

        if t > stim_start and t < stim_end:
            dKdt_si, dKdt_se = somatic_injection_current(my_cell, dKdt_si, dKdt_se, 1.0, I_stim)

        return dNadt_si, dNadt_se, dNadt_di, dNadt_de, dKdt_si, dKdt_se, dKdt_di, dKdt_de, \
            dCldt_si, dCldt_se, dCldt_di, dCldt_de, dCadt_si, dCadt_se, dCadt_di, dCadt_de, \
            dresdt_si, dresdt_se, dresdt_di, dresdt_de, dndt, dhdt, dsdt, dcdt, dqdt, dzdt

    # calibrate 
    t_span = (0, 15)

    k0 = [Na_si0, Na_se0, Na_di0, Na_de0, K_si0, K_se0, K_di0, K_de0, Cl_si0, Cl_se0, Cl_di0, Cl_de0, Ca_si0, Ca_se0, Ca_di0, Ca_de0, \
        k_res_si0, k_res_se0, k_res_di0, k_res_de0, n0, h0, s0, c0, q0, z0]

    sol = solve_ivp(calibrate, t_span, k0, max_step=1e-4)
    Na_si, Na_se, Na_di, Na_de, K_si, K_se, K_di, K_de, Cl_si, Cl_se, Cl_di, Cl_de, Ca_si, Ca_se, Ca_di, Ca_de, \
        k_res_si, k_res_se, k_res_di, k_res_de, n, h, s, c, q, z = sol.y

    # solve
    t_span = (0, t_dur)

    k0 = [Na_si[-1], Na_se[-1], Na_di[-1], Na_de[-1], K_si[-1], K_se[-1], K_di[-1], K_de[-1], Cl_si[-1], Cl_se[-1], Cl_di[-1], Cl_de[-1], Ca_si[-1], Ca_se[-1], Ca_di[-1], Ca_de[-1], \
        k_res_si[-1], k_res_se[-1], k_res_di[-1], k_res_de[-1], n[-1], h[-1], s[-1], c[-1], q[-1], z[-1]]

    sol = solve_ivp(dkdt, t_span, k0, max_step=1e-4)

    init_cell = ICPRmodel(T, Na_si0, Na_se0, Na_di0, Na_de0, K_si0, K_se0, K_di0, K_de0, Cl_si0, Cl_se0, Cl_di0, Cl_de0, Ca_si0, Ca_se0, Ca_di0, Ca_de0, k_res_si0, k_res_se0, k_res_di0, k_res_de0, alpha, Ca_si0, Ca_di0, n0, h0, s0, c0, q0, z0)
    print_initial_values(init_cell)

    return sol
