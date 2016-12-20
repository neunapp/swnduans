(function(){
    "use strict"
    angular.module("common.services")
        .factory("temaservice",temaservice)
        function temaservice($http){
          var self = {};

          //servicio que recupera lista de temas por buscador
          self.listar_temas = function(kword){
            console.log(kword);
            return  $http.get("/api/tema/listar/"+kword+"/");
          }

          //servicio que lista temas de un especiaista
          self.listar_temas_especialista = function(){
            return  $http.get("/api/especialista/listar-temas/");
          }

          //servicio que registra nuevo especialista
          self.add_especialista = function(json){
            console.log(json);
            return $http.post("/api/tema/especialista/save/", json)
          }

          //servicio que registra nuevo tema
          self.add_tema = function(json){
            console.log(json);
            return $http.post("/api/tema/save/", json)
          }

          return self;
        }
}());
