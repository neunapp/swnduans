(function(){
    "use strict";
    angular.module("DuansApp")
        .controller("SearchCtrl", ['$http', SearchCtrl]);

    function SearchCtrl($http){
        var self = this;

        self.busqueda = false;

        self.resultados_busqueda = function(){
          self.busqueda = true;
          console.log(self.busqueda);
        }
    }
}());
