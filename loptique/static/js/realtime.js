function change_saldo() {
    const subtotal = document.querySelector('#id_sub_total');
    subtotal.value = (parseFloat(document.querySelector('#id_anteojolejos-0-precio_final_lente').value) +
        parseFloat(document.querySelector('#id_anteojocerca-0-precio_final_lente').value) +
        parseFloat(document.querySelector('#id_multifocal-0-precio_final').value) +
        parseFloat(document.querySelector('#id_anteojolejos-0-precio_final_armazon').value) +
        parseFloat(document.querySelector('#id_anteojolejos-0-precio_final_tratamientos').value) +
        parseFloat(document.querySelector('#id_anteojocerca-0-precio_final_armazon').value) +
        parseFloat(document.querySelector('#id_anteojocerca-0-precio_final_tratamientos').value)
    )

    const seña = document.querySelector('#id_seña');
    const descuento = document.querySelector('#id_descuento');
    const saldo = document.querySelector('.field-saldo');
    const total = document.querySelector('.field-total');
    saldo.innerHTML = " <div><label>Saldo:</label><p>" + (subtotal.value - descuento.value - seña.value) + "</p></div>"
    total.innerHTML = " <div><label>Total:</label><p>" + (subtotal.value - descuento.value) + "</p></div>"
}

function change_lente1() {
    const lente = document.querySelector('#id_anteojolejos-0-precio_lente');
    const descuento = document.querySelector('#id_anteojolejos-0-descuento_lente');
    const final = document.querySelector('#id_anteojolejos-0-precio_final_lente');
    final.value = (lente.value - descuento.value);
    change_saldo();
}

function change_lente2() {
    const lente = document.querySelector('#id_anteojocerca-0-precio_lente');
    const descuento = document.querySelector('#id_anteojocerca-0-descuento_lente');
    const final = document.querySelector('#id_anteojocerca-0-precio_final_lente');
    final.value = (lente.value - descuento.value);
    change_saldo();
}

function change_multifocal() {
    const precio = document.querySelector('#id_multifocal-0-precio');
    const descuento = document.querySelector('#id_multifocal-0-descuento');
    const final = document.querySelector('#id_multifocal-0-precio_final');
    final.value = (precio.value - descuento.value);
    change_saldo();
}

function change_armazon1() {
    const armazon = document.querySelector('#select2-id_anteojolejos-0-armazon-container');
    const precio_armazon = document.querySelector('#id_anteojolejos-0-precio_armazon');
    const descuento_armazon = document.querySelector('#id_anteojolejos-0-descuento_armazon');
    const final_armazon = document.querySelector('#id_anteojolejos-0-precio_final_armazon');
    const nombre_armazon = armazon.textContent
    var precio = parseFloat(nombre_armazon.slice(nombre_armazon.indexOf("$") + 1, nombre_armazon.indexOf(")")));
    precio_armazon.value = precio;
    final_armazon.value = precio - descuento_armazon.value;
    change_saldo();
}

function change_tratamientos1() {
    const tratamientos = document.querySelector('#id_anteojolejos-0-tratamientos');
    const precio_tratamientos = document.querySelector('#id_anteojolejos-0-precio_tratamientos');
    const descuento_tratamientos = document.querySelector('#id_anteojolejos-0-descuento_tratamientos');
    const final_tratamientos = document.querySelector('#id_anteojolejos-0-precio_final_tratamientos');
    const tratamientos_texto = tratamientos.nextSibling.textContent;
    var precio_total = 0.00;
    var precio_actual = "";
    var leyendo_precio = false;
    for (i = 0; i < tratamientos_texto.length; i++) {
        if (leyendo_precio) {
            if (tratamientos_texto[i] === ")") {
                precio_total += parseFloat(precio_actual);
                leyendo_precio = false;
                precio_actual = "";
            } else {
                precio_actual += tratamientos_texto[i];
            }
        } else {
            if (tratamientos_texto[i] === "$") {
                leyendo_precio = true;
            }
        }
    }
    precio_tratamientos.value = precio_total;
    final_tratamientos.value = precio_total - descuento_tratamientos.value;
    change_saldo();
//var precio = parseFloat(nombre_armazon.slice(nombre_armazon.indexOf("$") + 1, nombre_armazon.indexOf(")")));
//precio_armazon.value = precio;
//final_armazon.value = precio - descuento_armazon.value;
}

function change_armazon2() {
    const armazon = document.querySelector('#select2-id_anteojocerca-0-armazon-container');
    const precio_armazon = document.querySelector('#id_anteojocerca-0-precio_armazon');
    const descuento_armazon = document.querySelector('#id_anteojocerca-0-descuento_armazon');
    const final_armazon = document.querySelector('#id_anteojocerca-0-precio_final_armazon');
    const nombre_armazon = armazon.textContent
    var precio = parseFloat(nombre_armazon.slice(nombre_armazon.indexOf("$") + 1, nombre_armazon.indexOf(")")));
    precio_armazon.value = precio;
    final_armazon.value = precio - descuento_armazon.value;
    change_saldo();
}

