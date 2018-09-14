$(document).ready(function(){
	$('#imageOverlay, .currentImage, .x').click(function(e){
		if (e.target  == this){
			IMAGE_VIEWER.Hide();
		}
	});
});

var IMAGE_VIEWER = {
	Show : function (el) {
		$('#imageOverlay').fadeIn("fast");
		IMAGE_VIEWER.SetImage(el);
		disableScroll();
	}, Hide : function () {
		$('#imageOverlay').fadeOut("fast");
		enableScroll();
	}, SetImage : function (el) {
		var $el = $(el);
		console.log('el2 name:'+$el.find('.img').css('background-image'));
		var bgi = $el.find('.img').css('background-image');
		console.log('%c BGI:'+bgi,'color:#009');
		$('#imageOverlay .currentImage').css('background-image',bgi);
	}
}
