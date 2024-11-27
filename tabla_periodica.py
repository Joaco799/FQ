# Lista de todos los elementos de la tabla periódica con la información correspondiente
elementos = [
    ("Hidrógeno", "H", 1, 1.008, "1s¹", "Gas", "-259.16 °C", "-252.87 °C", "53 pm", 2.20),
    ("Helio", "He", 2, 4.0026, "1s²", "Gas", "-272.20 °C", "-268.93 °C", "31 pm", "No aplica"),
    ("Litio", "Li", 3, 6.94, "1s² 2s¹", "Sólido", "180.54 °C", "1590 °C", "152 pm", 0.98),
    ("Berilio", "Be", 4, 9.0122, "1s² 2s²", "Sólido", "1278 °C", "2469 °C", "112 pm", 1.57),
    ("Boro", "B", 5, 10.81, "1s² 2s² 2p¹", "Sólido", "2076 °C", "4000 °C", "87 pm", 2.04),
    ("Carbono", "C", 6, 12.011, "1s² 2s² 2p²", "Sólido", "3550 °C", "4827 °C", "67 pm", 2.55),
    ("Nitrógeno", "N", 7, 14.007, "1s² 2s² 2p³", "Gas", "-210.00 °C", "-195.79 °C", "56 pm", 3.04),
    ("Oxígeno", "O", 8, 15.999, "1s² 2s² 2p⁴", "Gas", "-218.79 °C", "-182.96 °C", "60 pm", 3.44),
    ("Flúor", "F", 9, 18.998, "1s² 2s² 2p⁵", "Gas", "-219.67 °C", "-188.11 °C", "64 pm", 3.98),
    ("Neón", "Ne", 10, 20.180, "1s² 2s² 2p⁶", "Gas", "-248.59 °C", "-246.05 °C", "38 pm", "No aplica"),
    ("Sodio", "Na", 11, 22.990, "1s² 2s² 2p⁶ 3s¹", "Sólido", "97.72 °C", "883 °C", "186 pm", 0.93),
    ("Magnesio", "Mg", 12, 24.305, "1s² 2s² 2p⁶ 3s²", "Sólido", "650 °C", "1090 °C", "160 pm", 1.31),
    ("Aluminio", "Al", 13, 26.982, "1s² 2s² 2p⁶ 3s² 3p¹", "Sólido", "660.32 °C", "2470 °C", "143 pm", 1.61),
    ("Silicio", "Si", 14, 28.085, "1s² 2s² 2p⁶ 3s² 3p²", "Sólido", "1414 °C", "2900 °C", "118 pm", 1.90),
    ("Fósforo", "P", 15, 30.974, "1s² 2s² 2p⁶ 3s² 3p³", "Sólido", "44.15 °C", "280.5 °C", "110 pm", 2.19),
    ("Azufre", "S", 16, 32.06, "1s² 2s² 2p⁶ 3s² 3p⁴", "Sólido", "115.21 °C", "444.6 °C", "104 pm", 2.58),
    ("Cloro", "Cl", 17, 35.45, "1s² 2s² 2p⁶ 3s² 3p⁵", "Gas", "-101.5 °C", "-34.04 °C", "99 pm", 3.16),
    ("Argón", "Ar", 18, 39.948, "1s² 2s² 2p⁶ 3s² 3p⁶", "Gas", "-189.35 °C", "-185.85 °C", "71 pm", "No aplica"),
    ("Potasio", "K", 19, 39.098, "1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", "Sólido", "63.38 °C", "759 °C", "243 pm", 0.82),
    ("Calcio", "Ca", 20, 40.078, "1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", "Sólido", "842 °C", "1484 °C", "197 pm", 1.00),
    ("Escandio", "Sc", 21, 44.956, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹", "Sólido", "1539 °C", "2836 °C", "162 pm", 1.36),
    ("Titanio", "Ti", 22, 47.867, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d²", "Sólido", "1668 °C", "3287 °C", "147 pm", 1.54),
    ("Vanadio", "V", 23, 50.942, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d³", "Sólido", "1910 °C", "3380 °C", "134 pm", 1.63),
    ("Cromo", "Cr", 24, 52.00, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁴", "Sólido", "1907 °C", "2671 °C", "130 pm", 1.66),
    ("Manganeso", "Mn", 25, 54.938, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵", "Sólido", "1246 °C", "2061 °C", "139 pm", 1.55),
    ("Hierro", "Fe", 26, 55.845, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶", "Sólido", "1538 °C", "2862 °C", "126 pm", 1.83),
    ("Cobalto", "Co", 27, 58.933, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁷", "Sólido", "1495 °C", "2927 °C", "125 pm", 1.88),
    ("Níquel", "Ni", 28, 58.693, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁸", "Sólido", "1455 °C", "2730 °C", "124 pm", 1.91),
    ("Cobre", "Cu", 29, 63.546, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰", "Sólido", "1084.62 °C", "2562 °C", "128 pm", 1.90),
    ("Zinc", "Zn", 30, 65.38, "1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s²", "Sólido", "419.58 °C", "907 °C", "139 pm", 1.65),
    # Agregar los demás elementos siguiendo el mismo patrón...
]

# Función para generar un archivo HTML para cada elemento
def crear_html(elemento):
    nombre, simbolo, numero_atomico, peso_atomico, config_electronica, estado_fisico, punto_fusion, punto_ebullicion, radio_atomico, electronegatividad = elemento

    # Código HTML con el formato solicitado
    html_code = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{nombre} ({simbolo})</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; }}
        header {{ background-color: #001f3f; color: white; text-align: center; padding: 20px 0; }}
        main {{ padding: 20px; max-width: 800px; margin: auto; background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }}
        h2 {{ color: #0074D9; border-bottom: 2px solid #ddd; padding-bottom: 5px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        table, th, td {{ border: 1px solid #ddd; }}
        th, td {{ padding: 10px; text-align: left; }}
        th {{ background-color: #f4f4f9; }}
    </style>
</head>
<body>
    <header>
        <h1>Tabla Periódica</h1>
        <h2>Dolo - Cata - Joaco - Tizi</h2>
    </header>

    <main>
        <h2>Elemento: {nombre} ({simbolo})</h2>
        <p>{nombre} es un elemento químico de la tabla periódica que se encuentra en estado {estado_fisico}.</p>

        <h2>Propiedades Físicas y Químicas</h2>
        <table>
            <tr><th>Propiedad</th><th>Valor</th></tr>
            <tr><td>Número atómico</td><td>{numero_atomico}</td></tr>
            <tr><td>Peso atómico</td><td>{peso_atomico}</td></tr>
            <tr><td>Configuración electrónica</td><td>{config_electronica}</td></tr>
            <tr><td>Estado físico</td><td>{estado_fisico}</td></tr>
            <tr><td>Punto de fusión</td><td>{punto_fusion}</td></tr>
            <tr><td>Punto de ebullición</td><td>{punto_ebullicion}</td></tr>
            <tr><td>Radio atómico</td><td>{radio_atomico}</td></tr>
            <tr><td>Electronegatividad</td><td>{electronegatividad}</td></tr>
        </table>

        <h2>Historia</h2>
        <p>Descubierto en su mayoría por {nombre} en 1868.</p>

        <h2>Usos</h2>
        <ul>
            <li>Uso en {nombre} en diversas industrias.</li>
        </ul>
    </main>
</body>
</html>
"""

    # Crear un archivo HTML para el elemento
    file_name = f"{simbolo}.html"
    with open(file_name, "w") as file:
        file.write(html_code)
    print(f"Archivo {file_name} creado con éxito.")

# Crear archivos HTML para todos los elementos
for elemento in elementos:
    crear_html(elemento)
