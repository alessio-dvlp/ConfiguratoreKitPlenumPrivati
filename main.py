import streamlit as st
from streamlit_image_select import image_select
import config
import math
import stripe
import requests
import random
import string
import time

# Configurazione base pagina streamlit e CSS
st.set_page_config(
    page_title="Configuratore",
    initial_sidebar_state="collapsed",
    page_icon="images/widairIcon.png")

# Applico CSS alla pagina
with open('css/style.css') as f:
       st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

posizioneTastoAiuto = [0.89,0.11]
if 'flagCaricamento' not in st.session_state:
    st.session_state.flagCaricamento = True

if st.session_state.flagCaricamento == False:
       # CSS per la navbar
       st.markdown(
       """
       <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
       <style>
       .navbar {
              position: fixed;
              top: 0;
              left: 0;
              right: 0;
              background-color: #ffffff;  */Sfondo */
              color: #9a99a0;  /* Testo grigio scuro */
              padding: 16px;  /* Spazio ridotto per una barra più sottile */
              z-index: 1000;
              display: flex;
              align-items: center;
              font-size: 12px;  /* Testo più piccolo */
              box-shadow: 0 2px 20px rgba(0, 0, 0, 0.05);  /* Ombra leggera */
       }
       .navbar a {
              color: #9a99a0;
              text-decoration: none;
              padding: 0 10px;  /* Spazio ridotto tra i link */
       }
       .navbar a:hover {
              color: #0b5baa;  /* Colore blu al passaggio del mouse */
              text-decoration: none;  /* Nessuna sottolineatura al passaggio del mouse */
       }
       body {
              padding-top: 50px;  /* Spazio per la barra fissa */
       }
       .material-icons {
              vertical-align: middle;  /* Allinea verticalmente l'icona */
              margin-right: 5px;  /* Spazio tra l'icona e il testo */
              font-size: 16px;  /* Dimensione dell'icona (puoi modificarla) */
       }
       .logo {
              height: 30px;  /* Altezza del logo aziendale */
              margin-right: 10px;  /* Spazio tra il logo aziendale e i contatti */
       }
       </style>
       """,
       unsafe_allow_html=True
       )

       # Contenuto HTML Navbar
       st.markdown(
       """
       <div class="navbar">
              <a href="http://www.widair.com" target="_blank">  <!-- Link al logo aziendale -->
              <img src="https://widair.com/img/logo-1717496166.jpg" alt="Logo Aziendale" class="logo"> <!-- Logo aziendale -->
              <a href="tel:+3896699635">
              <span class="material-icons">phone</span>Chiamaci
              </a>
              <a href="mailto:info@widair.com">
              <span class="material-icons">email</span>Mandaci una mail
              </a>
       </div>
       """,
       unsafe_allow_html=True
       )

def aiuto():
       st.markdown("""
       <style>.st-emotion-cache-o19u9w.e1pbrot50 {
              display: none;}
       </style>

       <div style="margin-bottom: 15px; display: flex; align-items: center;">
       <img src="https://img.icons8.com/?size=32&id=WV326xpsBMyb&format=png&color=000000" style="margin-right: 12px;"/>
       <div>
              <strong style="display: block;">Telefono</strong>
              <a href="tel:+3896699635" style="text-decoration: none; color: gray; display: block;">+389 669 9635</a>
       </div>
       </div>
       <div style="margin-bottom: 15px; display: flex; align-items: center;">
       <img src="https://img.icons8.com/?size=30&id=6BBCqlzE4iKd&format=png&color=000000" style="margin-right: 12px;"/>
       <div>
              <strong style="display: block;">Email</strong>
              <a href="mailto:info@widair.com" style="text-decoration: none; color: gray; display: block;">info@widair.com</a>
       </div>
       </div>
       <div style="display: flex; align-items: center;">
       <img src="https://img.icons8.com/?size=32&id=VJz2Ob51dvZJ&format=png&color=000000" style="margin-right: 12px;"/>
       <div>
              <strong style="display: block;">Sito web</strong>
              <a href="http://www.widair.com" target="_blank" style="text-decoration: none; color: gray; display: block;">www.widair.com</a>
       </div>
       </div>
       """, unsafe_allow_html=True)
       st.write("")

