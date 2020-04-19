

from . import zynthian_engine

#------------------------------------------------------------------------------
# Puredata Engine Class
#------------------------------------------------------------------------------

class zynthian_engine_midiglue(zynthian_engine):

    # ---------------------------------------------------------------------------
    # Controllers & Screens
    # ---------------------------------------------------------------------------

    _ctrls=[
        ['volume',7,96],
        ['modulation',1,0],
        ['ctrl 2',2,0],
        ['ctrl 3',3,0]
    ]

    _ctrl_screens=[
        ['main',['volume','modulation','ctrl 2','ctrl 3']]
    ]

    bank_list=[
        ('Steinway D',1,'Steinway D','_','D4:A'),
        ('Steinway B',2,'Steinway B','_','Modelb:A'),
    ]

    #----------------------------------------------------------------------------
    # Initialization
    #----------------------------------------------------------------------------

    def __init__(self, zyngui=None):
        super().__init__(zyngui)
        self.name = "MidiGlue"
        self.nickname = "MG"
        self.jackname = "MidiGlue"

        self.options['midi_chan']=True

        self.preset = ""
        self.preset_config = None
        print("I'm alive!")
        #self.bank_dirs = [
        #    ('_', self.my_data_dir + "/presets/puredata")
        #]

        #self.base_command=("/usr/bin/pd", "-jack", "-rt", "-alsamidi", "-mididev", "1", "-send", ";pd dsp 1")       
        self.command=("/usr/bin/xev", "-rv")


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
        return self.bank_list

    #def set_bank(self, layer, bank):
    #    print("Should set bank")
    #   pass


    #----------------------------------------------------------------------------
    # Preset Managament
    #----------------------------------------------------------------------------

    def get_preset_list(self, bank):
        print('Getting Preset List for from bank:')
        print(bank)
        # hacking something just for debug now
        preset_list=[]
        for i in range(0, 10):
            path = ""
            bank_msb = i
            bank_lsb = 10+i
            prg = 20+i
            preset_list.append((path,[bank_msb,bank_lsb,prg],"preset" + str(i), i))
        print(preset_list)
        return preset_list

   

    #----------------------------------------------------------------------------
    # Controllers Managament
    #----------------------------------------------------------------------------

 
    #--------------------------------------------------------------------------
    # Special
    #--------------------------------------------------------------------------


#******************************************************************************
