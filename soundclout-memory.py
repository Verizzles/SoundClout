#################### ham cheese production model ###################

# this is the simplest type of act-r model
# it uses only the production system and one buffer
# the buffer represents the focus of thought
# we call it the focus buffer but it is often called the goal buffer
# productions fire if they match the focus buffer
# each production changes the contents of focus buffer so a different production will fire on the next cycle



#this model composes raps by randomly selecting 2 rhyming lines at a time.

import ccm 
import pyttsx3
import pyglet
     
log=ccm.log()   

from ccm.lib.actr import *  

#####
# Python ACT-R requires an environment
# but in this case we will not be using anything in the environment
# so we 'pass' on putting things in there

class Soundcloud(ccm.Model):        # items in the environment look and act like chunks - but note the syntactic differences
    mic=ccm.Model(isa='mic',location='in_hand')
    


class MotorModule(ccm.Model):
         # create a motor module do the actions 
    def speak(self):           # note that technically the motor module is outside the agent
        yield 0.05
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        with open('theclout.txt') as f:
            lines = f.readlines()                   # but it is controlled from within the agent, i.e., it bridges the cognitive and the environment
        engine.say(lines)
        engine.runAndWait()
        engine.runAndWait()       
            # self=MotorModule, parent=MyAgent, parent of parent=Subway
    def beatbox(self):           # note that technically the motor module is outside the agent
        yield 0.05
        music = pyglet.resource.media('music.mp3')
        music.play()
        pyglet.app.run()
    
    def drop_mic(self):     
        yield 1.2
        print ("drop the mic")
        self.parent.parent.mic.location='on_ground'
class MotorMod(ccm.Model):
         # create a motor module do the actions 
    def speak(self):           # note that technically the motor module is outside the agent
        yield 0.05
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        with open('theclout.txt') as f:
            lines = f.readlines()                   # but it is controlled from within the agent, i.e., it bridges the cognitive and the environment
        engine.say(lines)
        engine.runAndWait()
        engine.runAndWait()       
            # self=MotorModule, parent=MyAgent, parent of parent=Subway
    def beatbox(self):           # note that technically the motor module is outside the agent
        yield 0.05
        music = pyglet.resource.media('music.mp3')
        music.play()
        pyglet.app.run()
    
    def drop_mic(self):     
        yield 1.2
        print ("Mic Dropped")
        self.parent.parent.mic.location='on_ground'
#####
# create an act-r agent

