//npm install node-libcurl
var Curl = require( 'node-libcurl' ).Curl;
var ip = process.argv[2];
 
var curl = new Curl();

if (!ip) {
	console.log("Usage: node "+process.argv[1]+" ip");
	process.exit();
};

curl.setOpt( 'URL', 'ipinfo.io/'+ip );
curl.setOpt( 'FOLLOWLOCATION', true );
 
curl.on( 'end', function( statusCode, body, headers ) {
 
    console.info( statusCode );
    console.info( '---' );
    console.info(JSON.parse(body));
    console.info( '---' );
    console.info( this.getInfo( 'TOTAL_TIME' ) );
 
    this.close();
});
 
curl.on( 'error', curl.close.bind( curl ) );
curl.perform();
