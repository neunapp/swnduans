(function(){
    "use strict";
    angular.module("DuansApp")
        .controller("ThemeSpecialistListCtrl", ['temaservice','$http',ThemeSpecialistListCtrl]);

    function ThemeSpecialistListCtrl(temaservice){
        var self = this;

        self.busqueda = false;

        //listamos themas publicados de un especialista
        self.lista_themas = function(){
          //peticion al servidor
          temaservice.listar_temas_especialista()
            .then(function(response){
              self.temas = response.data;
            });
        }
  }
}());
