
#define LED 13

#define punto 100
#define raya 600
#define space_w 600
#define space_ch 200

int mssg = 0;
void setup()
{
   pinMode(LED, OUTPUT); //Pin 13 como salida
   Serial.begin(9600); //inicio Serial
}
 
void loop()
{
   if (Serial.available() > 0)
   {
      mssg = Serial.read();

      if(mssg == '-')
        {
          digitalWrite(13, HIGH); delay(raya);
          digitalWrite(13, LOW); delay(space_ch);
        }

      if(mssg == '.')
        {
          digitalWrite(13, HIGH); delay(punto);
          digitalWrite(13, LOW); delay(space_ch);
        }

      if(mssg == ' ')
        {
          digitalWrite(13, LOW); delay(space_w);
        }
   }
}
