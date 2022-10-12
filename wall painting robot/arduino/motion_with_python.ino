int motor=7,yukari_asagi=6,yukari_asagi2=5,boya=4;
char message;
int PUL=8;
int DIR=9;
int EN=10; 
int sinir=13;
int adim=100;
int ms=300;
long ilerleme=0L;
long y_siniri=40600L;
bool sola=false;
bool saga=false;
bool home_go=false;
void setup() {
  pinMode (PUL, OUTPUT);
  pinMode (DIR, OUTPUT);
  pinMode (EN, OUTPUT);
  pinMode (sinir,INPUT);
  digitalWrite(EN,HIGH);
  pinMode(motor,OUTPUT);
  pinMode(yukari_asagi,OUTPUT);
  pinMode(yukari_asagi2,OUTPUT);
  pinMode(boya,OUTPUT);
  digitalWrite(motor,HIGH);
  digitalWrite(yukari_asagi,HIGH);
  digitalWrite(yukari_asagi2,HIGH);
  digitalWrite(boya,HIGH);
  Serial.begin(9600);
}
 
void loop() {
if(Serial.available()>0)
{
  message=Serial.read();
  if(message == '1')
  {
  digitalWrite(motor,HIGH);
  delay(200);
  digitalWrite(yukari_asagi,LOW);
  digitalWrite(yukari_asagi2,LOW);
  delay(200);
  digitalWrite(motor,LOW);
  message="";
  Serial.println("Boya Tabancası Yukarı!");
  }
  if(message == '2')
  {
  digitalWrite(motor,HIGH);
  message="";
  Serial.println("Z Motoru Durdu!");
  }
  if(message == '3')
  {
  digitalWrite(motor,HIGH);
  delay(200);
  digitalWrite(yukari_asagi,HIGH);

  digitalWrite(yukari_asagi2,HIGH);
  delay(200);
  digitalWrite(motor,LOW);
  message="";
  Serial.println("Boya Tabancası Aşağı!");
  }
  if(message == '4')
  {
    if (digitalRead(sinir!=0))
    {
      
      Serial.println("Robot Sola!");
      saga=false;
      sola=true;
      digitalWrite(DIR,HIGH);
      delay(50);
      
      }
    else Serial.println("En uc sinira ulasildi!");
  
  message="";
  }
  if(message == '5')
  {
   Serial.println("Robot Dur!");
   sola=false;
   saga=false;
  message="";
  }
  if(message == '6')
  {
     if (ilerleme<y_siniri)
    {
      
      Serial.println("Robot Sağa!");
      saga=true;
      sola=false;
      digitalWrite(DIR,LOW);
      delay(50);
      
      
      }
     else Serial.println("En uc sinira ulasildi!");
     message="";
  }
  if(message == '7')
  {
  digitalWrite(motor,HIGH);
  delay(100);
  digitalWrite(yukari_asagi,HIGH);
  digitalWrite(yukari_asagi2,HIGH);
  digitalWrite(boya,HIGH);
  sola=false;
  saga=false;
  Serial.println("Sistem Durdu!");
  message="";
  }
  if(message == '8')
  {
  digitalWrite(boya,LOW);
  Serial.println("Boya Tabancası Çalıştırılıyor!");
  message="";
  }
  if(message == '9')
  {
  digitalWrite(boya,HIGH);
  Serial.println("Boya Tabancası Durduruldu!");
  message="";
  }
  if (message == 'h')
  {
    Serial.println("Home Pozisyonuna Gidiliyor..!");
    saga=false;
    sola=false;
    home_go=true;
    digitalWrite(DIR,HIGH);
    delay(50);
    message="";
    }
//MOTOR HAREKETLERİ
  
    
   
  }
if (sola==true)
  {
    if (digitalRead(sinir)!=0)
    {
      digitalWrite(PUL,HIGH);
      delayMicroseconds(ms);
      digitalWrite(PUL,LOW);
      delayMicroseconds(ms);
      ilerleme--;
      }
     else
     {
      Serial.println("Sinir anahtarına ulaşıldı");
      sola=false;
      }
    
    }
if (saga==true)
  {
    if (ilerleme<y_siniri)
    {
      digitalWrite(PUL,HIGH);
          delayMicroseconds(ms);
          digitalWrite(PUL,LOW);
          delayMicroseconds(ms);
          ilerleme++;
      }
     else 
     {
      saga=false;
      }
        
        }
if (home_go==true)
{
  // Bu kısma Yukarı - Aşağı Kısmınıda Ekle
  if (digitalRead(sinir)!=0)
  {
    digitalWrite(PUL,HIGH);
    delayMicroseconds(ms);
    digitalWrite(PUL,LOW);
    delayMicroseconds(ms);
  }
  else 
  {
    Serial.println("Home Pozisyonu Uygulandı");
    home_go=false;
    ilerleme=0L;
    }
  
  
  }
 }

  
