document.onkeydown = checkKey;
var $div;
var x;
var y;




$(document).ready(function(){

	$(document).mousemove(function(e) {
		x = e.pageX;
		y = e.pageY;
	})

//	$(document).click(function(e) {
//	    var target = $(e.target);	
//		$div = target;
//		console.log('target:'+JSON.stringify($div));
//		document.onkeydown = checkKey;

//	});
});

var col = "rgb(100,100,100)";


function modColor(color, index, increment){
	var regExp = /\(([^)]+)\)/;
	var matches = regExp.exec(color);

	
	//matches[1] contains the value between the parentheses
	var colors = matches[1].split(',');
	var oldColor = parseInt(colors[index]);
	console.log('old:'+oldColor+', index:'+index);
	var newColor =	oldColor + increment;
	console.log('colors:'+JSON.stringify(colors));
	colors[index] = newColor
	return "rgb("+colors[0]+","+colors[1]+","+colors[2]+")";
		
}

function checkKey(e) {

    elementMouseIsOver = document.elementFromPoint(x, y);
	$div = $(elementMouseIsOver);
    e = e || window.event;
	sign = -1;
	var increment = 25;
	oldColor =$div.parent().css('background-color') ;
	if (event.shiftKey){
		sign = 1;
	}
	rgb = -1; // R == 0, G == 1, B == 2
	switch(e.keyCode){
		
		// R
		case 82: /* R */	rgb = 0;					break;		
		case 71: /* G */	rgb = 1;					break;		
		case 66: /* B */	rgb = 2;					break;

		case 49: /* 1 */	SineCanvas.bubble(10,10);	break;	
		case 50: /* 2 */	SetColor('rgb(0,145,0');	break;	
		case 51: /* 3 */	SetColor('rgb(0,165,0');	break;	
		case 52: /* 4 */	SetColor('rgb(0,185,0');	break;	
		case 53: /* 5 */	SetColor('rgb(255,125,0');	break;	
		case 54: /* 6 */	SetColor('rgb(235,105,0');	break;	
		case 55: /* 7 */	SetColor('rgb(205,85,0');	break;	
		case 56: /* 8 */	SetColor('rgb(185,65,0');	break;	
		case 57: /* 9 */	SetColor('rgb(255,0,255');	break;	
		case 48: /* 0 */	SetColor('rgb(125,0,125');	break;	
		default:
			break;
    }
	if (rgb != -1){
		$div.parent().css('background-color', modColor(oldColor,rgb,increment*sign));

	}
	console.log("new color :"+$div.parent().css('background-color'));

}

function SetColor(color){
	$div.parent().css('background-color', color);
	
}

// Obtient une interpolation linéaire entre 2 valeurs
Math.lerp = function (value1, value2, amount) {
	var delta = value2 - value1;
	return value1 + delta * amount/60;
};
