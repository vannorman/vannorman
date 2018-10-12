var	buffer = 250;
var tabs = []
var buttons = []
var lastTop = 0;
$(window).scroll(function(e){
	var top = $(window).scrollTop();
	var dt = top - lastTop;	 // were we scrolling up or down?
	lastTop = top;
	currentTab = "";
	$('.tab_button').each(function(){
		if ($(this).parent().hasClass('selected')){
			currentTab = $(this).attr('id').replace("button_","");
		}
	});

	// For each tab, if you're scrolling and pass a threshhold away from that tab, swap to the other tab
	for (i in tabs) {
		var thisTab = tabs[i].attr('id').replace("tab_","");
		if (thisTab == currentTab){
			if (i < tabs.length - 1) {
				nextTabTop =  tabs[parseInt(i)+1].offset().top;
			} else if (i > 0) {
				nextTabTop =  tabs[parseInt(i)].offset().top;
			}
			if (i < tabs.length - 1 && dt > 0 && top > nextTabTop - buffer){
				HighlightTab(buttons[parseInt(i)+1]);
			} else if (i > 0 && dt < 0 && top < tabs[parseInt(i)].offset().top - buffer * 2){
				HighlightTab(buttons[parseInt(i)-1]);
			} else {
				console.log("top;"+top+", next top:"+nextTabTop);
			}
		} else {
//			console.log("thistab:"+thisTab+", curtab:"+currentTab);
		}
	}
	return;	

});
var navBtn = "#navLinks ul li .inner";
$(document).ready(function(){
	$('.tab').each(function(){ tabs.push($(this))});

	$('.tab_button').each(function(){ buttons.push($(this))});
	for (i in tabs){
		console.log("added "+i+":"+tabs[i].attr('id'));
	}
	//	tabs = ['tab_about','tab_portfolio','tab_contact'];
//	for (i in tabs){
//		t = tabs[i];
//		console.log(t+': '+$('#'+t).offset().top);
//	}
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

