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
            if self.pets[pet_name]['energy'] >= 0:
                energy_loss = distance / 2
                new_energy = self.pets[pet_name]['energy'] - energy_loss
                if new_energy <= 0:
                    self.pets[pet_name]['energy'] = 0
                    self.pets[pet_name]['state'] = 'Muerto'
                    self.print_result(f'{pet_name}, Muy tarde. Ya me mori.')
                else:
                    self.pets[pet_name]['energy'] = new_energy
                    self.print_result(f'{pet_name} corrio {distance} metros. Ahora mi energia es {new_energy}')
            else:
                self.print_result(f'{pet_name}, Muy tarde. Ya me mori.')
        else:
            print(f'Error: El gato {pet_name} no existe.')

    def eat(self, pet_name, mouse_weight):
        if pet_name in self.pets:
            if self.pets[pet_name]['energy'] >= 0:
                new_energy = self.pets[pet_name]['energy'] + 12 + mouse_weight
                self.pets[pet_name]['energy'] = new_energy
                self.print_result(f'{pet_name}, Gracias. Ahora mi energia es {new_energy}')
            else:
                self.print_result(f'{pet_name}, Muy tarde. Ya me mori.')
        else:
            print(f'Error: El gato {pet_name} no existe.')

    def play(self, pet_name, minutes):
        if pet_name in self.pets:
            if self.pets[pet_name]['energy'] >= 0:
                energy_loss = minutes * 0.1
                new_energy = self.pets[pet_name]['energy'] - energy_loss
                if new_energy <= 0:
                    self.pets[pet_name]['energy'] = 0
                    self.pets[pet_name]['state'] = 'Muerto'
                    self.print_result(f'{pet_name}, Muy tarde. Ya me mori.')
                else:
                    self.pets[pet_name]['energy'] = new_energy
                    self.print_result(f'{pet_name}, Gracias por jugar conmigo. Ahora mi energia es {new_energy}')
            else:
                self.print_result(f'{pet_name}, Muy tarde. Ya me mori.')
        else:
            print(f'Error: El gato {pet_name} no existe.')

    def print_summary(self, pet_name):
        if pet_name in self.pets:
            name = pet_name
            energy = self.pets[pet_name]['energy']
            pet_type = self.pets[pet_name]['type']
            state = 'Vivo' if energy > 0 else 'Muerto'
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
                state = 'Vivo' if energy > 0 else 'Muerto'
                dot.node(pet_name, f'{pet_name}\nEnergia: {energy}\nTipo: {pet_type}\nEstado: {state}')
            dot.render('mascotas', format='png', cleanup=True)
            self.print_result(dot.source)
        except Exception as e:
            self.print_result(f'Error al generar el grafico: {str(e)}')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    command, *params = line.strip().split(': ')
                    if command == 'Crear_Gato':
                        pet_name = params[0]
                        self.create_pet(pet_name)
                    elif command == 'Resumen_Mascota':
                        pet_name = params[0]
                        self.print_summary(pet_name)
                    elif command == 'Dar_de_Comer':
                        pet_name, mouse_weight = params[0].split(', ')
                        self.eat(pet_name, int(mouse_weight))
                    elif command == 'Jugar':
                        pet_name, minutes = params[0].split(', ')
                        self.play(pet_name, int(minutes))
        except Exception as e:
            self.print_result(f'Error al cargar el archivo: {str(e)}')

    def print_result(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('.petworld_result', 'a') as file:
            file.write(f'[{timestamp}] {message}\n')