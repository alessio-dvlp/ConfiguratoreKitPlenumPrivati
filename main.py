import streamlit as st
from streamlit_image_select import image_select
import config
import math

# Configurazione base pagina streamlit e CSS
st.set_page_config(
    page_title="Configuratore",
    initial_sidebar_state="collapsed"
)

# Applico CSS alla pagina
with open('css/style.css') as f:
       st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def tipologiaImpianto():
    st.caption("Pagina 1 di 14")
    st.image("images/WidboxHomepage.png")
    st.write("**WIDBOX - Il sistema di climatizzazione canalizzata che ti offre Widair.**")
    st.write("Il widbox che viene fornito è adatto ad abitazioni/locali commerciali che dovranno essere controsoffittati, si ricorda che l’impianto canalizzato è pensato per essere nascosto nel controsoffitto.")
    st.write("In pochi minuti e semplici passi configura e dimensiona il tuo impianto di climatizzazione secondo le reali esigenze del tuo appartamento. Personalizza gli elementi di diffusione in ogni stanza e seleziona le alternative che fanno al caso tuo. Verrai guidato dal nostro configuratore che eseguirà tutto il dimensionamento dell’impianto per te gratuitamente e infine otterrai un preventivo istantaneo. Ti resta solo che iniziare la tua configurazione...")
    if st.button("**Inizia la configurazione**", type="primary", use_container_width=True):
       st.session_state.page = "Funzione Impianto"
       st.rerun()

def funzioneImpianto():
       if 'fattoreFunzioneImpianto' not in st.session_state:
             st.session_state.fattoreFunzioneImpianto = 100
       st.caption("Domanda 2 di 14")
       st.title("Funzione dell'impianto")
       sceltaFunzioneImpianto = image_select(
                     label="Scegli la funzione dell'impianto",
                     images=["images/24.png", "images/25.png"],
                     captions=["Riscaldamento & Raffreddamento", "Raffreddamento (l'impianto funzionerà anche per riscaldamento, tuttavia, è sotto dimensionato per questa funzione)"],
                     return_value = "index"
                     )
              
       if sceltaFunzioneImpianto == 0:
             st.session_state.fattoreFunzioneImpianto = 150
       else:
             st.session_state.fattoreFunzioneImpianto = 100
       
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Tipologia Impianto"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Luogo Impianto"
                     st.rerun()

def luogoImpianto():
       if 'locazioneImpianto' not in st.session_state:
             st.session_state.locazioneImpianto = ""
       st.caption("Domanda 3 di 14")
       st.title("Dove ne hai bisogno?")
       sceltaLuogo = image_select(
              label="Scegli luogo dell'impianto",
              images=["images/home.png", "images/shop.png"],
              captions=["Abitazione", "Locale commerciale"],
              return_value = "index",
              )
       if sceltaLuogo == 1:
              st.session_state.locazioneImpianto = "Locale commerciale"
       else:
              st.session_state.locazioneImpianto = "Abitazione"

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Funzione Impianto"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Numero Stanze"
                     st.rerun()

def numeroStanze():
       if 'nStanze' not in st.session_state:
             st.session_state.nStanze = 1
       
       st.caption("Domanda 4 di 14")
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

def definisciStanze():
       
       if 'scelteElDif' not in st.session_state:
             st.session_state.scelteElDif = {}
       
       st.caption("Domanda 5 di 14")
       st.title("Definisci le tue stanze")
       for i in range(st.session_state.nStanze):
              with st.expander(f"**Stanza {i+1}**", icon=":material/deployed_code:", expanded=True):
                     nomeStanza = st.selectbox("Nome stanza", ['Salotto', 'Cucina', 'Camera patronale', 'Cameretta', 'Studio', "Bagno", 'Altro'], key=f"NomeStanza{i+1}")
                     if nomeStanza == "Altro":
                            nomeStanzaCustom = st.text_input("**Inserisci nome stanza**")
                            st.session_state.scelteElDif[f"NomeStanza{i+1}"] = nomeStanzaCustom

                            mqStanza = st.text_input(f"Mq {nomeStanza}", key=f"MqStanza{i+1}")
                            if mqStanza and not mqStanza.isdigit():
                                   st.error("Per favore, inserisci un valore numerico intero per i metri quadri.")
                            else:
                                   st.session_state.scelteElDif[f"MqStanza{i+1}"] = mqStanza
       
                            altezzaStanza = st.text_input(f"Altezza {nomeStanza}", key=f"AltezzaStanza{i+1}")
                            if altezzaStanza and not altezzaStanza.isdigit():
                                   st.error("Per favore, inserisci un valore numerico intero per l'altezza.")
                            else:
                                   st.session_state.scelteElDif[f"AltezzaStanza{i+1}"] = altezzaStanza
                     else:
                            st.session_state.scelteElDif[f"NomeStanza{i+1}"] = nomeStanza
                            mqStanza = st.text_input(f"Mq {nomeStanza}", key=f"MqStanza{i+1}")
                            # Controllo se mqStanza e altezzaStanza contengono solo numeri
                            if mqStanza and not mqStanza.isdigit():
                                   st.error("Per favore, inserisci un valore numerico intero per i metri quadri.")
                            else:
                                   st.session_state.scelteElDif[f"MqStanza{i+1}"] = mqStanza
                                   #config.elencoStanze[f"MqStanza{i+1}"] = mqStanza

                            altezzaStanza = st.text_input(f"Altezza {nomeStanza}", key=f"AltezzaStanza{i+1}")
                            if altezzaStanza and not altezzaStanza.isdigit():
                                   st.error("Per favore, inserisci un valore numerico intero per l'altezza.")
                            else:
                                   st.session_state.scelteElDif[f"AltezzaStanza{i+1}"] = altezzaStanza
                                   #config.elencoStanze[f"AltezzaStanza{i+1}"] = altezzaStanza
       
       #st.write(st.session_state.scelteElDif)

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Numero Stanze"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Controllo Temperatura"
                     st.rerun()

