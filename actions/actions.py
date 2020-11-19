# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import logging
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

logger = logging.getLogger(__name__)
vers = "vers: 0.1.0, date: Octubre 09, 2020"
logger.debug(vers)


#===============CONSTANTS=====================
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

FROM_EMAIL_ADDRESS = 'notificaciones@e-gattaca.com'
FROM_EMAIL_PASSWORD ='Bogota.GTK.2019*'

#TO_SALES_EMAIL_ADDRESS  = 'comercial@gattaca.co'
#TO_OPERATIONS_EMAIL_ADDRESS  = 'antonio.almonacid@gattaca.co'
#TO_BOSS_EMAIL_ADDRESS  = 'comercial@gattaca.co'

TO_SALES_EMAIL_ADDRESS  = 'jmedina@gattaca.co'
TO_OPERATIONS_EMAIL_ADDRESS  = 'jmedina@gattaca.co'
TO_BOSS_EMAIL_ADDRESS  = 'jmedina@gattaca.co'

#===========================================


#===============ACTIONS=====================
class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template ="utter_greet")        
        return [UserUtteranceReverted()]

class ActionFallBack(Action):
    """Fail Gracefully"""

    def name(self):
        return "action_default_fallback"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template ="utter_i_cant_do_that")        
        return [UserUtteranceReverted()]


class SendMail(Action):
    def name(self):
        return 'action_send_mail'
    def run(self, dispatcher, tracker, domain):
        try:
            
           import os
           import smtplib
           from email.message import EmailMessage
           
           msg = EmailMessage()
           msg['Subject'] = tracker.get_slot('email_subject')
           msg['From'] = FROM_EMAIL_ADDRESS #sender's email address
           msg['To'] = tracker.get_slot('email_to_address')             
           msg.set_content(tracker.get_slot('email_message')) 
           
           logger.debug(tracker.get_slot('email_to_address'))    
           logger.debug("=========================")
           logger.debug(tracker.get_slot('email_message'))    
           logger.debug("=========================")
           logger.debug("Correo listo para enviar.")        
           
           with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
               smtp.login(FROM_EMAIL_ADDRESS, FROM_EMAIL_PASSWORD)	
               smtp.send_message(msg)
               
           return []
        except:
            logger.debug("Error al Enviar correo.")
            return []


#===============FORMS=====================
class TheBossForm(FormAction):
    """Collects manager information and adds it to the spreadsheet"""

    def name(self):
        return "manager_form"
    
    @staticmethod
    def required_slots(tracker):
        return [
            "business_email",
            "person_name",            
            "person_mobile",        
            "company",
            "boss_comments"
            ]
    
    def slot_mappings(self):     
        
    
      return {"business_email": [self.from_entity(entity="business_email"), self.from_text()],
                "person_name": [self.from_entity(entity="person_name"), self.from_text()],                
                "person_mobile": [self.from_entity(entity="person_mobile"), self.from_text()],
                "company": [self.from_entity(entity="company"), self.from_text()],                
                "boss_comments": [self.from_entity(entity="boss_comments"), self.from_text()],                  
                "email_subject": [self.from_entity(entity="email_subject"),self.from_text()] ,
                "email_to_address": [self.from_entity(entity="email_to_address"), self.from_text()]    
                }  
  
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
      
        personEmail = tracker.get_slot("business_email")
        personName = tracker.get_slot("person_name")
        companyName = tracker.get_slot("company")
        personMobile = tracker.get_slot("person_mobile")
        bossComments = tracker.get_slot("boss_comments")
        
                        
        Message =('Hola Jefe,\nSe ha comunicado con nosotros \"{}\" de la compañía \"{}\", y nos comenta que: \"{}\".\nSu número de contacto es \"{}\" y su correo electrónico \"{}\".\n\nQuedo a tus ordenes.\n\nAtentamente,\nGaBot'.format(personName, companyName, bossComments, personMobile, personEmail))
        SlotSet("email_message", Message)
        
        logger.debug(Message)    
        
        dispatcher.utter_message("Ya tengo todos los datos. Le enviaré la información a mi jefe y te contactará próximamente.")
        return [
                SlotSet("email_message", Message),
                SlotSet("email_subject", "GABOT - Contacto al Gerente"),
                SlotSet("email_to_address", TO_BOSS_EMAIL_ADDRESS)
                ]



