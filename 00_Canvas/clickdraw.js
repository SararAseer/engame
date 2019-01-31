var c=document.getElementById('slate');
var ctx=c.getContext('2d');
var b=document.getElementById('clear');
c.addEventListener("click", function (evt) {
    var mousePos = getMousePos(c, evt);
    //  ctx.fillRect(mousePos.x,mousePos.y,mousePos.x+10, mousePos.y+10);
    ctx.beginPath();
    if(document.getElementById("1").checked==true){
	ctx.fillRect(mousePos.x,mousePos.y,mousePos.x+10, mousePos.y+10);
    }
    else if(document.getElementById("1").checked==false){
	ctx.ellipse(mousePos.x, mousePos.y, 50, 50, Math.PI / 4, 0, 2 * Math.PI);
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