def controlloTemperatura():
       if 'sceltaControlloTemperatura' not in st.session_state:
             st.session_state.sceltaControlloTemperatura = ""
       if 'sceltaTipologiaSistema' not in st.session_state:
             st.session_state.sceltaTipologiaSistema = ""
       if 'prezzoBarraFilettata' not in st.session_state:
             st.session_state.prezzoBarraFilettata = 0
       if 'prezzoControlloTemperatura' not in st.session_state:
             st.session_state.prezzoControlloTemperatura = 0
       if 'prezzoSerrandaBypass' not in st.session_state:
             st.session_state.prezzoSerrandaBypass = 0

       st.caption("Domanda 6 di 14")
       st.title("Controllo temperatura e zone")
       st.session_state.sceltaControlloTemperatura = image_select(
              label="Scegli come controllare la temperatura",
              images=["images/12.png", "images/11.png"],
              captions=["MANUALE - Controllare manualmente l’apertura e chiusura delle tue zone e hai la stessa temperatura in tutta la casa controllabile tramite il termostato della macchina canalizzata.", "MOTORIZZATO - Gestisci l’apertura e chiusura delle tue zone tramite i nostri cronotermostati e controllare la temperatura separatamente in ogni stanza. Scegliendo un sistema motorizzato, viene incluso nel plenum macchina una serranda by-pass, utile a mantenere la pressione statica nella rete dei condotti all'interno dei limiti prestabiliti, assicurando il corretto funzionamento del sistema di climatizzazione."],
              use_container_width=True,
              return_value = "index"
              )
       
       if st.session_state.sceltaControlloTemperatura == 1:
              st.session_state.prezzoSerrandaBypass = 35
              st.session_state.prezzoBarraFilettata = 6 * 1.15
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
              st.session_state.prezzoBarraFilettata = 4 * 1.15

       
       if st.session_state.sceltaTipologiaSistema == 0:
              with st.container(border=True):
                     st.write("**Cronotermostato per sistema cablato**")
                     st.image("images/Zebra.png", caption="Cronotermostato digitale filare con programmazione settimanale a 2 livelli: Comfort/ECO. Consente un’impostazione adattata ad ogni impianto, il blocco delle funzionalità, la limitazione delle temperature di setup.")
                     st.write("")
       elif st.session_state.sceltaTipologiaSistema == 1:
              with st.container(border=True):
                     st.write("**Cronotermostato per sistema wireless**")
                     st.image("images/Zeus.png", caption="Termostato digitale con schermo e-ink a basso consumo, comunicazione radio bidirezionale, funziona in abbinamento alle centrali del sistema Zoning.")
       else:
              st.write("")

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

