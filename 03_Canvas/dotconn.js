// SoftDev2 pd6
// K#02: Connecting the Dots
// 2019-02-03

// getting variables in order

var c=document.getElementById('playground');
var ctx = c.getContext("2d");
var go = document.getElementById("circle");
var stop = document.getElementById("stop");
var rad=0;
var gro=true;
var stops=true;
var t=true;
// clear the canvas, there is no more "last dot"
go.addEventListener('click', function(e){
    stops=false;
    go.disabled=true;
    stop.disabled=false;
    begin();
})

stop.addEventListener('click', function(e){
    stops=true;
    go.disabled=false;
    stop.disabled=true;
    window.cancelAnimationFrame(begin);
   
})
function begin() {
    if(!stops){
	if(gro){
	    rad++;
	}
	else if(!gro){
	    rad--;
	}
	if(rad<=0){
	    gro=true;
	}
	else if(rad>=(c.width-2)/2){
	    gro=false;
	}
	ctx.beginPath();
	ctx.fillStyle = "rgba(255, 255, 255,.9)";
	ctx.border="none";
	ctx.ellipse(c.width/2,c.height/2, rad, rad, Math.PI / 4, 0, 2 * Math.PI);
	ctx.lineWidth = 1;
	ctx.stroke();
	ctx.fill();
    }
    requestAnimationFrame(begin);
}



