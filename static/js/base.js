var lastTop = 0;
$(window).scroll(function(e){
	var top = $(window).scrollTop() + 50;
	var dt = top - lastTop;	 // were we scrolling up or down?
	lastTop = top;
	if (dt < 0){
		top += $(window).height(); // if scrolling up, add a buffer
	}
	if (top > $('#tab_contact').offset().top){
		HighlightTab($('#button_contact'));
	} else if (top > $('#tab_portfolio').offset().top){
		HighlightTab($('#button_portfolio'));
	} else {
		HighlightTab($('#button_about'));
	}
});
var navBtn = "#navLinks ul li .inner";
$(document).ready(function(){
	$(navBtn).on('click',function(){
		HighlightTab($(this));
		switch($(this).attr('id')){
			case 'button_about': 
				ScrollTo('#tab_about');
				break;
			case 'button_portfolio': 
				ScrollTo('#tab_portfolio');
				break;
			case 'button_vrar': 
				ScrollTo('#tab_vrar');
				break;
			case 'button_contact': 
				ScrollTo('#tab_contact');
				break;
		}
	}); 
});

function HighlightTab($this){
	$(navBtn).each(function(){
		$(this).parent().removeClass('selected');
	});
	$this.parent().addClass('selected');

}

function ScrollTo(div){
	$('html, body').animate({scrollTop:$(div).offset().top}, 400);
}

