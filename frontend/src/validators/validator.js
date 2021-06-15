function noCaracteresEspeciales(inputtxt){
    var letters = /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/g
    if(inputtxt.match(letters)){
        return true
    }
    return false
}

const noEspacios = (valor) => !valor.includes(" ")

const noNumeros =  (valor) => !(/[0-9]/.test(valor))

const contieneMayuscula = (valor) => !/[A-Z]/.test(valor)

const contieneMinuscula = (valor) => !/[a-z]/.test(valor)

const espositivo = (valor) => (valor >= 0)

function esFuerte(clave){
    var mayuscula = false
    var minuscula = false
    var numero = false
        if(clave.length >= 8){
            for(var i = 0;i<clave.length;i++)
                        {
                            if(clave.charCodeAt(i) >= 65 && clave.charCodeAt(i) <= 90)
                            {
                                mayuscula = true;
                            }
                            else if(clave.charCodeAt(i) >= 97 && clave.charCodeAt(i) <= 122)
                            {
                                minuscula = true;
                            }
                            else if(clave.charCodeAt(i) >= 48 && clave.charCodeAt(i) <= 57)
                            {
                                numero = true;
                            }
                        }
                        if(mayuscula == true && minuscula == true && numero == true)
                        {
                            return true;
                        }
                    }
                    return false
}

function validacionFecha(fecha){
    var fechai = fecha
    var fecha_actual = new Date()
    var mes = (fecha_actual.getMonth()+1).toString()
    if(mes.length <= 1){
        mes = '0' + mes
    }
    var dia = fecha_actual.getDate()
    if(dia.length <= 1){
        dia = '0' + dia
    }
    var fecha_A = fecha_actual.getFullYear().toString()+'-'+mes+'-'+dia
    var limite = '1905-01-01'
    var esFechaFutura = false
    var esFechaLimite = false
    if(fechai >= fecha_A){
        esFechaFutura = true
    }
    if(fechai <= limite){
        esFechaLimite = true
    }
    if(esFechaFutura == true || esFechaLimite == true){
        return false
    }
    return true
}

export {esFuerte,noCaracteresEspeciales,noNumeros,contieneMayuscula,validacionFecha,contieneMinuscula,espositivo,noEspacios}