var pic = document.getElementById('vimage');
var clear_button = document.getElementById('but_clear');

var ox = -1;
var oy = -1;

function addDot(event){
  var edge = pic.getBoundingClientRect();
  var x = event.clientX - edge.left;
  var y = event.clientY - edge.top;

  var c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  c.setAttribute("cx",x);
  c.setAttribute("cy",y);
  c.setAttribute("r",25);
  c.setAttribute("fill","red");
  c.setAttribute("stroke","black");

  pic.appendChild(c);

  if (ox != -1){
    var line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', ox);
    line.setAttribute('x2', x);
    line.setAttribute('y1', oy);
    line.setAttribute('y2', y);
    line.setAttribute('stroke', 'black');
    pic.appendChild(line);
  }
  ox = x;
  oy = y;
}

function clearPic(){
  while (pic.lastChild) {
    pic.removeChild(pic.lastChild);
  }
  ox = -1
  oy = -1
}
