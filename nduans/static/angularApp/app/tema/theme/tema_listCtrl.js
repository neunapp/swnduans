(function(){
    "use strict";
    angular.module("DuansApp")
        .controller("TemaListCtrl", ['temaservice','calificacionservice','$http', TemaListCtrl]);

    function TemaListCtrl(temaservice,calificacionservice){
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

        //listamos top de especialistas
        self.lista_especilistas = function(){
          //peticion al servidor
          calificacionservice.top_7_specialist()
            .then(function(response){
              self.especialistas = response.data;
              console.log(self.especialistas);
            });
        }
  }
}());
