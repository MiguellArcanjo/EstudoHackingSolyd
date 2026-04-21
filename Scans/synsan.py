from scapy.all import IP, TCP, sr1

def syn_scan(target_ip, port):
    packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

    response = sr1(packet, timeout=2, verbose=0)

    if response is None:
        print(f"Porta {port}: Filtrada (Sem resposta)")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12: 
            rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
            sr1(rst_packet, timeout=1, verbose=0)
            print(f"Porta {port}: ABERTA")
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Porta {port}: FECHADA")

syn_scan("127.0.0.1", 1024)