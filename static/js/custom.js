// custom.js
// Getting Public Feed from Flickr (Photos, Titles etc)


$('#search_button').click( function(){

	// Removing old feed
	$('#feed_portion').html('');

	var flickerAPI = 'http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?';
    $.getJSON( flickerAPI, {
        tags: $('#tags').val(),
        tagmode: 'any',
        format: 'json',
        AccessControlAllowOrigin: '*'
    
    }).done(function( data ) {
        $.each( data.items, function( i, item ) {

            // Generating feed with photos on home page (Based on Search)
            $('#feed_portion').append('\
				<div class="feedimage">' + item['description'] + '\
		       </div>\
			');

        });
    });
});