#define PIR 5
#define Buzz 6
#define LED 7

int val=0; //initializing the value as zero

void setup(){
pinMode(Buzz, OUTPUT);
pinMode(LED, OUTPUT);
pinMode(PIR, INPUT);
Serial.begin(9600);
}

void loop(){
 val = digitalRead(PIR);
 if(val ==HIGH){ //movement detected
 digitalWrite(LED, HIGH); //turn LED on
 tone(Buzz, 1000); //send 1KHz signal..
 delay(1000); //for 1 sec
 noTone(Buzz); //stop sound
 Serial.println("Intruder Detected"); //print this text in Serial monitor

 }
else
{
 digitalWrite(LED, LOW);
 digitalWrite(Buzz, LOW);
 Serial.println("No movement detected");

}

}
