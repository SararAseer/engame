var c=document.getElementById('slate');
var ctx=c.getContext('2d');
var b=document.getElementById('clear');
c.addEventListener("click", function (evt) {
    var mousePos = getMousePos(c, evt);
    //  ctx.fillRect(mousePos.x,mousePos.y,mousePos.x+10, mousePos.y+10);
    ctx.beginPath();
    if(document.getElementById("1").checked==true){
	ctx.fillRect(mousePos.x,mousePos.y,10,10);
    }
    else if(document.getElementById("1").checked==false){
	ctx.ellipse(mousePos.x, mousePos.y, 1, 1, Math.PI / 4, 0, 2 * Math.PI);
    }
    ctx.stroke();
});

b.addEventListener("click", function () {
   ctx.clearRect(0, 0, c.width, c.height);
});
function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    }
}
/*
preventDefault()
Eliminates the default function of an object(ex button,checkbox,form). After clicking a button once where the preventDefault() function is triggered, that buttons functionality would become mute.

beginPath()
Saves the point at which you are drawing lines. It is like if Mario walked down the map, the game would start with beginPath() and save the last position he was at before starting another beginPath()

e.offsetX
Gives the x-position of the mouse at the instance it is clicked, based on the screen which is a grid of pixels.

e.offsetY
Gives the y-position of the mouse at the instance it is clicked , based on the screen which is a grid of pixels.
*/