def sceltaMacchina():
       st.caption("Domanda 7 di 14")
       st.title("Scegli la macchina consigliata per il tuo impianto")

       if 'sommaZone' not in st.session_state:
             st.session_state.sommaZone = 0
       st.session_state.sommaZone = st.session_state.nStanze
       # Lista per memorizzare i risultati
       risultati = []
       if 'prezzoPlenumMacchina' not in st.session_state:
             st.session_state.prezzoPlenumMacchina = 0
       if 'elencoNZonePerStanza' not in st.session_state:
             st.session_state.elencoNZonePerStanza = []
       mq_totali = 0
       soglieMitsubishi = [9000.0, 12000.0, 18000.0, 21000.0, 24000.0, 34000.0, 43000.0, 48000.0, 68000.0, 85000.0]
       soglieHaier = [12000.0, 18000.0, 24000.0, 36000.0, 43000.0, 48000.0, 55000.0]
       BTUMitsubishi = 0
       BTUHaier = 0

       # Iterare attraverso le stanze
       for i in range(st.session_state.nStanze+1):
              mq_key = f"MqStanza{i}"
              altezza_key = f"AltezzaStanza{i}"
              
              # Controlla se le chiavi esistono nel dizionario
              if mq_key in st.session_state.scelteElDif and altezza_key in st.session_state.scelteElDif:
                     mq = float(st.session_state.scelteElDif[mq_key])
                     altezza = float(st.session_state.scelteElDif[altezza_key])
                     prodotto = mq * altezza
                     risultati.append((st.session_state.scelteElDif[f"NomeStanza{i}"], prodotto))
                     mq_totali += prodotto

       # Stampa i risultati mq per stanza
       #for nome, prodotto in risultati:
       #       st.write(f"M3 {nome}: {prodotto}")
       
       #st.write(f"Mq totali: {mq_totali}")

       #BTUValore
       valoreBTU = st.session_state.fattoreFunzioneImpianto*mq_totali
       #st.write(f"BTU Macchina: {valoreBTU}")

       def arrotonda_valore(valore):
              if valore < 1:
                     return 1
              elif valore == 1:
                     return 1
              elif valore == 2:
                     return 2
              elif valore > 1 and valore < 2:
                     return 2
              elif valore > 2 and valore < 3:
                     return 3
              else:
                     return round(valore)

       i=1
       for elemento in risultati:
              risultato2 = elemento[1] * 100 / mq_totali
              m3pStanza = (risultato2 * (valoreBTU / 10)) / 100
              # Nuovo valore 350
              nZoneStanza = m3pStanza / 770.0
              #st.write(nZoneStanza)
              #nZoneStanza_arrotondata = math.ceil(nZoneStanza)
              st.session_state.elencoNZonePerStanza.append((st.session_state.scelteElDif[f"NomeStanza{i}"], arrotonda_valore(nZoneStanza)))
              i+=1

       # st.write(st.session_state.elencoNZonePerStanza)
       # Stampa i risultati zone per stanza
       #for nome, nZone in st.session_state.elencoNZonePerStanza:
       #      st.write(f"{nome}: {nZone} zone")
       #       st.session_state.sommaZone += nZone
       #if sommaZone != st.session_state.nStanze:
       #      Azioni da fare se sommaZone supera numeroStanze immesse

       # Trova la soglia appropriata Mitsubishi
       for soglia in soglieMitsubishi:
              if valoreBTU <= soglia:
                     BTUMitsubishi = soglia
                     break
       # Trova la soglia appropriata Haier
       for soglia in soglieHaier:
              if valoreBTU <= soglia:
                     BTUHaier = soglia
                     break
       
       #st.write(f"Portata Macchina Mitsubishi: {BTUMitsubishi}")
       #st.write(f"Portata Macchina Haier: {BTUHaier}")

       if 'flagHaier' not in st.session_state:
              st.session_state.flagHaier = False
       if 'flagMitsubishi' not in st.session_state:
              st.session_state.flagMitsubishi = False
       if 'tempBTUHaier' not in st.session_state:
              st.session_state.tempBTUHaier = ""
       if 'tempBTUMitsubishi' not in st.session_state:
              st.session_state.tempBTUMitsubishi = ""
       
       st.caption("Seleziona una macchina per il tuo impianto")
       col1top, col2top = st.columns([0.5,0.5])
       with col1top:
              with st.container(border=True):
                     st.image(f"{config.macchinaHaier[f'BTU{int(BTUHaier)}']['immagine']}")
                     flagHaier = st.checkbox(f"**{config.macchinaHaier[f'BTU{int(BTUHaier)}']['descrizione']}**",value=st.session_state.flagHaier,on_change=lambda: (setattr(st.session_state, 'flagHaier', True), setattr(st.session_state, 'flagMitsubishi', False)) if not st.session_state.flagHaier else None)
                     st.session_state.flagHaier = flagHaier
                     st.subheader(f"{format((config.macchinaHaier[f"BTU{int(BTUHaier)}"]["prezzo"]*1.10) + 156.80, '.2f')}€") #formato decimale

                     with st.expander("**Dati tecnici - Unità Haier**", expanded=False, icon=":material/settings:"):
                            st.write("**RAFFREDDAMENTO**")
                            st.write("**Classe energetica**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]["Raffreddamento - classe energetica"]}")
                            st.write("**Consumo energetico annuo**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]["Raffreddamento - consumo energetico annuo (kWh/a)"]} kWh/a")
                            st.write("**Costo energetico annuo**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]['Raffreddamento - costo energetico annuo (€/a)']}€/a")
                            st.divider()
                            st.write("**RISCALDAMENTO**")
                            st.write("**Classe energetica**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]["Riscaldamento - classe energetica"]}")
                            st.write("**Consumo energetico annuo**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]["Riscaldamento - consumo energetico annuo (kWh/a)"]} kWh/a")
                            st.write("**Costo energetico annuo**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]['Riscaldamento - costo energetico annuo (€/a)']}€/a")
                            st.divider()
                            st.write("**Alimentazione**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]["Alimentazione"]}")
                            st.write("**Livello potenza sonora (Max)**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]["Livello potenza sonora (Max) dB(A)"]} dB(A)")
                            st.write("**Tipo refrigerante**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]["Tipo refrigerante"]}")
                            st.write("**Portata**")
                            st.caption(f"{config.macchinaHaier[f"BTU{int(BTUHaier)}"]["portata"]}")
       with col2top:
              with st.container(border=True):
                     st.image(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["immagine"]}")
                     flagMitsubishi = st.checkbox(f"**{config.macchinaMitsubishi[f'BTU{int(BTUMitsubishi)}']['descrizione']}**",value=st.session_state.flagMitsubishi,on_change=lambda: (setattr(st.session_state, 'flagMitsubishi', True), setattr(st.session_state, 'flagHaier', False)) if not st.session_state.flagMitsubishi else None)
                     st.session_state.flagMitsubishi = flagMitsubishi
                     st.write(" ")
                     st.subheader(f"{format((config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["prezzo"]*1.10) + 100.00, '.2f')}€")

                     with st.expander("**Dati tecnici - Unità Mistubishi**", expanded=False, icon=":material/settings:"):
                            st.write("**RAFFREDDAMENTO**")
                            st.write("**Classe energetica**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["Raffreddamento - classe energetica"]}")
                            st.write("**Consumo energetico annuo**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["Raffreddamento - consumo energetico annuo (kWh/a)"]} kWh/a")
                            st.write("**Costo energetico annuo**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]['Raffreddamento - costo energetico annuo (€/a)']}€/a")
                            st.divider()
                            st.write("**RISCALDAMENTO**")
                            st.write("**Classe energetica**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["Riscaldamento - classe energetica"]}")
                            st.write("**Consumo energetico annuo**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["Riscaldamento - consumo energetico annuo (kWh/a)"]} kWh/a")
                            st.write("**Costo energetico annuo**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]['Riscaldamento - costo energetico annuo (€/a)']}€/a")
                            st.divider()
                            st.write("**Alimentazione**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["Alimentazione"]}")
                            st.write("**Livello potenza sonora (Max)**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["Livello potenza sonora (Max) dB(A)"]} dB(A)")
                            st.write("**Tipo refrigerante**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["Tipo refrigerante"]}")
                            st.write("**Portata**")
                            st.caption(f"{config.macchinaMitsubishi[f"BTU{int(BTUMitsubishi)}"]["portata"]}")

       # Necessario per calcolo Griglia di ripresa
       if flagHaier == True:
              st.session_state.tempBTUHaier = BTUHaier
       else:
              st.session_state.tempBTUHaier = None
       if flagMitsubishi == True:
              st.session_state.tempBTUMitsubishi = BTUMitsubishi
       else:
              st.session_state.tempBTUMitsubishi = None
              
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Controllo Temperatura"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
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
def comandi():
       st.caption("Domanda 8 di 14")
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

       # Da verificare
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
                     # Da verificare
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

