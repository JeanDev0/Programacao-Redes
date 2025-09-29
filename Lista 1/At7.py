number_of_switches = int(input("Quantos switches: "))
busy_ports = 0

for switch in range(number_of_switches):
    ports = int(input("Quantas portas estão ocupadas nesse switch? "))
    busy_ports = busy_ports + ports

print (f"Total de portas ocupadas dos {number_of_switches} switches é de {busy_ports} portas")    