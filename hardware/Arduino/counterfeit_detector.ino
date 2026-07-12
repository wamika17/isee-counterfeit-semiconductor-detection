
const int inputA = 2;
const int inputB = 3;
const int outputY = 4;

const int vinPin = A0;
const int voutPin = A1;

void setupPins();
void performTest();
void transmitData(int A, int B, int logicOut, float vin, float vout);

void setup() {

  Serial.begin(9600);

  setupPins();

  Serial.println("iSEE Counterfeit Detection System");
}

void loop() {

  performTest();

  delay(1000);

}

void setupPins() {

  pinMode(inputA, OUTPUT);
  pinMode(inputB, OUTPUT);

  pinMode(outputY, INPUT);

}

void performTest() {

  for(int A = 0; A <= 1; A++){

    for(int B = 0; B <= 1; B++){

      digitalWrite(inputA, A);

      digitalWrite(inputB, B);

      delay(100);

      int logicOut = digitalRead(outputY);

      float vin =
      analogRead(vinPin) * (5.0 / 1023.0);

      float vout =
      analogRead(voutPin) * (5.0 / 1023.0);

      transmitData(A, B, logicOut, vin, vout);

    }

  }

}

void transmitData(int A, int B, int logicOut,
                  float vin, float vout){

  Serial.print(A);
  Serial.print(",");

  Serial.print(B);
  Serial.print(",");

  Serial.print(logicOut);
  Serial.print(",");

  Serial.print(vin,3);
  Serial.print(",");

  Serial.println(vout,3);

}