def elementiDiffusione():
       st.caption("Domanda 9 di 14")
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

       # Iterare attraverso le stanze
       for i in range(st.session_state.nStanze+1):
              nome_key = f"NomeStanza{i}"
              # Controlla se le chiavi esistono nel dizionario
              if nome_key in st.session_state.scelteElDif:
                     st.session_state.elencoNomiStanze.append((st.session_state.scelteElDif[f"NomeStanza{i}"]))

       #Prendo nomi delle stanze
       if st.session_state.locazioneImpianto == "Abitazione":
              for i in range(st.session_state.nStanze):
                     st.subheader(st.session_state.elencoNomiStanze[i])
                     with st.expander(f"**Seleziona Bocchetta / Diffusore per {st.session_state.elencoNomiStanze[i]}**", icon=":material/deployed_code:", expanded=True):
                            st.session_state.elDifTip = image_select(
                            label=f"Scegli l'elemento di diffusione che preferisci",
                            images=["images/WBMA.png","images/WFUTURE15.png","images/DLAS40.png", "images/DLN40.png"],
                            captions=["Bocchetta a doppio filare di alette - WBMAV0 300x150mm","Bocchetta a barre fisse con telaio a scomparsa - WFUTURE15 400x150mm","Diffusore lineare a scomparsa a singola feritoia - WDLAS40 L.1000mm","Diffusore lineare a feritoie - WDLN40 L.800mm 2 Feritoie"],
                            use_container_width=True,
                            return_value = "index",
                            key=f"{st.session_state.elencoNomiStanze[i]}{i+1}"
                            )

                            if st.session_state.elDifTip == 1:
                                   st.write("**Anteprima bocchetta installata**")
                                   st.image("images/FUTURE (installata).png")
                            if st.session_state.elDifTip == 2:
                                   st.write("**Anteprima diffusore installata**")
                                   st.image("images/DLAS40 (installata).png")
                            if st.session_state.elDifTip == 3:
                                   st.write("**Anteprima diffusore installata**")
                                   st.image("images/DLN40 (installata).png")

                            # Imposto colori in base all'elemento di diffusione selezionato
                            if st.session_state.elDifTip == 0:
                                   st.session_state.elencoColori = ["images/RAL9010.png", "images/Alluminio Anodizzato.png"]
                                   st.session_state.descrizioneColori = ["RAL9010", "Alluminio Anodizzato"]
                            elif st.session_state.elDifTip == 1 or st.session_state.elDifTip == 3:
                                   st.session_state.elencoColori = ["images/RAL9010.png", "images/RAL9016.png", "images/Alluminio Anodizzato.png"]
                                   st.session_state.descrizioneColori = ["RAL9010", "RAL9016", "Alluminio Anodizzato"]
                            else:
                                   st.session_state.elencoColori = []
                                   st.session_state.descrizioneColori = []
           
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

       elif st.session_state.locazioneImpianto == "Locale commerciale":
              for i in range(st.session_state.nStanze):
                     st.subheader(st.session_state.elencoNomiStanze[i])
                     with st.expander(f"**Seleziona Bocchetta / Diffusore per {st.session_state.elencoNomiStanze[i]}**", icon=":material/deployed_code:", expanded=True):
                            st.session_state.elDifTip = image_select(
                            label=f"Scegli l'elemento di diffusione che preferisci",
                            images=["images/WBMA.png","images/WLAF15.png","images/WGUR.png","images/WFUTURE15.png","images/WAQ1.png","images/WBQE3Q.png","images/DLAS40.png", "images/DLN40.png"],
                            captions=["Bocchetta a doppio filare di alette - WBMAV0 300x150mm","Bocchetta ad alette fisse - WLAF15 400x150mm","Bocchetta a microugelli orientabili su pannello - WGUR 1000x200mm","Bocchetta a barre fisse con telaio a scomparsa - WFUTURE15 400x150mm","Diffusore multidirezionale a 4 vie - WAQ1 225x225mm","Diffusore a flusso elicoidale - WBQE3Q 400x400","Diffusore lineare a scomparsa a singola feritoia - WDLAS40 L.1000mm","Diffusore lineare a feritoie - WDLN40 L.800mm 2 Feritoie"],
                            use_container_width=True,
                            return_value = "index",
                            key=f"{st.session_state.elencoNomiStanze[i]}{i+1}"
                            )

                            if st.session_state.elDifTip == 1:
                                   st.write("Anteprima bocchetta installata")
                                   st.image("images/FUTURE (installata).png")
                            if st.session_state.elDifTip == 2:
                                   st.write("Anteprima bocchetta installata")
                                   st.image("images/DLAS40 (installata).png")
                            if st.session_state.elDifTip == 3:
                                   st.write("Anteprima bocchetta installata")
                                   st.image("images/DLN40 (installata).png")

                            # Imposto colori in base all'elemento di diffusione selezionato
                            if st.session_state.elDifTip == 0 or st.session_state.elDifTip == 1 or st.session_state.elDifTip == 2:
                                   st.session_state.elencoColori = ["images/RAL9010.png", "images/Alluminio Anodizzato.png"]
                                   st.session_state.descrizioneColori = ["RAL9010", "Alluminio Anodizzato"]
                            elif st.session_state.elDifTip == 3 or st.session_state.elDifTip == 4 or st.session_state.elDifTip == 7:
                                   st.session_state.elencoColori = ["images/RAL9010.png", "images/RAL9016.png", "images/Alluminio Anodizzato.png"]
                                   st.session_state.descrizioneColori = ["RAL9010", "RAL9016", "Alluminio Anodizzato"]
                            elif st.session_state.elDifTip == 5 or st.session_state.elDifTip == 6:
                                   st.session_state.elencoColori = []
                                   st.session_state.descrizioneColori = []

                            if st.session_state.elencoColori:  # Solo se ci sono colori disponibili
                                   st.session_state.elDifCol = image_select(
                                   label=f"Scegli un colore",
                                   images=st.session_state.elencoColori,
                                   captions=st.session_state.descrizioneColori,
                                   use_container_width=True,
                                   return_value="index",
                                   key=f"elDifCol{i+1}"
                                   )

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
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

