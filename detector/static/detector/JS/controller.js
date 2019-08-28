function test(){
	return "Hello world"
}

var canvasWidth = "280";
var canvasHeight = "280";
var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var paint;


var canvasDiv = document.getElementById('canvasDiv');
canvas = document.createElement('canvas');
canvas.setAttribute('width', canvasWidth);
canvas.setAttribute('height', canvasHeight);
canvas.setAttribute('id', 'canvas');
canvas.setAttribute("style","border-style:solid");
// canvas.setAttribute("style","background-color:black");
canvasDiv.appendChild(canvas);
if(typeof G_vmlCanvasManager != 'undefined') {
	canvas = G_vmlCanvasManager.initElement(canvas);
}
context = canvas.getContext("2d");


// Set background Color
context.fillStyle = 'rgb(0, 0, 0)';
context.fillRect(0, 0, 280, 280);

$('#canvas').mousedown(function(e){
  var mouseX = e.pageX - this.offsetLeft;
  var mouseY = e.pageY - this.offsetTop;

  paint = true;
  addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
  redraw();
});

$('#canvas').mousemove(function(e){
  if(paint){
    addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
    redraw();
  }
});

$('#canvas').mouseup(function(e){
  paint = false;
});

$('#canvas').mouseleave(function(e){
  paint = false;
});

function addClick(x, y, dragging)
{
  clickX.push(x);
  clickY.push(y);
  clickDrag.push(dragging);
}


function download(){

  var download = document.getElementById("download");
  var image = document.getElementById("canvas").toDataURL("image/png").replace("image/png", "image/octet-stream");
  download.setAttribute("href", image);

}



function redraw(){
  context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas
	// Set background Color
	context.fillStyle = 'rgb(0, 0, 0)';
	context.fillRect(0, 0, 280, 280);
  context.strokeStyle = 'rgb(255, 255, 255)';
		// Add behind elements.
	context.globalCompositeOperation = 'source-over'
	// Now draw!
  context.lineJoin = "round";
  context.lineWidth = 5;

  for(var i=0; i < clickX.length; i++) {
    context.beginPath();
    if(clickDrag[i] && i){
      context.moveTo(clickX[i-1], clickY[i-1]);
     }else{
       context.moveTo(clickX[i]-1, clickY[i]);
     }
     context.lineTo(clickX[i], clickY[i]);
     context.closePath();
     context.stroke();
  }
}
function Clear(){
  context.clearRect(0, 0, canvas.width, canvas.height);
  clickX = new Array();
  clickY = new Array();
  clickDrag = new Array();
}
