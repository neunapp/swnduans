(function(){
    "use strict";
    angular.module("DuansApp")
        .controller("TemaAddCtrl", ['$rootScope', '$scope','temaservice','NgEditor','$http', TemaAddCtrl]);

    function TemaAddCtrl($rootScope, $scope,temaservice,NgEditor){
        var self = this;

        //variables globales
        self.publicado = false;

        //inicializacion ng-editor
        $scope.doc = {content: 'escriba texto aqui'};
		    $scope.editor = new NgEditor({
			    top: 0,
			    uploadHeaders: {
				    'Authorization': 'Bearer ' + '',
				    'uid': ''
			    }
		    });

        //listamos top de especialistas
        self.agregar_tema = function(flat){
          if (flat) {
            self.publicado = true;
          }
          else {
            self.publicado = false;
          }
          //creamos el json kwords
          var kword = {
            'name':self.kword,
          };
          //json principal para tema
          var json = {
            'title':self.title,
            'description':self.description,
            'key_words':kword,
            //'category':'1',
            'content':$scope.doc.content,
            'publicado':self.publicado,
          }
          //enviamos los datos al servidor
          console.log(temaservice.add_tema(json));
          //proceso completado
          //window.location.href = '/mensaje-confirmacion/';
        }
  }
}());
