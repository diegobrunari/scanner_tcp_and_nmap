import nmap

nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]
scanner = nmap.PortScanner(nmap_search_path=nmap_path)


print("Seja bem-vindo ao Scanner")
print("<------------------------>")

ip = input("Digite o IP a ser varrido: ")
print(f"O IP digitado foi: {ip} ")
type(ip)

menu = input("""
\nEscolha o tipo de verredura a ser realizada:
      1 - Varredura do tipo SYN
      2 - Verredura do tipo UDP
      3 - Verredura do tipo Intensa
""")

print(f"A opção escolhida foi {menu}")

if menu == "1":
    print("Versão do NMAP: ", scanner.nmap_version())
    scanner.scan(ip, "1-1024", "-v -sS")
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas abertas: ", scanner[ip]['tcp'].keys())
elif menu == "2":
      print("Versão do NMAP: ", scanner.nmap_version())
      scanner.scan(ip, "1-1024", "-v -sU")
      print(scanner.scaninfo())
      print("Status do IP: ", scanner[ip].state())
      print(scanner[ip].all_protocols())
      print("")
      print("Portas abertas: ", scanner[ip]['udp'].keys())
elif menu == "3":
      print("Versão do NMAP: ", scanner.nmap_version())
      scanner.scan(ip, "1-1024", "-v -sC")
      print(scanner.scaninfo())
      print("Status do IP: ", scanner[ip].state())
      print(scanner[ip].all_protocols())
      print("")
      print("Portas abertas: ", scanner[ip]['tcp'].keys())
else:
     print("Opção inválida...")