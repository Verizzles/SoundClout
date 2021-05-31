import ccm
import pyttsx3
from speech import *
from ccm.lib.actr import * 

"""
This program will hopefully allow people to run experiments using a phonological loop in python ACT-R
Words should be presented in a list form ala: list = ["word1", "word2" , "word3".......etc]
The speech feels a bit gimmicky but it's a fun gimmick and I'm sticking to it
I also name my variables wildly because I am making this up as I go along and I like to use cusswords when I'm frustrated
"""

class Taint():
  
          
    
  def __init__(self):
    self.busy=False
   
      
         
   
  """
  very ugly method to get words in a form that they can be added to the declarative memory and later recalled
  remove the #'s from the print statements to make sure the strings look like some good shit ACT-R chunks
  """  
  def word(self, text):
    p = text
    word = ("isa:word" + " word:"+ p)
    return word
    

  
  


    
    
class Loop(ccm.Model):
   
  
  

  def __init__(self):    
    self.huff = Taint()
    
    
    
  """
  This will say everything and add the words to the declarative memory
  """
  def words(self, text):
    
    com = self.huff.word(text)
    
    return com
    
  
    
#

    
    