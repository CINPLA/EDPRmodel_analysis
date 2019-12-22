import matplotlib.pyplot as plt
import scipy
from scipy.constants import N_A

def calculate_axial_transport(my_cell, t):

    phi_si, phi_se, phi_di, phi_de, phi_sm, phi_dm = my_cell.membrane_potentials()

    j_Na_diff_i = my_cell.j_k_diff(my_cell.D_Na, my_cell.lamda_i, my_cell.Na_si, my_cell.Na_di)*my_cell.A_i*N_A
    Na_akkum_diff_i = scipy.integrate.cumtrapz(j_Na_diff_i, t, initial=0)

    j_Na_drift_i = my_cell.j_k_drift(my_cell.D_Na, my_cell.Z_Na, my_cell.lamda_i, my_cell.Na_si, my_cell.Na_di, phi_si, phi_di)*my_cell.A_i*N_A
    Na_akkum_drift_i = scipy.integrate.cumtrapz(j_Na_drift_i, t, initial=0)

    j_K_diff_i = my_cell.j_k_diff(my_cell.D_K, my_cell.lamda_i, my_cell.K_si, my_cell.K_di)*my_cell.A_i*N_A
    K_akkum_diff_i = scipy.integrate.cumtrapz(j_K_diff_i, t, initial=0)

    j_K_drift_i = my_cell.j_k_drift(my_cell.D_K, my_cell.Z_K, my_cell.lamda_i, my_cell.K_si, my_cell.K_di, phi_si, phi_di)*my_cell.A_i*N_A
    K_akkum_drift_i = scipy.integrate.cumtrapz(j_K_drift_i, t, initial=0)

    j_Cl_diff_i = my_cell.j_k_diff(my_cell.D_Cl, my_cell.lamda_i, my_cell.Cl_si, my_cell.Cl_di)*my_cell.A_i*N_A
    Cl_akkum_diff_i = scipy.integrate.cumtrapz(j_Cl_diff_i, t, initial=0)

    j_Cl_drift_i = my_cell.j_k_drift(my_cell.D_Cl, my_cell.Z_Cl, my_cell.lamda_i, my_cell.Cl_si, my_cell.Cl_di, phi_si, phi_di)*my_cell.A_i*N_A
    Cl_akkum_drift_i = scipy.integrate.cumtrapz(j_Cl_drift_i, t, initial=0)

    j_Ca_diff_i = my_cell.j_k_diff(my_cell.D_Ca, my_cell.lamda_i, my_cell.free_Ca_si, my_cell.free_Ca_di)*my_cell.A_i*N_A
    Ca_akkum_diff_i = scipy.integrate.cumtrapz(j_Ca_diff_i, t, initial=0)

    j_Ca_drift_i = my_cell.j_k_drift(my_cell.D_Ca, my_cell.Z_Ca, my_cell.lamda_i, my_cell.free_Ca_si, my_cell.free_Ca_di, phi_si, phi_di)*my_cell.A_i*N_A
    Ca_akkum_drift_i = scipy.integrate.cumtrapz(j_Ca_drift_i, t, initial=0)

    j_e_diff_i = (j_Na_diff_i + j_K_diff_i + 2*j_Ca_diff_i - j_Cl_diff_i)
    j_e_drift_i = (j_Na_drift_i + j_K_drift_i + 2*j_Ca_drift_i - j_Cl_drift_i)
    e_akkum_diff_i = (Na_akkum_diff_i*my_cell.Z_Na + K_akkum_diff_i*my_cell.Z_K + Cl_akkum_diff_i*my_cell.Z_Cl + Ca_akkum_diff_i*my_cell.Z_Ca)
    e_akkum_drift_i = (Na_akkum_drift_i*my_cell.Z_Na + K_akkum_drift_i*my_cell.Z_K + Cl_akkum_drift_i*my_cell.Z_Cl + Ca_akkum_drift_i*my_cell.Z_Ca)

    j_Na_diff_e = my_cell.j_k_diff(my_cell.D_Na, my_cell.lamda_e, my_cell.Na_se, my_cell.Na_de)*my_cell.A_e*N_A
    Na_akkum_diff_e = scipy.integrate.cumtrapz(j_Na_diff_e, t, initial=0)

    j_Na_drift_e = my_cell.j_k_drift(my_cell.D_Na, my_cell.Z_Na, my_cell.lamda_e, my_cell.Na_se, my_cell.Na_de, phi_se, phi_de)*my_cell.A_e*N_A
    Na_akkum_drift_e = scipy.integrate.cumtrapz(j_Na_drift_e, t, initial=0)

    j_K_diff_e = my_cell.j_k_diff(my_cell.D_K, my_cell.lamda_e, my_cell.K_se, my_cell.K_de)*my_cell.A_e*N_A
    K_akkum_diff_e = scipy.integrate.cumtrapz(j_K_diff_e, t, initial=0)

    j_K_drift_e = my_cell.j_k_drift(my_cell.D_K, my_cell.Z_K, my_cell.lamda_e, my_cell.K_se, my_cell.K_de, phi_se, phi_de)*my_cell.A_e*N_A
    K_akkum_drift_e = scipy.integrate.cumtrapz(j_K_drift_e, t, initial=0)

    j_Cl_diff_e = my_cell.j_k_diff(my_cell.D_Cl, my_cell.lamda_e, my_cell.Cl_se, my_cell.Cl_de)*my_cell.A_e*N_A
    Cl_akkum_diff_e = scipy.integrate.cumtrapz(j_Cl_diff_e, t, initial=0)

    j_Cl_drift_e = my_cell.j_k_drift(my_cell.D_Cl, my_cell.Z_Cl, my_cell.lamda_e, my_cell.Cl_se, my_cell.Cl_de, phi_se, phi_de)*my_cell.A_e*N_A
    Cl_akkum_drift_e = scipy.integrate.cumtrapz(j_Cl_drift_e, t, initial=0)

    j_Ca_diff_e = my_cell.j_k_diff(my_cell.D_Ca, my_cell.lamda_e, my_cell.Ca_se, my_cell.Ca_de)*my_cell.A_e*N_A
    Ca_akkum_diff_e = scipy.integrate.cumtrapz(j_Ca_diff_e, t, initial=0)

    j_Ca_drift_e = my_cell.j_k_drift(my_cell.D_Ca, my_cell.Z_Ca, my_cell.lamda_e, my_cell.Ca_se, my_cell.Ca_de, phi_se, phi_de)*my_cell.A_e*N_A
    Ca_akkum_drift_e = scipy.integrate.cumtrapz(j_Ca_drift_e, t, initial=0)

    j_e_diff_e = (j_Na_diff_e + j_K_diff_e + 2*j_Ca_diff_e - j_Cl_diff_e)
    j_e_drift_e = (j_Na_drift_e + j_K_drift_e + 2*j_Ca_drift_e - j_Cl_drift_e)
    e_akkum_diff_e = (Na_akkum_diff_e*my_cell.Z_Na + K_akkum_diff_e*my_cell.Z_K + Cl_akkum_diff_e*my_cell.Z_Cl + Ca_akkum_diff_e*my_cell.Z_Ca)
    e_akkum_drift_e = (Na_akkum_drift_e*my_cell.Z_Na + K_akkum_drift_e*my_cell.Z_K + Cl_akkum_drift_e*my_cell.Z_Cl + Ca_akkum_drift_e*my_cell.Z_Ca)

    return j_e_drift_i, j_e_diff_i, e_akkum_drift_i, e_akkum_diff_i, Na_akkum_drift_i, Na_akkum_diff_i, K_akkum_drift_i, K_akkum_diff_i, Cl_akkum_drift_i, Cl_akkum_diff_i, Ca_akkum_drift_i, Ca_akkum_diff_i, \
        j_e_drift_e, j_e_diff_e, e_akkum_drift_e, e_akkum_diff_e, Na_akkum_drift_e, Na_akkum_diff_e, K_akkum_drift_e, K_akkum_diff_e, Cl_akkum_drift_e, Cl_akkum_diff_e, Ca_akkum_drift_e, Ca_akkum_diff_e
