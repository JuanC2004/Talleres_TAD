'''
Author: Juan Camilo Quintero
Date: 14/10/22
Language: Python 3.0
'''
import math

class SingleLinkedList:
    #*Creamos una clase anidada en SingleLinkedList
    class Node:
        #*Creamos el método inicializador de la clase
        def __init__(self, value):
            #*Definimos la estructura de un nodo
            self.value = value
            self.next = None
    #*Metodo inicializador de la clase SingleLinkesList
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    #*Método que imprime el contenido de la lista simplemente enlazada
    def show_info_sll(self):
        node_list = []
        current_node = self.head
        #*Recorremos la lista hasta que no existan nodos
        while(current_node != None):
            #*A la lista node_list le agregamos al final el value del nodo visitado
            node_list.append(current_node.value)
            current_node = current_node.next
        print(f'{node_list} Cantidad de nodos {self.length}')

    #*Método que agrega un nodo nuevo al INICIO de la lista
    def unshift_node(self, value):
        aux = self.scroll_list(value)
        if(aux == False):
            new_node = self.Node(value)
            #*Consultar si la lista NO tiene head y tail
            if self.head == None and self.tail == None:
                #*En este caso la lista esta vacía, no contiene nodos
                self.head = new_node
                self.tail = new_node
            else:
                #*En este caso, la lista contiene al menos un nodo
                #*Para este caso habría que enlazar el nodo nuevo con la head de la lista
                new_node.next = self.head
                #*Actualizar la head de la lista
                self.head = new_node
            self.length += 1
        elif(aux == True):
            print('El valor ya se encuentra en la lista')

    #*Añadir nodo al final de la lista
    def push_node(self, value):
        aux = self.scroll_list(value)
        if aux == False:
            #*El nuevo nodo toma la estructura de Nodo
            new_node = self.Node(value)
            #*Validar si la lista esta vacía
            if self.head == None and self.tail == None:
                self.head = new_node
                self.tail = new_node
            else:
                #*Creamos el enlace de la tail actual de la lista con el nuevo nodo
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1
        elif aux == True:
            print('El valor ya se encuentra en la lista')

    #*Eliminar nodo al inicio de la lista
    def shift_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            #*Actualizamos el nombre de la cavbeza con la var aux remove_node
            remove_node = self.head
            #*Actualizamos la cabeza de la lista
            self.head = remove_node.next
            #*Eliminamos el enlace de remove_node con la lista
            remove_node.next = None
            self.length -=1
    
    #*Eliminar último nodo de la lista
    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            #*Cuando llega al nodo que actualmente es la cola de la lista
            new_tail = current_node
            while(current_node.next != None):
                new_tail = current_node
                current_node = current_node.next
            self.tail = new_tail
            #*Desvinculamos la cola anterior de la lista
            self.tail.next = None
            self.length -=1
            
    #*Obtener nodo
    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node
        
    #*Obtener el valor del nodo
    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print('No se encontro')
        elif index == 1:
            print(self.head.value)
        elif index == self.length:
            print(self.tail.value)
        else:
            current_node = self.head
            node_counter = 1
            #*Validar que el nodo a consultar sea el mismo del contador
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            print(current_node.value)
            
    #*Actualizar el valor del nodo
    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            #*Encontro el nodo y se puede actualizar
            search_node.value = new_value
        else:
            #*No encuentra el nodo
            return None
        
    #*Eliminar nodo
    def remove_node(self, index):
        if index == 1:
            self.shift_node()
        elif index == self.length:
            self.pop_node()
        else:
            remove_node = self.get_node(index)
            if remove_node!= None:
                previous_node = self.get_node(index - 1)
                previous_node.next = remove_node.next
                remove_node.next = None
                
    #*Insertar nodo
    def insert_node(self, index, value):
        aux = self.scroll_list(value)
        if aux == False:
            if index <= 0  or index > self.length+1:
                print('posicion erronea')
            elif index == 1:
                self.unshift_node(value)
            elif index == self.length+1:
                self.push_node(value)
            else: 
                previous_node = self.get_node(index-1)
                new_node = self.Node(value)
                next_node = previous_node.next
                previous_node.next = new_node
                new_node.next = next_node
                self.length +=1
        elif aux == True:
            print('El valor ya se encuentra en la lista')
            
    #*Invertir lista
    def reverse(self):
        i = 1
        tamaño = self.length-1
        while i <=  tamaño:
            self.insert_node(i,self.tail.value)
            self.pop_node()
            i+=1 

    def scroll_list(self, value):
        current_node = self.head
        node_counter = 1
        aux = False
        while(node_counter != self.length and aux != True):
            if current_node.value == value:
                aux = True
            current_node = current_node.next
            node_counter += 1
        return aux   
    
    def new_validation2(self):
        self.reverse()
        current_node = self.head
        node_counter = 1
        while(node_counter != self.length):
            current_node = math.sqrt(current_node.value)
            current_node = current_node.next
            node_counter += 1