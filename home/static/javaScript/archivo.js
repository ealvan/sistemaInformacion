
function consulta() {
    var mes = 2; //1 = enero, 2.... [4 meses]
    var digitos = 2; // los que decida 1 - 8
    var ulr = 'http://127.0.0.1:8000/rpta/?var1=' + mes + '&var2=' + digitos;
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
