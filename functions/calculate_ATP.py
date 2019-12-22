from scipy.constants import N_A
from scipy import integrate

def calculate_ATP(my_cell, t):

    j_pump_s = my_cell.j_pump(my_cell.Na_si, my_cell.K_se)
    j_pump_d = my_cell.j_pump(my_cell.Na_di, my_cell.K_de)

    ATP_per_sec = (j_pump_s * my_cell.A_s + j_pump_d * my_cell.A_d) * N_A
    ATP = integrate.cumtrapz(ATP_per_sec, t, initial=0)

    return ATP
