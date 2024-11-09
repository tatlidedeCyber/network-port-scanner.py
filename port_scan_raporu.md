# Penetrasyon Testi Raporu

## Test Bilgileri
- **Testi Yapan**: Emel Tatlıdede
- **Test Tarihi**: 2024-11-09
- **Hedef IP Adresi**: 192.168.1.1
- **Test Türü**: Port taraması
- **Testin Amacı**: Hedef sistemde yaygın olarak kullanılan portları tarayarak açık ve kapalı portları tespit etmek.

## Kullanılan Yöntemler
- **Port Tarama**: Yaygın kullanılan 13 port üzerinde tarama yapılmıştır.
- **Tarama Araçları**: Python tabanlı port tarama scripti kullanılmıştır.
- **Zaman Aşımı**: Bağlantı denemeleri için 1 saniyelik zaman aşımı süresi belirlenmiştir.

## Yaygın Portlar ve Hizmetler
Tarama sırasında kullanılan yaygın portların açıklamaları aşağıda belirtilmiştir:

| Port | Hizmet | Açıklama |
|------|--------|----------|
| 21   | FTP    | Dosya transferi için kullanılır. |
| 22   | SSH    | Güvenli uzak bağlantı sağlar. |
| 23   | Telnet | Uzak bağlantı için kullanılır, ancak güvenli değildir. |
| 25   | SMTP   | E-posta göndermek için kullanılır. |
| 53   | DNS    | Alan adı çözümlemesi sağlar. |
| 80   | HTTP   | Web sayfalarına erişmek için kullanılır. |
| 110  | POP3   | E-posta almak için kullanılır. |
| 143  | IMAP   | E-postaları almak için kullanılır. |
| 443  | HTTPS  | Güvenli web erişimi sağlar. |
| 3306 | MySQL  | Veritabanı bağlantıları için kullanılır. |
| 3389 | RDP    | Uzak masaüstü bağlantıları için kullanılır. |
| 8080 | HTTP Alternatif | Web sunucuları için alternatif bir port. |

## Tarama Sonuçları

### **Açık Portlar:**
- **Port 21**: Açık - **FTP (File Transfer Protocol)**: Dosya transferi için kullanılır. Bu port açık olduğu için uzaktan FTP ile dosya transferi yapılabilir.
- **Port 53**: Açık - **DNS (Domain Name System)**: Alan adı çözümlemesi sağlar. DNS üzerinden alan adı sorgulamaları yapılabilir.
- **Port 80**: Açık - **HTTP (Hypertext Transfer Protocol)**: Web sayfalarına erişim sağlar. Web sunucusuna HTTP ile erişilebilir.
- **Port 443**: Açık - **HTTPS (HTTP Secure)**: Güvenli web erişimi sağlar. Web sunucusuna HTTPS üzerinden güvenli bağlantı yapılabilir.

### **Kapalı Portlar:**
- **Port 22**: Kapalı - **SSH (Secure Shell)**: Güvenli uzak bağlantı sağlar. Bu port kapalı, bu da güvenli bağlantı sağlanamadığı anlamına gelir.
- **Port 23**: Kapalı - **Telnet**: Uzak bağlantı için kullanılır, ancak güvenli değildir. Bu port kapalı olduğu için telnet ile bağlantı sağlanamaz.
- **Port 25**: Kapalı - **SMTP (Simple Mail Transfer Protocol)**: E-posta göndermek için kullanılır. E-posta gönderme hizmeti kapalıdır.
- **Port 110**: Kapalı - **POP3 (Post Office Protocol 3)**: E-posta almak için kullanılır. Bu port kapalı, bu da e-posta alımının mümkün olmadığı anlamına gelir.
- **Port 143**: Kapalı - **IMAP (Internet Message Access Protocol)**: E-postaları almak için kullanılır. E-posta alımına imkan verilmez.
- **Port 3306**: Kapalı - **MySQL**: Veritabanı bağlantıları için kullanılır. MySQL veritabanı bağlantısı kurulamaz.
- **Port 3389**: Kapalı - **RDP (Remote Desktop Protocol)**: Uzak masaüstü bağlantıları için kullanılır. RDP bağlantısı yapılmaz.
- **Port 8080**: Kapalı - **HTTP Alternatif Port**: Web sunucuları için alternatif bir port. Alternatif web sunucusu portu kapalıdır.

