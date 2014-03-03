$(document).ready(function(){
	$('.heartbeat')
		.effect('blind', { direction: 'right', mode: 'hide' }, 500)
		.animate({width: 'toggle'});
})