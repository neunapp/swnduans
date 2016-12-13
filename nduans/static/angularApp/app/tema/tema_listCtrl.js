(function(){
    "use strict";
    angular.module("DuansApp")
        .controller("TemaListCtrl", ['temaservice','$http', TemaListCtrl]);

    function TemaListCtrl(temaservice){
        var self = this;

        self.busqueda = false;

        self.resultados_busqueda = function(){
          if (self.buscar.length > 2) {
            self.busqueda = true;
          }
          //peticion al servidor
          temaservice.listar_temas(self.buscar)
            .then(function(response){
              self.temas = response.data;
            });
        }
  }
}());
