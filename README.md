# utf8decoder
An utf8 decoder functionality to transform encoded paragraphs to human readable text. 

What can you do with this code? 
Function 'create_dictionary()' maps from information facilitated by utf8-chartable.de to a programmatic dictionary ready to be used in Python implementations. 

Using this dictionary, using a function from re such as re.sub, you can provide the text_transform function to create a relational mapping from a non-readable text to human readable text. 

Example: 

re.sub(r'.?\\\w{1,3}\\\w{1,3}.?', text_transformer, str)

Regex pattern matches a utf-8 encoded character with possible not related character behind and afterwards. 
