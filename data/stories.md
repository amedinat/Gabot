## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## customer_good_mood
* mood_great
  - utter_happy

## customer_happy_comercial_path
* customer_contact_commercial{"gtk_contact":"comercial"}
    - utter_moreinfo
    - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## customer_mood_unhappy
* mood_unhappy  
  - utter_unhappy
  
## customer_sucessCases
* wanna_know_sucessCases
    -utter_wanna_know_sucessCases
    - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## who_are_you
* company_info
    -utter_Gattaca_Info
    -utter_ourservices

## customer_interest_path
* customer_interest
    -utter_Gattaca_Info
    -utter_ourservices

## customer_contact_operations
* customer_contact_operations{"gtk_contact":"soporte"}
    - utter_moreinfo
    - operations_form                   <!--Run the sales_form action-->
    - form{"name": "operations_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## customer_form_operations_stop_but_continue
* customer_contact_operations{"gtk_contact":"soporte"}
    - utter_moreinfo
    - operations_form                   <!--Run the sales_form action-->
    - form{"name": "operations_form"}   <!--Activate the form-->
* stop
    - utter_ask_continue    
    - form{"name": null}  
* affirm
    - operations_form    
    - form{"name": "operations_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail     
 * thankyou
    - utter_noworries
    - utter_goodbye

## customer_want_talk_to_boss
* customer_contact_manager{"gtk_contact":"gerencia"}    
    - manager_form                   <!--Run the sales_form action-->
    - form{"name": "manager_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## Customer_interested_developmment
*customer_choice_development{"service":"desarrollo"}   
  - utter_Development_Info
  - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## Customer_interested_BPM
*customer_choice_BPM{"service":"BPM"}   
  - utter_BPM_Info
  - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## Customer_interested_Consultancy
*customer_choice_consultancy{"service":"consultoría"}   
  - utter_Consultancy_Info
  - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## Contact_Manager_Path_2

* greet
    - action_greet
    - slot{"gtk_contact":"gerente"}
* customer_contact_manager{"gtk_contact":"gerente"}
    - manager_form
    - form{"name":"manager_form"}
    - slot{"requested_slot":"person_name"}
* mood_unhappy
    - manager_form
    - slot{"person_name":"Felipe"}
* inform
    - manager_form
    - slot{"business_email":"billgates@microsoft.com"}
* inform
    - manager_form
    - slot{"person_mobile":"484561561"}
* affirm
    - manager_form
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail

## Contact_Manager_Path_3

* greet
    - action_greet
* customer_interest
    - utter_Gattaca_Info
    - utter_ourservices
    - action_default_fallback
    - slot{"gtk_contact":"gerente"}
* customer_contact_manager{"gtk_contact":"gerente"}
    - manager_form
    - form{"name":"manager_form"}
    - slot{"requested_slot":"person_name"}
* inform
    - manager_form
    - slot{"person_name":"Jairo"}
* mood_unhappy
    - manager_form
    - slot{"business_email":"dsadsad"}
* inform
    - manager_form
    - slot{"person_mobile":"45665"}
    - slot{"service":"ChatBots"}
* customer_choice_RPA{"service":"ChatBots"}
    - manager_form    
    - slot{"company":"Rasa ChatBots"}
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## Custom_Dev_Path1
* greet
    - action_greet
    - slot{"service":"Python"}
* customer_interest{"service":"Python"}
    - utter_Gattaca_Info
    - utter_ourservices
* customer_choice_development
    - utter_Development_Info
    - sales_form
    - form{"name":"sales_form"}
    - slot{"requested_slot":"person_name"}
    - slot{"person_short_name":"Julio"}
* inform{"person_short_name":"Julio"}
    - sales_form
    - slot{"person_name":"Julio"}
    - slot{"person_short_name":"Julio Ltda"}
* inform{"person_short_name":"Julio Ltda"}
    - sales_form
    - slot{"company":"Julio Ltda"}
* inform
    - sales_form
    - slot{"business_email":"mnklnhñlkn@sdsada.com"}
* inform
    - sales_form
    - form{"name":null}
    - slot{"person_mobile":"456141658"}
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## Product_Bizagi
* greet
    - action_greet
    - slot{"product":"Bizagi"}
* customer_interest{"product":"Bizagi"}
    - utter_BPM_Info
    - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## Product_Appian
* greet
    - action_greet
    - slot{"product":"Appian"}
* customer_interest{"product":"Appian"}
    - utter_BPM_Info
    - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## Product_Bonita
* greet
    - action_greet
    - slot{"product":"Bonita"}
* customer_interest{"product":"Bonita"}
    - utter_BPM_Info
    - sales_form                   <!--Run the sales_form action-->
    - form{"name": "sales_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
    - action_send_mail 
* thankyou
    - utter_noworries
    - utter_goodbye

## chitchat
* customer_interest
    - sales_form
    - form{"name": "sales_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## explain person_name slot
* customer_interest
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "person_name"}
* explain
    - utter_explain_person_name
    - sales_form
    - slot{"product": "Bizagi"}    
    - form{"name": null}

## New Story

* inform
    - utter_Gattaca_Info
    - utter_ourservices

## New Story

* inform
    - utter_Gattaca_Info
    - utter_ourservices
