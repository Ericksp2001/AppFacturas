## 📌 Introducción
Este proyecto ofrece una solución eficiente para gestionar y analizar facturas en formato PDF. A través de una interfaz moderna y fácil de usar, los usuarios pueden cargar archivos 📂, visualizar su contenido 🧐 y ejecutar diversas acciones para extraer información clave.

---

## 🛠 Tecnología
- **Frontend:** React ⚛️

---

## 💻 Breakpoints 
El diseño es responsivo y está optimizado para las siguientes resoluciones:
- **1366 × 768** (HD)
- **1920 × 1080** (Full HD)
- **2560 × 1600** (WQXGA)

---

## 🎨 Paleta de Colores
El frontend utilizará la siguiente guía de estilos basada en la tipografía **Poppins**:

|  Color         | Código Hex |
|--------------- |------------|
|  Azul Primario | `#3D71FD`  |
|  Blanco 1      | `#F8F8F8`  |
|  Blanco 2      | `#FFFFFF`  |
|  Negro         | `#000000`  |
|  Gris Oscuro   | `#3D3D3D`  |
|  Gris Medio 1  | `#747474`  |
|  Gris Medio 2  | `#7C7C7C`  |
|  Gris Claro    | `#8F8F8F`  |

---

## 🏗 Estructura de Componentes
El frontend se organiza de la siguiente manera:

### **📌 Pantallas Principales**
1. **📂 Pantalla de selección de archivos**: Permite a los usuarios subir facturas en formato PDF.
2. **📑 Pantalla de visualización y opciones**: Muestra los archivos cargados y permite seleccionar una acción.
   - **🖼 Ventana emergente de vista previa**: Al hacer doble clic en un archivo, se abrirá una vista previa del documento.
3. **ℹ️ Pantalla "Acerca de"**: Contiene información acerca del servicio y de los desarrolladores.
4. **📞 Pantalla "Contacto"**: Muestra información de contacto.

### **🛠 Componentes**
- `FileUploader`: Componente para la selección y carga de archivos.
- `FileList`: Muestra la lista de archivos cargados y un panel con las acciones disponibles.
- `FilePreviewModal`: Ventana emergente para la vista previa del documento.
- `Navbar`: Barra de navegación con enlaces a las diferentes secciones.
- `About`: Página con información sobre el proyecto.
- `Contact`: Página con la información de contacto.