def caricamento():
    # Aggiungi CSS per centrare l'immagine
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 9vh;  /* Altezza di base */
        }

        @media (max-width: 600px) {
            .centered {
                height: 19vh;  /* Altezza maggiore per schermi piccoli */
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.image("images/WidairAnimazione.gif")
    st.markdown('</div>', unsafe_allow_html=True)

    time.sleep(3.5)
    st.session_state.page = "Tipologia Impianto"
    st.session_state.flagCaricamento = False
    st.rerun()

def tipologiaImpianto(numeroPagina):
       st.caption(f"Pagina {numeroPagina} di 14")
       st.image("images/WidboxHomepage.png")
       st.write("**WIDBOX - Il sistema di climatizzazione canalizzata che ti offre Widair.**")
       st.write("Il widbox è adatto ad abitazioni/locali commerciali che dovranno essere controsoffittati.")
       st.write("In pochi minuti e semplici passi configura e dimensiona il tuo impianto di climatizzazione secondo le reali esigenze del tuo appartamento. Personalizza gli elementi di diffusione in ogni stanza e seleziona le alternative che fanno al caso tuo. Verrai guidato dal nostro configuratore che eseguirà tutto il dimensionamento dell’impianto per te gratuitamente e infine otterrai un preventivo istantaneo. Ti resta solo che iniziare la tua configurazione...")
       if st.button("**Inizia la configurazione**", type="primary", use_container_width=True):
              st.session_state.page = "Funzione Impianto"
              st.rerun()

def funzioneImpianto(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Funzione dell'impianto")

       if 'fattoreFunzioneImpianto' not in st.session_state:
             st.session_state.fattoreFunzioneImpianto = 100
       sceltaFunzioneImpianto = image_select(
                     label="Scegli la funzione dell'impianto",
                     images=["images/25.png","images/24.png"],
                     captions=["Raffreddamento (l'impianto funzionerà anche per riscaldamento, tuttavia, è sotto dimensionato per questa funzione)", "Riscaldamento & Raffreddamento"],
                     return_value = "index"
                     )
              
       if sceltaFunzioneImpianto == 0:
             st.session_state.fattoreFunzioneImpianto = 100
       else:
             st.session_state.fattoreFunzioneImpianto = 150
       
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Tipologia Impianto"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Luogo Impianto"
                     st.rerun()

def luogoImpianto(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Dove ne hai bisogno?")
       if 'locazioneImpianto' not in st.session_state:
             st.session_state.locazioneImpianto = ""
       sceltaLuogo = image_select(
              label="Scegli luogo dell'impianto",
              images=["images/home.png", "images/shop.png"],
              captions=["Abitazione", "Locale commerciale"],
              return_value = "index",
              )
       if sceltaLuogo == 0:
              st.session_state.locazioneImpianto = "Abitazione"
       else:
              st.session_state.locazioneImpianto = "Locale commerciale"

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Funzione Impianto"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Numero Stanze"
                     st.rerun()

def numeroStanze(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       if 'nStanze' not in st.session_state:
             st.session_state.nStanze = 1
       st.title("Quante stanze vuoi climatizzare?")
       st.session_state.nStanze = st.number_input("**Inserisci il numero di stanze**", min_value=1, max_value=7)
       if st.session_state.nStanze == 7:
              st.info("Il massimo numero di stanze da poter climatizzare è 7")

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Luogo Impianto"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Definisci Stanze"
                     st.rerun()

def definisciStanze(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       if 'dettagliStanze' not in st.session_state:
             st.session_state.dettagliStanze = {}
       
       st.title("Definisci le tue stanze")
       
       def input_stanza(i, nomeStanza):
              mqStanza = st.text_input(f"Mq {nomeStanza}", key=f"MqStanza{i+1}")
              if mqStanza:
                     try:
                            mqStanza = float(mqStanza.replace(',', '.'))  # Sostituisci la virgola con un punto per i decimali
                            st.session_state.dettagliStanze[f"MqStanza{i+1}"] = mqStanza
                     except ValueError:
                            st.error("Per favore, inserisci un valore numerico valido per i metri quadri.")

              altezzaStanza = st.text_input(f"Altezza {nomeStanza} in metri", key=f"AltezzaStanza{i+1}")
       
              if altezzaStanza:
                     try:
                            altezzaStanza = float(altezzaStanza.replace(',', '.'))  # Sostituisci la virgola con un punto per i decimali
                            st.session_state.dettagliStanze[f"AltezzaStanza{i+1}"] = altezzaStanza
                     except ValueError:
                            st.error("Per favore, inserisci un valore numerico valido per l'altezza.")

       for i in range(st.session_state.nStanze):
              with st.expander(f"**Stanza {i+1}**", icon=":material/deployed_code:", expanded=True):
                     nomeStanza = st.selectbox("Nome stanza", ['Salotto', 'Cucina', 'Camera patronale', 'Cameretta', 'Studio', "Bagno", 'Altro'], key=f"NomeStanza{i+1}")
                     
                     if nomeStanza == "Altro":
                            nomeStanzaCustom = st.text_input("**Inserisci nome stanza**", key=f"NomeStanzaCustom{i+1}")
                            st.session_state.dettagliStanze[f"NomeStanza{i+1}"] = nomeStanzaCustom
                            input_stanza(i, nomeStanzaCustom)
                     else:
                            st.session_state.dettagliStanze[f"NomeStanza{i+1}"] = nomeStanza
                            input_stanza(i, nomeStanza)
       
       if len(st.session_state.dettagliStanze) >= st.session_state.nStanze * 3:
              disabled = False
       else:
              disabled = True

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.dettagliStanze = {}
                     st.session_state.page = "Numero Stanze"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", disabled=disabled, type="primary", use_container_width=True):
                     st.session_state.page = "Controllo Temperatura"
                     st.rerun()

def controlloTemperatura(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       if 'sceltaControlloTemperatura' not in st.session_state:
             st.session_state.sceltaControlloTemperatura = ""
       if 'sceltaTipologiaSistema' not in st.session_state:
             st.session_state.sceltaTipologiaSistema = ""
       if 'prezzoBarraFilettata' not in st.session_state:
             st.session_state.prezzoBarraFilettata = 0
       if 'numeroBarraFilettata' not in st.session_state:
             st.session_state.numeroBarraFilettata = 0
       if 'prezzoControlloTemperatura' not in st.session_state:
             st.session_state.prezzoControlloTemperatura = 0
       if 'prezzoSerrandaBypass' not in st.session_state:
             st.session_state.prezzoSerrandaBypass = 0

       st.title("Controllo temperatura e zone")
       st.session_state.sceltaControlloTemperatura = image_select(
              label="Scegli come controllare la temperatura",
              images=["images/12.png", "images/11.png"],
              captions=["MANUALE - Controllare manualmente l’apertura e chiusura delle tue zone e hai la stessa temperatura in tutta la casa controllabile tramite il termostato della macchina canalizzata.", "MOTORIZZATO - Gestisci l’apertura e chiusura delle tue zone tramite i nostri cronotermostati e controllare la temperatura separatamente in ogni stanza. Scegliendo un sistema motorizzato, viene incluso nel plenum macchina una serranda by-pass, utile a mantenere la pressione statica nella rete dei condotti all'interno dei limiti prestabiliti, assicurando il corretto funzionamento del sistema di climatizzazione."],
              use_container_width=True,
              return_value = "index")
       
       if st.session_state.sceltaControlloTemperatura == 1:
              st.session_state.prezzoSerrandaBypass = config.listino_prezzi_accessori['Serranda By-pass']['prezzo']
              st.session_state.prezzoBarraFilettata = 6 * config.listino_prezzi_accessori['Barra filettata']['prezzo']
              st.session_state.numeroBarraFilettata = 6
              st.divider()
              st.session_state.sceltaTipologiaSistema = image_select(
              label="Tipologia di sistema",
              images=["images/10.png", "images/9.png"],
              captions=["CABLATO - Il termostato comunica con l’unità motorizzata tramite cavo.", "WIRELESS - Il termostato comunica wireless con l’unità motorizzata."],
              use_container_width=True,
              return_value = "index"
              )
       else:
              st.session_state.prezzoSerrandaBypass = 0
              st.session_state.sceltaTipologiaSistema = ""
              st.session_state.prezzoBarraFilettata = 4 * config.listino_prezzi_accessori['Barra filettata']['prezzo']
              st.session_state.numeroBarraFilettata = 4

       if st.session_state.sceltaTipologiaSistema == 0:
              with st.container(border=True):
                     st.write("**Cronotermostato per sistema cablato**")
                     st.image("images/Zebra.png", caption=config.listino_prezzi_accessori['Sistema Motorizzato Cablato']['Cronotermostato']['info'])
                     st.write("")
       elif st.session_state.sceltaTipologiaSistema == 1:
              with st.container(border=True):
                     st.write("**Cronotermostato per sistema wireless**")
                     st.image("images/Zeus.png", caption=config.listino_prezzi_accessori['Sistema Motorizzato Wireless']['Cronotermostato']['info'])

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.elencoNZonePerStanza = []
                     st.session_state.page = "Definisci Stanze"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Scelta Macchina"
                     st.rerun()

def sceltaMacchina(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Scegli la macchina consigliata per il tuo impianto")

       # Inizializzazione delle variabili di stato
       if 'sommaZone' not in st.session_state:
              st.session_state.sommaZone = 0
       if 'prezzoPlenumMacchina' not in st.session_state:
              st.session_state.prezzoPlenumMacchina = 0
       if 'elencoNZonePerStanza' not in st.session_state:
              st.session_state.elencoNZonePerStanza = []
       if 'flagMacchinaMitsubishiNonDisponibile' not in st.session_state:
              st.session_state.flagMacchinaMitsubishiNonDisponibile = False
       if 'flagMacchinaHaierNonDisponibile' not in st.session_state:
              st.session_state.flagMacchinaHaierNonDisponibile = False
       if 'flagHaier' not in st.session_state:
              st.session_state.flagHaier = False
       if 'flagMitsubishi' not in st.session_state:
              st.session_state.flagMitsubishi = True
       if 'tempBTUHaier' not in st.session_state:
              st.session_state.tempBTUHaier = ""
       if 'tempBTUMitsubishi' not in st.session_state:
              st.session_state.tempBTUMitsubishi = ""
       if 'costoTrasportoFlessibile' not in st.session_state:
              st.session_state.costoTrasportoFlessibile = 0
       if 'diametroFlessibile' not in st.session_state:
              st.session_state.diametroFlessibile = "0"
       
       mq_totali = 0
       risultati = []

       # Soglie
       soglieMitsubishi = [9000.0, 12000.0, 18000.0, 21000.0, 24000.0, 34000.0, 43000.0, 48000.0, 68000.0, 85000.0]
       soglieHaier = [12000.0, 18000.0, 24000.0, 36000.0, 43000.0, 48000.0, 55000.0]

       # Iterazione attraverso le stanze
       for i in range(st.session_state.nStanze + 1):
              mq_key = f"MqStanza{i}"
              altezza_key = f"AltezzaStanza{i}"
              
              if mq_key in st.session_state.dettagliStanze and altezza_key in st.session_state.dettagliStanze:
                     mq = float(st.session_state.dettagliStanze[mq_key])
                     altezza = float(st.session_state.dettagliStanze[altezza_key])
                     prodotto = mq * altezza
                     risultati.append((st.session_state.dettagliStanze[f"NomeStanza{i}"], prodotto))
                     mq_totali += prodotto

       # Calcolo BTU
       valoreBTU = st.session_state.fattoreFunzioneImpianto * mq_totali
       # Determinazione delle soglie
       def calcola_soglia(valoreBTU, soglie):
              for soglia in soglie:
                     if valoreBTU <= soglia:
                            return soglia
              return None
       
       BTUMitsubishi = calcola_soglia(valoreBTU, soglieMitsubishi)
       BTUHaier = calcola_soglia(valoreBTU, soglieHaier)
       st.session_state.flagMacchinaMitsubishiNonDisponibile = BTUMitsubishi is None
       st.session_state.flagMacchinaHaierNonDisponibile = BTUHaier is None

       # Funzione per arrotondare i valori
       def arrotonda_valore(valore):
              return max(1, math.ceil(valore))

       # Funzione per calcolare le zone per stanza
       def calcola_zone(portata_macchina, portata_diffusione):
              st.session_state.sommaZone = 0
              for nome, prodotto in risultati:
                     var = (prodotto * 100) / mq_totali
                     m3_elemento_diffusione_stanza = (var * int(portata_macchina)) / 100
                     n_zone_stanza = m3_elemento_diffusione_stanza / portata_diffusione
                     st.session_state.elencoNZonePerStanza.append((nome, arrotonda_valore(n_zone_stanza)))
                     st.session_state.sommaZone += arrotonda_valore(n_zone_stanza)
       
       # Calcolo della portata della macchina
       try:
              portataMacchina = min(
              int(config.macchinaHaier[f'BTU{int(BTUHaier)}']['portata'].replace(" m3/h", "")),
              int(config.macchinaMitsubishi[f'BTU{int(BTUMitsubishi)}']['portata'].replace(" m3/h", ""))
              )
       except:
              if BTUHaier == None and BTUMitsubishi == None:
                     st.caption("Per il tuo impianto sono necessarie più di 7 zone")
                     st.warning("[Configurazione solo su richiesta](https://www.widair.com/contattaci). Scrivici a mail: info@widair.com o chiamaci a cell. [+389 669 9635](tel:3896699635)")
                     disabilitaAvantiSceltaMacchina = True
                     return
              elif BTUHaier == None and BTUMitsubishi != None:
                     portataMacchina = int(config.macchinaMitsubishi[f'BTU{int(BTUMitsubishi)}']['portata'].replace(" m3/h", ""))
              elif BTUMitsubishi == None and BTUHaier != None:
                     portataMacchina = int(config.macchinaHaier[f'BTU{int(BTUHaier)}']['portata'].replace(" m3/h", ""))

       # Calcola le zone con la portata iniziale
       calcola_zone(portataMacchina, 350)

       # Se la somma delle zone supera 7, ricalcola con una portata maggiore
       if st.session_state.sommaZone > 7:
              st.session_state.sommaZone = 0
              st.session_state.elencoNZonePerStanza = []
              st.session_state.costoTrasportoFlessibile = 60
              st.session_state.diametroFlessibile = "200"
              calcola_zone(portataMacchina, 600)
       else:
              st.session_state.costoTrasportoFlessibile = 35
              st.session_state.diametroFlessibile = "150"

       # Funzione per visualizzare le informazioni delle macchine
       def mostra_macchina(macchina, BTU, flag_non_disponibile, checkbox_label):
              if not flag_non_disponibile:
                     with st.container(border=True):
                            st.image(macchina[f'BTU{int(BTU)}']['immagine'])
                            st.checkbox(f"**{macchina[f'BTU{int(BTU)}']['descrizione']}**", key=f"checkbox_{checkbox_label}")
                            if 'Mitsubishi' in str(macchina):
                                   st.subheader("")
                            if 'Haier' in str(macchina):
                                   st.subheader(f"{format(macchina[f'BTU{int(BTU)}']['prezzo'] + 156.80, '.2f')}€")
                            else:
                                   st.subheader(f"{format(macchina[f'BTU{int(BTU)}']['prezzo'] + 100, '.2f')}€")
                            # with st.expander("**Dati tecnici**", expanded=False, icon=":material/settings:"):
                            with st.popover("**Dati tecnici**", use_container_width=True):
                                   st.write("**POTENZA MACCHINA**")
                                   st.caption(f'{int(BTU)}BTU')
                                   st.write("**RAFFREDDAMENTO**")
                                   st.write("**Classe energetica**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['Raffreddamento - classe energetica']}")
                                   st.write("**Consumo energetico annuo**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['Raffreddamento - consumo energetico annuo (kWh/a)']} kWh/a")
                                   st.write("**Costo energetico annuo**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['Raffreddamento - costo energetico annuo (€/a)']}€/a")
                                   st.divider()
                                   st.write("**RISCALDAMENTO**")
                                   st.write("**Classe energetica**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['Riscaldamento - classe energetica']}")
                                   st.write("**Consumo energetico annuo**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['Riscaldamento - consumo energetico annuo (kWh/a)']} kWh/a")
                                   st.write("**Costo energetico annuo**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['Riscaldamento - costo energetico annuo (€/a)']}€/a")
                                   st.divider()
                                   st.write("**Alimentazione**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['Alimentazione']}")
                                   st.write("**Livello potenza sonora (Max)**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['Livello potenza sonora (Max) dB(A)']} dB(A)")
                                   st.write("**Tipo refrigerante**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['Tipo refrigerante']}")
                                   st.write("**Portata**")
                                   st.caption(f"{macchina[f'BTU{int(BTU)}']['portata']}") 
              else:
                     with st.container(border=True):
                            if 'Haier' in str(macchina):
                                   st.warning(f"Macchina Haier non disponibile per i BTU necessari")
                                   st.session_state['checkbox_Haier'] = False
                            else:
                                   st.warning(f"Macchina Mitsubishi non disponibile per i BTU necessari")
                                   st.session_state['checkbox_Mitsubishi'] = False

       # Visualizzazione delle macchine
       if st.session_state.sommaZone > 7:
              st.caption("Per il tuo impianto sono necessarie più di 7 zone")
              st.warning("[Configurazione solo su richiesta](https://www.widair.com/contattaci). Scrivici a mail: info@widair.com o chiamaci a cell. [+389 669 9635](tel:3896699635)")
              disabilitaAvantiSceltaMacchina = True
       else:
              st.caption("Seleziona una macchina per il tuo impianto")
              col1, col2 = st.columns([0.5,0.5])
              with col1:
                     mostra_macchina(config.macchinaHaier, BTUHaier, st.session_state.flagMacchinaHaierNonDisponibile, "Haier")
              with col2:
                     mostra_macchina(config.macchinaMitsubishi, BTUMitsubishi, st.session_state.flagMacchinaMitsubishiNonDisponibile, "Mitsubishi")

              st.session_state.flagHaier = st.session_state['checkbox_Haier']
              st.session_state.flagMitsubishi = st.session_state['checkbox_Mitsubishi']

              if st.session_state.flagHaier and st.session_state.flagMitsubishi:
                     st.warning("Non è possibile selezionare entrambe le macchina. Effettua una scelta.")
                     disabilitaAvantiSceltaMacchina = True
              elif not st.session_state.flagHaier and not st.session_state.flagMitsubishi:
                     st.warning("Seleziona una macchina.")
                     disabilitaAvantiSceltaMacchina = True
              else: 
                     disabilitaAvantiSceltaMacchina = False

       # Aggiornamento delle variabili temporanee - Necessario per calcolo griglia di ripresa
       st.session_state.tempBTUHaier = BTUHaier if st.session_state.flagHaier else None
       st.session_state.tempBTUMitsubishi = BTUMitsubishi if st.session_state.flagMitsubishi else None
              
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.flagMacchinaMitsubishiNonDisponibile = False
                     st.session_state.flagMacchinaHaierNonDisponibile = False
                     st.session_state.page = "Controllo Temperatura"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", disabled=disabilitaAvantiSceltaMacchina, use_container_width=True):
                     if st.session_state.flagHaier == True:
                            st.session_state.page = "Elementi Diffusione"
                            st.rerun()
                     else:
                            st.session_state.page = "Comandi"
                            st.rerun()

# Rendo visibile a tutti in quanto comandi è una pagina che non viene eseguita sempre
if 'prezzoComandoManualeMitsubishi' not in st.session_state:
             st.session_state.prezzoComandoManualeMitsubishi = 0
if 'prezzoWiFiComandoManualeMitsubishi' not in st.session_state:
             st.session_state.prezzoWiFiComandoManualeMitsubishi = 0
if 'nomeComandoManualeMitsubishi' not in st.session_state:
             st.session_state.nomeComandoManualeMitsubishi = None           
def comandi(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Comandi")

       sceltaComandoManualeMitsubishi = image_select(
              label="Scegli un comando per la tua macchina Mitsubishi",
              images=["images/Mitsubishi PAR-CT01MAA-PB - Nero.png", "images/Mitsubishi PAR-CT01MAA-SB v2.png", "images/Mitsubishi PAR-41MAA.png"],
              captions=["Mitsubishi Comando remoto a filo touch retroilluminato in varie finiture Nero PAR-CT01MAA-PB", "Mitsubishi - Comando remoto a filo touch retroilluminato in varie finiture Bianco PAR-CT01MAA-SB", "Mitsubishi - Comando remoto a filo touch retroilluminato in varie finiture Bianco PAR-41MAA"],
              use_container_width=True,
              return_value = "index"
       )
       if sceltaComandoManualeMitsubishi == 0:
              st.session_state.nomeComandoManualeMitsubishi = "Comando remoto a filo touch retroilluminato in varie finiture Nero PAR-CT01MAA-PB"
       elif sceltaComandoManualeMitsubishi == 1:
              st.session_state.nomeComandoManualeMitsubishi = "Comando remoto a filo touch retroilluminato in varie finiture Bianco PAR-CT01MAA-SB"
       else:
              st.session_state.nomeComandoManualeMitsubishi = "Comando remoto a filo touch retroilluminato in varie finiture Bianco PAR-41MAA"

       st.session_state.prezzoComandoManualeMitsubishi = 56.80
       
       if st.session_state.sceltaControlloTemperatura == 0 and st.session_state.flagMitsubishi == True:
              st.divider()
              sceltaWiFiComandoManualeMitsubishi = image_select(
              label="Vuoi integrare l'interfaccia Wi-Fi",
              images=["images/9.png", "images/36.png"],
              captions=["Interfaccia Wi-Fi", "Nessuna interfaccia Wi-Fi"],
              use_container_width=True,
              return_value = "index"
              )
              if sceltaWiFiComandoManualeMitsubishi == 0:
                     st.session_state.prezzoWiFiComandoManualeMitsubishi = 56.80
              else:
                     st.session_state.prezzoWiFiComandoManualeMitsubishi = 0

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Scelta Macchina"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Elementi Diffusione"
                     st.rerun()

def elementiDiffusione(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Scegli le bocchette o i diffusori per le tue stanze")

       if 'elDifTip' not in st.session_state:
              st.session_state.elDifTip = None
       if 'elDifCol' not in st.session_state:
              st.session_state.elDifCol = None
       if 'elencoColori' not in st.session_state:
              st.session_state.elencoColori = []
       if 'descrizioneColori' not in st.session_state:
              st.session_state.descrizioneColori = []
       if 'elencoNomiStanze' not in st.session_state:
              st.session_state.elencoNomiStanze = []
       if 'elencoElementiDiffusione' not in st.session_state:
              st.session_state.elencoElementiDiffusione = []
       
       for i in range(st.session_state.nStanze):
              nome_key = f"NomeStanza{i+1}"
              if nome_key in st.session_state.dettagliStanze:
                     st.session_state.elencoNomiStanze.append((st.session_state.dettagliStanze[nome_key]))
       
              st.subheader(st.session_state.elencoNomiStanze[i])
              if int(st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][i][1]) > 1:
                     st.caption(f"**Per questa stanza sono necessarie {int(st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][i][1])} bocchette/diffusori**")
              else: 
                     st.caption(f"**Per questa stanza è necessaria solo una bocchetta/diffusore**")

              images, captions = config.options[st.session_state.locazioneImpianto][st.session_state.diametroFlessibile]

              with st.expander(f"**Seleziona Bocchetta / Diffusore per {st.session_state.elencoNomiStanze[i]}**", icon=":material/deployed_code:", expanded=True):
                     st.session_state.elDifTip = image_select(
                     label=f"Scegli l'elemento di diffusione che preferisci",
                     images=images,
                     captions=captions,
                     use_container_width=True,
                     return_value="index",
                     key=f"{st.session_state.elencoNomiStanze[i]}{i+1}"
                     )

                     def set_colori(elDifTip, diametro):
                            if st.session_state.locazioneImpianto == "Abitazione":
                                   if elDifTip == 0:
                                          return ["images/RAL9010.png", "images/Alluminio Anodizzato.png"], ["RAL9010", "Alluminio Anodizzato"]
                                   elif elDifTip in [1, 3]:
                                          return ["images/RAL9010.png", "images/RAL9016.png", "images/Alluminio Anodizzato.png"], ["RAL9010", "RAL9016", "Alluminio Anodizzato"]
                                   else:
                                          return [], []
                            elif st.session_state.locazioneImpianto == "Locale commerciale":
                                   # Gestire colori differenziando per diametro
                                   if elDifTip == 0:
                                          return ["images/RAL9010.png", "images/Alluminio Anodizzato.png"], ["RAL9010", "Alluminio Anodizzato"]
                                   elif elDifTip in [1, 3]:
                                          return ["images/RAL9010.png", "images/RAL9016.png", "images/Alluminio Anodizzato.png"], ["RAL9010", "RAL9016", "Alluminio Anodizzato"]
                                   else:
                                          return [], []
                                   
                     def mostra_anteprima(diametro, elDifTip):
                            if st.session_state.locazioneImpianto == "Abitazione":
                                   immagini = {
                                          "150": {
                                          1: "images/FUTURE (installata).png",
                                          2: "images/DLAS40 (installata).png",
                                          3: "images/DLN40 (installata).png"
                                          },
                                          "200": {
                                          1: "images/FUTURE (installata).png",
                                          3: "images/DLN40 (installata).png"
                                          }
                                   }
                            elif st.session_state.locazioneImpianto == "Locale commerciale":
                                   immagini = {
                                          "150": {
                                          3: "images/FUTURE (installata).png",
                                          6: "images/DLAS40 (installata).png",
                                          7: "images/DLN40 (installata).png"
                                          },
                                          "200": {
                                          3: "images/FUTURE (installata).png",
                                          7: "images/DLN40 (installata).png"
                                          }
                                   }
                            
                            if diametro in immagini and elDifTip in immagini[diametro]:
                                   st.write("**Anteprima elemento diffusione installato**")
                                   st.image(immagini[diametro][elDifTip])

                     mostra_anteprima(st.session_state.diametroFlessibile, st.session_state.elDifTip)
                     st.session_state.elencoColori, st.session_state.descrizioneColori = set_colori(st.session_state.elDifTip, st.session_state.diametroFlessibile)

                     if st.session_state.elencoColori:  # Solo se ci sono colori disponibili
                            st.session_state.elDifCol = image_select(
                                   label=f"Scegli un colore",
                                   images=st.session_state.elencoColori,
                                   captions=st.session_state.descrizioneColori,
                                   use_container_width=True,
                                   return_value="index",
                                   key=f"elDifCol{i+1}"
                            )
                            
                     elDifTip = st.session_state.elDifTip
                     elDifCol = st.session_state.elDifCol
                     nuovo_elemento = [f"{st.session_state.elencoNomiStanze[i]}{i+1}", elDifTip, elDifCol]
                     st.session_state.elencoElementiDiffusione.append(nuovo_elemento)

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.elencoElementiDiffusione = []
                     if st.session_state.flagHaier == True:
                            st.session_state.page = "Scelta Macchina"
                            st.rerun()
                     else:
                            st.session_state.page = "Comandi"
                            st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Griglia Ripresa"
                     st.rerun()

def grigliaRipresa(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Griglia di ripresa portafiltro")

       if 'dimensioneGriglia' not in st.session_state:
              st.session_state.dimensioneGriglia = ""
       if 'prezzoGriglia' not in st.session_state:
              st.session_state.prezzoGriglia = 0
       if 'coloreGriglia' not in st.session_state:
              st.session_state.coloreGriglia = ""

       if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
              portata = config.macchinaHaier[f"BTU{int(st.session_state.tempBTUHaier)}"]['portata']
       else:
              portata = config.macchinaMitsubishi[f"BTU{int(st.session_state.tempBTUMitsubishi)}"]['portata']

       portata = int(portata.replace(" m3/h", ""))
       
       grigliaRipresaPortata = [1160, 1560, 2350, 3150]
       grigliaRipresaDimensioni = ['600x400', '800x400', '1000x400', '1000x600']

       for i, elemento in enumerate(grigliaRipresaPortata):
              if int(portata) <= elemento:
                     st.session_state.dimensioneGriglia = grigliaRipresaDimensioni[i]
                     break

       st.write("La griglia di ripresa è un componente che serve a recuperare l'aria dall'ambiente in modo che venga filtrata per trattenere polvere e impurità presenti, migliorando così la qualità dell'aria reimmessa nel sistema.")
       st.image("images/Griglia di ripresa.png")

       st.session_state.coloreGriglia = image_select(
              label=f"Scegli la finitura della tua griglia di ripresa",
              images=["images/RAL9010.png", "images/RAL9016.png", "images/Alluminio Anodizzato.png"],
              captions=["RAL9010", "RAL9016", "Alluminio Anodizzato"],
              use_container_width=True,
              return_value="index",
              )
       
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.elencoElementiDiffusione = []
                     st.session_state.page = "Elementi Diffusione"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Posizionamento"
                     st.rerun()

def posizionamento(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Posizionamento macchina interna")
       if st.session_state.locazioneImpianto == 'Abitazione':
              ambiente = "nella tua abitazione:"
       else:
              ambiente = "nel tuo locale commerciale:"
       st.write(f"Di seguito ti spieghiamo dove dovrebbe essere posizionata la macchina interna {ambiente}")
       st.image("images/16.png")
       st.write("La macchina canalizzata presenta una ripresa aria ambiente e una mandata aria ambiente. La ripresa aria deve essere effettuata in una zona comune, quale (ingresso, disimpegno, corridoio, ecc..) pertanto la macchina canalizzata dovrà essere posizionata: all’ingresso dell’appartamento/locale commerciale o in un disimpegno o in corridoio, ecc..")

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Griglia Ripresa"
                     st.rerun()
       with col2:
              if st.button("**Ho capito!**", type="primary", use_container_width=True):
                     st.session_state.page = "Distanze"
                     st.rerun()

def distanze(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Distanze")
       st.write("**DEFINISCI LA DISTANZA TRA LA MACCHINA INTERNA E LE STANZE/LOCALI**")
       if st.session_state.locazioneImpianto == 'Abitazione':
              st.write("Dopo aver deciso dove posizionare la macchina interna in base allo spazio presente nella tua abitazione, prendi la tua planimetria e definisci approssimativamente quanti metri passano tra dove verrà posizionata la macchina e l'uscio della porta di ogni stanza.")
              st.write("Definisci i metri di distanza come illustrato nell'immagine seguente.")
       else:
              st.write("Dopo aver deciso dove posizionare la macchina interna in base allo spazio presente nel tuo locale commerciale, prendi la tua planimetria e definisci approssimativamente quanti metri passano tra dove verrà posizionata la macchina e l'uscio della porta e/o il centro della stanza.")
              st.write("Definisci i metri come illustrato nelle immagini seguenti, seguendo la linea rossa nei diversi casi (diffusore/bocchetta).")

       sommaDistanza = 0
       if 'prezzoFlessibile' not in st.session_state:
              st.session_state.prezzoFlessibile = 0
       if 'scatoleFlessibile' not in st.session_state:
              st.session_state.scatoleFlessibile = 0
       if 'flagSanificante' not in st.session_state:
              st.session_state.flagSanificante = False
       st.session_state.flagSanificante = False
       flagSuRichiesta = False
       flagErrorDistanza = False

       if st.session_state.locazioneImpianto == 'Abitazione':
              st.image("images/MacchinaUscioPorta.png", caption="Se hai selezionato una bocchetta")
       else:
              col1, col2 = st.columns([0.5,0.5])
              with col1:
                     st.image("images/MacchinaUscioPorta.png", caption="Se hai selezionato una bocchetta/diffusore lineare")
              with col2:
                     st.image("images/MacchinaCentroStanza.png", caption="Se hai selezionato un diffusore a soffitto")
       st.write("")

       ultimi_elementi = st.session_state.elencoElementiDiffusione[-st.session_state.nStanze:]

       for i in range(st.session_state.nStanze):
              with st.expander(f"**{st.session_state.elencoNomiStanze[i]}**", icon=":material/deployed_code:", expanded=True):
                     if st.session_state.locazioneImpianto == 'Abitazione':
                            labelDistanza = "uscio/porta"
                     else:
                            labelDistanza = "centro della stanza" if ultimi_elementi[i][1] in [4, 5] else "uscio/porta"
                     distanza = st.text_input(f"Distanza in metri tra macchina e {labelDistanza}", key=f"{st.session_state.elencoNomiStanze[i]}{i+1}")
                     if distanza:
                            flagEmpty = False
                            if not distanza.isdigit():
                                   st.error("Per favore, inserisci un valore numerico.")
                                   flagErrorDistanza = True
                            else:
                                   distanza_float = float(distanza)
                                   # Se la stanza ha più elementi di diffusione, moltiplico la distanza data in input dall'utente per il numero di zone
                                   if st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][i][1] != 1:
                                          sommaDistanza += distanza_float * float(st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][i][1])
                                   else:
                                          sommaDistanza += distanza_float
                                   if distanza_float > 10:
                                          flagSuRichiesta = True
                                   elif distanza_float > 5:
                                          st.session_state.flagSanificante = True
                     else:
                            flagEmpty = True
       sommaDistanza += st.session_state.sommaZone * 2
                                          
       if flagSuRichiesta:
              st.warning("[Configurazione solo su richiesta](https://www.widair.com/contattaci). Scrivici a mail: info@widair.com o chiamaci a cell. [+389 669 9635](tel:3896699635)")
       else:
              scatoleFlessibile = int(math.ceil(sommaDistanza / 10) * 10 / 10)
              if st.session_state.diametroFlessibile == "150":
                     prezzo_key = 'Flessibile Ø 150 mm sanificante' if st.session_state.flagSanificante else 'Flessibile Ø 150 mm isolato'
              elif st.session_state.diametroFlessibile == "200":
                     prezzo_key = 'Flessibile Ø 200 mm sanificante' if st.session_state.flagSanificante else 'Flessibile Ø 200 mm isolato'
              st.session_state.scatoleFlessibile = scatoleFlessibile
              st.session_state.prezzoFlessibile = scatoleFlessibile * float(config.listino_prezzi_accessori[prezzo_key]['prezzo'])

       disabled = flagSuRichiesta or flagErrorDistanza or flagEmpty

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Posizionamento"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", disabled=disabled, use_container_width=True):
                     st.session_state.page = "Installazione"
                     st.rerun()

def installazione(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Installazione")
       st.write("Desideri l'installazione?")

       if 'sceltaInstallazioneSi' not in st.session_state:
              st.session_state.sceltaInstallazioneSi = False
       if 'sceltaInstallazioneNo' not in st.session_state:
              st.session_state.sceltaInstallazioneNo = True
       if 'prezzoFinaleInstallazione' not in st.session_state:
              st.session_state.prezzoFinaleInstallazione = 0
       
       # Calcolo del costo installazione zone
       costo_base = 140
       costo_installazione_zone = int(st.session_state.sommaZone) * costo_base

       # Aggiunta dei costi extra in base al numero di zone
       costi_extra = {2: 300, 3: 400, 4: 500, 5: 600, 6: 700}
       costo_installazione_zone += costi_extra.get(int(st.session_state.sommaZone), 800)

       # Aggiunta del costo per il controllo temperatura
       if st.session_state.sceltaControlloTemperatura == 1:
              costo_installazione_zone += 50 * int(st.session_state.sommaZone)

       # Funzione per calcolare il costo dell'installazione del macchinario
       def calcola_costo_macchinario(temp, marca):
              if temp is None:
                     return 0
              costi = {
                     'Haier': {12000: 1150, 18000: 1220, 24000: 1220, 36000: 1380, 43000: 1380, 48000: 1380, 55000: 1380},
                     'Mitsubishi': {9000: 1150, 12000: 1150, 18000: 1220, 21000: 1220, 24000: 1220, 34000: 1380, 43000: 1380, 48000: 1380, 68000: 1380, 85000: 1540}
              }
              return costi.get(marca, {}).get(int(temp), 0)

       # Calcolo del costo dell'installazione del macchinario
       if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
              costo_installazione_macchinario = calcola_costo_macchinario(st.session_state.tempBTUHaier, 'Haier')
       if st.session_state.tempBTUMitsubishi or st.session_state.tempBTUMitsubishi != None:
              costo_installazione_macchinario = calcola_costo_macchinario(st.session_state.tempBTUMitsubishi, 'Mitsubishi')

       # Calcolo del prezzo finale
       st.session_state.prezzoFinaleInstallazione = format((costo_installazione_zone + costo_installazione_macchinario) * 1.5, '.2f')
       
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              with st.container(border=True):
                     st.image("images/36.png")
                     st.session_state.sceltaInstallazioneNo = st.checkbox("No", value=st.session_state.sceltaInstallazioneNo, on_change=lambda: (setattr(st.session_state, 'sceltaInstallazioneNo', True), setattr(st.session_state, 'sceltaInstallazioneSi', False)) if not st.session_state.sceltaInstallazioneNo else None)
       with col2:
              with st.container(border=True):
                     st.image("images/Installation.png")
                     st.session_state.sceltaInstallazioneSi = st.checkbox(f"Si, +{st.session_state.prezzoFinaleInstallazione}€", value=st.session_state.sceltaInstallazioneSi, on_change=lambda: (setattr(st.session_state, 'sceltaInstallazioneSi', True), setattr(st.session_state, 'sceltaInstallazioneNo', False)) if not st.session_state.sceltaInstallazioneSi else None)
                     if st.session_state.sceltaInstallazioneSi:
                            st.write("**COSA COMPRENDE L'INSTALLAZIONE**")
                            st.write("**1. Installazione unità esterna (fissaggio a parete o pavimento)**")
                            st.write("**2. Installazione unità interna a soffitto**")
                            st.write("**3. Installazione tubazione**")
                            st.markdown("""
                            - Posa tubazione frigorifera in rame rivestita di mandata e ritorno fino a 7m
                            - Posa tubo di scarico condensa
                            - Posa corrugato con cavo di alimentazione unità""")
                            st.write("**4. Installazione Widbox**")
                            st.markdown("""
                            - Posa plenum macchina su unità interna
                            - Forometria su pareti/soffitto in cartongesso/mattone con spessore fino a 15cm (escluse opere su pareti in cemento armato)
                            - Posa Plenum porta-bocchetta/diffusore con incluso ripristino e rasatura localizzato nella zona di intervento parete/soffitto (esclusa opera di decorazione)
                            - Posa tubazioni flessibili
                            - Posa elementi di diffusione e griglia portafiltro
                                   
                            *N.B. Sono escluse opere di controsoffittatura*""")

       if st.session_state.sceltaInstallazioneNo:
              st.session_state.prezzoFinaleInstallazione = 0

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Distanze"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Optional"
                     st.rerun()

def optional(numeroPagina):
       col1, col2 = st.columns(posizioneTastoAiuto)
       with col1:
              st.caption(f"Domanda {numeroPagina} di 14")
       with col2:
              with st.popover("Aiuto"):
                     aiuto()
       st.title("Aggiungi Optional")

       if 'prezzoIonizzatore' not in st.session_state:
              st.session_state.prezzoIonizzatore = 0
       if 'sceltaCopriclima' not in st.session_state:
              st.session_state.sceltaCopriclima = None
       if 'sceltaColoreCopriclima' not in st.session_state:
              st.session_state.sceltaColoreCopriclima = None
       if 'prezzoCopriclima' not in st.session_state:
              st.session_state.prezzoCopriclima = 0
       
       st.subheader("Copriclima")
       st.session_state.sceltaCopriclima = image_select(
              label="Scegli il copriclima che preferisci",
              images=["images/36.png", "images/Alfa.png", "images/Sirio.png","images/Antares.png", "images/Altair.png", "images/Vega.png"],
              captions=["Nessun copriclima", "Copriclima Alfa", "Copriclima Sirio", "Copriclima Antares", "Copriclima Altair", "Copriclima Vega"],
              )
       
       if st.session_state.sceltaCopriclima != "images/36.png":
              if st.session_state.sceltaCopriclima != 0:
                     st.session_state.sceltaColoreCopriclima = image_select(
                     label="Scegli un colore per il tuo copriclima",
                     images=["images/RAL8025.png", "images/RAL9002.png", "images/RAL9005.png"],
                     captions=["RAL8025", "RAL9002", "RAL9005"],
                     )
       else:
              st.session_state.prezzoCopriclima = 0

       st.divider()
       st.subheader("Ionizzatore")
       st.write("Modulo di sanitizzazione attiva antibatterica con ionizzazione negativa priva di formazione di ozono. Utilizzando questo dispositivo nell’impianto di distribuzione aria si ottiene una riduzione delle cariche microbiche, batteriche e virali sia nell’aria che sulle superfici di contatto dell’impianto stesso.")
       sceltaIonizzatore = image_select(
              label="Desideri integrare uno ionizzatore?",
              images=["images/36.png", "images/Ionic.png"],
              captions=["Nessun Ionizzatore", "Ionizzatore IONIC"],
              return_value = "index",
              )
       if sceltaIonizzatore == 0:
              st.session_state.prezzoIonizzatore = 0
       else:
              st.session_state.prezzoIonizzatore = config.listino_prezzi_accessori['Ionizzatore']['prezzo']

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Installazione"
                     st.rerun()
       with col2:
              if st.button("**Visualizza riepilogo**", type="primary", use_container_width=True):
                     st.session_state.page = "Riepilogo"
                     st.rerun()

def riepilogo():
       st.title("Riepilogo ordine e pagamento")
       st.caption("Qui di seguito visualizzerai il riepilogo dell'ordine. Verifica la correttezza dei dati e procedi con il pagamento.")
       if 'prezzoFinale' not in st.session_state:
              st.session_state.prezzoFinale = 0
       st.write("")

       if 'riepilogo_ordine' not in st.session_state:
              st.session_state.riepilogo_ordine = ""

       st.session_state.riepilogo_ordine = ""

       # Funzione Impianto
       st.subheader("Funzione impianto")
       if st.session_state.fattoreFunzioneImpianto == 150:
              st.caption("Riscaldamento & Raffreddamento")
              st.session_state.riepilogo_ordine += "Impianto di riscaldamento & raffreddamento "
       else:
              st.caption("Raffreddamento")
              st.session_state.riepilogo_ordine += "Impianto di raffreddamento "
       st.divider()

       # Luogo Impianto
       st.subheader("Luogo impianto")
       st.caption(st.session_state.locazioneImpianto)
       st.session_state.riepilogo_ordine += f"per {st.session_state.locazioneImpianto.lower()}. "
       st.divider()

       # Elementi di diffusione per stanza
       st.subheader("Stanze ed elementi diffusione")
       if st.session_state.locazioneImpianto == "Abitazione":
              if st.session_state.diametroFlessibile == "150":
                     associazione_nomi = {
                     0: 'Bocchetta a doppio filare di alette - WBMAV0 300x150mm',
                     1: 'Bocchetta a barre fisse con telaio a scomparsa - WFUTURE15 400x150mm',
                     2: 'Diffusore lineare a scomparsa a singola feritoia - WDLAS40 L.1000mm',
                     3: 'Diffusore lineare a feritoie - WDLN40 L.800mm 2 Feritoie',
                     }
              elif st.session_state.diametroFlessibile == "200":
                     associazione_nomi = {
                     0: 'Bocchetta a doppio filare di alette - WBMAV0 300x200mm',
                     1: 'Bocchetta a barre fisse con telaio a scomparsa - WFUTURE15 500x200mm',
                     2: 'Diffusore circolare con frontale chiuso - WLCA 200',
                     3: 'Diffusore lineare a feritoie - WDLN40 L.800mm 3 Feritoie',
                     4: 'Diffusore quadrato con frontale chiuso - WLKA 200'
                     }
       else:
              if st.session_state.diametroFlessibile == "150":
                     associazione_nomi = {
                     0: 'Bocchetta a doppio filare di alette - WBMAV0 300x150mm',
                     1: 'Bocchetta ad alette fisse - WLAF15 400x150mm',
                     2: 'Bocchetta a microugelli orientabili su pannello - WGUR 1000x200mm',
                     3: 'Bocchetta a barre fisse con telaio a scomparsa - WFUTURE15 400x150mm',
                     4: 'Diffusore multidirezionale a 4 vie - WAQ1 225x225mm',
                     5: 'Diffusore a flusso elicoidale - WBQE3Q 400x400mm',
                     6: 'Diffusore lineare a scomparsa a singola feritoia - WDLAS40 L.1000mm',
                     7: 'Diffusore lineare a feritoie - WDLN40 L.800mm 2 Feritoie'
                     }
              elif st.session_state.diametroFlessibile == "200":
                     associazione_nomi = {
                     0: 'Bocchetta a doppio filare di alette - WBMAV0 300x150mm',
                     1: 'Bocchetta ad alette fisse - WLAF15 500x200mm',
                     2: 'Diffusore circolare con frontale chiuso - WLCA 200',
                     3: 'Bocchetta a barre fisse con telaio a scomparsa - WFUTURE15 500x200mm',
                     4: 'Diffusore multidirezionale a 4 vie - WAQ1 300x300mm',
                     5: 'Diffusore a flusso elicoidale - WBQE3Q 500x500mm',
                     6: 'Diffusore quadrato con frontale chiuso - WLKA 200',
                     7: 'Diffusore lineare a feritoie - WDLN40 L.800mm 3 Feritoie'
                     }
       
       associazione_colori = {
              0: 'RAL 9010 - Panna',
              1: 'RAL 9016 - Bianco',
              2: 'Alluminio Anodizzato',
       }

       def ripetiElemento(nome_associato, colore_associato, numeroElementi):
              for i in range(numeroElementi):
                     st.image(f"images/{nome_associato}.png")
                     if nome_associato == "Diffusore circolare con frontale chiuso - WLCA 200" or nome_associato == "Diffusore quadrato con frontale chiuso - WLKA 200":
                            st.session_state.prezzoElementiDiffusione += config.listino_prezzi_accessori[nome_associato]['prezzo']
                            st.caption(f"{nome_associato}, {colore_associato}")
                     else:
                            st.session_state.prezzoElementiDiffusione += config.listino_prezzi_accessori[nome_associato]['prezzo'] + config.listino_prezzi_accessori[nome_associato]['prezzoPlenum']
                            st.caption(f"{nome_associato}, {colore_associato}")
                     
                     st.session_state.riepilogo_ordine += f"{nome_associato}, {colore_associato} "

                     if st.session_state.sceltaControlloTemperatura == 0:
                            if 'prezzoSerranda' in config.listino_prezzi_accessori[nome_associato]:
                                   st.session_state.prezzoElementiDiffusione += config.listino_prezzi_accessori[nome_associato]['prezzoSerranda']
                                   flagSerranda = True
                            else:
                                   flagSerranda = False
                     else:
                            flagSerranda = False

                     if flagSerranda == True:
                            st.caption("Serranda di regolazione inclusa.")
                            st.session_state.riepilogo_ordine += "(serranda di regolazione inclusa). "
                     if nome_associato != "Diffusore circolare con frontale chiuso - WLCA 200" and nome_associato != "Diffusore quadrato con frontale chiuso - WLKA 200":
                            st.caption(f"Plenum in pannello preisolato incluso con 1 attacchi Ø {st.session_state.diametroFlessibile}")
                            st.session_state.riepilogo_ordine += f" - Plenum in pannello preisolato con 1 attacchi Ø {st.session_state.diametroFlessibile}. "

       # Itera sulla lista di dati
       if 'prezzoElementiDiffusione' not in st.session_state:
              st.session_state.prezzoElementiDiffusione = 0
       contatore = 0
       st.session_state.prezzoElementiDiffusione = 0
       for item in st.session_state.elencoElementiDiffusione[-st.session_state.nStanze:]:
              nome_con_numero = item[0]  # Primo elemento (nome con numero)
              numero = item[1]           # Secondo elemento (numero)
              numeroColore = item[2]     # Terzo elemento (numero colore)
              # Rimuovi il numero finale dal nome
              nome = ''.join(filter(lambda x: not x.isdigit(), nome_con_numero))
              with st.expander(f"**{nome.strip()}**", icon=":material/deployed_code:", expanded=True):
                     # Sostituisci il numero con il nome corrispondente
                     nome_associato = associazione_nomi.get(numero, 'Elemento diffusione sconosciuto')  # Usa 'Sconosciuto' se il numero non è trovato
                     st.image(f"images/{nome_associato}.png")
                     st.session_state.prezzoElementiDiffusione += config.listino_prezzi_accessori[nome_associato]['prezzo'] + config.listino_prezzi_accessori[nome_associato]['prezzoPlenum']
                     if st.session_state.sceltaControlloTemperatura == 0:
                            if 'prezzoSerranda' in config.listino_prezzi_accessori[nome_associato]:
                                   st.session_state.prezzoElementiDiffusione += config.listino_prezzi_accessori[nome_associato]['prezzoSerranda']
                                   flagSerranda = True
                            else:
                                   flagSerranda = False
                     else:
                            flagSerranda = False
                     
                     colore_associato = associazione_colori.get(numeroColore, 'Colore sconosciuto')
                     st.caption(f"{nome_associato}, {colore_associato}")
                     st.session_state.riepilogo_ordine += f"{nome_associato}, {colore_associato} "
                     # Aggiungo cavalletti, tappi e eventuali kit di continuità
                     if nome_associato == "Diffusore lineare a scomparsa a singola feritoia - WDLAS40 L.1000mm":
                            st.session_state.prezzoElementiDiffusione += (config.listino_prezzi_accessori['Cavalletti']*2) + config.listino_prezzi_accessori['Tappi di chiusura']
                            st.caption("Tappi inclusi nel prezzo")
                            st.session_state.riepilogo_ordine += " - Cavaletti e tappi inclusi"
                     if nome_associato == "Diffusore lineare a feritoie - WDLN40 L.800mm 2 Feritoie":
                            st.session_state.prezzoElementiDiffusione += (config.listino_prezzi_accessori['Cavalletti']*2)
                            st.caption("Cavaletti inclusi nel prezzo")
                            st.session_state.riepilogo_ordine += " - Cavaletti inclusi)"
                     if flagSerranda == True:
                            st.caption("Serranda di regolazione inclusa.")
                            st.session_state.riepilogo_ordine += "(serranda di regolazione inclusa). "
                     
                     # Mostro per il primo elemento
                     if st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][contatore][1] != 1:
                            if nome_associato != "Diffusore circolare con frontale chiuso - WLCA 200" and nome_associato != "Diffusore quadrato con frontale chiuso - WLKA 200":
                                   st.caption(f"Plenum in pannello preisolato incluso con 1 attacchi Ø {st.session_state.diametroFlessibile}")
                                   st.session_state.riepilogo_ordine += f" - Plenum in pannello preisolato con 1 attacchi Ø {st.session_state.diametroFlessibile}. "
                     
                     if st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][contatore][1] >= 2:
                            numeroElementi = st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][contatore][1]-1
                            ripetiElemento(nome_associato, colore_associato, numeroElementi)
                     else:
                            if nome_associato != "Diffusore circolare con frontale chiuso - WLCA 200" and nome_associato != "Diffusore quadrato con frontale chiuso - WLKA 200":
                                   st.caption(f"Plenum in pannello preisolato incluso con {st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][contatore][1]} attacchi Ø {st.session_state.diametroFlessibile}")
                                   st.session_state.riepilogo_ordine += f" - Plenum in pannello preisolato con {st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][contatore][1]} attacchi Ø {st.session_state.diametroFlessibile}. "
                     contatore += 1
       st.divider()

       # Controllo temperatura
       st.subheader("Controllo Temperatura")
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.session_state.sceltaControlloTemperatura == 0:
                     st.caption("Controllo della temperatura manuale")
                     st.session_state.riepilogo_ordine += " Controllo della temperatura manuale. "
              else:
                     if st.session_state.sceltaTipologiaSistema == 0:
                            st.caption(f"Controllo della temperatura motorizzato cablato - include serranda bypass montata sul plenum macchina, centralina, {st.session_state.nStanze} cronotermostati, interfaccia di comunicazione, scatola stagna e cablatura sistema")
                            st.session_state.riepilogo_ordine += f"Controllo della temperatura motorizzato cablato - include serranda bypass montata sul plenum macchina, centralina, {st.session_state.nStanze} cronotermostati, interfaccia di comunicazione, scatola stagna e cablatura sistema. "
                     else:
                            st.caption(f"Controllo della temperatura motorizzato wireless - include serranda bypass montata sul plenum macchina centralina, {st.session_state.nStanze} cronotermostati, interfaccia di comunicazione, scatola stagna e cablatura sistema")
                            st.session_state.riepilogo_ordine += f"Controllo della temperatura motorizzato wireless - include serranda bypass montata sul plenum macchina centralina, {st.session_state.nStanze} cronotermostati, interfaccia di comunicazione, scatola stagna e cablatura sistema. "
       with col2:
              if st.session_state.sceltaControlloTemperatura != 0:
                     if st.session_state.sceltaTipologiaSistema == 0:
                            st.session_state.prezzoControlloTemperatura = 283.86 + (89.07*st.session_state.nStanze) + 248.29 + 50 + 100
                            st.write(f":green[**+ {format(st.session_state.prezzoControlloTemperatura, '.2f')}€**]")
                     else:
                            st.session_state.prezzoControlloTemperatura = 321.62 + (124.18*st.session_state.nStanze) + 248.29 + 50 + 100
                            st.write(f":green[**+ {format(st.session_state.prezzoControlloTemperatura, '.2f')}€**]")
       st.divider()

       # Scelta Macchina
       st.subheader("Macchina")
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
                     st.image(f"{config.macchinaHaier[f'BTU{int(st.session_state.tempBTUHaier)}']['immagine']}")
              else:
                     st.image(f"{config.macchinaMitsubishi[f'BTU{int(st.session_state.tempBTUMitsubishi)}']['immagine']}")
       with col2:
              if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
                     st.caption(f"{config.macchinaHaier[f'BTU{int(st.session_state.tempBTUHaier)}']['descrizione']}")
                     st.session_state.riepilogo_ordine += f"Macchina {config.macchinaHaier[f'BTU{int(st.session_state.tempBTUHaier)}']['descrizione']} (+ Plenum macchina con {st.session_state.sommaZone} attacchi Ø {st.session_state.diametroFlessibile}). "
                     if st.session_state.sceltaControlloTemperatura == 1:
                            st.session_state.riepilogo_ordine += "Attacchi motorizzati. "
              else:
                     st.caption(f"{config.macchinaMitsubishi[f'BTU{int(st.session_state.tempBTUMitsubishi)}']['descrizione']}")
                     st.session_state.riepilogo_ordine += f"Macchina {config.macchinaMitsubishi[f'BTU{int(st.session_state.tempBTUMitsubishi)}']['descrizione']}. (+ Plenum macchina con {st.session_state.sommaZone} attacchi Ø {st.session_state.diametroFlessibile}). "
                     if st.session_state.sceltaControlloTemperatura == 1:
                            st.session_state.riepilogo_ordine += "Attacchi motorizzati. "
              

              if st.session_state.diametroFlessibile == '150':
                     if st.session_state.sceltaControlloTemperatura == 1:
                            prezzoCollarini = 78.00
                     else:
                            prezzoCollarini = 3.0
              elif st.session_state.diametroFlessibile == '200':
                     if st.session_state.sceltaControlloTemperatura == 1:
                            prezzoCollarini = 79.50
                     else:
                            prezzoCollarini = 3.35

              if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
                     prezzoMacchina = config.macchinaHaier[f'BTU{int(st.session_state.tempBTUHaier)}']['prezzo'] + 156.80
                     st.session_state.prezzoPlenumMacchina = config.macchinaHaier[f'BTU{int(st.session_state.tempBTUHaier)}']['prezzoPlenumMacchina'] + (st.session_state.sommaZone * prezzoCollarini)
                     st.write(f":green[**+ {format(prezzoMacchina, '.2f')}€**]")
              else:
                     prezzoMacchina = config.macchinaMitsubishi[f'BTU{int(st.session_state.tempBTUMitsubishi)}']['prezzo'] + 100
                     st.session_state.prezzoPlenumMacchina = config.macchinaMitsubishi[f'BTU{int(st.session_state.tempBTUMitsubishi)}']['prezzoPlenumMacchina'] + (st.session_state.sommaZone * prezzoCollarini)
                     st.write(f":green[**+ {format(prezzoMacchina, '.2f')}€**]")
       
       #Comandi
       if st.session_state.flagHaier != True:
              if st.session_state.prezzoComandoManualeMitsubishi != 0:
                     st.subheader("Comandi")
                     col1, col2 = st.columns([0.5,0.5])
                     with col1:
                            st.caption(f"{st.session_state.nomeComandoManualeMitsubishi}")
                            st.session_state.riepilogo_ordine += f"{st.session_state.nomeComandoManualeMitsubishi}. "
                     with col2:
                            st.write(":green[**+ 56.80€**]")

                     if st.session_state.prezzoWiFiComandoManualeMitsubishi != 0:
                            col1, col2 = st.columns([0.5,0.5])
                            with col1:
                                   st.caption("Hai integrato un modulo Wi-Fi al tuo impianto di climatizzazione")
                                   st.session_state.riepilogo_ordine += "Modulo Wi-Fi incluso. "
                            with col2:
                                   st.write(":green[**+ 56.80€**]")
              st.divider()
       else:
              st.session_state.prezzoWiFiComandoManualeMitsubishi = 0
              st.session_state.prezzoComandoManualeMitsubishi = 0
              st.divider()

       # Griglia portafiltro
       st.subheader("Griglia portafiltro")
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              st.image("images/Griglia di ripresa.png")
       with col2:
              if st.session_state.coloreGriglia == 0:
                     coloreGriglia = "Panna RAL 9010"
              elif st.session_state.coloreGriglia == 1:
                     coloreGriglia = "Bianco RAL 9016"
              else:
                     coloreGriglia = "Alluminio Anodizzato"
              st.caption(f"La griglia di ripresa adatta al tuo impianto è una {st.session_state.dimensioneGriglia}. Colore {coloreGriglia}. Filtro e controtelaio inclusi nel prezzo finale.")
              st.session_state.riepilogo_ordine += f"Griglia di ripresa portafiltro {st.session_state.dimensioneGriglia} - Colore {coloreGriglia} (Filtro e controtelaio inclusi). "
              st.session_state.prezzoGriglia = config.listino_prezzi_accessori[f'Griglia di ripresa {st.session_state.dimensioneGriglia} mm']['prezzo']
              if st.session_state.coloreGriglia == 0 or st.session_state.coloreGriglia == 1:
                     st.session_state.prezzoGriglia = st.session_state.prezzoGriglia * 1.15
              # Prezzo Finale Griglia portafiltro
              #st.write(f":green[**+ {format(st.session_state.prezzoGriglia, '.2f')}€**]")
       st.divider()

       # Flessibile
       st.subheader("Tubazione")
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.session_state.flagSanificante == True:
                     st.image("images/Sanificante.png")
              else:
                     st.image("images/Isolato.png")
       with col2:
              if st.session_state.flagSanificante == True:
                     labelFlessibile = "tubazione semirigida sanificante"
              else:
                     labelFlessibile = "tubazione flessibile isolata"
              st.caption(f"Per il tuo impianto sono necessari {st.session_state.scatoleFlessibile*10} metri di {labelFlessibile} Ø {st.session_state.diametroFlessibile}")
              st.session_state.riepilogo_ordine += f"{st.session_state.scatoleFlessibile*10} metri di {labelFlessibile} Ø 150. "
              # st.write(f":green[**+ {format(st.session_state.prezzoFlessibile, '.2f')}€**]")
              st.write()
       st.divider()

       # Installazione
       if st.session_state.prezzoFinaleInstallazione != 0:
              st.subheader("Installazione")
              col1, col2 = st.columns([0.5,0.5])
              with col1:
                     st.caption("Hai richiesto l'installazione dell'impianto")
                     st.session_state.riepilogo_ordine += "Installazione dell'impianto inclusa. "
              with col2:
                     st.write(f":green[**+ {format(float(st.session_state.prezzoFinaleInstallazione), '.2f')}€**]")
              st.divider()

       # Optional
       if st.session_state.sceltaCopriclima != "images/36.png" or st.session_state.prezzoIonizzatore != 0:
              st.subheader("Optional")
              if st.session_state.sceltaCopriclima != "images/36.png":
                     st.write(f"**Copriclima**")
                     modelloCopriclima = st.session_state.sceltaCopriclima
                     modelloCopriclima = modelloCopriclima.replace("images/", "")
                     modelloCopriclima = modelloCopriclima.replace(".png", "")
                     coloreCopriclima = st.session_state.sceltaColoreCopriclima
                     coloreCopriclima = coloreCopriclima.replace("images/", "")
                     coloreCopriclima = coloreCopriclima.replace(".png", "")
                     col1, col2 = st.columns([0.5,0.5])
                     with col1:
                            st.image(st.session_state.sceltaCopriclima)
                     with col2:
                            st.write(f"**Modello {modelloCopriclima} - Colore {coloreCopriclima}**")
                            st.session_state.riepilogo_ordine += f"Copriclima modello {modelloCopriclima} - Colore {coloreCopriclima}. "
                            st.caption("Nascondi la tua unità esterna e rendila più indiscreta esteticamente")
                            if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
                                   st.session_state.prezzoCopriclima = config.macchinaHaier[f'BTU{int(st.session_state.tempBTUHaier)}']['prezzoCopriclima'] + 50
                            else:
                                   st.session_state.prezzoCopriclima = config.macchinaMitsubishi[f'BTU{int(st.session_state.tempBTUMitsubishi)}']['prezzoCopriclima'] + 50
                            #st.write(f":green[**+ {format(st.session_state.prezzoCopriclima, '.2f')}€**]")

              if st.session_state.prezzoIonizzatore != 0:
                     st.write(f"**Ionizzatore**")
                     col1, col2 = st.columns([0.5,0.5])
                     with col1:
                            st.image("images/IonicRiepilogo.png")
                     with col2:
                            st.caption("Modulo di sanificazione attiva antibatterica con ionizzazione negativa priva di formazione di ozono.")
                            st.session_state.riepilogo_ordine += "Ionizzatore incluso. "
                            #st.write(f":green[**+ {format(st.session_state.prezzoIonizzatore, '.2f')}€**]")
              st.divider()
       

       
       # Accessori in dotazione
       if 'prezzoAccessori' not in st.session_state:
              st.session_state.prezzoAccessori = 0
       st.session_state.prezzoAccessori = 0
       st.subheader("Accessori in dotazione")
       st.session_state.riepilogo_ordine += f"Accessori in dotazione: {st.session_state.sommaZone*2} fascette stringitubo, {st.session_state.numeroBarraFilettata} barre filettate, 15 dadi flangiati M8, 15 viti autoforanti 4,2x16mm, 6 Tasselli in ottone."
       st.caption(f"{st.session_state.sommaZone*2} fascette stringitubo")
       if st.session_state.diametroFlessibile == '150':
              st.session_state.prezzoAccessori += float(st.session_state.sommaZone * 2) * 0.84
       elif st.session_state.diametroFlessibile == '200':
              st.session_state.prezzoAccessori += float(st.session_state.sommaZone * 2) * 1.01
       st.caption(f"{st.session_state.numeroBarraFilettata} barre filettate")
       st.session_state.prezzoAccessori += float(st.session_state.prezzoBarraFilettata)
       st.caption("15 dadi flangiati M8")
       st.session_state.prezzoAccessori += 2.00
       st.caption("15 viti autoforanti 4,2x16mm")
       st.session_state.prezzoAccessori += 0.40
       st.caption("6 Tasselli in ottone")
       st.session_state.prezzoAccessori += 3.00
       st.divider()

       # Download Libretto Istruzioni
       st.subheader("Libretto di istruzioni Widbox")
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              st.caption("Scarica il libretto di istruzioni Widbox che ti guida passo passo nell'installazione del tuo impianto.")
       with col2:
              with open("file/Libricino istruzioni Widbox.pdf", "rb") as pdf:
                     st.download_button(
                            label="Scarica PDF",
                            data=pdf,
                            file_name="Libricino istruzioni Widbox.pdf",
                            mime="application/pdf",
                            use_container_width=False,
                            type="primary"
                     )
       st.divider()

       st.subheader("**Preferenze di pagamento**")
       pagamentoBonificoBancario = st.radio("**Come vuoi pagare?**", ['Carta di credito', 'Bonifico Bancario'], horizontal=True)
       if pagamentoBonificoBancario == 'Bonifico Bancario':
              Nome = st.text_input('Inserisci il tuo nome')
              Mail = st.text_input('Inserisci la tua mail, ti invieremo un codice alfanumerico da mettere nella causale e il nostro IBAN')
              NumeroDiTelefono = st.text_input('Inserisci il tuo numero di telefono')
       else:
              Nome = ""
              Mail = ""
              NumeroDiTelefono = ""
       st.divider()

       # 55€ di spedizione + 35€ per ogni scatola di sanificante da 150 (60€ per ogni scatola di sanificante da 200)
       st.subheader("Totale Ordine")
       st.caption("Spedizione inclusa in tutta italia (isole maggiori comprese es. Sicilia, Sardegna)")
       prezzoImponibileIniziale = float(st.session_state.prezzoPlenumMacchina) + float(st.session_state.prezzoSerrandaBypass) + float(st.session_state.prezzoElementiDiffusione*1.10) + float(st.session_state.prezzoControlloTemperatura) + float(prezzoMacchina) + float(st.session_state.prezzoComandoManualeMitsubishi) + float(st.session_state.prezzoWiFiComandoManualeMitsubishi) + float(st.session_state.prezzoGriglia) + float(config.listino_prezzi_accessori[f'Griglia di ripresa {st.session_state.dimensioneGriglia} mm']['prezzoControtelaio']) + float(st.session_state.prezzoFlessibile) + float(st.session_state.scatoleFlessibile*float(st.session_state.costoTrasportoFlessibile)) + float(st.session_state.prezzoFinaleInstallazione) + float(st.session_state.prezzoCopriclima) + float(st.session_state.prezzoIonizzatore) + float(st.session_state.prezzoAccessori) + 55
       prezzoConIva = float(prezzoImponibileIniziale * 1.22)
       commissione = float((prezzoConIva * 5)/100)
       prezzoImponibileFinale = float(prezzoImponibileIniziale + commissione)
       st.session_state.prezzoFinale = float((prezzoImponibileIniziale + commissione) * 1.22)
                                  
       st.metric(value=f"{format(prezzoImponibileFinale, '.2f')}€", label=":gray[Prezzo IVA esclusa]")
       st.write(f"{format(st.session_state.prezzoFinale, '.2f')}€ (IVA inclusa)")

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Optional"
                     st.rerun()
       with col2:
              if pagamentoBonificoBancario == 'Bonifico Bancario':
                     alphanumeric_characters = string.ascii_letters + string.digits
                     code = ''.join(random.choice(alphanumeric_characters) for _ in range(6))
                     configuratoreNtfy = st.secrets["ConfiguratoreNTFY"]
                     notifica = f"""
                     IBAN: IT40H0200830290000106048658
                     Codice alfanumerico da inserire nella causale del bonifico: {code.upper()}
                     Importo: {format((float(st.session_state.prezzoFinale)),'.2f')}€\n
                     Ordine:\n{st.session_state.riepilogo_ordine}\n
                     """ 
                     if st.button("**RICEVI MAIL**", type="primary", use_container_width=True):
                            if Mail != "":
                                   try:
                                          requests.post(configuratoreNtfy,
                                                 data=notifica.encode('utf-8'),
                                                 headers={
                                                        "Title": f"{Nome} - {Mail} - {NumeroDiTelefono}",
                                                 })
                                          st.success('Riceverai a breve una mail con i dati per effettuare il bonifico', icon=":material/mail:")
                                   except Exception as e:
                                          st.error("Errore nell'invio della mail. Contatta il supporto [cliccando qui](https://www.widair.com/contattaci) o riprova", icon=":material/mail:")
                            else:
                                   st.error(f"Non hai inserito la tua mail", icon=":material/mail:")
              else:
                     stripe.api_key = st.secrets["stripeAPI_test"]
                     session = stripe.checkout.Session.create(
                            payment_method_types=['card','paypal'],
                            line_items=[{
                                   'price_data': {
                                   'currency': 'eur',
                                   'product_data': {
                                   'name': "Impianto canalizzato",
                                   'description': st.session_state.riepilogo_ordine
                                   },
                                   'unit_amount': int(st.session_state.prezzoFinale*100),
                                   },
                                   'quantity': 1,
                                   }],
                                   mode='payment',
                                   success_url='https://widair.com/content/7-conferma-ordine',
                                   cancel_url='https://widair.com',
                                   shipping_address_collection={
                                          'allowed_countries': ['IT'],  # Paesi in cui è consentita la spedizione
                                   },
                                   phone_number_collection={"enabled": True},
                                   tax_id_collection={"enabled": True},
                                   custom_fields=[
                                   {
                                          "key": "codiceUnivoco",
                                          "label": {"type": "custom", "custom": "Codice Univoco"},
                                          "type": "text",
                                          "optional": True,
                                   },
                                   {
                                          "key": "codiceFiscale",
                                          "label": {"type": "custom", "custom": "Codice Fiscale"},
                                          "type": "text"
                                   },
                                   {
                                          "key": "indirizzoFatturazione",
                                          "label": {"type": "custom", "custom": "Indirizzo di fatturazione"},
                                          "type": "text"
                                   }
                                   ],
                            )
                     st.link_button("**CONFERMA E PAGA**", session.url, type="primary", use_container_width=True)

caricamentoPagina = st.Page(caricamento, title = "Caricamento")
tipologiaImpiantoPagina = st.Page(tipologiaImpianto, title = "Tipologia Impianto")
funzioneImpiantoPagina = st.Page(funzioneImpianto, title = "Funzione Impianto")
luogoImpiantoPagina = st.Page(luogoImpianto, title = "Luogo Impianto")
numeroStanzePagina = st.Page(numeroStanze, title = "Numero Stanze")
definisciStanzePagina = st.Page(definisciStanze, title = "Definisci Stanze")
controlloTemperaturaPagina = st.Page(controlloTemperatura, title = "Controllo Temperatura")
sceltaMacchinaPagina = st.Page(sceltaMacchina, title = "Scelta Macchina")
comandiPagina = st.Page(comandi, title = "Comandi")
elementiDiffusionePagina = st.Page(elementiDiffusione, title = "Elementi Diffusione")
grigliaRipresaPagina = st.Page(grigliaRipresa, title="Griglia Ripresa")
posizionamentoPagina = st.Page(posizionamento, title = "Posizionamento")
distanzePagina = st.Page(distanze, title = "Distanze")
installazionePagina = st.Page(installazione, title = "Installazione")
optionalPagina = st.Page(optional, title = "Optional")
riepilogoPagina = st.Page(riepilogo, title = "Riepilogo")

if 'page' not in st.session_state:
    st.session_state.page = "Caricamento"

if st.session_state.page == "Caricamento":
    caricamento()
if st.session_state.page == "Tipologia Impianto":
    tipologiaImpianto(1)
elif st.session_state.page == "Funzione Impianto":
    funzioneImpianto(2)
elif st.session_state.page == "Luogo Impianto":
    luogoImpianto(3)
elif st.session_state.page == "Numero Stanze":
    numeroStanze(4)
elif st.session_state.page == "Definisci Stanze":
    definisciStanze(5)
elif st.session_state.page == "Controllo Temperatura":
    controlloTemperatura(6)
elif st.session_state.page == "Scelta Macchina":
    sceltaMacchina(7)
elif st.session_state.page == "Comandi":
    comandi(8)
elif st.session_state.page == "Elementi Diffusione":
    elementiDiffusione(9)
elif st.session_state.page == "Posizionamento":
    posizionamento(10)
elif st.session_state.page == "Griglia Ripresa":
    grigliaRipresa(11)
elif st.session_state.page == "Distanze":
    distanze(12)
elif st.session_state.page == "Installazione":
    installazione(13)
elif st.session_state.page == "Optional":
    optional(14)
elif st.session_state.page == "Riepilogo":
    riepilogo()