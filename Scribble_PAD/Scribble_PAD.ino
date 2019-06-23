int ldr=A0;
int bl=A1;
int tr=A2;
int br=A3;
int tl=A5;


int sensorVal;
int mouseTL;
int mouseTR;
int mouseBL;
int mouseBR;


void setup() {
            pinMode(tl,INPUT);
            pinMode(tr,INPUT);
            pinMode(bl,INPUT);
            pinMode(br,INPUT);
            pinMode(ldr,INPUT);
            
            Serial.begin(9600);

}

void loop() {
        
        sensorVal=analogRead(ldr);
        mouseTL = analogRead(tl);
        mouseTR = analogRead(tr);
        mouseBL = analogRead(bl);
        mouseBR = analogRead(br);

        
        Serial.print(sensorVal);
        Serial.print(",");
        Serial.print(mouseTL); 
        Serial.print(",");
        Serial.print(mouseTR); 
        Serial.print(",");
        Serial.print(mouseBL);
        Serial.print(",");
        Serial.print(mouseBR);
        Serial.print('\n');
//        delay(1000);

}
