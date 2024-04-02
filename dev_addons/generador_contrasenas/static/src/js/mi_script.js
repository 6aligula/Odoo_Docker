odoo.define('generador_contrasenas', function(require) {
    'use strict';

    var ajax = require('web.ajax');

    function generarContrasena() {
        var form = document.getElementById('generador_form');
        console.log("llega");
        var formData = new FormData(form);
        ajax.jsonRpc("/generador_contrasenas/generar", 'call', {
            'longitud': formData.get('longitud'),
            'con_digitos': formData.get('con_digitos') ? true : false,
            'con_mayusculas': formData.get('con_mayusculas') ? true : false,
            'con_minusculas': formData.get('con_minusculas') ? true : false,
            'con_simbolos': formData.get('con_simbolos') ? true : false
        }).then(function (data) {
            document.getElementById('contrasena_generada').innerText = 'Contraseña Generada: ' + data.contrasena;
        });
    }

    // Asegúrate de exponer la función para que sea accesible globalmente si se llama desde onclick en tu plantilla
    window.generarContrasena = generarContrasena;
});
