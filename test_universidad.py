from enum import Enum

class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

class Sexo(Enum):
    MASCULINO = 1
    FEMENINO = 2

class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre
        self._estudiantes = []
        self._asociados = []
        self._titulares = []
        self._investigadores = []
### DAR DE ALTA PERSONAS
    def añadir_estudiante(self, nombre, DNI, direccion, sexo):
        for e in self._estudiantes:
            if e.DNI == DNI:
                print('Este alumno ya esta dado de alta.')
                return

        self._estudiantes.append(Estudiante(nombre, DNI, direccion, sexo))
    
    def añadir_profesor_asociado(self, nombre, DNI, direccion, sexo, departamento):
        for a in self._asociados:
            if a.DNI == DNI:
                print('Este profesor ya esta dado de alta.')
                return
        self._asociados.append(Profesor_asociado(nombre, DNI, direccion, sexo, departamento))

    def añadir_profesor_titular(self, nombre, DNI, direccion, sexo, departamento, area_investigacion):
        for t in self._titulares:
            if t.DNI == DNI:
                print('Este profesor ya esta dado de alta.')
                return
        self._titulares.append(Profesor_titular(nombre, DNI, direccion, sexo, departamento, area_investigacion))  
        self._investigadores.append(Investigador(nombre, DNI, direccion, sexo, departamento, area_investigacion))

    def añadir_investigador(self, nombre, DNI, direccion, sexo, departamento, area_investigacion):
        for i in self._investigadores:
            if i.DNI == DNI:
                print('Este investigador ya esta dado de alta.')
                return
        self._investigadores.append(Investigador(nombre, DNI, direccion, sexo, departamento, area_investigacion))
### ELIMINAR PERSONAS
    def eliminar_estudiante(self, DNI):
        for i in range(len(self._estudiantes)):
            if self._estudiantes[i].DNI == DNI:
                self._estudiantes.pop(i)
                print('El estudiante ha sido borrado.')
                return
        print('El DNI no corresponde con ningún estudiante matriculado.')

    def eliminar_asociado(self, DNI):
        for i in range(len(self._asociados)):
            if self._asociados[i].DNI == DNI:
                self._asociados.pop(i)
                print('El profesor asociado ha sido eliminado.')
                return
        print('El DNI no corresponde con ningún profesor asociado.')
    def eliminar_titular(self, DNI):
        for i in range(len(self._titulares)):
            if self._titulares[i].DNI == DNI:
                self._titulares.pop(i)
                print('El profesor titular ha sido eliminado.')
                return
        print('El DNI no corresponde con ningún profesor titular.')     

    def eliminar_investigador(self, DNI):
        for i in self._investigadores:
            if i.DNI == DNI:
                self._investigadores.remove(i)
                for t in self._titulares:
                    if t.DNI == DNI:
                        self._titulares.remove(t)
                        print('El investigador ha sido eliminado tanto como investigador como profesor titular.')
                        return
                print('El investigador ha sido eliminado.')
                return
        print('El DNI no corresponde con ningún investigador.')
### LISTAR PERSONAS
    def listar_estudiantes(self):
        print('LISTADO ESTUDIANTES')
        for e in self._estudiantes:
            print('\t', e.devolver_datos())

    def listar_asociados(self):
        print('LISTADO ASOCIADOS')
        for a in self._asociados:
            print('\t', a.devolver_datos())

    def listar_titulares(self):
        print('LISTADO TITULARES')
        for t in self._titulares:
            print('\t', t.devolver_datos())

    def listar_investigadores(self):
        print('LISTADO INVESTIGADORES')
        for i in self._investigadores:
            print('\t', i.devolver_datos())
