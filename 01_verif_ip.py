# Script RSI - Vérification de classe d'adresse IP
# Auteur: oktchoko-frank-rsi-cm

def verifier_classe_ip(ip):
    try:
        premier_octet = int(ip.split('.')[0])

        if 1 <= premier_octet <= 126:
            return f"L'IP {ip} est de Classe A"
        elif 128 <= premier_octet <= 191:
            return f"L'IP {ip} est de Classe B"
        elif 192 <= premier_octet <= 223:
            return f"L'IP {ip} est de Classe C"
        elif 224 <= premier_octet <= 239:
            return f"L'IP {ip} est de Classe D (Multicast)"
        elif 240 <= premier_octet <= 255:
            return f"L'IP {ip} est de Classe E (Réservée)"
        else:
            return "Classe invalide"
    except:
        return "Adresse IP invalide"

# Test
ip = input("Entrez une adresse IP: ")
print(verifier_classe_ip(ip))
