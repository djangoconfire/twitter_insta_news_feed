var google_map
var markers = []
var news_feeds = []
var feeds = []

$(function(){
	$('.refresh').hide()
	$('#search-form').submit(function(event){
		event.preventDefault();
		deleteMarkers()
		$('.refresh').show()
		// location.reload()
		var form_data=$(this).serializeArray();
		form_data = JSON.stringify(form_data);
		
		console.log(form_data);
		
		
		$('#loading-modal').modal('show')
		$('.feed-container').empty()
		$.ajax({
	           	url:'/search/tweets/',
	           	type:'post',
	            data:{form_data:form_data},
	            success: function(data){
	            	$.each(data, function(i, result){	
					news_feeds.push({
					src: 'twitter',
					feed: result.text,
					epoch: result.date,
					geo: result.geo,
					date: new Date(result.date),
					image: result.image
					})

					$.each(news_feeds, function(i, result){
					var counter = 0	
	        		if(counter < 20){
	        			if(result.geo){
	        				counter++;
	        				var latlng = new google.maps.LatLng(result.geo.coordinates[0],result.geo.coordinates[1])
	        			
	        				var marker = new google.maps.Marker({
						    position: latlng,
						    title: "News Feed",
						    maxWidth: 100
						})
						
						var feeds = new google.maps.feeds({
							content: contentString(result.feed)
						})

						marker.addListener('click', function() {	
							closeAllfeeds()						
							feeds.open(google_map, marker)
						})

						feeds.push(feeds)

						markers.push(marker)
	        			}
	        		}
	        			$('.feed-container').append(newsfeed(result))
	        		})

						console.log(news_feeds)
	       				showMarkers()
						$('#loading-modal').modal('hide')
	        	})

	        	},
	    		error: function(err){
					$('#loading-modal').modal('hide')
	    			console.log(err)
	    		}
					 })
				})
			})
	 
	    		


function closeAllfeeds(){
	for (var i=0; i < feeds.length; i++){
		feeds[i].close()
	}
}

function contentString(feed){
	res = '<div>' + feed + '</div>'
	return res
}

function setMapOnAll(map) {
	for (var i = 0; i < markers.length; i++) {
		markers[i].setMap(map)
	}
}

function clearMarkers() {
	setMapOnAll(null)
}

function showMarkers() {
	setMapOnAll(google_map)
}

function deleteMarkers() {
	clearMarkers()
	markers = []
}

function initMap() {
	var center = {lat: 51.5033640, lng: -0.1276250}
	var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 1,
		center: center
	})
	google_map = map
}



function newsfeed(feed){
	res = '<div class="col-sm-10 col-sm-offset-1 feed">'
		+ '<blockquote class="blockquote ' + feed.src + '-blockqoute">'
		+ '<div class="row">'
		+ '<div class="col-sm-12 date">'
		+  '</div>'
	if(feed.image != undefined){
		res += '<div class="col-sm-12 text-center">'
			+ '<image class="feed-image" src="'+ feed.image +'">'
			+ '</div>'
	}
	res += '<div class="col-sm-12 text-justify">'
		+ feed.feed
		+ '</div>'
		+ '<div class="col-sm-12 text-right source text-capitalize ' + feed.src + '">'
		+ feed.src
		+ '</div>'
		+ '</div>'
		+ '</blockquote>'
		+ '</div>'

	return res
	}	

		            	

	                    
	 