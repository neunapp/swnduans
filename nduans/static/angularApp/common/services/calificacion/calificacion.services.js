(function(){
    "use strict"
    angular.module("common.services")
        .factory("calificacionservice",calificacionservice)
        function calificacionservice($http){
          var self = {};

          //servicio que añade una califiacion
          self.calificacion_add = function(json){
            console.log(json);
            return $http.post("/api/calificar/tema/add", json)
                .success(function(res){
                  return '1';
                  //$location.href
                })
                .error(function(res){
                  return '0';
                });
          }

          return self;
        }
}());
