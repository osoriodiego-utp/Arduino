const int buttonPin = 2; 
const int ledPin = 13;
int buttonState = 0;


void setup() {
  pinMode(buttonPin, INPUT);  // Botton
  Serial.begin(9600);         // Conex
}

void loop() 
{
  buttonState = digitalRead(buttonPin);

  if (Serial.available() > 0)
  {
    if (buttonState == HIGH)
    {digitalWrite(ledPin, HIGH); Serial.println(1); } // Se envia 1 : encendido
      else
    {digitalWrite(ledPin, LOW); Serial.println(0); } // Se envia 0 : apagado
  }  
}
