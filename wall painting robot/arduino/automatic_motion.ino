int motor=7,yukari_asagi=6,yukari_asagi2=5,boya=4;
int PUL=8;
int DIR=9;
int EN=10; 
int adim=100;
int ms=300;
unsigned int ilerleme=0;
unsigned int y_siniri=40000;
bool sola=false;
bool saga=false;
bool home_go=false;
int z_time = 5000;
int y_ilerleme =5000;
int a;
int k=0;
int t=0;
bool ilk_home=false;
void setup() {
  pinMode (PUL, OUTPUT);
  pinMode (DIR, OUTPUT);
  pinMode (EN, OUTPUT);
  digitalWrite(EN,HIGH);
  pinMode(motor,OUTPUT);
  pinMode(yukari_asagi,OUTPUT);
  pinMode(yukari_asagi2,OUTPUT);
  pinMode(boya,OUTPUT);
  digitalWrite(motor,HIGH);
  digitalWrite(yukari_asagi,HIGH);
  digitalWrite(yukari_asagi2,HIGH);
  digitalWrite(boya,HIGH);
  


}

void loop() 
{
  if(ilk_home==false)
  {
    k=0;
    digitalWrite(motor,LOW);
    digitalWrite(yukari_asagi,HIGH);
    digitalWrite(yukari_asagi2,HIGH);
    delay(5000);
    ilk_home=true;
    }
   
  if (k==0)
  {
    digitalWrite(motor,HIGH);
    delay(50);
    digitalWrite(yukari_asagi,LOW);
    digitalWrite(yukari_asagi2,LOW);
    delay(50);
    digitalWrite(boya,LOW);
    digitalWrite(motor,LOW);
    delay(z_time-100);
    digitalWrite(motor,HIGH);
    digitalWrite(boya,HIGH);
    }
  
  for (int i = 0; i < y_ilerleme; i++)
  {
    if (ilerleme<y_siniri)
    {
      ilerleme++;
      digitalWrite(DIR,LOW);
      digitalWrite(PUL,HIGH);
      delayMicroseconds(ms);
      digitalWrite(PUL,LOW);
      delayMicroseconds(ms);
      }
    else 
    {
     k=1; 
      }
    }
  if (k==0)
  {
    digitalWrite(motor,HIGH);
    delay(50);
    digitalWrite(yukari_asagi,HIGH);
    digitalWrite(yukari_asagi2,HIGH);
    delay(50);
    digitalWrite(boya,LOW);
    digitalWrite(motor,LOW);
    delay(z_time-800);
    digitalWrite(boya,HIGH);
    digitalWrite(motor,HIGH);
    }
  
  for (int i = 0; i < y_ilerleme; i++)
  {
    if (ilerleme<y_siniri)
    {
      ilerleme++;
      digitalWrite(DIR,LOW);
      digitalWrite(PUL,HIGH);
      delayMicroseconds(ms);
      digitalWrite(PUL,LOW);
      delayMicroseconds(ms);
      }
    else
    {
      k=1;
      }
    
    }
   if (k==1) 
   
  {
   
      for (unsigned int j=0;j<y_siniri;j++)
      {
        digitalWrite(DIR,HIGH);
        digitalWrite(PUL,HIGH);
        delayMicroseconds(ms);
        digitalWrite(PUL,LOW);
        delayMicroseconds(ms);
        }
      ilerleme=0;
      k=0;
      ilk_home=false;
      
      }
    
    
    
    delay(1000);

    }
   
  
  
  



















  
