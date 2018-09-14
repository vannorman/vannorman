$(document).ready(function(){
	SetRandomBackground();
	$(window).scroll(function(){
		$('#top').css('background-position-y',(window).top());
	});
});	
function SetRandomBackground(){
	backgrounds = [
		'10327891.jpg',
		'168176.jpg',
		'608185.jpg',
		'732326783_preview_72cd26e14b7fcba028206a06f10548c0d5174cfc.jpg',
		'7b9.jpg',
		'7cb4156ebb88e4bfc6729129fdfa614b.jpg',
		'7xqz3QX.jpg',
		'80s_retro_game_over_wallpaper_by_leepiin-d9phs9b.png',
		'Outdrive-Review-Screenshot-Wallpaper-Neon-City.jpg',
		'aventador_1393358829_600x375.jpg',
		'big_1471700794_image.jpg',
		'cG6STRJ.jpg',
		'grand-theft-auto-v-1920x1080-sunset-city-hd-5980.jpg',
		'lamborghini-countach-poster-2.jpg',
		'logo.png',
		'm4uwhyR.jpg',
		'unnamed.jpg',
		'virgin_atlantic_romain_trystram_shanghai_dribbble.jpg'
	]

	var index = Math.floor(Math.random() * backgrounds.length);
	var bgsource = '/static/img/backgrounds/' + backgrounds[index];
	$('#top').css('background-image','url("'+bgsource+'")');
}

