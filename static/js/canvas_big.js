$(document).ready(function(){
	BigCanvas.init();
	$('#top ul li').mouseover(function(){
		BigCanvas.effectiveSpeed = 3.5;
	})
});
var colors = {
	gray : "rgba(50,50,50,0.5)",
	darkGray : "rbga(25,25,25,0.5)",
	lightGray : "rgba(100,100,100,0.5)",
};
var BigCanvas = {
	speed : 0.2,
	effectiveSpeed : 0.2,
	frequency : 20,
	step : -4,
	color : "rgba(255,125,0,0.2)",
	bubbleColor : "rgba(255,255,255,0.5)",
	DrawBlocks : function (ctx) {
		var width = ctx.canvas.width;
		var height = ctx.canvas.height;
		var blockWidth = 25;
		var g = 255;
		for (i=0;i<width/blockWidth;i++){
			g -= 10;
			for (j=0;j<height/blockWidth;j++){
				if (i % 2 == 0 && j % 2 == 0 || i%2 == 1 && j%2 == 1){
					ctx.fillStyle = "rgba("+g+","+g+","+g+",1)"; 
				} else {
					ctx.fillStyle = "rgba("+g*1.2+","+g*1.2+","+g*1.2+",1)"; 
				}
				ctx.fillRect(j*blockWidth,i*blockWidth,blockWidth,blockWidth);
			}	
		}
	}, draw : function () {
		var canvas = document.getElementById("canvas_big");
		canvas.width = 2000;
		canvas.height = 2000;
		var context = canvas.getContext("2d");
		BigCanvas.DrawBlocks(context);
	}, init : function () {
		window.requestAnimationFrame(BigCanvas.draw);
	}

}