class OperationForm(FormAction):
    """Collects operations information"""

    def name(self):
        return "operations_form"
    
    @staticmethod
    def required_slots(tracker):
        return [
            "business_email",
            "person_name",
            "company",        
            "company_project",                    
            "person_mobile"        
            ]
    
    def slot_mappings(self):     
        
        return {"business_email": [self.from_entity(entity="business_email"), self.from_text()],
                "person_name": [self.from_entity(entity="person_name"), self.from_text()],
                "company": [self.from_entity(entity="company"), self.from_text()],
                "company_project": [self.from_entity(entity="company_project"), self.from_text()],                  
                "person_mobile": [self.from_entity(entity="person_mobile"), self.from_text()],
                "email_subject": [self.from_entity(entity="email_subject"),self.from_text()] ,
                "email_to_address": [self.from_entity(entity="email_to_address"), self.from_text()]    
                }  
        
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        personEmail = tracker.get_slot("business_email")
        personName = tracker.get_slot("person_name")
        companyName = tracker.get_slot("company")
        personMobile = tracker.get_slot("person_mobile")
        askProyecto = tracker.get_slot("company_project")
        
                        
        Message =('Hola,\nSe ha comunicado con nosotros \"{}\" de la compañía \"{}\", del proyecto \"{}\".\nSu número de contacto es \"{}\" y su correo electrónico \"{}\".\n\nTe agradezco tu ayuda en atender esta solicitud.\n\nAtentamente,\nGaBot'.format(personName, companyName, askProyecto, personMobile, personEmail))
        SlotSet("email_message", Message)
        
        logger.debug(Message)    
        
        dispatcher.utter_message("Ya tengo todos los datos. Un compañero de Operaciones te contactará en breve.")
        return [
                SlotSet("email_message", Message),
                SlotSet("email_subject", "GABOT - Contacto Operaciones"),
                SlotSet("email_to_address", TO_OPERATIONS_EMAIL_ADDRESS)
                ]
    
     
class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "sales_form"
    
    @staticmethod
    def required_slots(tracker):
        return [
            "business_email",
            "person_name",
            "company",
            "person_mobile"        
            ]
    
    def slot_mappings(self):                      
        
        return {"business_email": [self.from_entity(entity="business_email"), self.from_text()],
                "person_name": [self.from_entity(entity="person_name"), self.from_text()],
                "company": [self.from_entity(entity="company"), self.from_text()],                
                "person_mobile": [self.from_entity(entity="person_mobile"), self.from_text()],
                "email_subject": [self.from_entity(entity="email_subject"),self.from_text()] ,
                "email_to_address": [self.from_entity(entity="email_to_address"), self.from_text()]    
                }
    
    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:        
    
        personEmail = tracker.get_slot("business_email")
        personName = tracker.get_slot("person_name")
        companyName = tracker.get_slot("company")
        personMobile = tracker.get_slot("person_mobile")
        askService = tracker.get_slot("service")
        askProduct = tracker.get_slot("product")     
                        
        Message =('Hola,\nSe ha comunicado con nosotros \"{}\" de la compañía \"{}\", porqué está interesado en \"{}-{}\".\nSu número de contacto es \"{}\" y su correo electrónico \"{}\".\n\nTe agradezco tu ayuda en atender esta solicitud.\n\nAtentamente,\nGaBot'.format(personName, companyName, askService, askProduct, personMobile, personEmail))
        SlotSet("email_message", Message)
        
        logger.debug(Message)    
        
        dispatcher.utter_message("Ya tengo todos los datos. Un compañero de Comercial te contactará muy pronto.")                   
        return [
                SlotSet("email_message", Message),
                SlotSet("email_subject", "GABOT - Contacto Comercial"),
                SlotSet("email_to_address", TO_SALES_EMAIL_ADDRESS)
                ]
         
        
    