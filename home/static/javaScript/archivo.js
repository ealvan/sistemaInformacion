
function consulta() {
    var ulr = 'http://127.0.0.1:8000/rpta/';
    console.log(ulr);
    var datos;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            datos = JSON.parse(this.responseText);
            render(datos);
        }
    };
    xhttp.open("GET",ulr,true);
    xhttp.send();
}

function consulta2() {
    var ulr = 'http://127.0.0.1:8000/queryRecibidos/';
    console.log(ulr);
    var datos;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            datos = JSON.parse(this.responseText);
            render(datos);
        }
    };
    xhttp.open("GET",ulr,true);
    xhttp.send();
}

function render(datos) {
    var table = "<table id='answere1'>";
    var row = datos[0];
    table += '<tr>';
    for(key in row){
        table += '<th>';
        table += key;
        table += '</th>';
    }
    table += '</tr>';
    for(var i in datos){
        table += '<tr>';
        row = datos[i];
        for(key in row){
            table += '<td>';
            table += row[key];
            table += '</td>';
        }
        table += '</tr>';
    }
    table += "</table>";
    console.log(table)
    document.getElementById("answere1").innerHTML = table;
}
