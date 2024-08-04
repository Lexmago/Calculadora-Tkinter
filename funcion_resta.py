import re

def resta(entry):
    op = entry # Recibirá una entrada, el valor de self.display_current_value
    nums = re.findall(r'\d+',op)# Buscará los numeros separados por -
    nums = [int(num) for num in nums]# Los convierte a entero
    
    if not nums:
        return 0 # Evita bugs
    
    r = nums[0] # Tambien para evitar bugs

    for num in nums[1:]: # Aqui surge la magia, ignora el primer valor para que ese sea el restado
        r -= num # cada iteración realiza un decremento al primer valor

    return r # Devuelve el resultado de la resta