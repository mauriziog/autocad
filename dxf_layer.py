import ezdxf

def estrai_layer_da_dxf(dxf_file, csv_file):
    # Apri il file DXF
    doc = ezdxf.readfile(dxf_file)
    
    # Ottieni la sezione dei layer
    layers = doc.layers
    
    # Lista per raccogliere i dati dei layer
    dati_layer = []
    
    for layer in layers:
        # Estrai i parametri principali del layer
        nome = layer.dxf.name
        colore = layer.dxf.color
        stato = "Bloccato" if layer.is_locked else "Sbloccato"
        tipolinea = layer.dxf.linetype
        
        # Aggiungi i dati del layer alla lista
        dati_layer.append([nome, colore, stato, tipolinea])
    
    # Scrivi i dati in un file CSV
    with open(csv_file, mode='w', newline='') as file:
        import csv
        writer = csv.writer(file)
        
        # Scrivi l'intestazione
        writer.writerow(["Nome Layer", "Colore", "Stato", "Tipo Linea"])
        
        # Scrivi i dati
        writer.writerows(dati_layer)
    
    print(f"Layer estratti e salvati in {csv_file}.")

# Esempio di utilizzo
dxf_file = "esempio.dxf"  # Sostituisci con il percorso del tuo file DXF
csv_file = "layer_output.csv"  # Sostituisci con il nome desiderato per il file CSV

estrai_layer_da_dxf(dxf_file, csv_file)