### ASIGNATURAS MATRICULADAS
    def añadir_asignatura_matriculada(self, estudiante, asignatura):
        for e in self._estudiantes:
            if e.DNI == estudiante:
                e.añadir_asignatura(asignatura)
                return
        print('Este DNI no corresponde a ningun estudiante.')

    def eliminar_asignatura_matriculada(self, estudiante, asignatura):
        for e in self._estudiantes:
            if e.DNI == estudiante:
                e.eliminar_asignatura(asignatura)
                return
        print('Este DNI no corresponde a ningun estudiante.')
    
    def listar_asignaturas_matriculadas(self, estudiante):
        for e in self._estudiantes:
            if e.DNI == estudiante:
                e.listar_asignaturas()
                return
        print('Este DNI no corresponde a ningun estudiante.') 
### ASIGNATURAS IMPARTIDAS
    def añadir_asignatura_impartida(self, profesor, asignatura):
        for a in self._asociados:
            if a.DNI == profesor:
                a.añadir_asignatura(asignatura)
                return
        for t in self._titulares:
            if t.DNI == profesor:
                t.añadir_asignatura(asignatura)
                return
        print('Este DNI no corresponde a ningun profesor.')

    def eliminar_asignatura_impartida(self, profesor, asignatura):
        for a in self._asociados:
            if a.DNI == profesor:
                a.eliminar_asignatura(asignatura)
                return
        for t in self._titulares:
            if t.DNI == profesor:
                t.eliminar_asignatura(asignatura)
                return
        print('Este DNI no corresponde a ningun profesor.')

    def listar_asignaturas_impartidas(self, profesor):
        for a in self._asociados:
            if a.DNI == profesor:
                a.listar_asignaturas()
                return
        for t in self._titulares:
            if t.DNI == profesor:
                t.listar_asignaturas()
                return
        print('Este DNI no corresponde a ningun profesor.')      
### DEPARTAMENTO
    def cambiar_dpt(self, DNI, dpt_nuevo):
        for a in self._asociados:
            if a.DNI == DNI:
                if a.departamento == dpt_nuevo:
                    print('Esta persona ya pertenece a este departamento.')
                    return
                a.cambiar_dpt(dpt_nuevo)
                print('El departamento ha sido cambiado.')
                return
        for i in self._investigadores:
            if i.DNI == DNI:
                if i.departamento == dpt_nuevo:
                    print('Esta persona ya pertenece a este departamento.')
                    return
                i.cambiar_dpt(dpt_nuevo)
                for t in self._titulares:
                    if t.DNI == DNI:
                        t.cambiar_dpt(dpt_nuevo)
                print('El departamento ha sido cambiado.')
                return
        print('Esta persona no esta dada de alta en la universidad.')

class Persona():
    def __init__(self, nombre, DNI, direccion, sexo: Sexo):
        if not nombre.isalpha():
            raise ValueError('El nombre solo puede contener letras"')
        self.nombre = nombre
        if len(DNI) != 9:
            raise ValueError("El DNI debe tener 9 caracteres")
        self.DNI = DNI
        self.direccion = direccion
        if not isinstance(sexo, Sexo):
            raise ValueError('El sexo debe de ser una instancia de la enumeración Sexo.')
        self.sexo = sexo.value

class Miembro_dpt(Persona):
    def __init__(self, nombre, DNI, direccion, sexo, departamento: Departamento):
        super().__init__(nombre, DNI, direccion, sexo)
        if not isinstance(departamento, Departamento):
            raise ValueError('El departamento debe ser una instancia de la enumeracion Departamento.')
        self.departamento = departamento

    def cambiar_dpt(self, dpt_nuevo):
        self.departamento = dpt_nuevo

class Estudiante(Persona):
    def __init__(self, nombre, DNI, direccion, sexo):
        super().__init__(nombre, DNI, direccion, sexo)
        self._asignaturas_matriculadas = []

    def devolver_datos(self):
        return (f'Nombre: {self.nombre} DNI: {self.DNI} Dirección: {self.direccion} Sexo: {Sexo(self.sexo)}')
    
    def añadir_asignatura(self, asignatura):
        for a in self._asignaturas_matriculadas:
            if a == asignatura:
                print('Este alumno ya esta matriculado en esta asignatura.')
                return
        self._asignaturas_matriculadas.append(asignatura)

    def listar_asignaturas(self):
        print('LISTADO ASIGNATURAS MATRICULADAS')
        for a in self._asignaturas_matriculadas:
            print('\t', a)
    
    def eliminar_asignatura(self, asignatura):
        try:
            self._asignaturas_matriculadas.remove(asignatura)
        except:
            raise Exception('Este estudiante no esta matriculado de esta asignatura.')
        
