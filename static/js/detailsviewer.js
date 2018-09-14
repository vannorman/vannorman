$(document).ready(function(){
	$('#detailsOverlay').click(function(e){
		if (e.target  == this){
			DETAILS_VIEWER.Hide();
		}
	});
});

var DETAILS_VIEWER = {
	Show : function (text) {
		$('#imageOverlay').fadeIn("fast");
	}, Hide : function () {
		$('#imageOverlay').fadeOut("fast");
	}
}

