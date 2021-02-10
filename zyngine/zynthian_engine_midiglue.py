# -*- coding: utf-8 -*-

from . import zynthian_engine

#------------------------------------------------------------------------------
# Passing by MIDI instrument selection
#------------------------------------------------------------------------------

class zynthian_engine_midiglue(zynthian_engine):

    # ---------------------------------------------------------------------------
    # Controllers & Screens
    # ---------------------------------------------------------------------------

    _ctrls=[
        ['volume',7,100],
        ['modulation',1,0],
        ['pan',10,64],
        ['portamento on/off',65,'off','off|on'],
        ['portamento time',5,0],
        ['resonance',71,64],
        ['release time',72,64],
        ['attack time',73,64],
        ['cutoff',74,64],
        ['decay time',75,64],
        ['sustain on/off',64,'off','off|on'],
        ['sostenuto on/off',66,'off','off|on'],
        ['soft on/off',67,'off','off|on'],
        ['vibrato rate',76,64],
        ['vibrato depth',77,64],
        ['vibrato delay',78,64],
        ['effect 1 reverb',91,64],
        ['effect 3 chorus',93,0]
    ]


    _ctrl_screens=[
        ['main',['volume','modulation','pan']],
        ['sound',['resonance', 'cutoff', 'effect 1 reverb', 'effect 3 chorus']],
        ['pedals', ['sustain on/off', 'sostenuto on/off', 'soft on/off']],
        ['portamento', ['portamento on/off', 'portamento time']],
        ['vibrato', ['vibrato rate', 'vibrato depth', 'vibrato delay']],
        ['envelope', ['attack time', 'decay time', 'release time']]
    ]


    #----------------------------------------------------------------------------
    # Initialization
    #----------------------------------------------------------------------------

    def __init__(self, zyngui=None):
        super().__init__(zyngui)
        self.name = "MidiGlue"
        self.nickname = "MG"
        # aiming at Roland FP-30
        self.jackname = "Roland Digital Piano"

        self.options['midi_chan']=True

        self.preset = ""
        self.preset_config = None
        
        # location where data about midi banks should be stored
        self.banks_dirs=[
            ('EX', self.ex_data_dir + "/midiglue"),
            ('MY', self.my_data_dir + "/midiglue"),
            ('_', self.data_dir + "/midiglue")
		]
  
        #self.command=("/usr/bin/xev", "-rv")
        self.start()
        self.reset()

    # ---------------------------------------------------------------------------
    # Layer Management
    # ---------------------------------------------------------------------------

    # ---------------------------------------------------------------------------
    # MIDI Channel Management
    # ---------------------------------------------------------------------------

    def set_midi_chan(self, layer):
        self.setup_router(layer)
      
    #----------------------------------------------------------------------------
    # Bank Managament
    #----------------------------------------------------------------------------

    def get_bank_list(self, layer=None):
        # each CSV file in data directory is a bank
        return self.get_filelist(self.banks_dirs,"csv")

        #return self.bank_list

    #----------------------------------------------------------------------------
    # Preset Managament
    #----------------------------------------------------------------------------

    def get_preset_list(self, bank):
        import csv
        # open bank file, retrieve instruments
        preset_list=[]
        with open(bank[0], newline='\n') as csvfile:
            bankreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for row in bankreader:
                preset_list.append(("",[int(row['MSB']),int(row['LSB']),int(row['PC'])],row['name']))
        return preset_list   

    #----------------------------------------------------------------------------
    # Controllers Managament
    #----------------------------------------------------------------------------
    #    # bad attempt at dynamically selcting output MIDI device, left because could inspire future work
    #    def send_controller_value(self, zctrl):
    #        print("change control")
    #        val = zctrl.get_value()
    #        print(val)
    #        if val == 0:
    #            return
    #        if val > 64:
    #            jackname = "KMidimon"
    #        else:
    #            jackname = "events-in"
    #        if jackname != self.jackname:
    #            self.jackname = jackname
    #            print("switch to: " + jackname)
    #            zynthian_engine_midiglue._ctrls=[
    #                 ['volume',7,val],
    #                 ['modulation',1,0],
    #                 ['ctrl 2',2,0],
    #                 ['ctrl 3',3,0]
    #            ]
    #            self.stop()
    #            self.refresh_all()
            
    #--------------------------------------------------------------------------
    # Special
    #--------------------------------------------------------------------------


#******************************************************************************