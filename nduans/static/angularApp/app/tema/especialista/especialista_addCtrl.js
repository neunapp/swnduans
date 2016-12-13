(function(){
    "use strict";
    angular.module("DuansApp")
        .controller("AddEspecialistaCtrl", ['temaservice','$window',
                    AddEspecialistaCtrl]);

    function AddEspecialistaCtrl(temaservice,$window,$timeout, Cropper){
        var self = this;

        //inicializsmos valores para api localizacion
        self.address = {
          name: '',
          components: {
            placeId: '',
            street: '',
            city: '',
            state: '',
            countryCode: '',
            country: '',
            district: '',
          }
        };

        //validamos datos e torneo
        self.validar_especialista = function(){
          //personalizamos la fechas
          console.log('validar');
        }


        //metodo para guadar los datos de un especialista
        self.crear_especialista = function(){
          //validar datos
          self.validar_especialista();
          //creamos json para Location
          var location = {
            'name':self.address.name,
            'location_id': self.address.components.placeId,
            'street': self.address.components.street,
            'city': self.address.components.city,
            'state': self.address.components.state,
            'country_short': self.address.components.countryCode,
            'country': self.address.components.country,
            'district': self.address.components.district,
          }
          //creamos json para usuario
          var usuario = {
            'email':self.usuario.email,
            'first_name':self.usuario.first_name,
            'last_name':self.usuario.last_name,
            'phone':self.usuario.phone,
            'gender':self.usuario.gender,
          }
          //creamos json para especialidad
          var especialist = {
            'user':usuario,
            'location':location,
            'specialty':self.specialty,
            'date_birth':self.date_birth,
            'description':self.description,
          };
          //ejecutamos el POST
          console.log(temaservice.add_especialista(especialist));
          //si el proceso se completa correctamente
          window.location.href = '/mensaje-confirmacion/';
        }
    }
}());
