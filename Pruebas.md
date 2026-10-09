# [ Funcionamiendo de funciones bases del codigo/ step by step

> Demostrar las funciones basicas del codigo 
> **Fecha:** 08/10/2026  
> **Autores:**  [ Alejandro Arcila Rua / Gabriela Galindo Herrera]  

---

## 📋 Requisitos
Antes de iniciar, asegúrate de contar con lo siguiente:
- [ ] **Requisito 1:** Registro de nueva aeronave
- [ ] **Requisito 2:** Registro de componente a nueva aeronave
- [ ] **Requisito 3:** Parte del codigo (Agregar horas de uso)
- [ ] **Requisito 4:** Reporte de mantenimiento
- [ ] **Requisito 5:** Reiniciar horas de uso de un coponente
- [ ] **Requisito 6:** Autoevaluacion

---

## 🚀 Step by step

### Paso 1: [Nueva aeronave]

<div align="center">

### 1.1 Lista previa, contiene tres aeronaves y 5 componentes para cada una preestablecidas:
  
![Diagrama](./Imagenes/1A_Lista_previa.png)

### 1.2 Proceso de creacion de la aeronave

![Diagrama](./Imagenes/1B_Creacion_aeronave.png)

### 1.3 (Paso2) Creacion del componente

![Diagrama](./Imagenes/1C_Creacion_componente.png)

### 1.4 Verificacion de modificaciones exitosas

![Diagrama](./Imagenes/1D_Verificacion.png)

</div>

---

### Paso 2: [Nuevo componente]

<div align="center">
  
![Diagrama](./Imagenes/1B_Creacion_aeronave.png)

</div>

---

### Paso 3: [Codigo horas de uso]

<div align="center">

![Diagrama](./Imagenes/3A_lineas_de_adicion_de_horas_de_uso.png)

</div>

- La opcion 3 del menu evalua antes de que puedas introducir las horas de vuelo, si el avion esta en estado habilitado para vuelo (NO en estado "en tierra") derivado de algun componente que exceda las horas limite.

- En este segmento de codigo se empleo tanto for como if junto con valores booleanos para evaluar los estados pertinentes del aeronave

---

### Paso 4: [Reporte de horas de uso]

<div align="center">

### Reporte sin alerta

![Diagrama](./Imagenes/4A_Reporte_sin_alerta.png)

</div>

<div align="center">

  ### Adicion de horas de uso/vuelo
  
![Diagrama](./Imagenes/4B_Adicion_horas_de_vuelo.png)

</div>

<div align="center">

 ### Reporte de numero de horas exedido, solicitud de mantenimiento

![Diagrama](./Imagenes/4C_reporte_de_mantenimiento_con_alerta.png)

</div>


---

### Paso 5: [Mantenimiento componente]

<div align="center">

### Forma de realizar mantenimiento de un componente
![Diagrama](./Imagenes/5A_Mantenimiento_de_componente_en_aeronave_con_un_solo_componente.png)

</div>

<div align="center">

### Alarma de componente vencido

![Diagrama](./Imagenes/5B_Mantenimiento_del_componente_que_salto_la_alerta.png)

</div>

<div align="center">

### Revision de estado final de todos los componentes

![Diagrama](./Imagenes/5C_Estado_de_los_componentes_posterior_al_cambio.png)

</div>


---

### Paso 6: [Autoevaluacion]

| Autoevaluación | Integrante | Nota |
| :--- | :--- | :--- |
| - | Alejandro Arcila Rua | 5.0 |
| - | Gabriela Galindo Herrera | 5.0 | 

---
