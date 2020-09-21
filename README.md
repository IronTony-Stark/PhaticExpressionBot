# PhaticExpressionBot
Chatbot which has no understanding of conversation. Chatbot's answers are only based on templates

## How to use
Bot parses _templates.txt_ and _defaults.txt_ files  
In _templates.txt_ are written patterns and answers to those patterns
Bot will try to find pattern that best matches user input. If there's such pattern, bot will take an answer to it
and send as a reply. If such pattern is absent, one of default answers will be used   
  
Patterns and answers in _templates.txt_ are written in the following format:  

~~~  
~priority#Pattern  
...  
~priority#Pattern  
@answer  
...  
@answer
~~~  
  
Where:
  
**Priority** is a number from 1 to 5. The lower the number the higher the priority. If several patterns match input, 
then pattern with the lowest priority number will be used
   
**Pattern** is a.. Well, pattern. It must be written in [regEx](https://en.wikipedia.org/wiki/Regular_expression) format.    
E.g `I('m|am) \w+` will match `I am Bob` or `I'm Bob` or even `I'm something else` 
 
**Answer** is written in plain text. If you used groups in pattern, you can get them with {groupIndex} syntax  
For example
```
#I'm (\w+)
@Hello, {0}
```
```
>I'm Bob
>Hello, Bob
```

You can create several patterns for the same answer and vice versa  
  
Bot also counts how many times different answers were given. Bot will send answer which was used least

Default answers also have priority and are also being counted. Firstly, answers with the highest priority (lowest
priority number) will be used. Once all of them were used once, bot will start to use answers with the second
highest priority etc 
 
