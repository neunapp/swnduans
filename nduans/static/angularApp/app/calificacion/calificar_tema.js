(function(){
    "use strict";
    angular.module("DuansApp")
        .controller("CalificarTemaCtrl", ['calificacionservice','$http', CalificarTemaCtrl]);

    function CalificarTemaCtrl(calificacionservice){
        var self = this;
        self.puntaje = 1;

        self.calificar_tema = function(tema){
          //generamos json
          var json = {
            'theme':tema,
            'point':self.puntaje,
          }
          calificacionservice.calificacion_add(json);
        }
    }
}());
