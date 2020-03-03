
def print_final_values(my_cell):
    q_si = my_cell.total_charge([my_cell.Na_si[-1], my_cell.K_si[-1], my_cell.Cl_si[-1], my_cell.Ca_si[-1], my_cell.X_si[-1]], my_cell.V_si)
    q_se = my_cell.total_charge([my_cell.Na_se[-1], my_cell.K_se[-1], my_cell.Cl_se[-1], my_cell.Ca_se[-1], my_cell.X_se[-1]], my_cell.V_se)        
    q_di = my_cell.total_charge([my_cell.Na_di[-1], my_cell.K_di[-1], my_cell.Cl_di[-1], my_cell.Ca_di[-1], my_cell.X_di[-1]], my_cell.V_di)
    q_de = my_cell.total_charge([my_cell.Na_de[-1], my_cell.K_de[-1], my_cell.Cl_de[-1], my_cell.Ca_de[-1], my_cell.X_de[-1]], my_cell.V_de)
    print("Final values")
    print("----------------------------")
    print("total charge at the end (C): ", q_si + q_se + q_di + q_de)
    print("Q_si (C):", q_si)
    print("Q_se (C):", q_se)
    print("Q_di (C):", q_di)
    print("Q_de (C):", q_de)
