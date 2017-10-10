var serial; // variable to hold an instance of the serialport library
var portName = '/dev/cu.usbmodem1411';  // fill in your serial port name here
var pot1;
var pot2;
var pot3;
var button1;
var whatever1 = 0;
var whatever2 = 0;
var whatever3 = 0;
var whatever4 = 0;
var whatever5 = 0;
var whatever6 = 0;
var active = 0; 

function preload(){
note1 = loadSound("http://res.cloudinary.com/cwang12/video/upload/v1507486597/C_Note_vjmdjm.mp3")
note2 = loadSound("http://res.cloudinary.com/cwang12/video/upload/v1507486599/D_Note_ygdgkx.mp3")
note3 = loadSound("http://res.cloudinary.com/cwang12/video/upload/v1507486596/E_Note_lg6wch.mp3")
Chopin = loadSound("http://res.cloudinary.com/cwang12/video/upload/v1507486604/Fantaisie-Impromptu_Opus_66_-_Frederic_Chopin_a5tn78.mp3")
Mario = loadSound("http://res.cloudinary.com/cwang12/video/upload/v1507486591/Mario_e2i9pq.mp3")
}



function setup() {
 createCanvas(600, 400);
 
 serial = new p5.SerialPort();    // make a new instance of the serialport library
 serial.on('list', printList);    // set a callback function for the serialport list event
 serial.on('data', serialEvent);    // callback for when new data arrives
 
 // change the data rate to whatever you wish
 var options = { baudrate: 9600};
 serial.open(portName, options);
 
}


function draw() {
  background(0);
  fill(255,0,0,80);
  ellipse(width/4, height/2, pot1, pot1);
  fill(0,255,0,80);
  ellipse(width/2, height/2, pot2, pot2);
  fill(0,0,255,80);
  ellipse(width*(3/4), height/2, pot3, pot3);
  



  

      if (pot1>10 && button1 ==0) {
        if(whatever1%100 == 0){
         note1.play();
         fill(255,0,0,100);
        }
        whatever1++;
        }
      if (pot2>10 & button1 ==0) {
        if(whatever2%100 == 0){
          note2.play();
        }
        whatever2++;
        }
      if (pot3>10 & button1 == 0) {
        if (whatever3%100 == 0){
          note3.play();
        }
        whatever3++;
        }

      if (pot1>200 && pot2>200 && pot3>200) {
        note1.stop();
        note2.stop();
        note3.stop();
        if (whatever4 % 100100 == 0){
          Mario.play();
        }
          whatever4++;
        }
      //if ((pot1<200 || pot2<200 || pot3<200) && button1 == 0) {
       //  Mario.stop();
      //  }
      

  


    if ((pot1<200 || pot2<200 || pot3<200) && button1 != 0) {
        Mario.stop()
        whatever1 = 0;
        whatever2 = 0; 
        whatever3 = 0;
      }

 
}

function serialEvent() {
  // read a string from the serial port
  // until you get carriage return and newline:
  var inString = serial.readStringUntil('\r\n');
 
  //check to see that there's actually a string there:
  if (inString.length > 0 ) {
    var sensors = split(inString, ',');            // split the string on the commas
    if (sensors.length > 3) {  
                 // if there are three elements
      pot1 = map(sensors[0], 0, 1023, 0, 255);   // element 0 is the locH
      pot2 = map(sensors[1], 0, 1023, 0, 255);
      pot3 = map(sensors[2], 0, 1023, 0, 255) ;// element 1 is the locV
      button1 = map(sensors[3], 0, 1, 0, 255);
      
    }
  }
}


// print list of ports for debugging
function printList(portList) {
  // portList is an array of serial port names
  for (var i = 0; i < portList.length; i++) {
    // Display the list the console:
  print(i + " " + portList[i]);
   }
}