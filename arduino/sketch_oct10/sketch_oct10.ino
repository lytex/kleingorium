#include <math.h>   

void setup() {
  int i;
  for (i=2; i<13;i++) {
    pinMode(i, OUTPUT);
  }
  Serial.begin(9600);
  // Serial.println("hola");
}

int setPins2(int i, int j) {
    int s0, s1;
    if (i < 0) {
      s0 = 0;
      i = -i;
    } else {
      s0 = 1;
      i = i;
    }
    if (j < 0) {
      s1 = 0;
      j = -j;
    } else {
      s1 = 1;
      j = j;
    }
    
    i = i - 2;
    j = j - 2;
    int bits[] = {LOW, HIGH};
    unsigned int i0 = (i & 4)>>2;
    unsigned int i1 = (i & 2)>>1;
    unsigned int i2 = (i & 1);
    unsigned int j0 = (j & 4)>>2;
    unsigned int j1 = (j & 2)>>1;
    unsigned int j2 = (j & 1);
    char buffer[40];
    sprintf(buffer, "i = %i ", i);
    Serial.println(buffer); 
    sprintf(buffer, "%i - %i ", s0, (i0*4 + i1*2 + i2+2));
    sprintf(buffer, "%i - %i ", s1, (j0*4 + j1*2 + j2+2));
    Serial.println(buffer); 
    digitalWrite(2, bits[i0]);
    digitalWrite(3, bits[i1]);
    digitalWrite(4, bits[i2]);
    digitalWrite(5, bits[s0]);
    digitalWrite(6, bits[j0]);
    digitalWrite(7, bits[j1]);
    digitalWrite(8, bits[j2]);
    digitalWrite(9, bits[s1]);
    return 0;
}

int setPins(int i, int j, int s0, int s1) {
    i = i - 2;
    j = j - 2;
    int bits[] = {LOW, HIGH};
    unsigned int i0 = (i & 4)>>2;
    unsigned int i1 = (i & 2)>>1;
    unsigned int i2 = (i & 1);
    int j0 = (j & 4)>>2;
    int j1 = (j & 2)>>1;
    int j2 = (j & 1);
    char buffer[40];
    sprintf(buffer, "i = %i ", i);
    Serial.println(buffer); 
    sprintf(buffer, "%i - %i ", s0, (i0*4 + i1*2 + i2+2));
    sprintf(buffer, "%i - %i ", s1, (j0*4 + j1*2 + j2+2));
    Serial.println(buffer); 
    digitalWrite(2, bits[i0]);
    digitalWrite(3, bits[i1]);
    digitalWrite(4, bits[i2]);
    digitalWrite(5, bits[s0]);
    digitalWrite(6, bits[j0]);
    digitalWrite(7, bits[j1]);
    digitalWrite(8, bits[j2]);
    digitalWrite(9, bits[s1]);
    return 0;
}
// Dorian
void loop() {
  char buffer[40];
  int step = 50;
  int a = 1;
  int i = 6;
  for (int i=7; i<11; i++) {
    // i = -i;
    for (int rep=0; rep<8; rep++) {
      setPins2(-i, -5);
      delay(1*step);
      setPins2(-i, -6);
      delay(1*step);
      setPins2(-i, -7);
      delay(1*step);
      setPins2(-i, -9);
      delay(1*step);
      setPins2(-i, -2);
      delay(1*step);
    }
  }
}