def grigliaRipresa():
       st.caption("Domanda 10 di 14")
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
                     portataGriglia = elemento
                     st.session_state.dimensioneGriglia = grigliaRipresaDimensioni[i]
                     break

       st.write("La griglia di ripresa è un componente che serve a recuperare l'aria dall'ambiente in modo che venga filtrata per trattenere polvere e impurità presenti, migliorando così la qualità dell'aria reimmessa nel sistema.")
       st.write()
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
                     st.session_state.page = "Elementi Diffusione"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", use_container_width=True):
                     st.session_state.page = "Posizionamento"
                     st.rerun()

def posizionamento():
       st.caption("Domanda 11 di 14")
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

def distanze():
       st.caption("Domanda 12 di 14")
       st.title("Distanze")
       st.write("**DEFINISCI LA DISTANZA TRA LA MACCHINA INTERNA E LE STANZE/LOCALI**")
       st.write("Dopo aver deciso dove posizionare la macchina interna in base allo spazio presente nel tuo alloggio/locale commerciale, definisci approssimativamente quanti metri passano tra dove verrà posizionata la macchina e il centro della stanza e/o parete/uscio della porta.")
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

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              st.image("images/MacchinaUscioPorta.png", caption="Se hai selezionato una bocchetta")
       with col2:
              st.image("images/MacchinaCentroStanza.png", caption="Se hai selezionato un diffusore")

       st.write("")

       ultimi_elementi = st.session_state.elencoElementiDiffusione[-st.session_state.nStanze:]
       #st.write(ultimi_elementi[0][1])
       #st.write(ultimi_elementi[1][1])

       for i in range(st.session_state.nStanze):
              with st.expander(f"**{st.session_state.elencoNomiStanze[i]}**", icon=":material/deployed_code:", expanded=True):
                     if ultimi_elementi[i][1] == 0:
                            labelDistanza = "uscio/porta"
                     else:
                            labelDistanza = "centro della stanza"
                     distanza = st.text_input(f"Distanza in metri tra macchina e {labelDistanza}", key=f"{st.session_state.elencoNomiStanze[i]}{i+1}")
                     if distanza and not distanza.isdigit():
                            st.error("Per favore, inserisci un valore numerico.")
                     elif distanza != "":
                            sommaDistanza += float(distanza)
                            if float(distanza) > 5 and float(distanza) <= 10:
                                   st.session_state.flagSanificante = True
                            elif float(distanza) > 10:
                                   flagSuRichiesta = True
                     else:
                            flagErrorDistanza = True
       
       if flagSuRichiesta != True:
              if st.session_state.flagSanificante == True:
                     st.session_state.scatoleFlessibile = int((math.ceil(int(sommaDistanza) / 10) * 10)/10)
                     st.session_state.prezzoFlessibile = float(st.session_state.scatoleFlessibile)*92.4
              else:
                     st.session_state.scatoleFlessibile = int((math.ceil(int(sommaDistanza) / 10) * 10)/10)
                     st.session_state.prezzoFlessibile = float(st.session_state.scatoleFlessibile)*46
       else:
              st.warning("[Configurazione solo su richiesta](https://www.widair.com/contattaci). Scrivici a mail: info@widair.com o chiamaci a cell. 3896699635")

       #st.write(sommaDistanza)
       #st.write(f"{st.session_state.prezzoFlessibile}€")
       #st.write(f"Mt flessibile necessario: {format(math.ceil(int(sommaDistanza) / 10) * 10, '.2f')}")

       if flagSuRichiesta or flagErrorDistanza:
              disabled = True
       else:
              disabled = False

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Posizionamento"
                     st.rerun()
       with col2:
              if st.button("**Avanti**", type="primary", disabled=disabled, use_container_width=True):
                     st.session_state.page = "Installazione"
                     st.rerun()

