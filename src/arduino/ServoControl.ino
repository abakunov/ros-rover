#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>

class NewHardware : public ArduinoHardware
{
  public:
  NewHardware():ArduinoHardware(&Serial1, 115200){};
};

ros::NodeHandle_<NewHardware> nh;

Servo horizontal_servo;
Servo vertical_servo;

void horizontal_servo_cb( const std_msgs::UInt16& cmd_msg){
  horizontal_servo.write(cmd_msg.data);  
  digitalWrite(13, HIGH-digitalRead(13));    
}

void vertical_servo_cb( const std_msgs::UInt16& cmd_msg){
  vertical_servo.write(cmd_msg.data); 
  digitalWrite(13, HIGH-digitalRead(13));  
}


ros::Subscriber<std_msgs::UInt16> horizontal_sub("horizontal_servo", horizontal_servo_cb);
ros::Subscriber<std_msgs::UInt16> vertical_sub("vertical_servo", vertical_servo_cb);


void setup(){
  pinMode(13, OUTPUT);

  nh.initNode();
  nh.subscribe(horizontal_sub);
  nh.subscribe(vertical_sub);
  
  horizontal_servo.attach(44); 
  vertical_servo.attach(45);
}

void loop(){
  nh.spinOnce();
  delay(1);
}
