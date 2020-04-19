

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

    # first string: key to retrieve preset in sounds' dict, second string: how it is diplayed in the GUI
    bank_list=[
        ('Studio Set',1,'Studio Set'),
        ('Supernatural',2,'Supernatural'),
    ]
    
    sounds={
            "Studio Set": [
                ("",[85,64,1],"FA Preview"),
                ("",[85,64,2],"Jazz Duo")
            ],
            "Supernatural": [
                ("",[89,64,1],"Piano: Full Grand 1"),
                ("",[85,64,21],"E.Piano: Phaser Dyno"),
                ("",[85,64,89],"Ensemble Strings: StringsSect1"),
            ]
    }

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
        preset_list = self.sounds[bank[0]]
        print(preset_list)
        return preset_list   

    #----------------------------------------------------------------------------
    # Controllers Managament
    #----------------------------------------------------------------------------
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
