(function(){
    "use strict"
    angular.module("common.services")
        .factory("temaservice",temaservice)
        function temaservice($http){
          var self = {};

          //servicio que recupera lista de torneos
          self.listar_temas = function(kword){
            console.log(kword);
            return  $http.get("/api/tema/listar/"+kword+"/");
          }

          //servicio que registra nuevo especialista
          self.add_especialista = function(json){
            console.log(json);
            return $http.post("/api/tema/especialista/save/", json)
          }

          return self;
        }
}());
