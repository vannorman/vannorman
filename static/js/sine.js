$(document).ready(function(){
	SineCanvas.init();
	$('#top ul li').mouseover(function(){
		SineCanvas.effectiveSpeed = 3.5;
	})
});
var color = "rgba(255,125,0,0.2)";
var SineCanvas = {
	speed : 0.2,
	effectiveSpeed : 0.2,
	frequency : 20,
	step : -4,
	color : "rgba(255,125,0,0.2)",
	bubbleColor : "rgba(255,255,255,0.5)",
	plotSine : function (ctx, xOffset, yOffset) {
		var width = ctx.canvas.width;
		var height = ctx.canvas.height;
		var scale = 20;
		ctx.beginPath();
		ctx.lineWidth = 0;
		ctx.strokeStyle = color; 
		var x = 4;
		var y = 0;
		var amplitude = 28;
		var leftOffset = 6;
		var cutoffSlope = 24;
		var yOffset = 20;
		while (x < width) {
			var dx = (x+xOffset)/SineCanvas.frequency ;
			y = height/2 + yOffset + amplitude * Math.sin(dx);
			y2 = 150 + (-x * cutoffSlope + ctx.canvas.width/2)    ; // slant, but not needed with overlfow hidden
			if (y < y2){
				y = y2;
			}
			ctx.lineTo(x-leftOffset, y);
			ctx.lineTo(x-leftOffset,ctx.canvas.height);
				
			x++;
		}
		if (SineCanvas.speed != SineCanvas.effectiveSpeed) {
			SineCanvas.effectiveSpeed = Math.lerp(SineCanvas.effectiveSpeed,SineCanvas.speed,2);
//			console.log('ef:'+SineCanvas.effectiveSpeed);
		}
		ctx.stroke();
	}, draw : function () {
		var canvas = document.getElementById("canvas");
		var context = canvas.getContext("2d");
		context.clearRect(0, 0, 500, 500);
		SineCanvas.plotSine(context, SineCanvas.step, 50);
		SineCanvas.step -= SineCanvas.effectiveSpeed;
//		SineCanvas.bubbles(context);	
		window.requestAnimationFrame(SineCanvas.draw);
	}, init : function () {
		window.requestAnimationFrame(SineCanvas.draw);

//	}, bubbles : function (ctx) {
//		ctx.strokeStyle = "rgb(0,0,255)";// SineCanvas.bubbleColor;
//		ctx.fillRect(10,10,10,50); // fill in the pixel at (10,10)
			
	}

}


