from scipy.constants import N_A
from scipy import integrate

def calculate_ATP(my_cell, t):
    """
    Calculates the accumulative number of ATP molecules
    consumed by the 3Na/2K pumps and Ca/2Na exchangers.
    """

    j_pump_s = my_cell.j_pump(my_cell.Na_si, my_cell.K_se)
    j_pump_d = my_cell.j_pump(my_cell.Na_di, my_cell.K_de)

    ATP_pump_per_sec = (j_pump_s * my_cell.A_s + j_pump_d * my_cell.A_d) * N_A
    ATP_pump = integrate.cumtrapz(ATP_pump_per_sec, t, initial=0)

    j_Ca_dec_s = my_cell.tau * (my_cell.Ca_si - my_cell.Ca0_si)*my_cell.V_si/my_cell.A_s
    j_Ca_dec_d = my_cell.tau * (my_cell.Ca_di - my_cell.Ca0_di)*my_cell.V_di/my_cell.A_d
    
    ATP_Ca_per_sec = (j_Ca_dec_s * my_cell.A_s + j_Ca_dec_d * my_cell.A_d) * N_A
    ATP_Ca = integrate.cumtrapz(ATP_Ca_per_sec, t, initial=0)

    return ATP_pump, ATP_Ca
