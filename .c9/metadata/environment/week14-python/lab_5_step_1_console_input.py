{"filter":false,"title":"lab_5_step_1_console_input.py","tooltip":"/week14-python/lab_5_step_1_console_input.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":3},"action":"remove","lines":["\"\"\"","Your module description","\"\"\""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["import boto3","","def translate_text(**kwargs): ","    client = boto3.client('translate')","    response = client.translate_text(**kwargs)","    print(response) ","","### Change below this line only ###","","kwargs={","    \"Text\":\"I am learning to code in AWS\",","    \"SourceLanguageCode\":\"en\",","    \"TargetLanguageCode\":\"fr\"","    }","","def main():","    translate_text(**kwargs)","","if __name__==\"__main__\":","    main()",""],"id":2}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":0},"end":{"row":20,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1656284341056,"hash":"15ea65b677cd88032bc62d7d8219b5e58571d994"}