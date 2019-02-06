// SoftDev2 pd6
// K#02: Connecting the Dots
// 2019-02-03

// getting variables in order
var c=document.getElementById('slate');
var ctx = c.getContext("2d");
var go = document.getElementById("circle");
var stop = document.getElementById("stop");
var rad=0;
var gro=true;

// clear the canvas, there is no more "last dot"
go.addEventListener('click', function(e){
    gro=true;
    if(rad==10){
	gro=false;
    }
})

stop.addEventListener('click', function(e){
    gro=false;
    if(rad==0){
	gro=true;
    }
})


		    
while(true){
    ctx.clearRect(0, 0, c.width, c.height);
    ctx.ellipse(ctx.width/2,ctx.height/2, rad, rad, Math.PI / 4, 0, 2 * Math.PI);
    if(gro){
	rad++;
    }
    else if(!gro){
	rad--;
    }
}
