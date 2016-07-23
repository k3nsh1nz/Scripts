//npm install node-libcurl
var Curl = require( 'node-libcurl' ).Curl;
 
var curl = new Curl();
 
curl.setOpt( 'URL', 'ipinfo.io/8.8.8.8' );
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
