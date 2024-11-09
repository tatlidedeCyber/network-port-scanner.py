import socket  # socket modülünü içe aktarıyoruz; bu, ağ bağlantılarını oluşturmak için gerekli.TCP için

# Yaygın kullanılan bazı port numaralarını ve bu portların hangi hizmetler için kullanıldığını içeren bir sözlük.
port_info = {
    21: "FTP (File Transfer Protocol) - Dosya transferi için kullanılır.",  # 21 numaralı port, FTP hizmeti içindir.
    22: "SSH (Secure Shell) - Güvenli uzak bağlantı sağlar.",  # 22 numaralı port, SSH hizmeti içindir.
    23: "Telnet - Uzak bağlantı için kullanılır, ancak güvenli değildir.",  # 23 numaralı port, Telnet hizmetini belirtir.
    25: "SMTP (Simple Mail Transfer Protocol) - E-posta göndermek için kullanılır.",  # 25 numaralı port, SMTP hizmeti içindir.
    53: "DNS (Domain Name System) - Alan adı çözümlemesi sağlar.",  # 53 numaralı port, DNS hizmetini belirtir.
    80: "HTTP (Hypertext Transfer Protocol) - Web sayfalarına erişmek için kullanılır.",  # 80 numaralı port, HTTP hizmetini belirtir.
    110: "POP3 (Post Office Protocol 3) - E-posta almak için kullanılır.",  # 110 numaralı port, POP3 hizmeti içindir.
    143: "IMAP (Internet Message Access Protocol) - E-postaları almak için kullanılır.",  # 143 numaralı port, IMAP hizmetini belirtir.
    443: "HTTPS (HTTP Secure) - Güvenli web erişimi sağlar.",  # 443 numaralı port, HTTPS hizmetini belirtir.
    3306: "MySQL - Veritabanı bağlantıları için kullanılır.",  # 3306 numaralı port, MySQL veritabanı hizmeti içindir.
    3389: "RDP (Remote Desktop Protocol) - Uzak masaüstü bağlantıları için kullanılır.",  # 3389 numaralı port, RDP hizmetini belirtir.
    8080: "HTTP Alternatif Port - Web sunucuları için alternatif bir port."  # 8080 numaralı port, alternatif bir HTTP portudur.
}

# Belirli bir IP adresi ve port numarasına bağlantı kurmayı deneyen bir işlev.
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Yeni bir TCP soketi oluşturur.
    sock.settimeout(3)  # Zaman aşımını 1 saniye olarak ayarlar; bağlantı denemesi 3 saniye sonra sona erecektir.
    try:
        result = sock.connect_ex((ip, port))  # Bağlantıyı dener; başarılı olursa 0 döner, aksi halde hata kodu.
        if result == 0:
            # Eğer bağlantı başarılı ise, port açıktır.
            return True
    except socket.error:
        # Bağlantı sırasında herhangi bir hata oluşursa, işlemi sessizce geçer.
        pass
    finally:
        sock.close()  # Soketi kapatarak bağlantıyı sonlandırır.
    return False  # Port kapalıysa False döndürür.

# Hedef IP adresindeki yaygın portları tarayan ve açık olan portları açıklayan işlev.
def explain_ports(ip):
    print(f"{ip} adresindeki yaygın portları tarıyoruz...\n")  # Kullanıcıya tarama yapıldığını bildirir.
    for port, description in port_info.items():  # port_info sözlüğünde tanımlı her port için döngü başlatır.
        is_open = scan_port(ip, port)  # Belirtilen IP adresinde portun açık olup olmadığını kontrol eder.
        status = "Açık" if is_open else "Kapalı"  # Port durumu belirlenir; eğer açıksa "Açık", kapalıysa "Kapalı".
        print(f"Port {port}: {status} - {description}")  # Port durumu ve açıklaması kullanıcıya yazdırılır.

# Ana işlev; kullanıcıdan IP adresini alarak port tarama işlemini başlatır.
def main():
    ip_address = input("Hedef IP adresini girin: ")  # Kullanıcıdan hedef IP adresini girmesi istenir.
    explain_ports(ip_address)  # Belirtilen IP adresindeki yaygın portları taramak için explain_ports işlevini çağırır.

# Kodun doğrudan çalıştırıldığında ana işlevi çağıran koşul.
if __name__ == "__main__":
    main()  # main işlevi çalıştırılır; böylece kullanıcıdan IP alınarak tarama işlemi başlatılır.
