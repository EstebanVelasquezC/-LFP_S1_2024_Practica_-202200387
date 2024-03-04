import datetime
from graphviz import Digraph

class PetManager:
    def __init__(self):
        self.pets = {}

    def create_pet(self, pet_name):
        self.pets[pet_name] = {'energy': 0, 'type': 'Gato', 'state': 'Vivo'}
        self.print_result(f'Se creo el gato {pet_name}')

    def run(self, pet_name, distance):
        if pet_name in self.pets:
            # Verifica si el gato está vivo
            if self.pets[pet_name]['energy'] >= 0:
                # Implementa la lógica para correr y actualizar la energía
                energy_loss = distance / 2
                new_energy = self.pets[pet_name]['energy'] - energy_loss
                self.pets[pet_name]['energy'] = max(0, new_energy)
                if new_energy <= 0:
                    self.pets[pet_name]['state'] = 'Muerto'
                    self.print_result(f'{pet_name}, Muy tarde. Ya me morí.')
                else:
                    self.print_result(f'{pet_name} corrió {distance} metros. Ahora mi energía es {new_energy}')
            else:
                self.print_result(f'{pet_name}, Muy tarde. Ya me morí.')
        else:
            print(f'Error: El gato {pet_name} no existe.')

    def eat(self, pet_name, mouse_weight):
        if pet_name in self.pets:
            # Verifica si el gato está vivo
            if self.pets[pet_name]['energy'] >= 0:
                # Calcula la nueva energía después de comer
                new_energy = self.pets[pet_name]['energy'] + 12 + mouse_weight
                self.pets[pet_name]['energy'] = new_energy
                self.print_result(f'{pet_name}, Gracias. Ahora mi energía es {new_energy}')
            else:
                self.pets[pet_name]['state'] = 'Muerto'
                self.print_result(f'{pet_name}, Muy tarde. Ya me morí.')
        else:
            print(f'Error: El gato {pet_name} no existe.')

    def play(self, pet_name, minutes):
        if pet_name in self.pets:
            # Verifica si el gato está vivo
            if self.pets[pet_name]['energy'] >= 0:
                # Calcula la nueva energía después de jugar
                energy_loss = minutes * 0.1
                new_energy = self.pets[pet_name]['energy'] - energy_loss
                self.pets[pet_name]['energy'] = max(0, new_energy)
                if new_energy <= 0:
                    self.pets[pet_name]['state'] = 'Muerto'
                    self.print_result(f'{pet_name}, Muy tarde. Ya me morí.')
                else:
                    self.print_result(f'{pet_name}, Gracias por jugar conmigo. Ahora mi energía es {new_energy}')
            else:
                self.print_result(f'{pet_name}, Muy tarde. Ya me morí.')
        else:
            print(f'Error: El gato {pet_name} no existe.')

    def print_summary(self, pet_name):
        if pet_name in self.pets:
            name = pet_name
            energy = self.pets[pet_name]['energy']
            pet_type = self.pets[pet_name]['type']
            state = 'Vivo' if energy >= 0 else 'Muerto'
            self.print_result(f'{name}, Energia: {energy},{pet_type},{state}')
        else:
            print(f'Error: El gato {pet_name} no existe.')

    def print_global_summary(self):
        self.print_result('--------Resumen Global --------')
        for pet_name in self.pets:
            self.print_summary(pet_name)
        self.print_result('----------------------------------------------------------')
        self.generate_graph()

    def generate_graph(self):
        try:
            dot = Digraph(comment='Mascotas')
            for pet_name, pet_info in self.pets.items():
                energy = pet_info['energy']
                pet_type = pet_info['type']
                state = 'Vivo' if energy >= 0 else 'Muerto'
                dot.node(pet_name, f'{pet_name}\nEnergia: {energy}\nTipo: {pet_type}\nEstado: {state}')
            dot.render('mascotas', format='png', cleanup=True)
            self.print_result(dot.source)
        except Exception as e:
            self.print_result(f'Error al generar el gráfico: {str(e)}')

    def print_result(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('.petworld_result', 'a') as file:
            file.write(f'[{timestamp}] {message}\n')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    self.process_command(line.strip())
        except Exception as e:
            self.print_result(f'Error al cargar el archivo: {str(e)}')

    def process_command(self, command):
        # Implementa la lógica para procesar cada comando según el formato del archivo
        pass