def installazione():
       st.caption("Domanda 13 di 14")
       st.title("Installazione")
       st.write("Desideri l'installazione?")

       if 'sceltaInstallazioneSi' not in st.session_state:
              st.session_state.sceltaInstallazioneSi = None
       if 'sceltaInstallazioneNo' not in st.session_state:
              st.session_state.sceltaInstallazioneNo = None
       if 'prezzoFinaleInstallazione' not in st.session_state:
              st.session_state.prezzoFinaleInstallazione = 0

       # ultimi_elementi_zone = st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:]
       #st.write(ultimi_elementi_zone)
       #for nome, nStanze in ultimi_elementi_zone:
       #       st.session_state.sommaZone += nStanze

       costoInstallazioneZone = int(st.session_state.sommaZone)*140
       if int(st.session_state.sommaZone) == 2:
              costoInstallazioneZone+=300
       elif int(st.session_state.sommaZone) == 3:
              costoInstallazioneZone+=400
       elif int(st.session_state.sommaZone) == 4:
              costoInstallazioneZone+=500
       elif int(st.session_state.sommaZone) == 5:
              costoInstallazioneZone+=600
       elif int(st.session_state.sommaZone) == 6:
              costoInstallazioneZone+=700
       else:
              costoInstallazioneZone+=800
       
       if st.session_state.sceltaControlloTemperatura == 1:
              costoInstallazioneZone += 50*int(st.session_state.sommaZone)

       if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
              if int(st.session_state.tempBTUHaier) == 12000:
                     costoInstallazioneMacchinario = 1150
              elif int(st.session_state.tempBTUHaier) == 18000 or int(st.session_state.tempBTUHaier) == 24000:
                     costoInstallazioneMacchinario = 1220
              elif int(st.session_state.tempBTUHaier) == 36000 or int(st.session_state.tempBTUHaier) == 43000 or int(st.session_state.tempBTUHaier) == 48000 or int(st.session_state.tempBTUHaier) == 55000:
                     costoInstallazioneMacchinario = 1380
       if st.session_state.tempBTUMitsubishi or st.session_state.tempBTUMitsubishi != None:
              if int(st.session_state.tempBTUMitsubishi) == 9000 or int(st.session_state.tempBTUMitsubishi) == 12000:
                     costoInstallazioneMacchinario = 1150
              elif int(st.session_state.tempBTUMitsubishi) == 18000 or int(st.session_state.tempBTUMitsubishi) == 21000 or int(st.session_state.tempBTUMitsubishi) == 24000:
                     costoInstallazioneMacchinario = 1220
              elif int(st.session_state.tempBTUMitsubishi) == 34000 or int(st.session_state.tempBTUMitsubishi) == 43000 or int(st.session_state.tempBTUMitsubishi) == 48000 or int(st.session_state.tempBTUMitsubishi) == 60000:
                     costoInstallazioneMacchinario = 1380
              elif  int(st.session_state.tempBTUMitsubishi) == 85000:
                     costoInstallazioneMacchinario = 1540

       st.session_state.prezzoFinaleInstallazione = format((costoInstallazioneZone+costoInstallazioneMacchinario)*1.5, '.2f')
       
       col1top, col2top = st.columns([0.5,0.5])
       with col1top:
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
       with col2top:
              with st.container(border=True):
                     st.image("images/36.png")
                     st.session_state.sceltaInstallazioneNo = st.checkbox("No", value=st.session_state.sceltaInstallazioneNo, on_change=lambda: (setattr(st.session_state, 'sceltaInstallazioneNo', True), setattr(st.session_state, 'sceltaInstallazioneSi', False)) if not st.session_state.sceltaInstallazioneNo else None)

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

