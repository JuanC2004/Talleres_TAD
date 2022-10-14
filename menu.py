'''
Author: Juan Camilo Quintero
Date: 14/10/22
Language: Python 3.0
'''

from SingleLinkedList import SingleLinkedList
from DoubleLinkedList import DoubleLinkedList
from colorama import *
init()

inst_Sll = SingleLinkedList()
inst_Dll = DoubleLinkedList()

class menu:

    def menu():
        aux = input(Fore.CYAN + 'Ingrese la letra a si desea realizar listas simplemente enlazadas\n Ingrese la letra b si desea realizar listas doblemente enlazadas\n Ingrese la letra c si desea salir: ')
        if aux == 'a':
            print('Se ha elegido single Linked List')
            aux1 = input('Ingrese una letra entre a y f segun lo que desea realizar: ')
            if(aux1 == 'a'):
                print('Se a elegido insetrar nodo')
                aux2 = int(input(Fore.GREEN + 'Ingrese un numero del 1 al 3: '))
                if(aux2 == 1):
                    print('Se ha elegido insertar nodo al inicio')
                    inst_Sll.unshift_node(1)
                elif(aux2 == 2):
                    print('Se ha elegido insertar nodo al final')
                    inst_Sll.push_node(2)
                elif(aux2 == 3):
                    print('Se ha elegido insertar nodo en una posicion especifica')
                    n = int(input(Fore.LIGHTMAGENTA_EX + 'Ingrese la posicion en la que se desea insertar el nodo'))
                    inst_Sll.insert_node(n,3)
            elif(aux1 == 'b'):
                print('Se ha elegido eliminar nodo')
                aux2 = int(input('Ingrese un numero del 1 al 3: '))
                if(aux2 == 1):
                    print('Se ha elegido eliminar nodo al inicio')
                    inst_Sll.shift_node()
                elif(aux2 == 2):
                    print('Se ha elegido eliminar nodo al final')
                    inst_Sll.pop_node()
                elif(aux2 == 3):
                    print('Se ha elegido eliminar un nodo en una posicion especifica')
                    n = int(input('Ingrese la posicion del nodo a eliminar: '))
                    inst_Sll.remove_node(n)
            elif(aux1 == 'c'):
                print('Se ha elegido consultar valor de un nodo')
                n = int(input('Ingrese la posicion del nodo a consultar: '))
                inst_Sll.get_node_value(n)
            elif(aux1 == 'd'):
                print('Se ha elegido modificar el valor de un nodo')
                n = int(input('Ingrese la posicion del nodo a modificar'))
                n1 = int (input('Ingrese el nuevo valor del nodo: '))
                inst_Sll.update_node_value(n,n1)
            elif(aux1 == 'e'):
                print('Se ha elegido invertir la lista')
                inst_Sll.reverse()
            elif(aux == 'f'):
                print('Se ha elegido validacion especial')
        elif aux == 'b':
            print('Se ha elegido Double Linked List')
        elif aux == 'c':
            print('Se ha elegido cerrar el programa')