import os
from fpdf import FPDF

def generar_factura(tree, codigo_cliente, nombre_cliente, direccion_cliente):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    #Encabezado
    pdf.cell(200, 10, txt="Factura", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Cliente: {nombre_cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Dirección: {direccion_cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Código Cliente: {codigo_cliente}", ln=True)
    pdf.cell(200, 10, txt="", ln=True)

    #Tabla de productos
    pdf.cell(40, 10, txt="Código Producto", border=1)
    pdf.cell(60, 10, txt="Producto", border=1)
    pdf.cell(30, 10, txt="Cantidad", border=1)
    pdf.cell(30, 10, txt="Precio Total", border=1)
    pdf.ln()

    total_factura = 0.0

    for child in tree.get_children():
        item = tree.item(child)
        codigo_producto = str(item["values"][0])
        producto = str(item["values"][1])
        cantidad = str(item["values"][2])
        precio_total = float(item["values"][3][2:])
        
        total_factura += precio_total
        
        pdf.cell(40, 10, txt=codigo_producto, border=1)
        pdf.cell(60, 10, txt=producto, border=1)
        pdf.cell(30, 10, txt=cantidad, border=1)
        pdf.cell(30, 10, txt=f"Q.{precio_total:.2f}", border=1)
        pdf.ln()

    #Total de la factura
    pdf.cell(160, 10, txt="Total:", border=1)
    pdf.cell(30, 10, txt=f"Q.{total_factura:.2f}", border=1)
    pdf.ln()

    #Mensaje de agradecimiento
    pdf.cell(200, 10, txt="Gracias por su compra", ln=True, align="C")

    #Guardar PDF
    if not os.path.exists("compras"):
        os.makedirs("compras")
    pdf.output(f"compras/factura_{codigo_cliente}.pdf")