## Değerlendirme ve Yorumlar

- **Açık Portlar:**
  - **Port 21 (FTP)**: Bu port üzerinden dosya transferi yapılabilir. FTP protokolü güvenli değildir, bu nedenle bu portun açık olması bir güvenlik riski oluşturur.
  - **Port 53 (DNS)**: DNS sorguları yapılabilir. DNS üzerinde yapılacak saldırılar (örneğin DNS spoofing) mümkündür.
  - **Port 80 (HTTP)**: Web sayfalarına HTTP protokolü üzerinden erişilebilir. Bu port üzerinden yapılan bağlantılarda şifreleme yapılmaz, dolayısıyla güvenlik riskleri taşıyabilir.
  - **Port 443 (HTTPS)**: Güvenli web erişimi sağlar, ancak SSL/TLS yapılandırmalarının düzgün olup olmadığına dikkat edilmelidir.

- **Kapalı Portlar:**
  - **Port 22 (SSH)**: SSH bağlantısının kapalı olması, uzaktan güvenli erişim sağlanamaması anlamına gelir. Bu da bir güvenlik önlemidir.
  - **Port 23 (Telnet)**: Telnet'in kapalı olması da güvenlik açısından olumlu bir durumdur çünkü Telnet şifresiz veri gönderir ve güvenli değildir.
  - **Port 25 (SMTP)**: E-posta göndermek için kullanılan SMTP servisi kapalıdır, dolayısıyla e-posta ile saldırılar gerçekleştirilemez.
  - **Port 110 (POP3) ve 143 (IMAP)**: E-posta alımı için kullanılan portlar kapalıdır. Bu, e-posta saldırılarına karşı bir güvenlik önlemidir.
  - **Port 3306 (MySQL)**: Veritabanı bağlantısı kurulamaz, bu da veritabanı saldırılarının önüne geçmek için bir güvenlik tedbiridir.
  - **Port 3389 (RDP)**: Uzak masaüstü bağlantısı kapalıdır, bu da saldırganların masaüstüne erişmesini engeller.
  - **Port 8080 (HTTP Alternatif)**: Web uygulamalarının alternatif portu kapalıdır, bu da olası saldırıları engellemek için önemlidir.

## Sonuçlar ve Öneriler

- **Açık portlar**: Sistemdeki açık portlar, saldırganlar için potansiyel zafiyetler sunmaktadır. Özellikle port 21 (FTP), 80 (HTTP) ve 443 (HTTPS) dikkat edilmesi gereken açık portlardır. Bu portların güvenlik yapılandırmalarının gözden geçirilmesi gerekmektedir.
- **Kapalı portlar**: Güvenlik açısından kapalı olan portlar (SSH, Telnet, SMTP vb.) sistemin daha güvenli olduğunu göstermektedir. Ancak, belirli hizmetlerin kapalı olması, işletim sisteminin yapılandırma durumunu da gözler önüne sermektedir.

### Öneriler:
1. **FTP** servisi yerine güvenli bir dosya transfer protokolü (örneğin, SFTP) kullanılabilir.
2. **HTTP** portu üzerinde şifreleme yapılmıyorsa, SSL/TLS sertifikası ile HTTPS kullanılmaya başlanmalıdır.
3. **DNS** güvenliği artırılmalıdır. DNSSEC (DNS Security Extensions) kullanımı tavsiye edilir.
4. **Sistem güncellemeleri** düzenli olarak yapılmalıdır. Açık portlar üzerinden bilinen zafiyetler kullanılabilir.
5. **Güvenlik Duvarı** kullanımı ve ağ segmentasyonu yapılmalıdır.

## Test Sonuçları Özeti
Tarama, hedef IP adresinde 13 yaygın port üzerinde gerçekleştirildi ve aşağıda belirtilen portlar üzerinde açık ya da kapalı durumları tespit edilmiştir:

- 4 açık port
- 9 kapalı port

Sistemdeki açık portlar hakkında daha fazla güvenlik önlemi alınması gerektiği sonucuna varılmıştır.

**Testin Sonlanma Durumu**: Başarılı - Test tamamlandı.
