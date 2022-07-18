//NTP
#include <NTPClient.h>
#include <WiFiUdp.h>

//Json
#include <ArduinoJson.h>

//WiFi
#include <ESP8266WiFi.h>
#define WIFI_SSID "DONNY"
#define WIFI_PASSWORD "ciko1234"

//HTTP Client
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
const char* serverName = "Masukan url"

//Firebase
#include <FirebaseESP8266.h>
#define FIREBASE_HOST "pdam-piuhuy8mgg-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "qnfcqidW9Na5zQ0raV8DLsNheTySOmMP4smn5LSP"
#define API_KEY "AIzaSyDD1kh52ShwP6ZoJbZjCPFJ8xlvoMuKZNw"
#define USER_EMAIL "donnyfadhillah23@gmail.com"
// #define USER_PASSWORD "*********"
#include "addons/TokenHelper.h"
#include "addons/RTDBHelper.h"
//FlowSwitch
#define int1 D5
#define int2 D6

//Inisialisasi NTP
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "id.pool.ntp.org", 25200, 10000);
char dayWeek [7][12] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
String months[12]={"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}; 

String dayName;

//Inisialisasi Firebase
FirebaseData fbdo;
FirebaseData limit;
FirebaseData usage;

FirebaseConfig config;
FirebaseAuth auth;

//Inisialisasi Flow Meter

void ICACHE_RAM_ATTR pulseCounter1();
void ICACHE_RAM_ATTR pulseCounter2();
void ICACHE_RAM_ATTR pulseCounter3();
void ICACHE_RAM_ATTR flowMeter1();
void ICACHE_RAM_ATTR flowMeter2();
void ICACHE_RAM_ATTR flowMeter3();

#define sensorInt1 D1
#define sensorInt2 D2
#define sensorInt3 D3 
#define flowsensor1 D1
#define flowsensor2 D2
#define flowsensor3 D3

float konstanta = 4.5; //konstanta flow meter

volatile byte pulseCount1;
volatile byte pulseCount2;
volatile byte pulseCount3;

float debit1;
float debit2;
float debit3;
unsigned int flowmlt1;
unsigned int flowmlt2;
unsigned int flowmlt3;
unsigned long totalmlt1;
unsigned long totalmlt2;
unsigned long totalmlt3;

unsigned long usageTotal;

unsigned long oldTime;
unsigned long timeCounter;
int timeCounter1 = 0;

#define led D4

//Inisialisasi Pressure Sensor
#define pressure_pin A0
float offset = 0.483;
float v, p;

//Path Firebase
String usage1 = "/customerLog/aggHrjj/usage1";
String usage2 = "/customerLog/aggHrjj/usage2";
String usage3 = "/customerLog/aggHrjj/usage3";

String limitUsage = "/customerLog/aggHrjj/limitUsage";
String pressure = "/customerLog/aggHrjj/pressure";
String statusValve = "/customerLog/aggHrjj/statusValve";
String totalUsage = "/customerLog/aggHrjj/totalUsage";

String pathHistory = "/customerHistory/aggHrjj/";

//API
DynamicJsonDocument doc(1024);

String dayName_func(){
  timeClient.update();
  String dayData = dayWeek[timeClient.getDay()];
  return dayData;
}

void setup() {
  Serial.begin(9600);

  pinMode(led, OUTPUT);
  
  //Connect WiFi
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());

  Serial.println("Getting Ready...");

  //Konfigurasi Firebase
  config.api_key = API_KEY;
  config.database_url = FIREBASE_HOST;
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  auth.user.email = USER_EMAIL;
  //auth.user.password = USER_PASSWORD;
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

  //Konfigurasi flowsensor
  pinMode(flowsensor1, INPUT);
  pinMode(flowsensor2, INPUT);
  pinMode(flowsensor3, INPUT);
  digitalWrite(flowsensor1, HIGH);
  digitalWrite(flowsensor2, HIGH);
  digitalWrite(flowsensor3, HIGH);

  pulseCount1 = 0;
  pulseCount2 = 0;
  pulseCount3 = 0;
  debit1 = 0.0;
  debit2 = 0.0;
  debit3 = 0.0;
  flowmlt1 = 0;
  flowmlt2 = 0;
  flowmlt3 = 0;

  Firebase.getInt(usage, usage1);
  totalmlt1 = usage.intData();
  Firebase.getInt(usage, usage2);
  totalmlt2 = usage.intData();
  Firebase.getInt(usage, usage3);
  totalmlt3 = usage.intData();
  Firebase.getInt(usage, totalUsage);
  usageTotal = usage.intData();
  oldTime = 0;

  //tokenHabis = false;

  attachInterrupt(sensorInt1, pulseCounter1, FALLING);
  attachInterrupt(sensorInt2, pulseCounter2, FALLING);
  attachInterrupt(sensorInt3, pulseCounter3, FALLING);
  
  //Konfigurasi FlowSwitch
  pinMode(int1, OUTPUT);
  pinMode(int2, OUTPUT);

  //Konfigurasi Pressure
  pinMode(pressure_pin, INPUT);

  digitalWrite(led, HIGH);

  //Konfigurasi NTP
  dayName = dayName_func();

  //Json
  //DynamicJsonDocument doc(1024);

  Serial.print("Usage 1: "); Serial.println(totalmlt1);
  Serial.print("Usage 2: "); Serial.println(totalmlt2);
  Serial.print("Usage 3: "); Serial.println(totalmlt3);
  Serial.print("Total Usage: "); Serial.println(usageTotal);
  Serial.print("Hari: "); Serial.println(dayName);

  Serial.println("Ready...");
}

