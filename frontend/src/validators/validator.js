
const noCaracteresEspeciales = (valor) => !(/\W|_/.test(valor.replace(' ', '')))

const noNumeros =  (valor) => !(/[0-9]/.test(valor))

const contieneMayuscula = (valor) => !/[A-Z]/.test(valor)

const contieneMinuscula = (valor) => !/[a-z]/.test(valor)

function esFuerte(clave){
    var mayuscula = false
    var minuscula = false
    var numero = false
    var caracter_raro = false
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
                            else
                            {
                                caracter_raro = true;
                            }
                        }
                        if(mayuscula == true && minuscula == true && caracter_raro == true && numero == true)
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

export {esFuerte,noCaracteresEspeciales,noNumeros,contieneMayuscula,validacionFecha,contieneMinuscula}