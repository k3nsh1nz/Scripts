var http = require('http');
var start = new Date();

var site = process.argv[2];
if (process.argv.length < 3) {
	console.log("Usage: "+process.argv[0]+" "+ process.argv[1] + " site.com");
} else{
	http.get({host: site, port: 80}, function(res) {
		console.log('Response time site:', new Date() - start, 'ms');
	});
};
