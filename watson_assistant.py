# -*- coding: UTF-8 -*-

from watson_developer_cloud import AssistantV1, WatsonApiException
import json, ast
#from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

def get_response_from_watson_assistamt(url, username, password, version, workspace_id):

    print "Enter your text here"
    inpt = raw_input('>>>')

    input_text={}
    input_text['text'] = str(inpt)

    # Initialize assistant
    assistant = AssistantV1(
        version=version,
        username=username,
        password=password,
        url=url
        )
    
    # Try to send request
    try:
        response = assistant.message(
            workspace_id=workspace_id,
            input=input_text
        ).get_result()
        # print(json.dumps(response, indent=2))

        # Returned answer string manupulation
        j = json.dumps(response, indent=2)
        out_json = json.loads(j)
        output = out_json['output']['text'][0]  # *** check here ***
        
        return output

    except WatsonApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

def get_response_from_language_translator(url, username, password):
    """
    language_translator = LanguageTranslator(
    username=username,
        password=password,
        url=url
    )
    try:
        translation = language_translator.translate(
        text='Hello',
        model_id='en-es')
        print(json.dumps(translation, indent=2, ensure_ascii=False))

        # Returned answer string manupulation
        j = json.dumps(response, indent=2)
        out_json = json.loads(j)
        output = out_json['output']['text'][0]  # *** check here ***
        
        return output

    except WatsonApiException as ex:
        return "Method failed with status code " + str(ex.code) + ": " + ex.message

    """
    return 0



def main():
    # Necessary credentials
    version= <'version'>
    username = <'username'>
    password = <'password'>
    url = <'url'>
    workspace_id= <'workspace_id'>
    
    
    # Send input text to watson conversation api and get the response of assistant
    assistant_response = get_response_from_watson_assistamt(url, username, password, version, workspace_id)
    print(assistant_response)
    
    # Send response from watson assistan to language translator and get response of it
    translator_response = get_response_from_language_translator(url, username, password)
    print(translator_response)
    

if __name__ == "__main__":
    main()
