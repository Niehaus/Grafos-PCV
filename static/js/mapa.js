var map; // mapa
var markers = []; // marcadores dos pontos
var positions = []; // vetor de posicoes 
var distMatrix; // matriz de distancias a pe
var numPoints; // numero de pontos lidos

var latlngbounds; // bounds da tela
var directionsDisplay;
var directionsService;
var distanceService;

function initialize() {	
	directionsDisplay = new google.maps.DirectionsRenderer();
	directionsService = new google.maps.DirectionsService();
    distanceService = new google.maps.DistanceMatrixService(); //request distance matrix

	var latlng = new google.maps.LatLng(-21.0, -44.0); // centraliza o mapa nessas coordenadas

	var options = {
        	zoom: 6,
		    center: latlng,
        	mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map(document.getElementById("mapa"), options);
	directionsDisplay.setMap(map);
	directionsDisplay.setOptions( { suppressMarkers: true } ); // remove marcadores originais das rotas
}

initialize();

function addMarker(ponto){
	var marker = new google.maps.Marker({
		position: new google.maps.LatLng(ponto.Latitude, ponto.Longitude),  // localizacao do marcador
		title: ponto.Descricao,                                             // descricao do marcador
		icon: 'img/marcador.png',                                           // imagem do marcador
        map: map                                                            // coloca marcador no mapa
	});
    
    positions.push(marker.position);

	var myOptions = {
		content: "<p>" + ponto.Descricao + "</p>",
		pixelOffset: new google.maps.Size(-150, 0)
    };

	markers.push(marker); // adicionar marcador no vetor de marcadores
			
	latlngbounds.extend(marker.position); // redimensiona o mapa para caber todos os marcadores
}

function buildResponseFor(index) {
    return function (response, status) {

    	if (status == google.maps.DistanceMatrixStatus.OK) {

        	var origins = response.originAddresses;
       		var destinations = response.destinationAddresses;

        	for (var i = 0; i < origins.length; i++) {
        	    var results = response.rows[i].elements;
        	    for (var j = 0; j < results.length; j++) {
        	        var element = results[j];
        	        var distance = element.distance.value;
        	        var duration = element.duration.text;
        	        var from = origins[i];
        	        var to = destinations[j];
			        console.log();
        	        console.log("node " + index + " - from: " + from);
        	        console.log("node " + j + " - to: " + to);
        	        console.log(distance);
			distMatrix[index][j] = distance;
        	    }
        	}
    	}
    	else {
        	alert("Erro");
    	}
    }
}

function findDistances(n, callback) {

    distMatrix = new Array(numP);
	for (var i = 0; i < numP; i++) {
  		distMatrix[i] = new Array(numP);
	}	

    for (i = 0; i < positions.length; i++) {
        // calcula a matriz de distancias entre todos os pontos a pe de acordo com o google maps
        distanceService.getDistanceMatrix({
            origins: [positions[i]],
            destinations: positions,
            travelMode: google.maps.TravelMode.WALKING,
            unitSystem: google.maps.UnitSystem.METRIC,
            avoidHighways: false,
            avoidTolls: false,
        }, buildResponseFor(i)); 
    }

    setTimeout(function () {
        callback(null, true);
    },1000);
    
}

var download = (function (){
    var a = document.createElement("a");
    document.body.appendChild(a);
    a.style = "display: none";
    return function () {
        var json = JSON.stringify(distMatrix.toString()),
            blob = new Blob([json], {type: "octet/stream"}),
            url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = "distancias.txt";
        a.click();
        window.URL.revokeObjectURL(url);
    };	
}());

function loadCircuit(n, callback) {

    var wayp = [];

    // colocar no vetor wayp todas as paradas intermediarias da rota, menos o marcador da primeira posicao, que sera o inicio e fim da rota do PCV
	for (i = 1; i < markers.length; i++) {
        wayp.push({
        location: markers[i].getPosition(),
        stopover: true
        });        
    }

	var request = { // Novo objeto google.maps.DirectionsRequest, contendo:
		origin: markers[0].getPosition(),           // origem - primeiro marcador
		destination: markers[0].getPosition(),      // destino - retorna para o primeiro marcador
        waypoints: wayp, //                         // pontos intermediarios
      	travelMode: google.maps.TravelMode.WALKING  // meio de transporte, nesse caso, caminhando
   	};
 
   	directionsService.route(request, function(result, status) {
      		if (status == google.maps.DirectionsStatus.OK) { // se OK
        		directionsDisplay.setDirections(result); // renderiza no mapa o resultado
      		}
		    else {
			    alert("fail");
		    }
	});

    setTimeout(function () {
        callback(null, true);
    },1000);
	
}

function carregarPontos(n, callback) {
	numP = 0;
	
	$.getJSON('js/pontos.json', function(pontos) {      // pega os pontos do arquivo
		
		latlngbounds = new google.maps.LatLngBounds();
		
		$.each(pontos, function(index, ponto) {
			// Add marker			
			addMarker(ponto);		                    // adiciona um marcador no mapa para cada ponto do arquivo
			numP++;
	});		
		
	map.fitBounds(latlngbounds);                        // redimensiona o mapa

	
	});

    setTimeout(function () {
        callback(null, true);
    },1000);
	/*setTimeout(function() {
		findDistances();
		}, 1000);

        setTimeout(function() {
		download(distMatrix.toString(), "distancias.txt");
        }, 3000);

        setTimeout(function() {
		loadCircuit();
        }, 5000);*/
}

function encadear() {
    var cadeia = [].slice.call(arguments);
    return function(dadoInicial, end) {
	var fns = cadeia.slice();
        function exec(err, data) {
            if (err) return end(err);
            var next = fns.pop();
            if (!next) return end(null, data);
            next(data, exec);
        }
        exec(null, dadoInicial);
    }
}


var result = encadear(download, loadCircuit, findDistances, carregarPontos);
result(0, function(err, result) {
    console.log(err, result);
});

