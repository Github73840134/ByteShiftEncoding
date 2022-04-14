# Byte Shift Encoding
#### A string encoder
The point of Byte Shift Encoding is for light encoding
that adds just the right amount of privacy to any ASCII text.  

I created this for times when putting map coordinates into projects and wondering if someone came across my project, would it be detremental to me.  

Privacy matters a lot to me, And I hope it does to you too.  
## How to use
Copy bse.py into your project and your ready to go
## Encoding Data
```bse.encode(Input,encoding=8)```  
Encode Input with a encoding.  
### * I recommend using 256, as it's a lot harder to rip apart
level can be 2-256, DONT USE 1 as it wont shift at all.  
Returns the shifted string
## Decoding Data with known encosion level
```bse.decode(encoded,encoding=8)```  
Decodes text with a level.  
Returns the unshifted string.  
## Decoding Data with unknown encosion level
```bse.autodecode(encoded,return_decosion_level=False)```  
Automatidcally decodes text with a level.  
Setting ```return_decosion_level``` True will return the decoded text along with the decosion level.  
Returns the unshifted string.  
## Getting encosion level
```bse.getlevel(encoded)```  
Returns the encosion level.  

©2022 SethEdwards