# Object oriented programming

## Tic Tac Toe
### Principal class.
In this part we can see how the functions on the code and of other objects are called in the main class to execute the game and use the properties for each of classes, for example the function "verificarGanador" and as you can see, we need to put the variable with that function is executed.
````Java
package tateti;

public class Tateti {

    public static void main(String[] args) {
        Ficha fichaX = new Ficha("X");
        Ficha fichaO = new Ficha();
        fichaO.setFicha("O");
       
        Jugador jugadorX = new Jugador(fichaX);
        Jugador jugadorO = new Jugador();
        jugadorO.setFicha(fichaO);
               
        Tablero tablero = new Tablero();
        tablero.imprimir();
        boolean ganador = false;
        for (int veces = 1; veces <= 9; veces++) {
            if(veces%2==0){
                jugadorO.ponerFicha(tablero);
                ganador = tablero.verificarGanador(jugadorO);
            }else{
                jugadorX.ponerFicha(tablero);
                ganador = tablero.verificarGanador(jugadorX);
            }
            tablero.imprimir();
            if(ganador){
                break;
            }
        }
        if(ganador){
            System.out.println("HAZ GANADO!!!");
        }else{
            System.out.println("VUELVE A INTENTARLO!!!");
        }  
    }
}
````
### Class to make the board and check the winner.
````Java
package tateti;

public class Tablero {
    private String[][] tablero;

    public Tablero() {
        tablero = new String[3][3];
        limpiar();
    }

    public Tablero(String[][] tablero) {
        this.tablero = tablero;
    }
   

    public String[][] getTablero() {
        return tablero;
    }

    public void setTablero(String[][] tablero) {
        this.tablero = tablero;
    }
   
    public void limpiar(){
        for (int f = 0; f < tablero.length; f++) {
            for (int c = 0; c < tablero[0].length; c++) {
                tablero[f][c] = " ___ ";
            }
        }
    }
   
    public void imprimir(){
        for (int f = 0; f < tablero.length; f++) {
            for (int c = 0; c < tablero[0].length; c++) {
                System.out.print(tablero[f][c]);
            }
            System.out.println("");
        }
    }
   
    public boolean verificarGanador(Jugador jugador){
        boolean valor = false;
        String ficha1 = " _"+jugador.getFicha().getFicha()+"_ ";
        String ficha3 = ficha1+ficha1+ficha1;
        String fila = tablero[0][0]+tablero[0][1]+tablero[0][2];
        //System.out.println("-->"+ficha3);
        //System.out.println("-->"+ficha1);
        if( ficha3.equals(fila)){
            valor  = true;
        }
        fila = tablero[1][0]+tablero[1][1]+tablero[1][2];
        if( ficha3.equals(fila)){
            valor  = true;
        }
         fila = tablero[2][0]+tablero[2][1]+tablero[2][2];
        if( ficha3.equals(fila)){
            valor  = true;
        }
         String columna = tablero[0][0]+tablero[1][0]+tablero[2][0];
        if( ficha3.equals(columna)){
            valor  = true;
        }
         columna = tablero[0][1]+tablero[1][1]+tablero[2][1];
        if( ficha3.equals(columna)){
            valor  = true;
        }
         columna = tablero[0][2]+tablero[1][2]+tablero[2][2];
        if( ficha3.equals(columna)){
            valor  = true;
        }
        String diagonal = tablero[0][0]+tablero[1][1]+tablero[2][2];
        if( ficha3.equals(diagonal)){
            valor  = true;
        }
         diagonal = tablero[2][0]+tablero[1][1]+tablero[0][2];
        if( ficha3.equals(diagonal)){
            valor  = true;
        }
        return valor;
    }
}

````
### Class to make the players.
````Java
package tateti;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Jugador {
    private Ficha ficha;

    public Jugador() {
    }

    public Jugador(Ficha ficha) {
        this.ficha = ficha;
    }

    public Ficha getFicha() {
        return ficha;
    }

    public void setFicha(Ficha ficha) {
        this.ficha = ficha;
    }
   
    public void ponerFicha(Tablero tablero){
        try {
            InputStreamReader isr = new InputStreamReader(System.in);
            BufferedReader br = new BufferedReader (isr);
            System.out.print("Fila   : ");
            int fila = Integer.parseInt(br.readLine());
            System.out.print("Columna: ");
            int columna = Integer.parseInt(br.readLine());
            tablero.getTablero()[fila][columna] = " _"+this.ficha.getFicha()+"_ ";
        } catch (IOException ex) {
            Logger.getLogger(Jugador.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
````
### Class to make the chips.
````Java
package tateti;
// Beans
public class Ficha {
    private String ficha;

    public Ficha() {
    }

    public Ficha(String ficha) {
        this.ficha = ficha;
    }

    public String getFicha() {
        return ficha;
    }

    public void setFicha(String ficha) {
        this.ficha = ficha;
    }  
}
````