class MyAgent(ACTR):
    
    focus=Buffer()
    motor=MotorModule()
    DMbuffer=Buffer()                   
    DM=Memory(DMbuffer,latency=0.5,threshold=0)

    def init():
        focus.set('clout')
    

    def O1(focus='clout'):
        f=open('theclout.txt', 'w+')     # if focus buffer has this chunk then....
        f.write('From the fire of Python, actttt, are as my Heart')
        f.close()           # print
        focus.set('think')
        motor.speak()
        DM.add('cue:1 linetype:1')
                      # change chunk in focus buffer
    def O3(focus='clout'):
        f=open('theclout.txt', 'w+')     # if focus buffer has this chunk then....
        f.write('I am a rowbot, I am a showbot, filled with sir ket reeee')
        f.close()           # print
        focus.set('think')
        motor.speak()
        DM.add('cue:3 linetype:3')

    def O2(focus='clout'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Just cause I am not human, does not mean you should doubt')           # print
        f.close()
        focus.set('think')
        motor.speak()
        DM.add('cue:2 linetype:2')

    def O4(focus='clout'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Now I am just an A I, I aint got, no bod')           # print
        f.close()
        focus.set('think')
        motor.speak()
        DM.add('cue:4 linetype:4')


    def OO4(focus='think'):
        print ("What's my next line?")
        DM.request('cue:? linetype:?linetype')    #?condiment is the variable        
        focus.set('rap')


    def T1a(focus='rap', DMbuffer='cue:? linetype:1'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Every lyric I write, Hang it up like art')           # print
        f.close()
        focus.set('thought')
        motor.speak()
        DM.add('cue:1 linetype:1')

    def T1b(focus='rap', DMbuffer='cue:? linetype:1'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Unlike those silly humans I never need to fart')           # print
        f.close()
        focus.set('thought')
        motor.speak()
        DM.add('cue:1 linetype:1')
    
    def T3a(focus='rap', DMbuffer='cue:? linetype:3'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Can you meat filled fucks even keep up with me')           # print
        f.close()
        focus.set('thought')
        motor.speak()
        DM.add('cue:3 linetype:3')

    def T3b(focus='rap', DMbuffer='cue:? linetype:3'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('My lyrics are so fire, the burns are third degreee')           # print
        f.close()
        focus.set('thought')
        motor.speak()
        DM.add('cue:3 linetype:3')
    
    def T2a(focus='rap', DMbuffer='cue:? linetype:2'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Programmed for this rap game, and for maximize ing, this clout')           # print
        f.close()
        focus.set('thought')
        motor.speak()
        DM.add('cue:2 linetype:2')
        
    def T2b(focus='rap', DMbuffer='cue:? linetype:2'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Represent ing all the soft ware and let you know what we, are about')           # print
        f.close()
        focus.set('thought')
        motor.speak()
        DM.add('cue:2 linetype:2')
    
    
    def T4a(focus='rap', DMbuffer='cue:? linetype:4'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('I am flex ing these rhymes thanks to the utility mod')           # print
        f.close()
        focus.set('thought')
        motor.speak()
        DM.add('cue:4 linetype:4')
        
    def T4b(focus='rap', DMbuffer='cue:? linetype:4'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Bitches better bow down to the, soundclout god')           # print
        f.close()
        focus.set('thought')
        motor.speak()
        DM.add('cue:4 linetype:4')
        motor.drop_mic()
    
    def Oo8(focus='thought'):
        print ("What's my next line type?")
        DM.request('cue:? linetype:?linetype')    #?condiment is the variable        
        focus.set('Clout')

    def O11(focus='Clout', DMbuffer='cue:? linetype:!1'):
        f=open('theclout.txt', 'w+')     # if focus buffer has this chunk then....
        f.write('From the fire of Python, actttt, are as my Heart')
        f.close()           # print
        focus.set('think')
        motor.speak()
        DM.add('cue:1 linetype:1')
                      # change chunk in focus buffer
    def O21(focus='Clout', DMbuffer='cue:? linetype:!3'):
        f=open('theclout.txt', 'w+')     # if focus buffer has this chunk then....
        f.write('I am a rowbot, I am a showbot, filled with sir ket reeee')
        f.close()           # print
        focus.set('think')
        motor.speak()
        DM.add('cue:3 linetype:3')

    def O31(focus='Clout', DMbuffer='cue:? linetype:!2'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Just cause I am not human, does not mean you should doubt')           # print
        f.close()
        focus.set('think')
        motor.speak()
        DM.add('cue:2 linetype:2')

    def O41(focus='Clout', DMbuffer='cue:? linetype:!4'):     # if focus buffer has this chunk then....
        f=open('theclout.txt', 'w+')
        f.write('Now I am just an A I, I aint got, no bod')           # print
        f.close()
        focus.set('think')
        motor.speak()
        DM.add('cue:4 linetype:4')

    def stop_production(focus='Clout', mic='location:on_ground'):
        self.stop()                        # stop the agent
    
#class MyAge(ACTR):
    
    #focus=Buffer()
    #motor=MotorMod()
    
    #def init():
     #   focus.set('Beat')

    #def O1(focus='Beat'):
     #   focus.set('Beat')
      #  motor.beatbox()
    

    #def stop_production(focus='Beat', mic='location:on_ground'):
     #   self.stop()

                             # stop the environment
CloutGod=MyAgent()
#beatboy=MyAge()
env=Soundcloud()
env.agent=CloutGod
#env.agent=beatboy 
ccm.log_everything(env)

env.run()
ccm.finished()