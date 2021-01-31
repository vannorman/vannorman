$(document).ready(function(){
	$('#muvIcon').on('click',function(){
		ZANCHAT.ToggleUserVoiceWindow();
	});
	$('#muvSubmit').on('click',function(e){
	
		ajaxFormSubmit(e,'#muvForm','/myuservoice/report/',function(response){
			ZANCHAT.ToggleUserVoiceWindow();
			$('#id_message').val('');
		});
	});
	$('#muvOverlay').on('click',function(){
		ZANCHAT.ToggleUserVoiceWindow();
	});
	$(document).on('click','#muvForm > #inputs > input',function(){
		$('.error').each(function(){
			$(this).remove();
		});
	});
		 	
});

var ZANCHAT = {

	showing : false,
	
	ToggleUserVoiceWindow : function (){
		if (!ZANCHAT.showing){
			ZANCHAT.Show();
		} else {
			ZANCHAT.Hide();
		}
		ZANCHAT.showing = !ZANCHAT.showing;
	}, Show : function () {
		$('#muvIcon').css('pointer-events','none');
		$('#muvWindow').fadeIn("fast");
		$('#muvOverlay').show();

	}, Hide : function (){
		$('#muvIcon').css('pointer-events','auto');
		$('#muvWindow').fadeOut("slow");
		$('#muvOverlay').hide();
	}
}



