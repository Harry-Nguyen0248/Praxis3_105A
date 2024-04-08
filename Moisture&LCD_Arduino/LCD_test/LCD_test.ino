// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
const int moistureSensorPin = A0;


const int buttonStart = 8;
const int buttonRec = 9;
const int buttonEnd = 10;

// State Variables
bool startMode = false;  // Initially, all modes are not active
bool recMode = false;
bool endMode = false;

// Button States
int previousStartState = HIGH; // Assuming HIGH is not pressed (using internal pull-up resistors)
int previousRecState = HIGH;
int previousEndState = HIGH;

unsigned long endModeStartTime = 0; // Tracks when endMode was activated
bool endModeActive = false; // Flag to check if we're tracking end mode time

int a = 0;



void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);

  pinMode(buttonStart, INPUT_PULLUP);
  pinMode(buttonRec, INPUT_PULLUP);
  pinMode(buttonEnd, INPUT_PULLUP);

  // lcd.print("HELLO WORLD!");


  // Print a message to the LCD.
  Serial.begin(9600);
}

void checkState() {
  int currentStartState = digitalRead(buttonStart);
  int currentRecState = digitalRead(buttonRec);
  int currentEndState = digitalRead(buttonEnd);

  // Start Mode Toggle
  if (!startMode && previousStartState == LOW && currentStartState == HIGH) {
    startMode = true; // Activate start mode
    recMode = false;  // Ensure rec mode is deactivated
    endMode = false;  // Ensure end mode is deactivated
    delay(50); // Debounce delay
  }

  // Rec Mode Toggle, only if Start Mode is active
  if (startMode && !recMode && previousRecState == LOW && currentRecState == HIGH) {
    recMode = true; // Activate rec mode
    startMode = false; // Deactivate start mode
    endMode = false;  // Ensure end mode is deactivated
    delay(50); // Debounce delay
  }

  // End Mode Toggle, only if Rec Mode is active
  if (recMode && !endMode && previousEndState == LOW && currentEndState == HIGH) {
    startMode = false; // Activate start mode
    recMode = false;  // Ensure rec mode is deactivated
    endMode = true;  // 
    a = 0; 
    delay(50); // Debounce delay
  }

  // Update the previous states
  previousStartState = currentStartState;
  previousRecState = currentRecState;
  previousEndState = currentEndState;
}

void displayNumber(int value) {
  lcd.setCursor(0, 0);
  lcd.print("Moisture: ");
  lcd.setCursor(12, 0);
  lcd.print(value);
}

void checkMoisture(int value) {
  lcd.setCursor(0, 1);
  if (value <= 300){
    lcd.print("Dry");
  }
  else if (value > 300 & value <= 700) {
    lcd.print("Good");
  }
  else if (value >700){
    lcd.print("Too damped");
  }
  else {
    lcd.print("Error");
  }
}

void idle() {
  lcd.setCursor(0, 0);
  lcd.print("Program Ready");
  lcd.setCursor(0, 1);
  lcd.print("Press to Start");
}

void start(){
  lcd.setCursor(0, 0);
  lcd.print("Program started");
  lcd.setCursor(0, 1);
  lcd.print("Ready to measure");
}

void collect(int value){
  while (a == 0) {
    lcd.setCursor(0, 0);
    lcd.print("Collecting in ");
    delay(500);
    lcd.setCursor(0, 1);
    lcd.print("3..");
    delay(1000);
    lcd.setCursor(4, 1);
    lcd.print("2..");
    lcd.setCursor(8, 1);
    delay(1000);
    lcd.print("1..");
    delay(1000);
    a += 1;
  }

  //
  checkMoisture(value);
  displayNumber(value);
}

void end() {
  lcd.setCursor(0, 0);
  lcd.print("Program ended");
  delay(1000);
  lcd.setCursor(0, 1);
  lcd.print("Have a nice day!");
  delay(1000);
}

void checkEndAndReset() {
  if (endMode && !endModeActive) {
    // End mode has just become active, start the timer
    endModeStartTime = millis();
    endModeActive = true;
  } else if (!endMode) {
    // If endMode is not active, reset the tracking flag
    endModeActive = false;
  }

  if (endModeActive && millis() - endModeStartTime > 5000) {
    // If endMode has been active for more than 5 seconds, reset states
    Serial.println("End mode active for more than 5 seconds. Resetting...");
    startMode = false;
    recMode = false;
    endMode = false;
    endModeActive = false; // Reset the endMode tracking flag
  }
}

void test(int value){
  Serial.print("Moisture Level: ");
  Serial.println(value);

  // Display the current state of each mode
  Serial.println("Mode Status:");
  Serial.print("Start Mode: ");
  Serial.println(startMode ? "Active" : "Inactive");

  Serial.print("Rec Mode: ");
  Serial.println(recMode ? "Active" : "Inactive");

  Serial.print("End Mode: ");
  Serial.println(endMode ? "Active" : "Inactive");

  Serial.println("-------------------------------");
}


void loop() {
  checkEndAndReset();
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  // print the number of seconds since reset:

  int rawValue = analogRead(moistureSensorPin);
  // int sensorValue = (rawValue/1023) * 100;
  // lcd.autoscroll();

  checkState();
  if (startMode){
    lcd.clear();
    start();
    // lcd.print("1");
  }
  if (recMode){
    lcd.clear();
    collect(rawValue);
    // lcd.print("2");

  }
  if (endMode){
    lcd.clear();
    end();
    // lcd.print("3");
  }
  if (!startMode && !recMode && !endMode) {
    lcd.clear();
    idle();
  }
  
  
  // Print the sensor value to the Serial Monitor
  test(rawValue);
  
  // Pause for 0.5 seconds (500 milliseconds) before the next read
  // delay(1000);
  lcd.clear();
}