def optional():
       st.caption("Domanda 14 di 14")
       st.title("Aggiungi Optional")

       if 'prezzoCopriclima' not in st.session_state:
              st.session_state.prezzoCopriclima = 0
       if 'prezzoIonizzatore' not in st.session_state:
              st.session_state.prezzoIonizzatore = 0
       if 'sceltaCopriclima' not in st.session_state:
              st.session_state.sceltaCopriclima = None
       
       st.subheader("Copriclima")
       st.session_state.sceltaCopriclima = image_select(
              label="Scegli il copriclima che preferisci",
              images=["images/Alfa.png", "images/Sirio.png","images/Antares.png", "images/Altair.png", "images/Vega.png", "images/36.png"],
              captions=["Copriclima Alfa", "Copriclima Sirio", "Copriclima Antares", "Copriclima Altair", "Copriclima Vega", "Nessun copriclima"],
              )

       if st.session_state.sceltaCopriclima != "images/36.png":
              st.session_state.prezzoCopriclima = 152.64
       else:
              st.session_state.prezzoCopriclima = 0

       st.divider()
       st.subheader("Ionizzatore")
       st.write("Modulo di sanitizzazione attiva antibatterica con ionizzazione negativa priva di formazione di ozono. Utilizzando questo dispositivo nell’impianto di distribuzione aria si ottiene una riduzione delle cariche microbiche, batteriche e virali sia nell’aria che sulle superfici di contatto dell’impianto stesso.")
       sceltaIonizzatore = image_select(
              label="Desideri integrare uno ionizzatore?",
              images=["images/Ionic.png", "images/36.png"],
              captions=["Ionizzatore IONIC", "Nessun ionizzatore"],
              return_value = "index",
              )
       if sceltaIonizzatore != 1:
              st.session_state.prezzoIonizzatore = 375
       else:
              st.session_state.prezzoIonizzatore = 0

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

       # Funzione Impianto
       st.subheader("Funzione impianto")
       if st.session_state.fattoreFunzioneImpianto == 150:
              st.caption("Riscaldamento & Raffreddamento")
       else:
              st.caption("Raffreddamento")
       st.divider()

       # Luogo Impianto
       st.subheader("Luogo impianto")
       st.caption(st.session_state.locazioneImpianto)
       st.divider()

       # Elementi di diffusione per stanza
       st.subheader("Stanze ed elementi diffusione")
       if st.session_state.locazioneImpianto == "Abitazione":
              associazione_nomi = {
              0: 'Bocchetta a doppio filare di alette - WBMAV0 300x150mm',
              1: 'Bocchetta a barre fisse con telaio a scomparsa - WFUTURE15 400x150mm',
              2: 'Diffusore lineare a scomparsa a singola feritoia - WDLAS40 L.1000mm',
              3: 'Diffusore lineare a feritoie - WDLN40 L.800mm 2 Feritoie',
              }
       else:
              associazione_nomi = {
              0: 'Bocchetta a doppio filare di alette - WBMAV0 300x150mm',
              1: 'Bocchetta ad alette fisse - WLAF15 400x150mm',
              2: 'Bocchetta a microugelli orientabili su pannello - WGUR 1000x200mm',
              3: 'Bocchetta a barre fisse con telaio a scomparsa - WFUTURE15 400x150mm',
              4: 'Diffusore multidirezionale a 4 vie - WAQ1 225x225mm',
              5: 'Diffusore a flusso elicoidale - WBQE3Q 400x400',
              6: 'Diffusore lineare a scomparsa a singola feritoia - WDLAS40 L.1000mm',
              7: 'Diffusore lineare a feritoie - WDLN40 L.800mm 2 Feritoie'
              }
       
       associazione_colori = {
              0: 'RAL 9010 - Panna',
              1: 'RAL 9016 - Bianco',
              2: 'Alluminio Anodizzato',
       }

       associazioni = {}

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
              st.write(f"**{nome}**")
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
              if flagSerranda == True:
                     st.caption("Serranda di regolazione inclusa.")

              st.caption(f"Plenum in pannello preisolato incluso con {st.session_state.elencoNZonePerStanza[-st.session_state.nStanze:][contatore][1]} attacchi")
              contatore += 1
              # Aggiungi al dizionario finale
              associazioni[nome] = nome_associato
       st.divider()

       # Controllo temperatura
       st.subheader("Controllo Temperatura")
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.session_state.sceltaControlloTemperatura == 0:
                     st.caption("Controllo della temperatura manuale")
              else:
                     if st.session_state.sceltaTipologiaSistema == 0:
                            st.caption(f"Controllo della temperatura motorizzato cablato - include serranda bypass montata sul plenum macchina, centralina, {st.session_state.nStanze} cronotermostati, interfaccia di comunicazione, scatola stagna e cablatura sistema")
                     else:
                            st.caption(f"Controllo della temperatura motorizzato wireless - include serranda bypass montata sul plenum macchina centralina, {st.session_state.nStanze} cronotermostati, interfaccia di comunicazione, scatola stagna e cablatura sistema")
       with col2:
              if st.session_state.sceltaControlloTemperatura != 0:
                     if st.session_state.sceltaTipologiaSistema == 0:
                            st.session_state.prezzoControlloTemperatura = 283.86 + (86.19*st.session_state.nStanze) + 231.62 + 50 + 100
                            st.write(f":green[**+ {format(st.session_state.prezzoControlloTemperatura, '.2f')}€**]")
                     else:
                            st.session_state.prezzoControlloTemperatura = 321.62 + (120.18*st.session_state.nStanze) + 231.62 + 50 + 100
                            st.write(f":green[**+ {format(st.session_state.prezzoControlloTemperatura, '.2f')}€**]")
       st.divider()

       # Scelta Macchina
       st.subheader("Macchina")
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
                     st.image(f"{config.macchinaHaier[f"BTU{int(st.session_state.tempBTUHaier)}"]['immagine']}")
              else:
                     st.image(f"{config.macchinaMitsubishi[f"BTU{int(st.session_state.tempBTUMitsubishi)}"]['immagine']}")
       with col2:
              if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
                     st.caption(f"{config.macchinaHaier[f"BTU{int(st.session_state.tempBTUHaier)}"]['descrizione']}")
              else:
                     st.caption(f"{config.macchinaMitsubishi[f"BTU{int(st.session_state.tempBTUMitsubishi)}"]['descrizione']}")

              if st.session_state.tempBTUHaier and st.session_state.tempBTUHaier != None:
                     prezzoMacchina = (config.macchinaHaier[f"BTU{int(st.session_state.tempBTUHaier)}"]['prezzo']*1.10) + 156.80
                     st.session_state.prezzoPlenumMacchina = config.macchinaHaier[f"BTU{int(st.session_state.tempBTUHaier)}"]['prezzoPlenumMacchina'] + (st.session_state.sommaZone * 3)
                     st.write(f":green[**+ {format(prezzoMacchina, '.2f')}€**]")
              else:
                     prezzoMacchina = (config.macchinaMitsubishi[f"BTU{int(st.session_state.tempBTUMitsubishi)}"]['prezzo']*1.10) + 100
                     st.session_state.prezzoPlenumMacchina = config.macchinaMitsubishi[f"BTU{int(st.session_state.tempBTUMitsubishi)}"]['prezzoPlenumMacchina'] + (st.session_state.sommaZone * 3)
                     st.write(f":green[**+ {format(prezzoMacchina, '.2f')}€**]")
       
       #Comandi
       if st.session_state.flagHaier != True:
              if st.session_state.prezzoComandoManualeMitsubishi != 0:
                     st.subheader("Comandi")
                     col1, col2 = st.columns([0.5,0.5])
                     with col1:
                            st.caption(f"{st.session_state.nomeComandoManualeMitsubishi}")
                     with col2:
                            st.write(":green[**+ 56.80€**]")

                     if st.session_state.prezzoWiFiComandoManualeMitsubishi != 0:
                            col1, col2 = st.columns([0.5,0.5])
                            with col1:
                                   st.caption("Hai integrato un modulo Wi-Fi al tuo impianto di climatizzazione")
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
              st.session_state.prezzoGriglia = config.listino_prezzi_accessori[f'Griglia di ripresa {st.session_state.dimensioneGriglia} mm']['prezzo']
              if st.session_state.coloreGriglia == 0 or st.session_state.coloreGriglia == 1:
                     st.session_state.prezzoGriglia = st.session_state.prezzoGriglia * 1.15
              
              # Prezzo Finale Griglia portafiltro
              #st.write(f":green[**+ {format(st.session_state.prezzoGriglia, '.2f')}€**]")
       st.divider()

       # Flessibile
       st.subheader("Flessibile")
       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.session_state.flagSanificante == True:
                     st.image("images/Sanificante.png")
              else:
                     st.image("images/Isolato.png")
       with col2:
              st.caption(f"Per il tuo impianto sono necessari {st.session_state.scatoleFlessibile*10} metri di flessibile")
              #st.write(f":green[**+ {format(st.session_state.prezzoFlessibile, '.2f')}€**]")
       st.divider()

       # Installazione
       if st.session_state.prezzoFinaleInstallazione != 0:
              st.subheader("Installazione")
              col1, col2 = st.columns([0.5,0.5])
              with col1:
                     st.caption("Hai richiesto l'installazione dell'impianto")
              with col2:
                     st.write(f":green[**+ {format(float(st.session_state.prezzoFinaleInstallazione), '.2f')}€**]")
              st.divider()

       # Optional
       if st.session_state.prezzoCopriclima != 0 or st.session_state.prezzoIonizzatore != 0:
              st.subheader("Optional")
              if st.session_state.prezzoCopriclima != 0:
                     st.write(f"**Copriclima**")
                     col1, col2 = st.columns([0.5,0.5])
                     with col1:
                            st.image(st.session_state.sceltaCopriclima)
                     with col2:
                            st.caption("Nascondi la tua unità esterna e rendila più indiscreta esteticamente")
                            #st.write(f":green[**+ {format(st.session_state.prezzoCopriclima, '.2f')}€**]")

              if st.session_state.prezzoIonizzatore != 0:
                     st.write(f"**Ionizzatore**")
                     col1, col2 = st.columns([0.5,0.5])
                     with col1:
                            st.image("images/IonicRiepilogo.png")
                     with col2:
                            st.caption("Modulo di sanificazione attiva antibatterica con ionizzazione negativa priva di formazione di ozono.")
                            #st.write(f":green[**+ {format(st.session_state.prezzoIonizzatore, '.2f')}€**]")
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

       # 55€ di spedizione + 35€ per ogni scatola di sanificante
       st.subheader("Totale Ordine")
       st.caption("Spedizione inclusa in tutta italia (isole comprese)")
       prezzoImponibileIniziale = float(st.session_state.prezzoPlenumMacchina) + float(st.session_state.prezzoBarraFilettata) + float(st.session_state.prezzoSerrandaBypass) + float(st.session_state.prezzoElementiDiffusione) + float(st.session_state.prezzoControlloTemperatura) + float(prezzoMacchina) + float(st.session_state.prezzoComandoManualeMitsubishi) + float(st.session_state.prezzoWiFiComandoManualeMitsubishi) + float(st.session_state.prezzoGriglia) + float(config.listino_prezzi_accessori[f'Griglia di ripresa {st.session_state.dimensioneGriglia} mm']['prezzoControtelaio']) + float(st.session_state.prezzoFlessibile) + float(st.session_state.scatoleFlessibile*35) + float(st.session_state.prezzoFinaleInstallazione) + float(st.session_state.prezzoCopriclima) + float(st.session_state.prezzoIonizzatore) + 55
       prezzoConIva = float(prezzoImponibileIniziale * 1.22)
       commissione = float((prezzoConIva * 3)/100)
       prezzoImponibileFinale = float(prezzoImponibileIniziale + commissione)
       st.session_state.prezzoFinale = float(prezzoImponibileFinale * 1.22)
                                  
       st.metric(value=f"{format(prezzoImponibileFinale, '.2f')}€", label=":lightgray[Prezzo IVA esclusa]")
       st.write(f"{format(st.session_state.prezzoFinale, '.2f')}€ (IVA inclusa)")

       col1, col2 = st.columns([0.5,0.5])
       with col1:
              if st.button("**Indietro**", type="secondary", use_container_width=True):
                     st.session_state.page = "Optional"
                     st.rerun()
       with col2:
              if st.button("**CONFERMA E PAGA**", type="primary", use_container_width=True):
                     st.session_state.page = ""
                     st.rerun()

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
    st.session_state.page = "Tipologia Impianto"

if st.session_state.page == "Tipologia Impianto":
    tipologiaImpianto()
elif st.session_state.page == "Funzione Impianto":
    funzioneImpianto()
elif st.session_state.page == "Luogo Impianto":
    luogoImpianto()
elif st.session_state.page == "Numero Stanze":
    numeroStanze()
elif st.session_state.page == "Definisci Stanze":
    definisciStanze()
elif st.session_state.page == "Controllo Temperatura":
    controlloTemperatura()
elif st.session_state.page == "Scelta Macchina":
    sceltaMacchina()
elif st.session_state.page == "Comandi":
    comandi()
elif st.session_state.page == "Elementi Diffusione":
    elementiDiffusione()
elif st.session_state.page == "Posizionamento":
    posizionamento()
elif st.session_state.page == "Griglia Ripresa":
    grigliaRipresa()
elif st.session_state.page == "Distanze":
    distanze()
elif st.session_state.page == "Installazione":
    installazione()
elif st.session_state.page == "Optional":
    optional()
elif st.session_state.page == "Riepilogo":
    riepilogo()
