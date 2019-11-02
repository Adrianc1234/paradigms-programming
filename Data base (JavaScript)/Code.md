# DATA BASE (JavaScript)
## Introduction.
This is a project where we can see how a basic Data Base works in JavaScript. this Data Base has these functions: `Read`, `Edit`, `Delete`, `update`. It is a basic way to make a Data Base and is a good way to start with JavaScript and understand the functional programming and how java works.

You can run this code here: [Compiler](https://playcode.io/466577?tabs=script_DataBase.js,preview,console).
## Code.
````JavaScript
//EDITAR
class Persona {
  constructor (nombre, edad, dir) {
    this.name = nombre;
    this.age = edad;
    this.ip = dir;
  }
````
````
  // obtener datos de una persona
  get  datos ()   {
     return this.obtener_datos();
   }
  // Método nombre
  obtener_datos () {
    return this.name;
    return this.edad;
    return this.ip;
  }

  //obtener promedio de edades
  get   promedio  ()   {
     return this.mean();
   }
  // Método
  mean () {
    var i;
     var prome = 0;
     for(i=0 ; i < 3; i++){
      prome = prome + edad[i]
      prome = prome / 5
     }
     console.log("This is the mean of the Ages: "+ prome)
  }
  //leemos todos los datos
  get Datos () {
    return this.lecture();
  }
//metodo de lectura de todos los datos
  lecture () {
    var i;
    for(i = 0; i < 3; i++) {
    console.log("Estos son los datos de " + names[i] + ": " )
    console.log("name: " + names[i])
    console.log("edad: " + edad[i])
    console.log("IP:" + IP[i]+"\n")
    }
  }

  // Eliminar
  get   elimination  ()   {
     return this.del(val);
   }
  // Método eliminar
  del (val) {
    var pos = names.indexOf(val);
    names.splice(pos,1)
    console.log("Nombres: " + names)
    edad.splice(pos,1)
    console.log("Edades" + edad)
    IP.splice(pos,1)
    console.log("IP:" + IP)
  }
  // este es para añadir a una persona
  get addition() {
    return this.add();
  }
  //funcion añadir
  add() {
    names.unshift(N_name);
    edad.unshift(N_age);
    IP.unshift(N_ip);
    console.log("ASI ESTA LA BASE DE DATOS")
    console.log("Lista de nombres: "+ names)
    console.log("Lista de IP: " + IP)
    console.log("Lista de edades: " + edad)
  }


  //este es para editar un dato
  get edit() {
    return this.editing()
  }

  //metodo de edicion
  editing(){
    console.log("Esta es la persona que deseas editar: "+ N_dname)
    pos = names.indexOf(N_dname)
    names[pos] = N_dname
    edad[pos] = N_dage
    IP[pos] = N_dip
    console.log("LOS NUEVOS DATOS DE "+ N_dname+" SON: ")
    console.log("Nombre: " + names[pos])
    console.log("Edad: " + edad[pos])
    console.log("IP: " + IP[pos])
  }

  //actualizar las edades
  get update() {
    return this.act();
  }
  //funcion para actualizar edades
  act() {
    var list = []
    console.log("Edades actuales: " + edad)
    edad.forEach(function(element) {
    var new_a = element + years;
    list.unshift(new_a);
    });
    edad = list
    edad = edad.reverse()
    console.log("Estos son las nuevas edades al pasar "+ years + " años: ")
    console.log(edad)
  } 
}

//listas
var names = ['Adrian', 'Liss','Hector'];
var edad = [19,15,16];
var IP = [124,123,125];
//parametros para user.
const user = new Persona (names, edad, IP );

//ver el promedio
console.log("mean:" + user.promedio +"\n")

//ver a las personas en la base de datos
console.log(user.Datos)

//eliminar a persona en la base de datos Var
//nombre que queremos borrar
var val = 'Adrian'; 
console.log("RESULTADOS DE LA ELIMINACION")
console.log(user.elimination)

//agregar a persona
var N_name = 'luis';
var N_age = 12;
var N_ip = 124
console.log("RESULTADOS DE LA AGREGACION.")
console.log(user.addition)

//editar un dato en especifico
var N_dname = "Luis";
var N_dage= 21;
var N_dip = 2001;
console.log("EDICION DE UN DATO")
console.log(user.edit)

//actualizar edades si ya paso un año
console.log("ACTUALIZACION DE EDADES")
var years = 2;
console.log(user.update)
````
