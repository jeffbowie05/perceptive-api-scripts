var request = require('request');
	
var oauth2_url = 'https://auth.psft.co/oauth/token';

function getAccessToken ( client_id, client_secret, username, password, callback ) {
	
	request({
		uri: oauth2_url,
		method: 'POST',
		form: {	
			grant_type: 'password', 
			client_id: client_id, 
			client_secret: client_secret,	
			username: username,	
			password: password 
		
		}
	}, tokenRequestResponse ( callback ));
	
}

function tokenRequestResponse ( callback ) { 

	return function ( error, response ) {
		
		if ( !error && response.statusCode == 200) { 
			// Send our data back to caller.
			callback ( JSON.parse(response.body).access_token );
		}
		else { 
			console.log('Error: ' + response.statusCode); 
		}
		
	}
}

exports.getAccessToken = getAccessToken;