void timeStamp(){
  timeClient.update();

  Serial.print(timeClient.getFormattedTime()+ " ");

  delay(1000);
}

String getDate(){
  timeClient.update();

  time_t epochTime = timeClient.getEpochTime();

  struct tm *ptm = gmtime ((time_t *)&epochTime); 

  int monthDay = ptm->tm_mday;

  int currentMonth = ptm->tm_mon+1;

  String currentMonthName = months[currentMonth-1];

  int currentYear = ptm->tm_year+1900;

  String currentDate = String(currentYear) + "-" + String(currentMonth) + "-" + String(monthDay);

  return currentDate;
}

//Fungsi untuk sum
void sumTotalUsage(long param){
  usageTotal += param;

  Firebase.setInt(usage, totalUsage, usageTotal);
}

void flowMeter(){
  if((millis() - oldTime) > 1000) 
  {
    Serial.println("FlowMeter Standby");
    flowMeter1();
    flowMeter2();
    flowMeter3();
  }
}
//Fungsi pengolahan debit air 1 (utama)
void flowMeter1()
{
    
    debit1 = ((1000.0 / (millis() - oldTime)) * pulseCount1) / konstanta;
    oldTime = millis();
    timeCounter += oldTime;

    Firebase.getInt(limit, limitUsage);
    Firebase.getInt(usage, usage1);
    unsigned int limitVal1 = limit.intData();
    
    flowmlt1 = (debit1 / 60) * 1000;
    totalmlt1 += flowmlt1;

    unsigned int totalVolume1;
    totalVolume1 = usage.intData();
    totalVolume1 += flowmlt1;

    Serial.print("Debit air: ");
    Serial.print(int(debit1));
    Serial.print("L/min");
    Serial.print("\t");

    Firebase.setInt(usage, usage1, totalVolume1);
    Serial.print("Volume: "); 
    Serial.print(totalmlt1);
    Serial.println("mL"); 

    limitVal1 -= flowmlt1;
    Firebase.setInt(limit, limitUsage, limitVal1);

    sumTotalUsage(totalmlt1);

    detachInterrupt(sensorInt1);
    
    attachInterrupt(sensorInt1, pulseCounter1, FALLING);
}

void pulseCounter1()
{
// Increment the pulse counter
    pulseCount1++;
}