function change_tratamientos2() {
    const tratamientos = document.querySelector('#id_anteojocerca-0-tratamientos');
    const precio_tratamientos = document.querySelector('#id_anteojocerca-0-precio_tratamientos');
    const descuento_tratamientos = document.querySelector('#id_anteojocerca-0-descuento_tratamientos');
    const final_tratamientos = document.querySelector('#id_anteojocerca-0-precio_final_tratamientos');
    const tratamientos_texto = tratamientos.nextSibling.innerText;
    var precio_total = 0.00;
    var precio_actual = "";
    var leyendo_precio = false;
    for (i = 0; i < tratamientos_texto.length; i++) {
        if (leyendo_precio) {
            if (tratamientos_texto[i] === ")") {
                precio_total += parseFloat(precio_actual);
                leyendo_precio = false;
                precio_actual = "";
            } else {
                precio_actual += tratamientos_texto[i];
            }
        } else {
            if (tratamientos_texto[i] === "$") {
                leyendo_precio = true;
            }
        }
    }
    precio_tratamientos.value = precio_total;
    final_tratamientos.value = precio_total - descuento_tratamientos.value;
    change_saldo();
//var precio = parseFloat(nombre_armazon.slice(nombre_armazon.indexOf("$") + 1, nombre_armazon.indexOf(")")));
//precio_armazon.value = precio;
//final_armazon.value = precio - descuento_armazon.value;
}

$(function() {

    // Add event listener to "price" input
    const seña = document.querySelector('#id_seña');
    seña.addEventListener('change', (event) => {
        change_saldo();
    });
    const subtotal = document.querySelector('#id_sub_total');
    subtotal.addEventListener('change', (event) => {
        change_saldo();
    });
    const descuento_total = document.querySelector('#id_descuento');
    descuento_total.addEventListener('change', (event) => {
        change_saldo();
    });

    const lente = document.querySelector('#id_anteojolejos-0-precio_lente');
    lente.addEventListener('change', (event) => {
        change_lente1();
    });
    const descuento = document.querySelector('#id_anteojolejos-0-descuento_lente');
    descuento.addEventListener('change', (event) => {
        change_lente1();
    });

    const lente2 = document.querySelector('#id_anteojocerca-0-precio_lente');
    lente2.addEventListener('change', (event) => {
        change_lente2();
    });
    const descuento2 = document.querySelector('#id_anteojocerca-0-descuento_lente');
    descuento2.addEventListener('change', (event) => {
        change_lente2();
    });

    const precio_multi = document.querySelector('#id_multifocal-0-precio');
    precio_multi.addEventListener('change', (event) => {
        change_multifocal();
    });
    const descuento_multi = document.querySelector('#id_multifocal-0-descuento');
    descuento_multi.addEventListener('change', (event) => {
        change_multifocal();
    });
    const final_multi = document.querySelector('#id_multifocal-0-precio_final');
    final_multi.addEventListener('change', (event) => {
        change_multifocal();
    });

    /*var armazon = document.querySelector('#select2-id_anteojolejos-0-armazon-container');
    armazon.addEventListener('click', (event) => {
        console.log("VAMA")
        change_armazon1();
    });*/

    jQuery('#select2-id_anteojolejos-0-armazon-container').on('DOMSubtreeModified', function (e) {
        console.log("lee el que puto")
        change_armazon1(); 
    });

    const precio_armazon = document.querySelector('#id_anteojolejos-0-precio_armazon');
    precio_armazon.addEventListener('change', (event) => {
        change_armazon1();
    });
    const descuento_armazon = document.querySelector('#id_anteojolejos-0-descuento_armazon');
    descuento_armazon.addEventListener('change', (event) => {
        change_armazon1();
    });
    const final_armazon = document.querySelector('#id_anteojolejos-0-precio_final_armazon');
    final_armazon.addEventListener('change', (event) => {
        change_armazon1();
    });


    const tratamientos = document.querySelector('#id_anteojolejos-0-tratamientos');
    tratamientos.addEventListener('change', (event) => {
        change_tratamientos1();
    });
    const precio_tratamientos = document.querySelector('#id_anteojolejos-0-precio_tratamientos');
    precio_tratamientos.addEventListener('change', (event) => {
        change_tratamientos1();
    });
    const descuento_tratamientos = document.querySelector('#id_anteojolejos-0-descuento_tratamientos');
    descuento_tratamientos.addEventListener('change', (event) => {
        change_tratamientos1();
    });
    const final_tratamientos = document.querySelector('#id_anteojolejos-0-precio_final_tratamientos');
    final_tratamientos.addEventListener('change', (event) => {
        change_tratamientos1();
    });

    //

    //var armazon2 = document.querySelector('.select2-selection__rendered');


    const precio_armazon2 = document.querySelector('#id_anteojocerca-0-precio_armazon');
    precio_armazon2.addEventListener('change', (event) => {
        change_armazon2();
    });
    const descuento_armazon2 = document.querySelector('#id_anteojocerca-0-descuento_armazon');
    descuento_armazon2.addEventListener('change', (event) => {
        change_armazon2();
    });
    const final_armazon2 = document.querySelector('#id_anteojocerca-0-precio_final_armazon');
    final_armazon2.addEventListener('change', (event) => {
        change_armazon2();
    });


    const tratamientos2 = document.querySelector('#id_anteojocerca-0-tratamientos');
    tratamientos2.addEventListener('change', (event) => {
        change_tratamientos2();
    });
    const precio_tratamientos2 = document.querySelector('#id_anteojocerca-0-precio_tratamientos');
    precio_tratamientos2.addEventListener('change', (event) => {
        change_tratamientos2();
    });
    const descuento_tratamientos2 = document.querySelector('#id_anteojocerca-0-descuento_tratamientos');
    descuento_tratamientos2.addEventListener('change', (event) => {
        change_tratamientos2();
    });
    const final_tratamientos2 = document.querySelector('#id_anteojocerca-0-precio_final_tratamientos');
    final_tratamientos2.addEventListener('change', (event) => {
        change_tratamientos2();
    });
})


