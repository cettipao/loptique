function getDescuento(descuento,subtotal){
    var total_descuento = 0;

    if (descuento.value.toLowerCase().indexOf("f") === (descuento.value.length-1)){
        total_descuento = parseFloat(descuento.value)
    }
    else{
        total_descuento = (parseFloat(descuento.value)*subtotal.value)/100;
    }
    if (isNaN(total_descuento)){
        total_descuento = 0;
        descuento.value = 0;
    }
    return total_descuento;
}

function change_saldo() {
    const subtotal = document.querySelector('#id_sub_total');

    const productos = document.querySelector('#id_productos');
    const productos_texto = productos.nextSibling.textContent;
    var precio_total = 0.00;
    var precio_actual = "";
    var leyendo_precio = false;
    for (i = 0; i < productos_texto.length; i++) {
        if (leyendo_precio) {
            if (productos_texto[i] === ")") {
                precio_total += parseFloat(precio_actual);
                leyendo_precio = false;
                precio_actual = "";
            } else {
                precio_actual += productos_texto[i];
            }
        } else {
            if (productos_texto[i] === "$") {
                leyendo_precio = true;
            }
        }
    }
    subtotal.value = precio_total;

    const seña = document.querySelector('#id_seña');
    const descuento = document.querySelector('#id_descuento');
    const saldo = document.querySelector('.field-saldo');
    const total = document.querySelector('#id_total');
    const total_descuento = getDescuento(descuento,subtotal);
    saldo.innerHTML = " <div><label>Saldo:</label><p>" + (subtotal.value - total_descuento - seña.value) + "</p></div>"
    total.value = (subtotal.value - total_descuento);
}

$(function() {
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
    const total = document.querySelector('#id_total');
    total.addEventListener('change', (event) => {
        change_saldo();
    });
    jQuery('#id_productos').next().on('DOMSubtreeModified', function (e) {
        change_saldo();
    });


})


