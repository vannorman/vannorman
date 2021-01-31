$(document).ready(function(){
	$('#vimeoPopupContainer').on('click',function(){
		VIMEO_OVERLAY.Hide();
		
	});
});

var VIMEO_OVERLAY = {
	moving : false,
	showing : false,
	Hide : function() {
		if (this.moving || !this.showing) return;
		VIMEO_OVERLAY.moving = true;
		$('#vimeoPopup').animate({ height : '0', width: '0'},500,function(){ 
			console.log('finished closing!');
			VIMEO_OVERLAY.moving = false;
			VIMEO_OVERLAY.showing = false;  
			$('#vimeoPopupContainer').hide();
			$('#vimeo_iframe').attr('src','');
		});
		enableScroll();
	}, Show : function(src){
		if (this.moving || this.showing) return;
		disableScroll();
		VIMEO_OVERLAY.moving = true;
		console.log('showing');
//		$('#vimeo_iframe').attr('src',src+"?api=1");	
		$('#vimeoPopupContainer').show();
		$('#vimeoPopup').html("<iframe id='vimeo_iframe' src='"+src+"?title=1&amp;byline=1&amp;portrait=1&amp;autoplay=true'; frameborder='0' webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>"); // re-init the html for autoplay
		w = window.innerWidth * .65;
		h = w * 540 / 960;
		$('#vimeoPopup iframe').width(w).height(h); 
		$('#vimeoPopup').animate({ height: h+"px", width: w+'px'},1100,function(){ 
			console.log('finished opening!');
			VIMEO_OVERLAY.moving = false; 
			VIMEO_OVERLAY.showing = true;
			console.log('this.showing:'+VIMEO_OVERLAY.showing);
		});
	}

}

	
	