//Fungsi pengolahan debit air 2
void flowMeter2()
{
    
    debit2 = ((1000.0 / (millis() - oldTime)) * pulseCount2) / konstanta;
    oldTime = millis();
    timeCounter += oldTime;

    Firebase.getInt(limit, limitUsage);
    Firebase.getInt(usage, usage2);
    // unsigned int limitVal2 = limit.intData();
    
    flowmlt2 = (debit2 / 60) * 1000;
    totalmlt2 += flowmlt2;

    unsigned int totalVolume2;
    totalVolume2 = usage.intData();
    totalVolume2 += flowmlt2;

    Serial.print("Debit air 2: ");
    Serial.print(int(debit2));
    Serial.print("L/min");
    Serial.print("\t");

    Firebase.setInt(usage, usage2, totalVolume2);
    Serial.print("Volume 2: "); 
    Serial.print(totalmlt2);
    Serial.println("mL"); 

    sumTotalUsage(totalmlt2);

    detachInterrupt(sensorInt2);

    attachInterrupt(sensorInt2, pulseCounter2, FALLING);

}

void pulseCounter2()
{
// Increment the pulse counter
    pulseCount2++;
}

//Fungsi pengolahan debit air 3
void flowMeter3()
{
    debit3 = ((1000.0 / (millis() - oldTime)) * pulseCount3) / konstanta;
    oldTime = millis();
    timeCounter += oldTime;

    Firebase.getInt(limit, limitUsage);
    Firebase.getInt(usage, usage3);
    // unsigned int limitVal3 = limit.intData();
    
    flowmlt3 = (debit3 / 60) * 1000;
    totalmlt3 += flowmlt3;

    unsigned int totalVolume3;
    totalVolume3 = usage.intData();
    totalVolume3 += flowmlt3;

    Serial.print("Debit air 3: ");
    Serial.print(int(debit3));
    Serial.print("L/min");
    Serial.print("\t");

    Firebase.setInt(usage, usage3, totalVolume3);
    Serial.print("Volume 3: "); 
    Serial.print(totalmlt3);
    Serial.println("mL"); 

    sumTotalUsage(totalmlt3);

    detachInterrupt(sensorInt3);
    attachInterrupt(sensorInt3, pulseCounter3, FALLING);
}

void pulseCounter3()
{
// Increment the pulse counter
    pulseCount3++;
}

void pushHistory(){
  String waktu = getDate();
  Firebase.getInt(usage, totalUsage);
  FirebaseJson json;
  json.set(waktu, usage.intData());
  Firebase.updateNode(usage, String(pathHistory + usage.pushName()), json);
}

//POST API Function
void pushAPI(){
  //Konfigurasi API
  WiFiClient wifiClient;
  HTTPClient http;
  http.begin(wifiClient, serverName);
  http.addHeader("Content-Type", "application/json");

 String jsonParam;

 JsonObject data = doc.as<JsonObject>();

 data["test1"] = "test";

 serializeJson(data, jsonParam);
 Serial.println(jsonParam);

 int httpResponse = http.POST(jsonParam);
 Serial.println(httpResponse);

  http.end();
}

//Send data to API function
void sendData(){
  String dayCounter = dayName_func();
  if(dayCounter != dayName){
    //masukin send data to APIs
    pushAPI();
    pushHistory();
    dayName = dayCounter;
  }
}

//Fungsi flowswitch
void FlowSwitch_Close(){
  digitalWrite(int1, HIGH);
  digitalWrite(int2, LOW);
}

void FlowSwitch_Open(){
  digitalWrite(int1, LOW);
  digitalWrite(int2, LOW);
}

//Fungsi pressure sensor
void PressureSensor(){
  float PSI;
  float Pa = 0.145;

  v = analogRead(A0)*5.00 / 1024;
  p = (v - offset) * 400;
  PSI = p * Pa;

  Firebase.setInt(usage, pressure, PSI);

  Serial.print("Pressure : ");
  Serial.print(PSI);
  Serial.print(" psi    ");
}

//Main Source Code
void loop() {
  Firebase.getInt(limit, limitUsage);
  Firebase.getInt(usage, usage1);
  Firebase.getBool(usage, statusValve);

  if (limit.intData() > 0){
    digitalWrite(D4, HIGH);
    FlowSwitch_Open();
    timeStamp();
    PressureSensor();
    flowMeter();
    // writeFirebase1();
    sendData();
    Serial.println(limit.intData());
    delay(1000);
  }else {
    timeStamp();
    FlowSwitch_Close();
    Firebase.setBool(usage, statusValve, false);
    Serial.println("Token Habis");
    // writeFirebase1();
    sendData();
    digitalWrite(D4, LOW);
    delay(1000);
  }
}
