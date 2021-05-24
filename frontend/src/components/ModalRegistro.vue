<template>
<transition name="modal-fade">
    <div class="modal-backdrop">
        <div class="modal">
        <header class="modal-header">
            <slot name="header">
            AGREGAR USUARIO
            </slot>
            <button
            type="button"
            class="btn-close"
            @click="close"
            >
            x
            </button>
        </header>

        <section class="modal-body">
            <slot name="body">
                    <label>Nombre:</label>
                    <br>
                    <input type="text" name="nombre" id="nombre"  autocomplete="off">
                    <br>
                    <label>Apellido:</label>
                    <br>
                    <input type="text" name="apellido" id="apellido"  autocomplete="off">
                    <br>
                    <label>Fecha Nacimiento:</label>
                    <br>
                    <input type="date" name="fecha" id="fecha" >
                    <br>
                    <label for="">Usuario:</label>
                    <br>
                    <input type="text" name="usuario" id="usuario"  autocomplete="off">
                    <br>
                    <label for="">Contraseña</label>
                    <br>
                    <input type="text" name="" id="">
                    <br>
                    <label for="">Tipo Usuario</label>
                    <br>
                        <select name="" id="">
                            <option value="">ADMINISTRADOR</option>
                            <option value="">PACIENTE</option>
                            <option value="">FUNCIONARIO</option>
                        </select>
            </slot>
        </section>

        <footer class="modal-footer">
            <button id="agregar" >AGREGAR USUARIO</button>
        </footer>
        </div>
    </div>
    </transition>
</template>

<script>
    export default {
        name: 'Modal',
        methods: {
        close() {
            this.$emit('close');
        },
        },
    };
    </script>
        <style>
    .modal-backdrop {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: rgba(0, 0, 0, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .modal {
        height: 600px;
        width: 500px;
        background: #FFFFFF;
        box-shadow: 2px 2px 20px 1px;
        overflow-x: auto;
        display: flex;
        flex-direction: column;
    }

    .modal-header,
    .modal-footer {
        padding: 25px;
        display: flex;
    }

    .modal-header {
        position: relative;
        border-bottom: 1px solid #eeeeee;
        color: #4AAE9B;
        justify-content: space-between;
    }

    .modal-footer {
        border-top: 1px solid #eeeeee;
        flex-direction: column;
        justify-content: flex-end;
    }

    .modal-body {
        color: black;
        position: relative;
        padding: 30px 10px;
        text-align: left;
    }
    .modal-body input{
        padding: 10px;
        width: 90%;
    }
    .modal-body select{
            font-family: 'Karla', sans-serif;
            font-size: 15px;
            padding: 10px;
            width: 90%;
    }
    .btn-close {
        position: absolute;
        top: 0;
        right: 0;
        border: none;
        font-size: 20px;
        padding: 10px;
        cursor: pointer;
        font-weight: bold;
        color: #4AAE9B;
        background: transparent;
    }

    .btn-green {
        color: white;
        background: #4AAE9B;
        border: 1px solid #4AAE9B;
        border-radius: 2px;
    }
    #agregar{
        background-color: rgb(20, 149, 158);
        color: white;
        border: none;
        padding: 20px;
        border-radius: 6px;
        font-family: 'Karla', sans-serif;
        font-size: 15px;
    }
    .modal-fade-enter,
    .modal-fade-leave-to {
        opacity: 0;
    }

    .modal-fade-enter-active,
    .modal-fade-leave-active {
        transition: opacity .3s ease;
    }
</style>