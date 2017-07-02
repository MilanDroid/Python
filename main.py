import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

'''
este es un comentario
de varias líneas
'''
#Esto es un método o función
def fib(n):
 #Esto inicializa variables
 a, b = 0, 1
 #Esto es un bucle while
 while a < n:
 #Esto imprime en pantalla
 print(a, end=' ')
 a, b = b, a+b
 print()
#Esto finaliza la función y manda a llamar la misma
fib(1000)