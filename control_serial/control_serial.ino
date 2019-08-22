char c;
int IN1 = 13;
int IN2 = 12;
int IN3 = 11;
int IN4 = 10;
int ENB = 9;
int flag = 0;
int vel = 50;
void setup()
{
   Serial.begin(9600);
   pinMode(IN1, OUTPUT);
   pinMode(IN2, OUTPUT);
   pinMode(IN3, OUTPUT);
   pinMode(IN4, OUTPUT);
    pinMode(ENB, OUTPUT);
}

void Adelante ()
{
 //Direccion motor
 digitalWrite (IN3, HIGH);
 digitalWrite (IN4, LOW);
 analogWrite (ENB, 50);
}

void Atras ()
{
 //Direccion motor
 digitalWrite (IN3, LOW);
 digitalWrite (IN4, HIGH);
 analogWrite (ENB, 50);
}

void Izquierda(){
 digitalWrite (IN1, HIGH);
 digitalWrite (IN2, LOW);
}

void Derecha(){
 digitalWrite (IN1, LOW);
 digitalWrite (IN2, HIGH);
}

void Recto(){
 digitalWrite (IN1, LOW);
 digitalWrite (IN2, LOW);
}

void Parar ()
{
 digitalWrite (IN1, LOW);
 digitalWrite (IN2, LOW);
 digitalWrite (IN3, LOW);
 digitalWrite (IN4, LOW);
 analogWrite (ENB, 0);
}
void loop()
{
  if(Serial.available()> 0)
  {
    c=Serial.read();
    flag = 0;
    if (c == '6'){
       vel = vel + 25;
       if(vel >= 250)
       {
        vel = 255;
       }
       analogWrite (ENB, vel);
       Serial.println(vel);
    }
    if (c == '7'){
       vel = vel - 25;
       if(vel <= 50)
       {
        vel = 50;
       }
       analogWrite (ENB, vel);
       Serial.println(vel);
    }
  }
  
  if (c == '1') {
    Adelante();
    if(flag == 0){
      Serial.println("Motor: foroward");
      flag=1;
    }
  }
  if (c == '2') {
    Atras();
    if(flag == 0){
      Serial.println("Motor: backward");
      flag=1;
    }
  }
  if (c == '3') {
    Derecha();
    if(flag == 0){
      Serial.println("Motor: right");
      flag=1;
    }
  }

  if (c == '4') {
    Izquierda();
    if(flag == 0){
      Serial.println("Motor: left");
      flag=1;
    }
  }
  if (c == '5') {
    Recto();
    if(flag == 0){
      Serial.println("Motor: onwards");
      flag=1;
    }
  }  
  if (c == '0') {
    Parar();
    if(flag == 0){
      Serial.println("Motor: off");
      flag=1;
    }
  }
}
