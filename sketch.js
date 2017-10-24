var video;
//Kaleidoscope
function setup() {
 createCanvas(800, 450);
 background(51);
 video = createCapture(VIDEO);
 video.size(800,450);
 angleMode(DEGREES);
 

}

function draw() {
 
  translate(400,height/2);
  
    for(var j= 450; j>=10; j-=50){
tint (255,j/2,0);

for(var i =0;i<=360; i+=30){
  rotate(30);
  image(video,0,0,j,j);
   }
 }

}