class Profesor(Miembro_dpt):
    def __init__(self,  nombre, DNI, direccion, sexo, departamento):
        super().__init__(nombre, DNI, direccion, sexo, departamento)
        self._asignaturas_impartidas = []

    def añadir_asignatura(self, asignatura):
        for a in self._asignaturas_impartidas:
            if a == asignatura:
                print('Este profesor ya imparte esta asignatura.')
                return
        self._asignaturas_impartidas.append(asignatura)
    
    def listar_asignaturas(self):
        print('LISTADO ASIGNATURAS IMPARTIDAS')
        for a in self._asignaturas_impartidas:
            print('\t', a)

    def eliminar_asignatura(self, asignatura):
        try:
            self._asignaturas_impartidas.remove(asignatura)
        except:
            print('Este profesor no imparte esta asignatura.')
        
    def devolver_datos(self):
        return (f'Nombre: {self.nombre} DNI: {self.DNI} Dirección: {self.direccion} Sexo: {Sexo(self.sexo)}, Departamento: {self.departamento}')

class Investigador(Miembro_dpt):
    def __init__(self, nombre, DNI, direccion, sexo, departamento, area_investigacion):
        super().__init__(nombre, DNI, direccion, sexo, departamento)
        self.area_investigacion = area_investigacion    

    def devolver_datos(self):
        return (f'Nombre: {self.nombre} DNI: {self.DNI} Dirección: {self.direccion} Sexo: {Sexo(self.sexo)} Departamento: {self.departamento} Área investigación: {self.area_investigacion} ')

class Profesor_asociado(Profesor):
    def __init__(self, nombre, DNI, direccion, sexo, departamento):
        super().__init__(nombre, DNI, direccion, sexo, departamento)

class Profesor_titular(Investigador, Profesor):
    def __init__(self, nombre, DNI, direccion, sexo, departamento, area_investigacion):
        Investigador.__init__(self, nombre, DNI, direccion, sexo, departamento, area_investigacion)
        Profesor.__init__(self, nombre, DNI, direccion, sexo, departamento)


def test_añadir_estudiante():
    u = Universidad('umu')
    u.añadir_estudiante('Joaquín', '48829491J', 'c/Mayor',  Sexo.MASCULINO)
    assert len(u._estudiantes) == 1

def test_eliminar_estudiante():
    u = Universidad('umu')
    u.añadir_estudiante('Joaquín', '48829491J', 'c/Mayor',  Sexo.MASCULINO)
    u.eliminar_estudiante('48829491J')
    assert len(u._estudiantes) == 0

def test_anadir_profesor_asociado():
    u = Universidad('umu')
    u.añadir_profesor_asociado('Gustavo', '37492065H','c/Mula',  Sexo.MASCULINO, Departamento.DIIC) 
    assert len(u._asociados) == 1

def test_eliminar_investigador_y_titular():
    u = Universidad('umu')
    u.añadir_profesor_titular('Sofía', '29475639V', 'c/Gran Vía', Sexo.FEMENINO, Departamento.DIIC, 'Redes')
    u.eliminar_investigador('29475639V')
    assert len(u._investigadores) ==  0 and len(u._titulares) == 0

def test_cambiar_departamento():
    u = Universidad('umu')
    u.añadir_profesor_titular('Sofía', '29475639V', 'c/Gran Vía', Sexo.FEMENINO, Departamento.DIIC, 'Redes')
    u.cambiar_dpt('29475639V', Departamento.DIS)
    assert u._titulares[0].departamento == Departamento.DIS