
function consulta() {
    var mes = document.getElementById("id_categoria").value; //1 = enero, 2.... [4 meses]
    var digitos = document.getElementById("numero_digitos").value; // los que decida 1 -
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
    var table = "<table class='datatable'";
    var row = datos[0];
    table += '<tr>';
    for(key in row){
        table += '<th>';
        /*if(key[0]==[i]){
            key[0] =="debe";
            table += key;
        }else{

        }*/
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

