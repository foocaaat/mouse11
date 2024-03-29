#!/usr/bin/python3
import sys
import os
import time
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
xmod = os.path.join(script_dir, "xmods")
mose = os.path.join(script_dir, "mose.sh")
dir_name = os.path.dirname (__file__)
# Change the current working directory to that directory
os.chdir (dir_name)
try:
    import keyboard 
    import mouse
except:
    os.system("sudo apt install xkbset xdotool -y")
    os.system("git clone https://github.com/boppreh/keyboard")
    os.system("mv keyboard keyboard2")
    os.system("mv keyboard2/keyboard .")
    os.system("rm -rf keyboard2")
    os.system("git clone https://github.com/boppreh/mouse")
    os.system("mv mouse mouse2")
    os.system("mv mouse2/mouse .")
    os.system("rm -rf mouse2")
    os.system("xdotool mousemove 1 1")
    import keyboard 
    import mouse
# from pynput.keyboard import Key, Controller
# keyboard2 = Controller()
# from pynput.mouse import Controller,Button
# mouse=Controller()

level5 = """
// Fairly complete set of symbol interpretations
// to provide reasonable default behavior.

default partial xkb_compatibility "default" {

    virtual_modifiers  LevelFive;

    interpret.repeat= False;
    setMods.clearLocks= True;
    latchMods.clearLocks= True;
    latchMods.latchToLock= True;

    interpret ISO_Level5_Shift+Any {
	useModMapMods= level1;
	virtualModifier= LevelFive;
	action= SetMods(modifiers=LevelFive);
    };

    interpret ISO_Level5_Shift {
	action= SetMods(modifiers=LevelFive);
    };

    interpret ISO_Level5_Latch+Any {
	useModMapMods= level1;
	virtualModifier= LevelFive;
	action= LatchMods(modifiers=LevelFive);
    };

    interpret ISO_Level2_Latch+AnyOf(all) {
    useModMapMods=level1;
    action= LatchMods(modifiers=Shift,clearLocks,latchToLock);
    };
    interpret ISO_Level2_Latch+AnyOfOrNone(all) {
    action= LatchMods(modifiers=Shift,clearLocks,latchToLock);
    };

    interpret ISO_Level5_Latch {
	action= LatchMods(modifiers=LevelFive);
    };

    interpret ISO_Level5_Lock+Any {
	useModMapMods= level1;
	virtualModifier= LevelFive;
	action= LockMods(modifiers=LevelFive);
    };

    interpret ISO_Level5_Lock {
	action= LockMods(modifiers=LevelFive);
    };
};

partial xkb_compatibility "level5_lock" {
    // This defines a Level5-Lock using the NumLock real modifier
    // in order to create arbitrary level-behaviour, which would
    // not be possible with the virtual modifier.
    // See also: types/level5 : EIGHT_LEVEL_LEVEL_FIVE_LOCK
    // See also: symbols/level5(lock)

    virtual_modifiers  NumLock;

    interpret ISO_Level5_Lock {
	action = LockMods(modifiers = NumLock);
    };
};
"""
mousekeys = """
default partial xkb_compatibility "mousekeys" {

    // Keypad actions.

    interpret.repeat= True;

    interpret KP_1 {
	action = MovePtr(x=-1,y= +1);
    };
    interpret KP_End {
	action = MovePtr(x=-1,y= +1);
    };
    interpret KP_Hold {
	action = MovePtr(x=+0,y= +0);
    };

    interpret KP_2 {
	action = MovePtr(x=+0,y= +1);
    };
    interpret KP_Down {
	action = MovePtr(x=+0,y=+0);
    };

    interpret KP_3 {
	action = MovePtr(x=+1,y=+1);
    };
    interpret KP_Next {
	action = MovePtr(x=+1,y=+1);
    };

    interpret KP_4 {
	action = MovePtr(x=-1,y=+0);
    };
    interpret KP_Left {
	action = MovePtr(x=+0,y=+0);
    };

    interpret KP_6 {
	action = MovePtr(x=+1,y=+0);
    };
    interpret KP_Right {
	action = MovePtr(x=+0,y=+0);
    };

    interpret KP_7 {
	action = MovePtr(x=-1,y=-1);
    };
    interpret KP_Home {
	action = MovePtr(x=-1,y=-1);
    };

    interpret KP_8 {
	action = MovePtr(x=+0,y=-1);
    };
    interpret KP_Left {
	action = MovePtr(x=+0,y=+0);
    };

    interpret KP_9 {
	action = MovePtr(x=+1,y=-1);
    };
    interpret KP_Prior {
	action = MovePtr(x=+1,y=-1);
    };

    interpret KP_5 {
	action = PointerButton(button=default);
    };
    interpret KP_Begin {
	action = PointerButton(button=default);
    };

    interpret KP_F2 {
	action = SetPtrDflt(affect=defaultButton,button=1);
    };
    interpret KP_Divide {
	action = SetPtrDflt(affect=defaultButton,button=1);
    };

    interpret KP_F3 {
	action = SetPtrDflt(affect=defaultButton,button=2);
    };
    interpret KP_Multiply {
	action = SetPtrDflt(affect=defaultButton,button=2);
    };

    interpret KP_F4 {
	action = SetPtrDflt(affect=defaultButton,button=3);
    };
    interpret KP_Subtract {
	action = SetPtrDflt(affect=defaultButton,button=3);
    };

    interpret KP_Separator {
	action = PointerButton(button=default,count=2);
    };
    interpret KP_Add {
	action = PointerButton(button=default,count=2);
    };

    interpret KP_0 {
	action = LockPointerButton(button=default,affect=lock);
    };
    interpret KP_Insert {
	action = LockPointerButton(button=default,affect=lock);
    };

    interpret KP_Decimal {
	action = LockPointerButton(button=default,affect=unlock);
    };
    interpret KP_Delete {
	action = LockPointerButton(button=default,affect=unlock);
    };

    // Additional mappings for Solaris keypad compatibility.

    interpret F25 { // aka KP_Divide
	action = SetPtrDflt(affect=defaultButton,button=1);
    };
    interpret F26 { // aka KP_Multiply
	action = SetPtrDflt(affect=defaultButton,button=2);
    };
    interpret F27 { // aka KP_Home
	action = MovePtr(x=-1,y=-1);
    };
    interpret F29 { // aka KP_Prior
	action = MovePtr(x=+1,y=-1);
    };
    interpret F31 { // aka KP_Begin
	action = PointerButton(button=default);
    };
    interpret F33 { // aka KP_End
	action = MovePtr(x=-1,y= +1);
    };
    interpret F35 { // aka KP_Next
	action = MovePtr(x=+1,y=+1);
    };

    interpret.repeat= False;

    // New keysym actions.

    interpret Pointer_Button_Dflt {
	action= PointerButton(button=default);
    };
    interpret Pointer_Button1 {
	action= PointerButton(button=1);
    };
    interpret Pointer_Button2 {
	action= PointerButton(button=2);
    };
    interpret Pointer_Button3 {
	action= PointerButton(button=3);
    };
    interpret Pointer_DblClick_Dflt {
	action= PointerButton(button=default,count=2);
    };
    interpret Pointer_DblClick1 {
	action= PointerButton(button=1,count=2);
    };
    interpret Pointer_DblClick2 {
	action= PointerButton(button=2,count=2);
    };
    interpret Pointer_DblClick3 {
	action= PointerButton(button=3,count=2);
    };
    interpret Pointer_Drag_Dflt {
	action= LockPointerButton(button=default);
    };
    interpret Pointer_Drag1 {
	action= LockPointerButton(button=1);
    };
    interpret Pointer_Drag2 {
	action= LockPointerButton(button=2);
    };
    interpret Pointer_Drag3 {
	action= LockPointerButton(button=3);
    };

    interpret Pointer_EnableKeys {
	action= LockControls(controls=MouseKeys);
    };
    interpret Pointer_Accelerate {
	action= LockControls(controls=MouseKeysAccel);
    };
    interpret Pointer_DfltBtnNext {
	action= SetPtrDflt(affect=defaultButton,button= +1);
    };
    interpret Pointer_DfltBtnPrev {
	action= SetPtrDflt(affect=defaultButton,button= -1);
    };

    // Allow an indicator for MouseKeys.
    indicator "Mouse Keys" {
        //!allowExplicit;
	indicatorDrivesKeyboard;
	controls= MouseKeys;
    };
};
"""
symbolus = """
default partial alphanumeric_keys modifier_keys

xkb_symbols "basic" {

    name[Group1]= "English (US)";

    key.type[Group1] = "EIGHT_LEVEL_SEMIALPHABETIC";
    key <TLDE> {	[     grave,	asciitilde	]	};
    key <AE01> {	[	  1,	exclam]	};
    key <AE02> {	[	  2,	at]	};
    key <AE03> {	[	  3,	numbersign]	};
    key <AE04> {	[	  4,	dollar]	};
    key <AE05> {	[	  5,	percent]	};
    key <AE06> {	[	  6,	asciicircum]	};
    key <AE07> {	[	  7,	ampersand]	};
    key <AE08> {	[	  8,	asterisk]	};
    key <AE09> {	[	  9,	parenleft]	};
    key <AE10> {	[	  0,	parenright]	};
    key <AE11> {	[     minus,	underscore]	};
    key <AE12> {	[     equal,	plus]	};



	key <AD01> {	[	  q,	Q, grave,	asciitilde	]	};
	key <AD02> {	[	  w,	W, 2, at, KP_Left, KP_Left  ]	};
	key <AD03> {	[	  e,	E, 3, numbersign, KP_Left, KP_Left		]	};
	key <AD04> {	[	  r,	R, 4, dollar, KP_Left, KP_Left		]	};
	key <AD05> {	[	  t,	T, minus, underscore, KP_Left, KP_Left		]	};
	key <AD06> {	[	  y,	Y, 1, 1, KP_Left, KP_Left 		]	};
	key <AD07> {	[	  u,	U, 7, ampersand, KP_Left, KP_Left 		]	};
    key <AD08> {	[ 	 i, I,		 Up,	 Up	]	}; 
	key <AD09> {	[	  o,	O, 0,    parenleft, KP_Left, KP_Left	]	};
    key <AD10> {	[	  p,	P		]	};
    key <AD11> {	[ bracketleft,	braceleft	]	};
    key <AD12> {	[ bracketright,	braceright	]	};

    key <AC01> {	[	  a,	A, 1, exclam, KP_Left, KP_Left		]	};
    key <AC02> {	[	  s,	S, Escape, Escape, KP_Left, KP_Left		]	};
    key <AC03> {	[	  d,	D, Escape, Escape, KP_Left, KP_Left		]	};
    key <AC04> {	[ 	 f, F,		 5, percent, KP_Left, KP_Left ]	};
    key <AC05> {	[	  g,	G, 6, asciicircum		]	};
    key <AC06> {	[	  h,	H, 7, ampersand, KP_Left, KP_Left  	]	};
    key <AC07> {    [    j, J,     Left, Left      ] };
    key <AC08> {	[ 	 k, K,		 Down,		Down	] 	};
    key <AC09> {	[ 	 l, L,		 Right,		Right	]	};
    key <AC10> {	[ semicolon,	colon		]	};
    key <AC11> {	[ apostrophe,	quotedbl	]	};

    key <AB01> {	[	  z,	Z, less, greater 	]	};
    key <AB02> {	[	  x,	X, bracketleft, bracketright, KP_Left, KP_Left		]	};
    key <AB03> {	[	  c,	C, braceleft, braceright, Pointer_Button3, Pointer_Button3, Pointer_Button3, Pointer_Button3		]	};
    key <AB04> {	[	  v,	V, parenleft, parenright		]	};
    key <AB05> {	[	  b,	B, equal,	plus, KP_Left, KP_Left		]	};
    key <AB06> {	[	  n,	N, 8, asterisk		]	};
    key <AB07> {	[	  m,	M, 9, parenleft, Pointer_Button2, Pointer_Button2, Pointer_Button2, Pointer_Button2		]	};
    key <AB08> {	[     comma,	less, comma,	less		]	};
    key <AB09> {	[    period,	greater, period,	greater		]	};
    key <AB10> {	[     slash,	question	]	};

    key <BKSL> {	[ backslash,         bar	]	};

   key <SPCE> { [        space,        space,  KP_Left, KP_Left, Pointer_Button1, Pointer_Button1, Pointer_Button1, Pointer_Button1 ] };
   key <TLDE> { [    grave, asciitilde,  dead_grave,   dead_tilde      ] };
   key <AC11> { [apostrophe,quotedbl,    dead_acute,   dead_diaeresis  ] };




   include "level3(ralt_switch)"
   key <CAPS> { [ ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift ] }; // Cur/Num Modifier
   modifier_map Mod3 { <CAPS> };
};

partial alphanumeric_keys
xkb_symbols "euro" {

    key.type[Group1] = "EIGHT_LEVEL_SEMIALPHABETIC";
    
    key <TLDE> {  [     Arabic_thal,        Arabic_shadda,            Arabic_percent,               U0609 ]};
    key <AE01> {  [               1,               exclam,                  Arabic_1,            NoSymbol ]};
    key <AE02> {  [               2,                   at,                  Arabic_2,            NoSymbol ]};
    key <AE03> {  [               3,           numbersign,                  Arabic_3,            NoSymbol ]};
    key <AE04> {  [               4,               dollar,                  Arabic_4,            NoSymbol ]};
    key <AE05> {  [               5,              percent,                  Arabic_5,               U2030 ]};
    key <AE06> {  [               6,          asciicircum,                  Arabic_6,            NoSymbol ]};
    key <AE07> {  [               7,            ampersand,                  Arabic_7,            NoSymbol ]};
    key <AE08> {  [               8,             asterisk,                  Arabic_8,            NoSymbol ]};
    key <AE09> {  [               9,           parenright,                  Arabic_9,            NoSymbol ]};
    key <AE10> {  [               0,            parenleft,                  Arabic_0,            NoSymbol ]};
    key <AE11> {  [           minus,           underscore,                    endash,               U2011 ]};
    key <AE12> {  [           equal,                 plus,                  notequal,               U2248 ]};

    key <AD01> {  [      Arabic_dad,         Arabic_fatha,                  NoSymbol,               U2066 ]};
    key <AD02> {  [      Arabic_sad,      Arabic_fathatan,                  NoSymbol,               U2067, KP_Left, KP_Left ]};
    key <AD03> {  [     Arabic_theh,         Arabic_damma,                  NoSymbol,               U2068 ]};
    key <AD04> {  [      Arabic_qaf,      Arabic_dammatan,                  NoSymbol,               U2069, KP_Left, KP_Left ]};
    key <AD05> {  [      Arabic_feh,                UFEF9,                Arabic_veh,            NoSymbol ]};
    key <AD06> {  [    Arabic_ghain,Arabic_hamzaunderalef,                  NoSymbol,               U202A ]};
    key <AD07> {  [      Arabic_ain,                grave,                  NoSymbol,               U202B ]};
    key <AD08> {  [       Arabic_ha,             division,		 Up,	 Up ]};
    key <AD09> {  [     Arabic_khah,             multiply,                  NoSymbol,            NoSymbol ]};
    key <AD10> {  [      Arabic_hah,     Arabic_semicolon,                  NoSymbol,               U200E ]};
    key <AD11> {  [     Arabic_jeem,                 less,              Arabic_tcheh,               U200F ]};
    key <AD12> {  [      Arabic_dal,              Arabic_thal,                  NoSymbol,               U061C ]};

    key <AC01> {  [    Arabic_sheen,         Arabic_kasra,                  NoSymbol,            NoSymbol, KP_Left, KP_Left ]};
    key <AC02> {  [     Arabic_seen,      Arabic_kasratan, Backspace, Backspace, KP_Left, KP_Left ]};
    key <AC03> {  [      Arabic_yeh,         bracketright, Escape, Escape, KP_Left, KP_Left ]};
    key <AC04> {  [      Arabic_beh,          bracketleft,		 Return, Return, KP_Left, KP_Left ]};
    key <AC05> {  [      Arabic_lam,               U0FEF7,                  NoSymbol,            NoSymbol ]};
    key <AC06> {  [     Arabic_alef,   Arabic_hamzaonalef,                     U0671,            NoSymbol ]};
    key <AC07> {  [      Arabic_teh,       Arabic_tatweel,     Left, Left ]};
    key <AC08> {  [     Arabic_noon,         Arabic_comma,		 Down,		Down ]};
    key <AC09> {  [     Arabic_meem,                slash,		 Right,		Right ]};
    key <AC10> {  [      Arabic_kaf,                colon,                Arabic_gaf,            NoSymbol ]};
    key <AC11> {  [      Arabic_tah,             quotedbl,                     U27E9,               U200D ]};
    key <BKSL> {  [       backslash,             ellipsis,                     U27E8,               U202F ]};

    key <LSGT> {  [             bar,            brokenbar,                  NoSymbol,            NoSymbol ]};
    key <AB01> { [Arabic_hamzaonyeh,           asciitilde,            guillemotright,               U203A ]};
    key <AB02> {  [    Arabic_hamza,         Arabic_sukun,             guillemotleft,               U2039 ]};
    key <AB03> { [Arabic_hamzaonwaw,           braceright,                  NoSymbol,            NoSymbol, Pointer_Button3, Pointer_Button3, Pointer_Button3, Pointer_Button3 ]};
    key <AB04> {  [       Arabic_ra,            braceleft,                  NoSymbol,            NoSymbol ]};
    key <AB05> {  [           UFEFB,                UFEF5,                  NoSymbol,            NoSymbol ]};
    key <AB06> {[Arabic_alefmaksura,   Arabic_maddaonalef,   Arabic_superscript_alef,            NoSymbol ]};
    key <AB07> { [Arabic_tehmarbuta,           apostrophe,                  NoSymbol,            NoSymbol, Pointer_Button2, Pointer_Button2, Pointer_Button2, Pointer_Button2 ]};
    key <AB08> {  [      Arabic_waw,                comma,                     U066C,            NoSymbol ]};
    key <AB09> {  [     Arabic_zain,               period,                Arabic_jeh,            NoSymbol ]};
    key <AB10> {  [      Arabic_zah, Arabic_question_mark,                     U066D,               U200C ]};
    
    key <TLDE> { [Arabic_thal,Arabic_shadda, percent,U2030]};
    key <AE01> { [ Arabic_1,         exclam, 1, NoSymbol ] };
    key <AE02> { [ Arabic_2,             at, 2, NoSymbol ] };
    key <AE03> { [ Arabic_3,     numbersign, 3, NoSymbol ] };
    key <AE04> { [ Arabic_4,         dollar, 4, NoSymbol ] };
    key <AE05> { [ Arabic_5, Arabic_percent, 5, U0609    ] };
    key <AE06> { [ Arabic_6,    asciicircum, 6, NoSymbol ] };
    key <AE07> { [ Arabic_7,      ampersand, 7, NoSymbol ] };
    key <AE08> { [ Arabic_8,       asterisk, 8, NoSymbol ] };
    key <AE09> { [ Arabic_9,     parenright, 9, NoSymbol ] };
    key <AE10> { [ Arabic_0,      parenleft, 0, NoSymbol ] };


   key <SPCE> { [        space,        space,  KP_Left, KP_Left, Pointer_Button1, Pointer_Button1, Pointer_Button1, Pointer_Button1 ] };
   key <TLDE> { [    grave, asciitilde,  dead_grave,   dead_tilde      ] };
   key <AC11> { [apostrophe,quotedbl,    dead_acute,   dead_diaeresis  ] };

   include "level3(ralt_switch)"
   key <CAPS> { [ ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift,ISO_Level5_Shift ] }; // Cur/Num Modifier
   modifier_map Mod3 { <CAPS> };
};


partial alphanumeric_keys
xkb_symbols "ibm238l" {

    include "us(basic)"
    name[Group1]= "English (US, IBM Arabic 238_L)";

    key <AB08> {        [     comma,    comma      ]       };
    key <AB09> {        [    period,    period     ]       };
    key <BKSL> {        [ quoteleft,    asciitilde ]       };
    key <LSGT> {        [ backslash,    bar        ]       };
    key <TLDE> {        [ leftcaret,    rightcaret ]       };
};

partial alphanumeric_keys
xkb_symbols "intl" {

    name[Group1]= "English (US, intl., with dead keys)";

    key <TLDE> { [dead_grave, dead_tilde,         grave,       asciitilde ] };
    key <AE01> { [	   1,     exclam,    exclamdown,      onesuperior ] };
    key <AE02> { [	   2,         at,   twosuperior, dead_doubleacute ] };
    key <AE03> { [	   3, numbersign, threesuperior,      dead_macron ] };
    key <AE04> { [	   4,     dollar,      currency,         sterling ] };
    key <AE05> { [	   5,    percent,      EuroSign,     dead_cedilla ] };
    key <AE06> { [    6, dead_circumflex,    onequarter,      asciicircum ] };
    key <AE07> { [	   7,  ampersand,       onehalf,	dead_horn ] };
    key <AE08> { [	   8,   asterisk, threequarters,      dead_ogonek ] };
    key <AE09> { [	   9,  parenleft, leftsinglequotemark, dead_breve ] };
    key <AE10> { [	   0, parenright, rightsinglequotemark, dead_abovering ] };
    key <AE11> { [     minus, underscore,           yen,    dead_belowdot ] };
    key <AE12> { [     equal,       plus,      multiply,         division ] };

    key <AD01> { [	   q,          Q,    adiaeresis,       Adiaeresis ] };
    key <AD02> { [	   w,          W,         aring,            Aring ] };
    key <AD03> { [	   e,          E,        eacute,           Eacute ] };
    key <AD04> { [	   r,          R,    registered,       registered ] };
    key <AD05> { [	   t,          T,         thorn,            THORN ] };
    key <AD06> { [	   y,          Y,    udiaeresis,       Udiaeresis ] };
    key <AD07> { [	   u,          U,        uacute,           Uacute ] };
    key <AD08> { [	   i,          I,        iacute,           Iacute ] };
    key <AD09> { [	   o,          O,        oacute,           Oacute ] };
    key <AD10> { [	   p,          P,    odiaeresis,       Odiaeresis ] };
    key <AD11> { [ bracketleft,  braceleft,  guillemotleft, leftdoublequotemark ] };
    key <AD12> { [bracketright, braceright, guillemotright, rightdoublequotemark ] };

    key <AC01> { [	   a,          A,        aacute,           Aacute ] };
    key <AC02> { [	   s,          S,        ssharp,          section ] };
    key <AC03> { [	   d,          D,           eth,              ETH ] };
    key <AC04> { [	   f,          F,             f,                F ] };
    key <AC05> { [	   g,          G,             g,                G ] };
    key <AC06> { [	   h,          H,             h,                H ] };
    key <AC07> { [	   j,          J,             j,                J ] };
    key <AC08> { [	   k,          K,            oe,               OE ] };
    key <AC09> { [	   l,          L,        oslash,         Ooblique ] };
    key <AC10> { [ semicolon,      colon,     paragraph,           degree ] };
    key <AC11> { [dead_acute, dead_diaeresis, apostrophe,        quotedbl ] };

    key <AB01> { [	   z,          Z,            ae,               AE ] };
    key <AB02> { [	   x,          X,             x,                X ] };
    key <AB03> { [	   c,          C,     copyright,             cent ] };
    key <AB04> { [	   v,          V,             v,                V ] };
    key <AB05> { [	   b,          B,             b,                B ] };
    key <AB06> { [	   n,          N,        ntilde,           Ntilde ] };
    key <AB07> { [	   m,          M,            mu,               mu ] };
    key <AB08> { [     comma,       less,      ccedilla,         Ccedilla ] };
    key <AB09> { [    period,    greater, dead_abovedot,       dead_caron ] };
    key <AB10> { [     slash,   question,  questiondown,        dead_hook ] };
    key <BKSL> { [ backslash,        bar,       notsign,        brokenbar ] };

    key <LSGT> { [ backslash,   bar,            backslash,      bar ] };

    include "level3(ralt_switch)"
};

// mounkey Based on symbols/us_intl keyboard map:
// Dead-keys definition for a very simple US/ASCII layout.
// by Conectiva (http://www.conectiva.com.br)
// modified by Ricardo Y. Igarashi (iga@that.com.br)

// Added the following deadkeys, to make it truly international:
//
// dead_macron: on AltGr-minus
// dead_breve: on AltGr-parenleft
// dead_abovedot: on AltGr-period
// dead_abovering: on AltGr-0
// dead_doubleacute: on AltGr-equal (as quotedbl is already used)
// dead_caron: on AltGr-less (AltGr-shift-comma)
// dead_cedilla: on AltGr-comma
// dead_ogonek: on AltGr-semicolon
// dead_belowdot: on AltGr-underscore (AltGr-shift-minus)
// dead_hook: on AltGr-question
// dead_horn: on AltGr-plus (AltGr-shift-equal)
// dead_diaeresis: on AltGr-colon (Alt-shift-semicolon)
//
// those were already there:
// dead_grave
// dead_acute
// dead_circumflex
// dead_tilde
// dead_diaeresis

partial alphanumeric_keys
xkb_symbols "alt-intl" {

  include "us"
  name[Group1]= "English (US, alt. intl.)";

  key <TLDE> { [ dead_grave, dead_tilde,    grave,	      asciitilde    ] };
  key <AE05> { [          5, percent,	    EuroSign			    ] };
  key <AE06> { [	  6, dead_circumflex, asciicircum,    asciicircum   ] };
  key <AE09> { [	  9, parenleft, leftsinglequotemark,  dead_breve ] };
  key <AE10> { [	  0, parenright, rightsinglequotemark, dead_abovering ] };
  key <AE11> { [      minus, underscore,    dead_macron,      dead_belowdot ] };
  key <AE12> { [      equal, plus,	    dead_doubleacute, dead_horn	    ] };

  key <AD03> { [          e, E,		     EuroSign,         cent	    ] };

  key <AC10> { [  semicolon, colon,	     dead_ogonek,   dead_diaeresis  ] };
  key <AC11> { [ dead_acute, dead_diaeresis, apostrophe,    quotedbl	    ] };

  key <AB08> { [      comma, less,	     dead_cedilla,  dead_caron	    ] };
  key <AB09> { [     period, greater,	     dead_abovedot, dead_circumflex ] };
  key <AB10> { [      slash, question,	     dead_hook,	    dead_hook	    ] };

  key <LSGT> { [ backslash,   bar,            backslash,      bar ] };

  include "level3(ralt_switch)"
};

partial alphanumeric_keys
xkb_symbols "dvorak" {

    name[Group1]= "English (Dvorak)";

    key <TLDE> { [       grave,	asciitilde, dead_grave, dead_tilde	] };

    key <AE01> { [	    1,	exclam 		]	};
    key <AE02> { [	    2,	at		]	};
    key <AE03> { [	    3,	numbersign	]	};
    key <AE04> { [	    4,	dollar		]	};
    key <AE05> { [	    5,	percent		]	};
    key <AE06> { [	    6,	asciicircum, dead_circumflex, dead_circumflex ]	};
    key <AE07> { [	    7,	ampersand	]	};
    key <AE08> { [	    8,	asterisk	]	};
    key <AE09> { [	    9,	parenleft,  dead_grave, dead_breve	] };
    key <AE10> { [	    0,	parenright	]	};
    key <AE11> { [ bracketleft,	braceleft	]	};
    key <AE12> { [ bracketright, braceright,  dead_tilde] };

    key <AD01> { [  apostrophe,	quotedbl, dead_acute, dead_diaeresis	] };
    key <AD02> { [	comma,	less,   dead_cedilla, dead_caron	] };
    key <AD03> { [      period,	greater, dead_abovedot, periodcentered	] };
    key <AD04> { [	    p,	P		]	};
    key <AD05> { [	    y,	Y		]	};
    key <AD06> { [	    f,	F		]	};
    key <AD07> { [	    g,	G		]	};
    key <AD08> { [	    c,	C		]	};
    key <AD09> { [	    r,	R		]	};
    key <AD10> { [	    l,	L		]	};
    key <AD11> { [	slash,	question	]	};
    key <AD12> { [	equal,	plus		]	};

    key <AC01> { [	    a,	A 		]	};
    key <AC02> { [	    o,	O		]	};
    key <AC03> { [	    e,	E		]	};
    key <AC04> { [	    u,	U		]	};
    key <AC05> { [	    i,	I		]	};
    key <AC06> { [	    d,	D		]	};
    key <AC07> { [	    h,	H		]	};
    key <AC08> { [	    t,	T		]	};
    key <AC09> { [	    n,	N		]	};
    key <AC10> { [	    s,	S		]	};
    key <AC11> { [	minus,	underscore	]	};

    key <AB01> { [   semicolon,	colon, dead_ogonek, dead_doubleacute ] };
    key <AB02> { [	    q,	Q		]	};
    key <AB03> { [	    j,	J		]	};
    key <AB04> { [	    k,	K		]	};
    key <AB05> { [	    x,	X		]	};
    key <AB06> { [	    b,	B		]	};
    key <AB07> { [	    m,	M		]	};
    key <AB08> { [	    w,	W		]	};
    key <AB09> { [	    v,	V		]	};
    key <AB10> { [	    z,	Z		]	};

    key <BKSL> { [  backslash,  bar             ]       };
};

// Dvorak intl., with dead keys
// Olivier Mehani (shtrom-xorg@ssji.net)
// Reproduce the per-key mapping of us(intl) for the dvorak layout
// aka "I just swapped my keys over"
partial alphanumeric_keys
xkb_symbols "dvorak-intl" {

    include "us(dvorak)"
    name[Group1]= "English (Dvorak, intl., with dead keys)";

    key <TLDE> { [dead_grave, dead_tilde,         grave,       asciitilde ] };

    key <AE01> { [	   1,     exclam,    exclamdown,      onesuperior ] };
    key <AE02> { [	   2,         at,   twosuperior, dead_doubleacute ] };
    key <AE03> { [	   3, numbersign, threesuperior,      dead_macron ] };
    key <AE04> { [	   4,     dollar,      currency,         sterling ] };
    key <AE05> { [	   5,    percent,      EuroSign,     dead_cedilla ] };
    key <AE06> { [    6, dead_circumflex,    onequarter,      asciicircum ] };
    key <AE07> { [	   7,  ampersand,       onehalf,	dead_horn ] };
    key <AE08> { [	   8,   asterisk, threequarters,      dead_ogonek ] };
    key <AE09> { [	   9,  parenleft, leftsinglequotemark, dead_breve ] };
    key <AE10> { [	   0, parenright, rightsinglequotemark, dead_abovering ] };
    key <AE11> { [ bracketleft,  braceleft,  guillemotleft, leftdoublequotemark ] };
    key <AE12> { [bracketright, braceright, guillemotright, rightdoublequotemark ] };

    key <AD01> { [dead_acute, dead_diaeresis, apostrophe,        quotedbl ] };
    key <AD02> { [     comma,       less,      ccedilla,         Ccedilla ] };
    key <AD03> { [    period,    greater, dead_abovedot,       dead_caron ] };
    key <AD04> { [	   p,          P,    odiaeresis,       Odiaeresis ] };
    key <AD05> { [	   y,          Y,    udiaeresis,       Udiaeresis ] };
    // key <AD06> { [	   f,	F		]	};
    // key <AD07> { [	   g,	G		]	};
    key <AD08> { [	   c,          C,     copyright,             cent ] };
    key <AD09> { [	   r,          R,    registered,       registered ] };
    key <AD10> { [	   l,          L,        oslash,         Ooblique ] };
    key <AD11> { [     slash,   question,  questiondown,        dead_hook ] };
    // key <AD12> { [     equal,       plus,      multiply,         division ] };

    key <AC01> { [	   a,          A,        aacute,           Aacute ] };
    key <AC02> { [	   o,          O,        oacute,           Oacute ] };
    key <AC03> { [	   e,          E,        eacute,           Eacute ] };
    key <AC04> { [	   u,          U,        uacute,           Uacute ] };
    key <AC05> { [	   i,          I,        iacute,           Iacute ] };
    key <AC06> { [	   d,          D,           eth,              ETH ] };
    // key <AC07> { [	   h,	H		]	};
    key <AC08> { [	   t,          T,         thorn,            THORN ] };
    key <AC09> { [	   n,          N,        ntilde,           Ntilde ] };
    key <AC10> { [	   s,          S,        ssharp,          section ] };
    // key <AC11> { [     minus, underscore,           yen,    dead_belowdot ] };

    key <AB01> { [ semicolon,      colon,     paragraph,           degree ] };
    key <AB02> { [	   q,          Q,    adiaeresis,       Adiaeresis ] };
    // key <AB03> { [	   j,	J		]	};
    key <AB04> { [	   k,          K,            oe,               OE ] };
    // key <AB05> { [	   x,	X		]	};
    // key <AB06> { [	   b,	B		]	};
    key <AB07> { [	   m,          M,            mu,               mu ] };
    key <AB08> { [	   w,          W,         aring,            Aring ] };
    // key <AB09> { [	   v,	V		]	};
    key <AB10> { [	   z,          Z,            ae,               AE ] };

    key <BKSL> { [ backslash,        bar,       notsign,        brokenbar ] };

    include "level3(ralt_switch)"
};

// Dvorak international without dead keys
// Stephane Magnenat (stephane at magnenat dot net, http://stephane.magnenat.net)
// Based on information from http://www.poupinou.org/dvorak/index.html
//
//  `   1   2   3   4   5   6   7   8   9   0   [   ]   \
//                  €
//
//      '   ,   .   p   y   f   g   c   r   l   /   =
//          ä   ê   ë   ü           ç
//
//      a   o   e   u   i   d   h   t   n   s   -
//      à   ô   é   û   î                   ß
//
//      ;   q   j   k   x   b   m   w   v   z
//      â   ö   è   ù   ï

partial alphanumeric_keys
xkb_symbols "dvorak-alt-intl" {

    include "us(dvorak)"
    name[Group1]= "English (Dvorak, alt. intl.)";

    key <AE04> { [         4,  dollar,    EuroSign ] };

    key <AD02> { [     comma,    less,  adiaeresis,       dead_caron ] };
    key <AD03> { [    period, greater, ecircumflex,   periodcentered	] };
    key <AD04> { [         p,       P,  ediaeresis,     dead_cedilla ] };
    key <AD05> { [         y,       Y,  udiaeresis ] };
    key <AD08> { [         c,       C,    ccedilla,    dead_abovedot ] };

    key <AC01> { [         a,       A,      agrave ] };
    key <AC02> { [         o,       O, ocircumflex ] };
    key <AC03> { [         e,       E,      eacute ] };
    key <AC04> { [         u,       U, ucircumflex ] };
    key <AC05> { [         i,       I, icircumflex ] };
    key <AC10> { [         s,       S,      ssharp,            U1E9E ] };

    key <AB01> { [ semicolon,   colon, acircumflex ] };
    key <AB02> { [         q,       Q,  odiaeresis,      dead_ogonek ] };
    key <AB03> { [         j,       J,      egrave, dead_doubleacute ] };
    key <AB04> { [         k,       K,      ugrave ] };
    key <AB05> { [         x,       X,  idiaeresis ] };

    include "level3(ralt_switch)"
};

// Left and right handed dvorak layouts
// by sqweek <sqweek@gmail.com> 2006-01-30
// Based on the corresponding layouts in the console-tools package.
partial alphanumeric_keys
xkb_symbols "dvorak-l" {

    include "us(dvorak)"
    name[Group1]= "English (Dvorak, left-handed)";

    key <AE01> {	[ bracketleft,	braceleft	]	};
    key <AE02> {	[ bracketright,	braceright	]	};
    key <AE03> {	[	slash,	question	]	};
    key <AE04> {	[	    p,	P		]	};
    key <AE05> {	[	    f,	F		]	};
    key <AE06> {	[	    m,	M		]	};
    key <AE07> {	[	    l,	L		]	};
    key <AE08> {	[	    j,	J		]	};
    key <AE09> {	[	    4,	dollar		]	};
    key <AE10> {	[	    3,	numbersign	]	};
    key <AE11> {	[	    2,	at		]	};
    key <AE12> {	[	    1,	exclam 		]	};

    key <AD01> {	[   semicolon,	colon 		]	};
    key <AD02> {	[	    q,	Q		]	};
    key <AD03> {	[	    b,	B		]	};
    key <AD04> {	[	    y,	Y		]	};
    key <AD05> {	[	    u,	U		]	};
    key <AD06> {	[	    r,	R		]	};
    key <AD07> {	[	    s,	S		]	};
    key <AD08> {	[	    o,	O		]	};
    key <AD09> {	[      period,	greater		]	};
    key <AD10> {	[	    6,	asciicircum	]	};
    key <AD11> {	[	    5,	percent		]	};
    key <AD12> {	[	equal,	plus		]	};

    key <AC01> {	[	minus,	underscore	]	};
    key <AC02> {	[	    k,	K		]	};
    key <AC03> {	[	    c,	C		]	};
    key <AC04> {	[	    d,	D		]	};
    key <AC05> {	[	    t,	T		]	};
    key <AC06> {	[	    h,	H		]	};
    key <AC07> {	[	    e,	E		]	};
    key <AC08> {	[	    a,	A 		]	};
    key <AC09> {	[	    z,	Z		]	};
    key <AC10> {	[	    8,	asterisk	]	};
    key <AC11> {	[	    7,	ampersand	]	};

    key <AB01> {	[  apostrophe,	quotedbl	] 	};
    key <AB02> {	[	    x,	X		]	};
    key <AB03> {	[	    g,	G		]	};
    key <AB04> {	[	    v,	V		]	};
    key <AB05> {	[	    w,	W		]	};
    key <AB06> {	[	    n,	N		]	};
    key <AB07> {	[	    i,	I		]	};
    key <AB08> {	[	comma,	less		]	};
    key <AB09> {	[	    0,	parenright	]	};
    key <AB10> {	[	    9,	parenleft	]	};
};

partial alphanumeric_keys
xkb_symbols "dvorak-r" {

    include "us(dvorak)"
    name[Group1]= "English (Dvorak, right-handed)";

    key <AE01> {	[	    1,	exclam 		]	};
    key <AE02> {	[	    2,	at		]	};
    key <AE03> {	[	    3,	numbersign	]	};
    key <AE04> {	[	    4,	dollar		]	};
    key <AE05> {	[	    j,	J		]	};
    key <AE06> {	[	    l,	L		]	};
    key <AE07> {	[	    m,	M		]	};
    key <AE08> {	[	    f,	F		]	};
    key <AE09> {	[	    p,	P		]	};
    key <AE10> {	[	slash,	question	]	};
    key <AE11> {	[ bracketleft,	braceleft	]	};
    key <AE12> {	[ bracketright,	braceright	]	};

    key <AD01> {	[	    5,	percent		]	};
    key <AD02> {	[	    6,	asciicircum ]	};
    key <AD03> {	[	    q,	Q		]	};
    key <AD04> {	[      period,	greater		]	};
    key <AD05> {	[	    o,	O		]	};
    key <AD06> {	[	    r,	R		]	};
    key <AD07> {	[	    s,	S		]	};
    key <AD08> {	[	    u,	U		]	};
    key <AD09> {	[	    y,	Y		]	};
    key <AD10> {	[	    b,	B		]	};
    key <AD11> {	[   semicolon,	colon 		]	};
    key <AD12> {	[	equal,	plus		]	};

    key <AC01> {	[	    7,	ampersand	]	};
    key <AC02> {	[	    8,	asterisk	]	};
    key <AC03> {	[	    z,	Z		]	};
    key <AC04> {	[	    a,	A 		]	};
    key <AC05> {	[	    e,	E		]	};
    key <AC06> {	[	    h,	H		]	};
    key <AC07> {	[	    t,	T		]	};
    key <AC08> {	[	    d,	D		]	};
    key <AC09> {	[	    c,	C		]	};
    key <AC10> {	[	    k,	K		]	};
    key <AC11> {	[	minus,	underscore	]	};

    key <AB01> {	[	    9,	parenleft	]	};
    key <AB02> {	[	    0,	parenright	]	};
    key <AB03> {	[	    x,	X		]	};
    key <AB04> {	[	comma,	less		]	};
    key <AB05> {	[	    i,	I		]	};
    key <AB06> {	[	    n,	N		]	};
    key <AB07> {	[	    w,	W		]	};
    key <AB08> {	[	    v,	V		]	};
    key <AB09> {	[	    g,	G		]	};
    key <AB10> {	[  apostrophe,	quotedbl	] 	};
};

// Classic dvorak layout
// by Piter Punk <piterpk@terra.com.br> - 2006-07-06
// Based on dvorak layout and e-mail from Russel L. Harris rlharris@oplink.net
// on xorg list.
partial alphanumeric_keys
xkb_symbols "dvorak-classic" {

    name[Group1]= "English (classic Dvorak)";

    key <TLDE> { [       grave,	asciitilde, dead_grave, dead_tilde	] };

    key <AE01> { [ bracketleft,	braceleft	]	};
    key <AE02> { [	    7,	ampersand	]	};
    key <AE03> { [	    5,	percent		]	};
    key <AE04> { [	    3,	numbersign	]	};
    key <AE05> { [	    1,	exclam 		]	};
    key <AE06> { [	    9,	parenleft,  dead_grave]	};
    key <AE07> { [	    0,	parenright	]	};
    key <AE08> { [	    2,	at		]	};
    key <AE09> { [	    4,	dollar		]	};
    key <AE10> { [	    6,	asciicircum, dead_circumflex, dead_circumflex ]	};
    key <AE11> { [	    8,	asterisk	]	};
    key <AE12> { [ bracketright, braceright,  dead_tilde] };

    key <AD01> { [	slash,	question	]	};
    key <AD02> { [	comma,	less,   dead_cedilla, dead_caron	] };
    key <AD03> { [      period,	greater, dead_abovedot, periodcentered	] };
    key <AD04> { [	    p,	P		]	};
    key <AD05> { [	    y,	Y		]	};
    key <AD06> { [	    f,	F		]	};
    key <AD07> { [	    g,	G		]	};
    key <AD08> { [	    c,	C		]	};
    key <AD09> { [	    r,	R		]	};
    key <AD10> { [	    l,	L		]	};
    key <AD11> { [  apostrophe,	quotedbl, dead_acute, dead_diaeresis	] };
    key <AD12> { [	equal,	plus		]	};

    key <AC01> { [	    a,	A 		]	};
    key <AC02> { [	    o,	O		]	};
    key <AC03> { [	    e,	E		]	};
    key <AC04> { [	    u,	U		]	};
    key <AC05> { [	    i,	I		]	};
    key <AC06> { [	    d,	D		]	};
    key <AC07> { [	    h,	H		]	};
    key <AC08> { [	    t,	T		]	};
    key <AC09> { [	    n,	N		]	};
    key <AC10> { [	    s,	S		]	};
    key <AC11> { [	minus,	underscore	]	};

    key <AB01> { [   semicolon,	colon, dead_ogonek, dead_doubleacute ] };
    key <AB02> { [	    q,	Q		]	};
    key <AB03> { [	    j,	J		]	};
    key <AB04> { [	    k,	K		]	};
    key <AB05> { [	    x,	X		]	};
    key <AB06> { [	    b,	B		]	};
    key <AB07> { [	    m,	M		]	};
    key <AB08> { [	    w,	W		]	};
    key <AB09> { [	    v,	V		]	};
    key <AB10> { [	    z,	Z		]	};
    key <BKSL> { [  backslash,  bar             ]       };
};

// programmer Dvorak, by Roland Kaufmann <rlndkfmn at gmail dot com>
// License: BSD, available at <http://www.kaufmann.no/roland/dvorak/license.html>
// Main features: Numbers are in shift position (like French), symbols have been
// placed in locations that give good hand-alternation and finger rolling with
// symbols that usually follows, accented characters are possible for I18N.
// Patch suggestions should be sent upstream.
partial alphanumeric_keys
xkb_symbols "dvp" {

    include "us(dvorak)"
    name[Group1] = "English (programmer Dvorak)";

    //             Unmodified       Shift           AltGr            Shift+AltGr
    // symbols row, left side
    key <TLDE> { [ dollar,          asciitilde,     dead_tilde                  ] };
    key <AE01> { [ ampersand,       percent                                     ] };
    key <AE02> { [ bracketleft,     7,              currency                    ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };
    key <AE03> { [ braceleft,       5,              cent                        ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };
    key <AE04> { [ braceright,      3,              yen                         ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };
    key <AE05> { [ parenleft,       1,              EuroSign                    ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };
    key <AE06> { [ equal,           9,              sterling                    ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };

    // symbols row, right side
    key <AE07> { [ asterisk,        0                                           ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };
    key <AE08> { [ parenright,      2,              onehalf                     ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };
    key <AE09> { [ plus,            4                                           ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };
    key <AE10> { [ bracketright,    6                                           ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };
    key <AE11> { [ exclam,          8,              exclamdown,      U2E18      ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };  // reversed interrobang
    key <AE12> { [ numbersign,      grave,          dead_grave                  ] };
    key <BKSP> { [ BackSpace,       BackSpace                                   ] };

    // upper row, left side
    key <AD01> { [ semicolon,       colon,          dead_diaeresis              ] };
    key <AD02> { [ comma,           less,           guillemotleft,   U201C      ] };
    key <AD03> { [ period,          greater,        guillemotright,  U201D      ] };
    key <AD04> { [ p,               P,              paragraph,       section    ] };
    key <AD05> { [ y,               Y,              udiaeresis,      Udiaeresis ] };

    // upper row, right side
    key <AD08> { [ c,               C,              ccedilla,        Ccedilla   ] };
    key <AD09> { [ r,               R,              registered,      trademark  ] };
    key <AD11> { [ slash,           question,       questiondown,    U203D      ] };  // interrobang
    key <AD12> { [ at,              asciicircum,    dead_circumflex, dead_caron ] };

    // home row, left side
    key <AC01> { [ a,               A,              aring,           Aring      ] };
    key <AC02> { [ o,               O,              oslash,          Ooblique   ] };
    key <AC03> { [ e,               E,              ae,              AE         ] };
    key <AC04> { [ u,               U,              eacute,          Eacute     ] };

    // home row, right side
    key <AC06> { [ d,               D,              eth,             ETH        ] };
    key <AC07> { [ h,               H,              dead_acute                  ] };
    key <AC08> { [ t,               T,              thorn,           THORN      ] };
    key <AC09> { [ n,               N,              ntilde,          Ntilde     ] };
    key <AC10> { [ s,               S,              ssharp,          U1E9E      ] };
    key <AC11> { [ minus,           underscore,     hyphen,          endash     ], type[Group1] = "FOUR_LEVEL_ALPHABETIC" };
    key <BKSL> { [ backslash,       bar                                         ] };

    // lower row, left side
    key <AB01> { [ apostrophe,      quotedbl,       dead_acute                  ] };

    // do NOT hardcode this switch; use lv3:ralt_switch option instead!
    //include "level3(ralt_switch)"
};

// Macintosh dvorak keyboard layout
// Based on the Dvorak keyboard layout found in MacOS
partial alphanumeric_keys
xkb_symbols "dvorak-mac" {
    name[Group1]= "English (Dvorak, Macintosh)";

    key <TLDE> { [ grave, asciitilde, dead_grave, grave ] };

    key <AE01> { [            1,      exclam,          exclamdown,                U2044 ] };
    key <AE02> { [            2,          at,           trademark,             EuroSign ] };
    key <AE03> { [            3,  numbersign,            sterling,                U2039 ] };
    key <AE04> { [            4,      dollar,                cent,                U203A ] };
    key <AE05> { [            5,     percent,            infinity,                UFB01 ] };
    key <AE06> { [            6, asciicircum,             section,                UFB02 ] };
    key <AE07> { [            7,   ampersand,           paragraph,         doubledagger ] };
    key <AE08> { [            8,    asterisk,  enfilledcircbullet,               degree ] };
    key <AE09> { [            9,   parenleft,         ordfeminine,       periodcentered ] };
    key <AE10> { [            0,  parenright,           masculine,   singlelowquotemark ] };
    key <AE11> { [  bracketleft,   braceleft, leftdoublequotemark, rightdoublequotemark ] };
    key <AE12> { [ bracketright,  braceright, leftsinglequotemark, rightsinglequotemark ] };

    key <AD01> { [ apostrophe,  quotedbl,               ae,           AE ] };
    key <AD02> { [      comma,      less,    lessthanequal,       macron ] };
    key <AD03> { [     period,   greater, greaterthanequal,        breve ] };
    key <AD04> { [          p,         P,         Greek_pi,        U220F ] };
    key <AD05> { [          y,         Y,              yen,       Aacute ] };
    key <AD06> { [          f,         F,         function,   Idiaeresis ] };
    key <AD07> { [          g,         G,        copyright,  doubleacute ] };
    key <AD08> { [          c,         C,         ccedilla,     Ccedilla ] };
    key <AD09> { [          r,         R,       registered,     permille ] };
    key <AD10> { [          l,         L,          notsign,       Ograve ] };
    key <AD11> { [      slash,  question,         division, questiondown ] };
    key <AD12> { [      equal,      plus,         notequal,    plusminus ] };

    key <AC01> { [     a,          A,             aring,       Aring ] };
    key <AC02> { [     o,          O,            oslash,    Ooblique ] };
    key <AC03> { [     e,          E,        dead_acute,       acute ] };
    key <AC04> { [     u,          U,    dead_diaeresis,   diaeresis ] };
    key <AC05> { [     i,          I,   dead_circumflex, asciicircum ] };
    key <AC06> { [     d,          D, partialderivative, Icircumflex ] };
    key <AC07> { [     h,          H,          abovedot,      Oacute ] };
    key <AC08> { [     t,          T,            dagger,       caron ] };
    key <AC09> { [     n,          N,        dead_tilde,  asciitilde ] };
    key <AC10> { [     s,          S,            ssharp,      Iacute ] };
    key <AC11> { [ minus, underscore,            endash,      emdash ] };

    key <LSGT> { [ section, plusminus ] };
    key <AB01> { [ semicolon, colon,       ellipsis,             Uacute ] };
    key <AB02> { [         q,     Q,             oe,                 OE ] };
    key <AB03> { [         j,     J,          U2206,        Ocircumflex ] };
    key <AB04> { [         k,     K, dead_abovering,              UF8FF ] };
    key <AB05> { [         x,     X,          U2248,             ogonek ] };
    key <AB06> { [         b,     B,       integral,           idotless ] };
    key <AB07> { [         m,     M,             mu,        Acircumflex ] };
    key <AB08> { [         w,     W,          U2211, doublelowquotemark ] };
    key <AB09> { [         v,     V,     squareroot,              U25CA ] };
    key <AB10> { [         z,     Z,    Greek_OMEGA,            cedilla ] };

    key <BKSL> { [ backslash, bar, guillemotleft, guillemotright ] };

    include "level3(ralt_switch)"
};

// phonetic layout for Russian letters on an US keyboard
// by Ivan Popov <pin@konvalo.org> 2005-07-17

// level3 modifier is a shortcut to the "us" meaning of the keys where
// we place cyrillic letters, handy for accessing the corresponding
// punctuation marks.
// It is important to have access to punctuation marks, and the rest of
// alphabetical keys are added for being consequent so that the users
// can expect the level3 modifier to give what the key label shows.

partial alphanumeric_keys
xkb_symbols "rus" {

    include "us(basic)"
    name[Group1]= "Russian (US, phonetic)";

key.type[group1]="FOUR_LEVEL_ALPHABETIC";

    key	<LatA> {	[ Cyrillic_a, Cyrillic_A ]	};
    key	<LatB> {	[ Cyrillic_be, Cyrillic_BE ]	};
    key	<LatW> {	[ Cyrillic_ve, Cyrillic_VE ]	};
    key	<LatG> {	[ Cyrillic_ghe, Cyrillic_GHE ]	};
    key	<LatD> {	[ Cyrillic_de, Cyrillic_DE ]	};
    key	<LatE> {	[ Cyrillic_ie, Cyrillic_IE ]	};
    key	<TLDE> {	[ Cyrillic_io, Cyrillic_IO, grave, asciitilde ] };
    key	<LatV> {	[ Cyrillic_zhe, Cyrillic_ZHE ]	};
    key	<LatZ> {	[ Cyrillic_ze, Cyrillic_ZE ]	};
    key	<LatI> {	[ Cyrillic_i, Cyrillic_I ]	};
    key	<LatJ> {	[ Cyrillic_shorti, Cyrillic_SHORTI ]	};
    key	<LatK> {	[ Cyrillic_ka, Cyrillic_KA ]	};
    key	<LatL> {	[ Cyrillic_el, Cyrillic_EL ]	};
    key	<LatM> {	[ Cyrillic_em, Cyrillic_EM ]	};
    key	<LatN> {	[ Cyrillic_en, Cyrillic_EN ]	};
    key	<LatO> {	[ Cyrillic_o, Cyrillic_O ]	};
    key	<LatP> {	[ Cyrillic_pe, Cyrillic_PE ]	};
    key	<LatR> {	[ Cyrillic_er, Cyrillic_ER ]	};
    key	<LatS> {	[ Cyrillic_es, Cyrillic_ES ]	};
    key	<LatT> {	[ Cyrillic_te, Cyrillic_TE ]	};
    key	<LatU> {	[ Cyrillic_u, Cyrillic_U ]	};
    key	<LatF> {	[ Cyrillic_ef, Cyrillic_EF ]	};
    key	<LatH> {	[ Cyrillic_ha, Cyrillic_HA ]	};
    key	<LatC> {	[ Cyrillic_tse, Cyrillic_TSE ]	};
    key <AC10> {        [ Cyrillic_che, Cyrillic_CHE, semicolon, colon ] };
    key	<AD11> {	[ Cyrillic_sha, Cyrillic_SHA, bracketleft, braceleft] };
    key	<AD12> {	[ Cyrillic_shcha, Cyrillic_SHCHA, bracketright, braceright ]	};
    key <AE12> {        [ Cyrillic_hardsign, Cyrillic_HARDSIGN, equal, plus ] };
    key	<LatY> {	[ Cyrillic_yeru, Cyrillic_YERU ]	};
    key	<LatX> {	[ Cyrillic_softsign, Cyrillic_SOFTSIGN ]	};
    key	<BKSL> {	[ Cyrillic_e, Cyrillic_E, backslash, bar ]	};
    key <AC11> {        [ Cyrillic_yu, Cyrillic_YU, apostrophe, quotedbl ] };
    key	<LatQ> {	[ Cyrillic_ya, Cyrillic_YA ]	};

    include "level3(ralt_switch)"
};

partial alphanumeric_keys
xkb_symbols "mac" {

    name[Group1]= "English (Macintosh)";

    key.type[group1]="FOUR_LEVEL";

    // Slightly improvised from http://homepage.mac.com/thgewecke/kblayout.jpg
    key <LSGT> { [   section,  plusminus,       section,        plusminus ] };
    key <TLDE> { [     grave, asciitilde,    dead_grave,        dead_horn ] };
    key <AE01> { [	   1,     exclam,    exclamdown,            U2044 ] };
    key <AE02> { [	   2,         at,     trademark,         EuroSign ] };
    key <AE03> { [	   3, numbersign,      sterling,            U2039 ] };
    key <AE04> { [	   4,     dollar,          cent,            U203A ] };
    key <AE05> { [	   5,    percent,      infinity,            UFB01 ] };
    key <AE06> { [         6,asciicircum,       section,            UFB02 ] };
    key <AE07> { [	   7,  ampersand,     paragraph,     doubledagger ] };
    key <AE08> { [	   8,   asterisk, enfilledcircbullet,      degree ] };
    key <AE09> { [	   9,  parenleft,   ordfeminine,   periodcentered ] };
    key <AE10> { [	   0, parenright,     masculine,singlelowquotemark] };
    key <AE11> { [     minus, underscore,        endash,           emdash ] };
    key <AE12> { [     equal,       plus,      notequal,        plusminus ] };

    key <AD01> { [	   q,          Q,            oe,               OE ] };
    key <AD02> { [	   w,          W,         U2211,doublelowquotemark] };
    key <AD03> { [	   e,          E,    dead_acute,            acute ] };
    key <AD04> { [	   r,          R,    registered,            U2030 ] };
    key <AD05> { [	   t,          T,        dagger,       dead_caron ] };
    key <AD06> { [	   y,          Y,           yen,       onequarter ] };
    key <AD07> { [	   u,        U,  dead_diaeresis,        diaeresis ] };
    key <AD08> { [	   i,        I, dead_circumflex,            U02C6 ] };
    key <AD09> { [	   o,          O,        oslash,         Ooblique ] };
    key <AD10> { [	   p,          P,      Greek_pi,            U220F ] };
    key <AD11> { [ bracketleft,  braceleft, leftdoublequotemark, rightdoublequotemark ] };
    key <AD12> { [bracketright, braceright, leftsinglequotemark, rightsinglequotemark ] };
    key <BKSL> { [ backslash,        bar, guillemotleft,   guillemotright ] };

    key <AC01> { [	   a,          A,         aring,            Aring ] };
    key <AC02> { [	   s,          S,        ssharp,      dead_stroke ] };
    key <AC03> { [	   d,          D, partialderivative,          eth ] };
    key <AC04> { [	   f,          F,      function,        dead_hook ] };
    key <AC05> { [	   g,          G,     copyright, dead_doubleacute ] };
    key <AC06> { [	   h,          H, dead_abovedot,    dead_belowdot ] };
    key <AC07> { [	   j,          J,         U2206,          onehalf ] };
    key <AC08> { [	   k,          K,dead_abovering,            UF8FF ] };
    key <AC09> { [	   l,          L,       notsign,            THORN ] };
    key <AC10> { [ semicolon,      colon,         U2026,            thorn ] };
    key <AC11> { [apostrophe,   quotedbl,            ae,               AE ] };

    key <AB01> { [	   z,          Z,   Greek_OMEGA,     dead_cedilla ] };
    key <AB02> { [	   x,          X,         U2248,      dead_ogonek ] };
				// unclear whether "approxeq" is 2248 or 2245
    key <AB03> { [	   c,          C,      ccedilla,         Ccedilla ] };
    key <AB04> { [	   v,          V,    squareroot,            U25CA ] };
    key <AB05> { [	   b,          B,      integral,         idotless ] };
    key <AB06> { [	   n,          N,    dead_tilde,            U02DC ] };
    key <AB07> { [	   m,          M,            mu,    threequarters ] };
    key <AB08> { [     comma,       less, lessthanequal,      dead_macron ] };
    key <AB09> { [    period,    greater, greaterthanequal,    dead_breve ] };
    key <AB10> { [     slash,   question,      division,     questiondown ] };

    include "level3(ralt_switch)"
};

// Colemak symbols for xkb on X.Org Server 7.x
// 2006-01-01 Shai Coleman, http://colemak.com/

partial alphanumeric_keys
xkb_symbols "colemak" {

    name[Group1]= "English (Colemak)";

    key <TLDE> { [        grave,   asciitilde,      dead_tilde,       asciitilde ] };
    key <AE01> { [            1,       exclam,      exclamdown,      onesuperior ] };
    key <AE02> { [            2,           at,       masculine,      twosuperior ] };
    key <AE03> { [            3,   numbersign,     ordfeminine,    threesuperior ] };
    key <AE04> { [            4,       dollar,            cent,         sterling ] };
    key <AE05> { [            5,      percent,        EuroSign,              yen ] };
    key <AE06> { [            6,  asciicircum,         hstroke,          Hstroke ] };
    key <AE07> { [            7,    ampersand,             eth,              ETH ] };
    key <AE08> { [            8,     asterisk,           thorn,            THORN ] };
    key <AE09> { [            9,    parenleft,  leftsinglequotemark,  leftdoublequotemark ] };
    key <AE10> { [            0,   parenright, rightsinglequotemark,  rightdoublequotemark ] };
    key <AE11> { [        minus,   underscore,          endash,           emdash ] };
    key <AE12> { [        equal,         plus,        multiply,         division ] };

    key <AD01> { [            q,            Q,      adiaeresis,       Adiaeresis ] };
    key <AD02> { [            w,            W,           aring,            Aring ] };
    key <AD03> { [            f,            F,          atilde,           Atilde ] };
    key <AD04> { [            p,            P,          oslash,         Ooblique ] };
    key <AD05> { [            g,            G,     dead_ogonek,       asciitilde ] };
    key <AD06> { [            j,            J,         dstroke,          Dstroke ] };
    key <AD07> { [            l,            L,         lstroke,          Lstroke ] };
    key <AD08> { [            u,            U,          uacute,           Uacute ] };
    key <AD09> { [            y,            Y,      udiaeresis,       Udiaeresis ] };
    key <AD10> { [    semicolon,        colon,      odiaeresis,       Odiaeresis ] };
    key <AD11> { [  bracketleft,    braceleft,   guillemotleft,        0x1002039 ] };
    key <AD12> { [ bracketright,   braceright,  guillemotright,        0x100203a ] };
    key <BKSL> { [    backslash,          bar,      asciitilde,       asciitilde ] };

    key <AC01> { [            a,            A,          aacute,           Aacute ] };
    key <AC02> { [            r,            R,      dead_grave,       asciitilde ] };
    key <AC03> { [            s,            S,          ssharp,        0x1001e9e ] };
    key <AC04> { [            t,            T,      dead_acute, dead_doubleacute ] };
    key <AC05> { [            d,            D,  dead_diaeresis,       asciitilde ] };
    key <AC06> { [            h,            H,      dead_caron,       asciitilde ] };
    key <AC07> { [            n,            N,          ntilde,           Ntilde ] };
    key <AC08> { [            e,            E,          eacute,           Eacute ] };
    key <AC09> { [            i,            I,          iacute,           Iacute ] };
    key <AC10> { [            o,            O,          oacute,           Oacute ] };
    key <AC11> { [   apostrophe,     quotedbl,          otilde,           Otilde ] };

    key <AB01> { [            z,            Z,              ae,               AE ] };
    key <AB02> { [            x,            X, dead_circumflex,       asciitilde ] };
    key <AB03> { [            c,            C,        ccedilla,         Ccedilla ] };
    key <AB04> { [            v,            V,              oe,               OE ] };
    key <AB05> { [            b,            B,      dead_breve,       asciitilde ] };
    key <AB06> { [            k,            K,  dead_abovering,       asciitilde ] };
    key <AB07> { [            m,            M,     dead_macron,       asciitilde ] };
    key <AB08> { [        comma,         less,    dead_cedilla,       asciitilde ] };
    key <AB09> { [       period,      greater,   dead_abovedot,       asciitilde ] };
    key <AB10> { [        slash,     question,    questiondown,       asciitilde ] };

    key <CAPS> { [    BackSpace,    BackSpace,       BackSpace,        BackSpace ] };
    key <LSGT> { [        minus,   underscore,          endash,           emdash ] };
    key <SPCE> { [        space,        space,           space,     nobreakspace ] };

    include "level3(ralt_switch)"
};


// Colemak-DH (ANSI) symbols for xkb on X.Org Server 7.x
// 2014-10-25 by SteveP, https://colemakmods.github.io/mod-dh/

xkb_symbols "colemak_dh" {

    name[Group1]= "English (Colemak-DH)";

    key <TLDE> { [        grave,   asciitilde,      dead_tilde,       asciitilde ] };
    key <AE01> { [            1,       exclam,      exclamdown,      onesuperior ] };
    key <AE02> { [            2,           at,       masculine,      twosuperior ] };
    key <AE03> { [            3,   numbersign,     ordfeminine,    threesuperior ] };
    key <AE04> { [            4,       dollar,            cent,         sterling ] };
    key <AE05> { [            5,      percent,        EuroSign,              yen ] };
    key <AE06> { [            6,  asciicircum,         hstroke,          Hstroke ] };
    key <AE07> { [            7,    ampersand,             eth,              ETH ] };
    key <AE08> { [            8,     asterisk,           thorn,            THORN ] };
    key <AE09> { [            9,    parenleft,  leftsinglequotemark,  leftdoublequotemark ] };
    key <AE10> { [            0,   parenright, rightsinglequotemark,  rightdoublequotemark ] };
    key <AE11> { [        minus,   underscore,          endash,           emdash ] };
    key <AE12> { [        equal,         plus,        multiply,         division ] };

    key <AD01> { [            q,            Q,      adiaeresis,       Adiaeresis ] };
    key <AD02> { [            w,            W,           aring,            Aring ] };
    key <AD03> { [            f,            F,          atilde,           Atilde ] };
    key <AD04> { [            p,            P,          oslash,         Ooblique ] };
    key <AD05> { [            b,            B,      dead_breve,       asciitilde ] };
    key <AD06> { [            j,            J,         dstroke,          Dstroke ] };
    key <AD07> { [            l,            L,         lstroke,          Lstroke ] };
    key <AD08> { [            u,            U,          uacute,           Uacute ] };
    key <AD09> { [            y,            Y,      udiaeresis,       Udiaeresis ] };
    key <AD10> { [    semicolon,        colon,      odiaeresis,       Odiaeresis ] };
    key <AD11> { [  bracketleft,    braceleft,   guillemotleft,        0x1002039 ] };
    key <AD12> { [ bracketright,   braceright,  guillemotright,        0x100203a ] };
    key <BKSL> { [    backslash,          bar,      asciitilde,       asciitilde ] };

    key <AC01> { [            a,            A,          aacute,           Aacute ] };
    key <AC02> { [            r,            R,      dead_grave,       asciitilde ] };
    key <AC03> { [            s,            S,          ssharp,        0x1001e9e ] };
    key <AC04> { [            t,            T,      dead_acute, dead_doubleacute ] };
    key <AC05> { [            g,            G,     dead_ogonek,       asciitilde ] };
    key <AC06> { [            m,            M,     dead_macron,       asciitilde ] };
    key <AC07> { [            n,            N,          ntilde,           Ntilde ] };
    key <AC08> { [            e,            E,          eacute,           Eacute ] };
    key <AC09> { [            i,            I,          iacute,           Iacute ] };
    key <AC10> { [            o,            O,          oacute,           Oacute ] };
    key <AC11> { [   apostrophe,     quotedbl,          otilde,           Otilde ] };

    key <LSGT> { [            z,            Z,              ae,               AE ] };
    key <AB01> { [            x,            X, dead_circumflex,       asciitilde ] };
    key <AB02> { [            c,            C,        ccedilla,         Ccedilla ] };
    key <AB03> { [            d,            D,  dead_diaeresis,       asciitilde ] };
    key <AB04> { [            v,            V,              oe,               OE ] };
    key <AB05> { [            z,            Z,              ae,               AE ] }; //Z appears here too because <LSGT> key is not present on ANSI keyboards
    key <AB06> { [            k,            K,  dead_abovering,       asciitilde ] };
    key <AB07> { [            h,            H,      dead_caron,       asciitilde ] };
    key <AB08> { [        comma,         less,    dead_cedilla,       asciitilde ] };
    key <AB09> { [       period,      greater,   dead_abovedot,       asciitilde ] };
    key <AB10> { [        slash,     question,    questiondown,       asciitilde ] };

    key <SPCE> { [        space,        space,           space,     nobreakspace ] };

    include "level3(ralt_switch)"
};

// Colemak-DH (ISO) symbols for xkb on X.Org Server 7.x
// https://colemakmods.github.io/mod-dh/

xkb_symbols "colemak_dh_iso" {

    include "us(colemak_dh)"
    name[Group1]= "English (Colemak-DH ISO)";

    key <AB05> { [ backslash, bar, asciitilde, brokenbar] };

    include "level3(ralt_switch)"
};

// I do NOT like dead-keys - the International keyboard as defined by Microsoft
// does not fit my needs. Why use two keystrokes for all simple characters (eg '
// and <space> generates a single ') just to have an é (eacute) in two strokes
// as well? I type ' more often than é (eacute).
//
// This file works just like a regular keyboard, BUT has all dead-keys
// accessible at level3 (through AltGr). An ë (ediaeresis) is now: AltGr+"
// followed by an e. In other words, this keyboard is not international as long
// as you leave the right Alt key alone.
//
// The original MS International keyboard was intended for Latin1 (iso8859-1).
// With the introduction of iso8859-15, the (important) ligature oe (and OE)
// became available. I added them next to ae. Because I write ediaeresis more
// often than registered, I moved registered to be next to copyright and added
// ediaeresis and idiaeresis. - Adriaan
//
// Note: there is an "altgr-weur" layout (in extras) which is no longer based on
// the Microsoft layout, supports all chars that altgr-intl offers, but is
// optimized for 10 Western European languages. More info: https://altgr-weur.eu

partial alphanumeric_keys
xkb_symbols "altgr-intl" {

   include "us(intl)"
   name[Group1]= "English (intl., with AltGr dead keys)";


   key <TLDE> { [    grave, asciitilde,  dead_grave,   dead_tilde      ] };
   key <AC11> { [apostrophe,quotedbl,    dead_acute,   dead_diaeresis  ] };


   key <AE01> { [        1, exclam,      onesuperior,  exclamdown      ] };
   key <AD04> { [        r, R,           ediaeresis,   Ediaeresis      ] };
   key <AD08> {	[ 	 i, I,		 Up,	 Up	]	}; 
   key <AC07> { [    j, J,     Left, Left      ] };
   key <AC08> {	[ 	 k, K,		 Down,		Down	] 	};
   key <AC09> {	[ 	 l, L,		 Right,		Down	]	};
   key <AC04> {	[ 	 f, F,		 Escape,		Escape	]	};
   key <CAPS> { [ F23 ] };






	key <AD01> {	[	  q,	Q, 1, exclam 		]	};
	key <AD02> {	[	  w,	W, 2, at		]	};
	key <AD03> {	[	  e,	E, 3, numbersign		]	};
	key <AD04> {	[	  r,	R, 4, dollar		]	};
	key <AD05> {	[	  t,	T, 5, percent		]	};
	key <AD06> {	[	  y,	Y, 6, asciicircum		]	};
	key <AD07> {	[	  u,	U, 7, ampersand		]	};
	key <AD09> {	[	  o,	O, 9, parenleft		]	};

  key <AB06> {	[	  n,	N, 8, asterisk		]	};
  key <AB07> {	[	  m,	M, 0, parenright		]	};





   key <AE06> { [        6, asciicircum, dead_circumflex, onequarter    ] };
   key <AE07> { [        7, ampersand,   dead_horn,       onehalf       ] };
   key <AE08> { [        8, asterisk,    dead_ogonek,     threequarters ] };


   key <AE01> {	[	  1,	exclam, F1, F1 		]	};
   key <AE02> {	[	  2,	at, F2, F2		]	};
   key <AE03> {	[	  3,	numbersign, F3, F3	]	};
   key <AE04> {	[	  4,	dollar, F4, F4		]	};
   key <AE05> {	[	  5,	percent, F5, F5		]	};
   key <AE06> {	[	  6,	asciicircum, F6, F6	]	};
   key <AE07> {	[	  7,	ampersand, F7, F7	]	};
   key <AE08> {	[	  8,	asterisk, F8, F8	]	};
   key <AE09> {	[	  9,	parenleft, F9, F9	]	};
   key <AE10> {	[	  0,	parenright, F10, F10	]	};
   key <AE11> {	[     minus,	underscore, F11, F11	]	};
   key <AE12> {	[     equal,	plus, F12, F12		]	};


   include "level3(ralt_switch)"
};

// This (altgr-weur) layout is based on combined letter frequencies
// for English, German, Dutch, French, Spanish, Portuguese, Italian,
// Danish, Norwegian, Swedish and Finnish: all accented characters for
// those languages are available through AltGr- combinations. Further
// explanation can be found at: https://www.altgr-weur.eu/
// - Adriaan and Enno

// Version info (for altgr-weur ONLY):
// $Id: altgr-weur,v 2.0 2021/04/12 11:27:12 adriaan Exp $

partial alphanumeric_keys
xkb_symbols "altgr-weur" {

   name[Group1]= "English (Western European AltGr dead keys)";

   key <TLDE> { [     grave, asciitilde,      dead_grave,        dead_tilde ] };
   key <AE01> { [         1,     exclam,      exclamdown,     dead_abovedot ] };
   key <AE02> { [         2,         at,     twosuperior,  dead_doubleacute ] };
   key <AE03> { [         3, numbersign,   threesuperior,       dead_macron ] };
   key <AE04> { [         4,     dollar,            cent,               yen ] };
   key <AE05> { [         5,    percent,        EuroSign,          sterling ] };
   key <AE06> { [         6,asciicircum, dead_circumflex,        dead_caron ] };
   key <AE07> { [ 7,      ampersand, doublelowquotemark, singlelowquotemark ] };
   key <AE08> { [ 8,           asterisk,          ssharp,        dead_greek ] };
   key <AE09> { [ 9, parenleft,   leftdoublequotemark,  leftsinglequotemark ] };
   key <AE10> { [ 0, parenright, rightdoublequotemark, rightsinglequotemark ] };
   key <AE11> { [     minus, underscore,          endash,            emdash ] };
   key <AE12> { [     equal,       plus,          degree,    dead_abovering ] };

   key <AD01> { [         q,          Q,           aring,             Aring ] };
   key <AD02> { [         w,          W,              ae,                AE ] };
   key <AD03> { [         e,          E,      ediaeresis,        Ediaeresis ] };
   key <AD04> { [         r,          R,          egrave,            Egrave ] };
   key <AD05> { [         t,          T,          oslash,            Oslash ] };
   key <AD06> { [         y,          Y,          ugrave,            Ugrave ] };
   key <AD07> { [         u,          U,      udiaeresis,        Udiaeresis ] };
   key <AD08> { [         i,          I,      idiaeresis,        Idiaeresis ] };
   key <AD09> { [         o,          O,      odiaeresis,        Odiaeresis ] };
   key <AD10> { [         p,          P,          ograve,            Ograve ] };
              // U203[9A]: single right/left-pointing angle quotation marks
   key <AD11> { [ bracketleft, braceleft,  guillemotleft,             U2039 ] };
   key <AD12> { [bracketright,braceright, guillemotright,             U203A ] };

   key <AC01> { [         a,          A,      adiaeresis,        Adiaeresis ] };
   key <AC02> { [         s,          S,          agrave,            Agrave ] };
   key <AC03> { [         d,          D,          eacute,            Eacute ] };
   key <AC04> { [         f,          F,     ecircumflex,       Ecircumflex ] };
   key <AC05> { [         g,          G,     icircumflex,       Icircumflex ] };
   key <AC06> { [         h,          H,     ucircumflex,       Ucircumflex ] };
   key <AC07> { [         j,          J,          uacute,            Uacute ] };
   key <AC08> { [         k,          K,          iacute,            Iacute ] };
   key <AC09> { [         l,          L,          oacute,            Oacute ] };
   key <AC10> { [ semicolon,      colon,     ocircumflex,       Ocircumflex ] };
   key <AC11> { [apostrophe,   quotedbl,      dead_acute,    dead_diaeresis ] };

   key <AB01> { [         z,          Z,          aacute,            Aacute ] };
   key <AB02> { [         x,          X,     acircumflex,       Acircumflex ] };
   key <AB03> { [         c,          C,        ccedilla,          Ccedilla ] };
   key <AB04> { [         v,          V,          atilde,            Atilde ] };
   key <AB05> { [         b,          B,          otilde,            Otilde ] };
   key <AB06> { [         n,          N,          ntilde,            Ntilde ] };
   key <AB07> { [         m,          M,          igrave,            Igrave ] };
   key <AB08> { [     comma,       less,    dead_cedilla,       dead_ogonek ] };
   key <AB09> { [    period,    greater,              oe,                OE ] };
   key <AB10> { [     slash,   question,    questiondown,       dead_stroke ] };
              //                             ij ligature        IJ ligature
   key <BKSL> { [ backslash,        bar,           U0133,             U0132 ] };

   include "level3(ralt_switch)"
};

// Intel ClassmatePC Keyboard Layout
// by Piter PUNK <piterpk@terra.com.br>
//
// The keyboard layouts below maps the us(basic), us(intl) and us(alt-intl)
// to ClassmatePC keyboard. All layouts uses RCTL as level3(switch) since
// the keyboard does not have AltGr key. The EuroSign is engraved at 5 key.

// classmate - us(basic)
partial alphanumeric_keys
xkb_symbols "classmate" {
    // #HW-SPECIFIC
    include "us(basic)"
    name[Group1]= "English (US)";

    key <LSGT> { [ backslash,	bar,		backslash,	bar ] };

    include "eurosign(5)"
    include "level3(switch)"
};

// classmate-intl - us(intl)
// RCTL is generated by Fn+Alt, because of that, when trying to access
// the level3 symbols at 7,8,9,0, u,i,o,p, j,k,l,;, and m,.,/, we get
// the keypad keycodes. The keypad is changed to make Fn+Alt+<KP_key>
// generate the same symbol as the original key.
partial alphanumeric_keys
xkb_symbols "classmate-intl" {
    // #HW-SPECIFIC
    include "us(intl)"
    name[Group1]= "English (US)";
    key.type[Group1]="FOUR_LEVEL";

    key <LSGT> { [ backslash,   bar,         backslash,            bar            ] };

    key <KP7>  { [ KP_Home,     KP_7,        onehalf,              dead_horn      ] };
    key <KP8>  { [ KP_Up,       KP_8,        threequarters,        dead_ogonek    ] };
    key <KP9>  { [ KP_Prior,    KP_9,        leftsinglequotemark,  dead_breve     ] };
    key <KPMU> { [ KP_Multiply, KP_Multiply, rightsinglequotemark, dead_abovering ] };

    key <KP4>  { [ KP_Left,     KP_4,        uacute,               Uacute         ] };
    key <KP5>  { [ KP_Begin,    KP_5,        iacute,               Iacute         ] };
    key <KP6>  { [ KP_Right,    KP_6,        oacute,               Oacute         ] };
    key <KPSU> { [ KP_Subtract, KP_Subtract, odiaeresis,           Odiaeresis     ] };

    key <KP2>  { [ KP_Down,     KP_2,        oe,                   OE             ] };
    key <KP3>  { [ KP_Next,     KP_3,        oslash,               Ooblique       ] };
    key <KPAD> { [ KP_Add,      KP_Add,      paragraph,            degree         ] };

    key <KP0>  { [ KP_Insert,   KP_0,        mu,                   mu             ] };
    key <KPDL> { [ KP_Delete,   KP_Decimal,  dead_abovedot,        dead_caron     ] };
    key <KPDV> { [ KP_Divide,   KP_Divide,   questiondown,         dead_hook      ] };

    include "level3(switch)"
};

// classmate-alt-intl - us(alt-intl)
// RCTL is generated by Fn+Alt, because of that, when trying to access
// the level3 symbols at 7,8,9,0, u,i,o,p, j,k,l,;, and m,.,/, we get
// the keypad keycodes. The keypad is changed to make Fn+Alt+<KP_key>
// generate the same symbol as the original key.
partial alphanumeric_keys
xkb_symbols "classmate-alt-intl" {
    // #HW-SPECIFIC
    include "us(alt-intl)"
    name[Group1]= "English (US)";
    key.type[Group1]="FOUR_LEVEL";

    key <LSGT> { [ backslash,   bar,         backslash,            bar            ] };

    key <KPSU> { [ KP_Subtract, KP_Subtract  ] };

    key <KP9>  { [ KP_Prior,    KP_9,        leftsinglequotemark,  dead_breve     ] };
    key <KPMU> { [ KP_Multiply, KP_Multiply, rightsinglequotemark, dead_abovering ] };

    key <KPAD> { [ KP_Add,      KP_Add,      dead_ogonek,          dead_diaeresis ] };

    key <KPDL> { [ KP_Delete,   KP_Decimal,  dead_abovedot,        dead_circumflex] };
    key <KPDV> { [ KP_Divide,   KP_Divide,   dead_hook,            dead_hook      ] };

    include "level3(switch)"
};

// classmate-altgr-intl - us(altgr-intl)
// RCTL is generated by Fn+Alt, because of that, when trying to access
// the level3 symbols at 7,8,9,0, u,i,o,p, j,k,l,;, and m,.,/, we get
// the keypad keycodes. The keypad is changed to make Fn+Alt+<KP_key>
// generate the same symbol as the original key.
partial alphanumeric_keys
xkb_symbols "classmate-altgr-intl" {
    // #HW-SPECIFIC
    include "us(altgr-intl)"
    name[Group1]= "English (US)";
    key.type[Group1]="FOUR_LEVEL";

    key <LSGT> { [ backslash,   bar,         backslash,            bar            ] };

    key <KP7>  { [ KP_Home,     KP_7,        dead_horn,            dead_horn      ] };
    key <KP8>  { [ KP_Up,       KP_8,        dead_ogonek,          dead_ogonek    ] };
    key <KP9>  { [ KP_Prior,    KP_9,        leftsinglequotemark,  dead_breve     ] };
    key <KPMU> { [ KP_Multiply, KP_Multiply, rightsinglequotemark, dead_abovering ] };

    key <KP4>  { [ KP_Left,     KP_4,        uacute,               Uacute         ] };
    key <KP5>  { [ KP_Begin,    KP_5,        iacute,               Iacute         ] };
    key <KP6>  { [ KP_Right,    KP_6,        oacute,               Oacute         ] };
    key <KPSU> { [ KP_Subtract, KP_Subtract, odiaeresis,           Odiaeresis     ] };

    key <KP1>  { [ KP_End,      KP_1,        idiaeresis,           Idiaeresis     ] };
    key <KP2>  { [ KP_Down,     KP_2,        oe,                   OE             ] };
    key <KP3>  { [ KP_Next,     KP_3,        oslash,               Ooblique       ] };
    key <KPAD> { [ KP_Add,      KP_Add,      paragraph,            degree         ] };

    key <KP0>  { [ KP_Insert,   KP_0,        mu,                   mu             ] };
    key <KPDL> { [ KP_Delete,   KP_Decimal,  dead_abovedot,        dead_caron     ] };
    key <KPDV> { [ KP_Divide,   KP_Divide,   questiondown,         dead_hook      ] };

    include "level3(switch)"
};

partial alphanumeric_keys
xkb_symbols "olpc" {

   // #HW-SPECIFIC

   include "us(basic)"
   name[Group1]= "English (US)";

   // OLPC international US English keyboard layout.
   // It's a little different from the usual international layout.
   // See: http://wiki.laptop.org/go/Image:Keyboard_english.png

   key <TLDE> { [     grave, asciitilde,    dead_grave, dead_tilde ] };
   key <AE01> { [         1,     exclam,    exclamdown, exclamdown ] };
   key <AE02> { [         2,         at,       notsign,    notsign ] };
   key <AE03> { [         3, numbersign,     0x1000300,  0x1000300 ] }; // combining grave
   key <AE04> { [         4,     dollar,     0x1000301,  0x1000301 ] }; // combining acute
   key <AE05> { [         5,    percent,     0x1000306,  0x1000306 ] }; // combining breve above
   key <AE06> { [         6,asciicircum,     0x100030A,  0x100030A ] }; // combining ring above
   key <AE07> { [         7,  ampersand,     0x1000302,  0x1000302 ] }; // combining circumflex above
   key <AE08> { [         8,   asterisk,     0x100030C,  0x100030C ] }; // combining caron above
   key <AE09> { [         9,  parenleft,     0x1000307,  0x1000307 ] }; // combining dot above
   key <AE10> { [         0, parenright,     0x1000308,  0x1000308 ] }; // combining diaeresis above
   key <AE11> { [     minus, underscore,     0x1000304,  0x1000304 ] }; // combining macron above
   key <AE12> { [     equal,       plus,     0x1000303,  0x1000303 ] }; // combining tilde above

   key <AD01> { [         q,          Q,  Greek_omega, Greek_OMEGA ] };
   key <AD02> { [         w,          W,       oslash,      Oslash ] };
   key <AD03> { [         e,          E,           oe,          OE ] };
   key <AD04> { [         r,          R,    0x1000327,   0x1000327 ] }; // combining cedilla
   key <AD05> { [         t,          T,    0x100032E,   0x100032E ] }; // combining breve below
   key <AD06> { [         y,          Y,    0x1000325,   0x1000325 ] }; // combining ring below
   key <AD07> { [         u,          U,    0x100032D,   0x100032D ] }; // combining circumflex below
   key <AD08> { [         i,          I,    0x100032C,   0x100032C ] }; // combining caron below
   key <AD09> { [         o,          O,    0x1000323,   0x1000323 ] }; // combining dot below
   key <AD10> { [         p,          P,    0x1000324,   0x1000324 ] }; // combining diaeresis below
   key <AD11> { [ bracketleft,  braceleft,  0x1000331,   0x1000331 ] }; // combining macron below
   key <AD12> { [bracketright, braceright,  0x1000330,   0x1000330 ] }; // combining tilde below

   key <AC01>  { [         a,          A,          ae,               AE ] };
   key <AC02>  { [         s,          S,      ssharp,        0x1001E9E ] }; // uppercase S sharp
   key <AC03>  { [         d,          D,         eth,              ETH ] };
   key <AC04>  { [         f,          F,       thorn,            THORN ] };
   key <AC06>  { [         h,          H,    sterling,         sterling ] };
   key <AC07>  { [         j,          J,    EuroSign,         EuroSign ] };
   key <AC10>  { [ semicolon,      colon,   masculine,      ordfeminine ] };
   key <AC11>  { [ apostrophe,  quotedbl,    currency,         currency ] };
   key <AC12>  { [ backslash,        bar,      section,         section ] };

   key <AB03>  { [         c,          C,    ccedilla,         Ccedilla ] };
   key <AB06>  { [         n,          N,      ntilde,           Ntilde ] };
   key <AB07>  { [         m,          M,          mu,               mu ] };
   key <AB08>  { [     comma,     less,  guillemotleft,   guillemotleft ] };
   key <AB09>  { [    period,  greater, guillemotright,  guillemotright ] };
   key <AB10>  { [     slash,   question, questiondown,    questiondown ] };

   key <I219>  { [  multiply,   division, ISO_Next_Group, ISO_Prev_Group ] };

   include "level3(ralt_switch)"
};

partial alphanumeric_keys
xkb_symbols "olpc2" {
   include "us(olpc)"
   name[Group1]= "English (the divide/multiply toggle the layout)";
   include "group(olpc)"
};

xkb_symbols "olpcm" {

   // #HW-SPECIFIC

   include "us(basic)"
   name[Group1]= "English (US)";

   // Mechanical (non-membrane) OLPC int'l US English keyboard layout.
   // See: http://wiki.laptop.org/go/OLPC_English_Non-membrane_Keyboard

   key <TLDE> { [     grave, asciitilde,    dead_grave, dead_tilde ] };
   key <AE01> { [         1,     exclam,    exclamdown, exclamdown ] };
   key <AE02> { [         2,         at,       notsign,    notsign ] };
   key <AE03> { [         3, numbersign,     0x1000300,  0x1000300 ] }; // combining grave
   key <AE04> { [         4,     dollar,     0x1000301,  0x1000301 ] }; // combining acute
   key <AE05> { [         5,    percent,     0x1000306,  0x1000306 ] }; // combining breve above
   key <AE06> { [         6,asciicircum,     0x100030A,  0x100030A ] }; // combining ring above
   key <AE07> { [         7,  ampersand,     0x1000302,  0x1000302 ] }; // combining circumflex above
   key <AE08> { [         8,   asterisk,     0x100030C,  0x100030C ] }; // combining caron above
   key <AE09> { [         9,  parenleft,     0x1000307,  0x1000307 ] }; // combining dot above
   key <AE10> { [         0, parenright,     0x1000308,  0x1000308 ] }; // combining diaeresis above
   key <AE11> { [     minus, underscore,     0x1000304,  0x1000304 ] }; // combining macron above

   key <AD01> { [         q,          Q,  Greek_omega, Greek_OMEGA ] };
   key <AD02> { [         w,          W,       oslash,      Oslash ] };
   key <AD03> { [         e,          E,           oe,          OE ] };
   key <AD04> { [         r,          R,    0x1000327,   0x1000327 ] }; // combining cedilla
   key <AD05> { [         t,          T,    0x100032E,   0x100032E ] }; // combining breve below
   key <AD06> { [         y,          Y,    0x1000325,   0x1000325 ] }; // combining ring below
   key <AD07> { [         u,          U,    0x100032D,   0x100032D ] }; // combining circumflex below
   key <AD08> { [         i,          I,    0x100032C,   0x100032C ] }; // combining caron below
   key <AD09> { [         o,          O,    0x1000323,   0x1000323 ] }; // combining dot below
   key <AD10> { [         p,          P,    0x1000324,   0x1000324 ] }; // combining diaeresis below
   key <AD11> { [ bracketleft,  braceleft,  0x1000331,   0x1000331 ] }; // combining macron below
   key <AD12> { [bracketright, braceright,  0x1000330,   0x1000330 ] }; // combining tilde below

   key <AC01>  { [         a,          A,          ae,               AE ] };
   key <AC02>  { [         s,          S,      ssharp,        0x1001E9E ] }; // uppercase S sharp
   key <AC03>  { [         d,          D,         eth,              ETH ] };
   key <AC04>  { [         f,          F,       thorn,            THORN ] };
   key <AC06>  { [         h,          H,    sterling,         sterling ] };
   key <AC07>  { [         j,          J,    EuroSign,         EuroSign ] };
   key <AC10>  { [ semicolon,      colon,   masculine,      ordfeminine ] };
   // no AC11 or AC12 on olpcm

   key <AB03>  { [         c,          C,    ccedilla,         Ccedilla ] };
   key <AB06>  { [         n,          N,      ntilde,           Ntilde ] };
   key <AB07>  { [         m,          M,          mu,               mu ] };
   key <AB08>  { [     comma,     less,  guillemotleft,   guillemotleft ] };
   key <AB09>  { [    period,  greater, guillemotright,  guillemotright ] };
   key <AB10>  { [     slash,   question, questiondown,    questiondown ] };

   key <AA02>  { [ backslash,        bar,      section,         section ] };
   key <AA06>  { [     equal,       plus,     0x1000303,  0x1000303 ] };
   key <AA07>  { [ apostrophe,  quotedbl,    currency,         currency ] };

   include "level3(ralt_switch)"
};

// Based on Cherokee Nation Official Layout
// http://www.cherokee.org/extras/downloads/font/Keyboard.htm

partial alphanumeric_keys modifier_keys
xkb_symbols "chr" {

    name[Group1]= "Cherokee";
    key.type[group1]="ALPHABETIC";

    key <TLDE> { [      grave,      U13CA ] };
    key <AE01> { [          1,      U13B1 ] };
    key <AE02> { [          2,      U13C7 ] };
    key <AE03> { [          3,      U13E7 ] };
    key <AE04> { [      U13D9,      U13B0 ] };
    key <AE05> { [      U13E6,      U13B9 ] };
    key <AE06> { [      U13DC,      U13DD ] };
    key <AE07> { [      U13CB,      U13E1 ] };
    key <AE08> { [      U13D6,      U13BA ] };
    key <AE09> { [      U13D2,  parenleft ] };
    key <AE10> { [      U13C4, parenright ] };
    key <AE11> { [      U13BF,      U13BC ] };
    key <AE12> { [      U13F3,      U13BD ] };

    key <AD01> { [      U13AA,      U13C6 ] };
    key <AD02> { [      U13B3,      U13EB ] };
    key <AD03> { [      U13A1,      U13E3 ] };
    key <AD04> { [      U13DB,      U13CF ] };
    key <AD05> { [      U13D4,      U13D8 ] };
    key <AD06> { [      U13EF,      U13F2 ] };
    key <AD07> { [      U13A4,      U13AD ] };
    key <AD08> { [      U13A2,      U13F1 ] };
    key <AD09> { [      U13A3,      U13EC ] };
    key <AD10> { [      U13C1,      U13EA ] };
    key <AD11> { [      U13D5,      U13D1 ] };
    key <AD12> { [      U13B6,      U13E4 ] };
    key <BKSL> { [      U13E9,      U13EE ] };

    key <AC01> { [      U13A0,      U13CC ] };
    key <AC02> { [      U13CD,      U13CE ] };
    key <AC03> { [      U13D7,      U13D0 ] };
    key <AC04> { [      U13A9,      U13C8 ] };
    key <AC05> { [      U13A6,      U13E5 ] };
    key <AC06> { [      U13AF,      U13B2 ] };
    key <AC07> { [      U13DA,      U13AB ] };
    key <AC08> { [      U13B8,      U13A7 ] };
    key <AC09> { [      U13B5,      U13AE ] };
    key <AC10> { [      U13E8,      U13E0 ] };
    key <AC11> { [ apostrophe,   quotedbl ] };

    key <AB01> { [      U13AC,      U13C3 ] };
    key <AB02> { [      U13F4,      U13ED ] };
    key <AB03> { [      U13D3,      U13DF ] };
    key <AB04> { [      U13A5,      U13DE ] };
    key <AB05> { [      U13A8,      U13F0 ] };
    key <AB06> { [      U13BE,      U13BB ] };
    key <AB07> { [      U13C5,      U13B7 ] };
    key <AB08> { [      comma,      U13E2 ] };
    key <AB09> { [     period,      U13B4 ] };
    key <AB10> { [      U13C2,      U13C9 ] };
};

// Add Hawaiian `okina and kahako to US layout
// Author: Greg Meyer <gregory.meyer@gmail.com>, 2020
// this mapping follows the one for Windows here: http://www.olelo.hawaii.edu/enehana/winkbd.php
// `okina replaces apostrophe (apostrophe moves to level 3)
// vowels with kahako (macron) are level 3 symbols
partial alphanumeric_keys
xkb_symbols "haw"  {

    include "us(basic)"
    name[Group1] = "Hawaiian";

    // `okina replaces single apostrophe
    // alt gives the literal apostrophe
    key <AC11> {[ U02BB, quotedbl, apostrophe ] };

    // kahako
    key <AC01> {[ a, A, amacron, Amacron ]};
    key <AD03> {[ e, E, emacron, Emacron ]};
    key <AD07> {[ u, U, umacron, Umacron ]};
    key <AD08> {[ i, I, imacron, Imacron ]};
    key <AD09> {[ o, O, omacron, Omacron ]};

    include "level3(ralt_switch)"
};

// Serbian charecters added as third level symbols to US keyboard layout.

partial alphanumeric_keys
xkb_symbols "hbs" {

  include "us"
  name[Group1]= "Serbo-Croatian (US)";

  key <TLDE> { [ grave, asciitilde ] };
  key <AE06> { [ 6, dead_caron, asciicircum, asciicircum ] };
  key <AE08> { [ 8, asterisk, multiply, division ] };
  key <AE11> { [ minus, underscore, endash, emdash ] };
  key <AC09> { [ l, L, U1C9, U1C8 ] };
  key <AB06> { [ n, N, U1CC, U1CB ] };
  key <AB01> { [ z, Z, U1C6, U1C5 ] };
  key <AD03> { [ e, E, EuroSign, cent ] };
  key <AC03> { [ d, D, dstroke, Dstroke ] };
  key <AC11> { [ dead_acute, quotedbl, apostrophe, apostrophe ] };
  key <SPCE> { [ space, space, nobreakspace, nobreakspace ] };
  key <AB08> { [ comma, less, U3003, guillemotright ] };
  key <AB09> { [ period, greater, ellipsis, guillemotleft ] };

  include "level3(ralt_switch)"
};

// Workman Keyboard Layout symbols for xkb on X.Org Server 7.x
// 09-06-2010 OJ Bucao. http://www.workmanlayout.com

partial alphanumeric_keys
xkb_symbols "workman" {

    include "us(basic)"
    name[Group1]= "English (Workman)";

    key <AD01> {  [   q,  Q   ] };
    key <AD02> {  [   d,  D   ] };
    key <AD03> {  [   r,  R   ] };
    key <AD04> {  [   w,  W   ] };
    key <AD05> {  [   b,  B   ] };
    key <AD06> {  [   j,  J   ] };
    key <AD07> {  [   f,  F   ] };
    key <AD08> {  [   u,  U   ] };
    key <AD09> {  [   p,  P   ] };
    key <AD10> {  [   semicolon,  colon   ] };

    key <AC01> {  [   a,  A   ] };
    key <AC02> {  [   s,  S   ] };
    key <AC03> {  [   h,  H   ] };
    key <AC04> {  [   t,  T   ] };
    key <AC05> {  [   g,  G   ] };
    key <AC06> {  [   y,  Y   ] };
    key <AC07> {  [   n,  N   ] };
    key <AC08> {  [   e,  E   ] };
    key <AC09> {  [   o,  O   ] };
    key <AC10> {  [   i,  I   ] };

    key <AB01> {  [   z,  Z   ] };
    key <AB02> {  [   x,  X   ] };
    key <AB03> {  [   m,  M   ] };
    key <AB04> {  [   c,  C   ] };
    key <AB05> {  [   v,  V   ] };
    key <AB06> {  [   k,  K   ] };
    key <AB07> {  [   l,  L   ] };

    key <CAPS> { [    BackSpace,       Escape,       BackSpace,        BackSpace ] };

    include "level3(ralt_switch)"
};

partial alphanumeric_keys
xkb_symbols "workman-intl" {

    include "us(intl)"
    name[Group1]= "English (Workman, intl., with dead keys)";

    key <AD01> { [     q,          Q,    adiaeresis,       Adiaeresis ] };
    key <AD02> { [     d,          D,           eth,              ETH ] };
    key <AD03> { [     r,          R,    registered,       registered ] };
    key <AD04> { [     w,          W,         aring,            Aring ] };
    key <AD05> { [     b,          B,             b,                B ] };
    key <AD06> { [     j,          J,             j,                J ] };
    key <AD07> { [     f,          F,             f,                F ] };
    key <AD08> { [     u,          U,        uacute,           Uacute ] };
    key <AD09> { [     p,          P,    odiaeresis,       Odiaeresis ] };
    key <AD10> { [ semicolon,  colon,     paragraph,           degree ] };

    key <AC01> { [     a,          A,        aacute,           Aacute ] };
    key <AC02> { [     s,          S,        ssharp,          section ] };
    key <AC03> { [     h,          H,             h,                H ] };
    key <AC04> { [     t,          T,         thorn,            THORN ] };
    key <AC05> { [     g,          G,             g,                G ] };
    key <AC06> { [     y,          Y,    udiaeresis,       Udiaeresis ] };
    key <AC07> { [     n,          N,        ntilde,           Ntilde ] };
    key <AC08> { [     e,          E,        eacute,           Eacute ] };
    key <AC09> { [     o,          O,        oacute,           Oacute ] };
    key <AC10> { [     i,          I,        iacute,           Iacute ] };

    key <AB01> { [     z,          Z,            ae,               AE ] };
    key <AB02> { [     x,          X,             x,                X ] };
    key <AB03> { [     m,          M,            mu,               mu ] };
    key <AB04> { [     c,          C,     copyright,             cent ] };
    key <AB05> { [     v,          V,             v,                V ] };
    key <AB06> { [     k,          K,            oe,               OE ] };
    key <AB07> { [     l,          L,        oslash,         Ooblique ] };

    key <CAPS> { [ BackSpace, Escape,     BackSpace,        BackSpace ] };

    include "level3(ralt_switch)"
};

// Norman keyboard layout symbols for xkb on X.Org Server 7.x
// Written 11/23/2012, revised 3/7/2013 by David Norman http://normanlayout.info
// To the extent possible under law, the author(s) have dedicated all
// copyright and related and neighboring rights to this software to the
// public domain worldwide. This software is distributed without any warranty.

partial alphanumeric_keys
xkb_symbols "norman" {

    include "us(basic)"
    name[Group1]= "English (Norman)";

    key <AD01> { [ q, Q ] };
    key <AD02> { [ w, W ] };
    key <AD03> { [ d, D ] };
    key <AD04> { [ f, F ] };
    key <AD05> { [ k, K ] };
    key <AD06> { [ j, J ] };
    key <AD07> { [ u, U ] };
    key <AD08> { [ r, R ] };
    key <AD09> { [ l, L ] };
    key <AD10> { [ semicolon, colon ] };

    key <AC01> { [ a, A ] };
    key <AC02> { [ s, S ] };
    key <AC03> { [ e, E ] };
    key <AC04> { [ t, T ] };
    key <AC05> { [ g, G ] };
    key <AC06> { [ y, Y ] };
    key <AC07> { [ n, N ] };
    key <AC08> { [ i, I ] };
    key <AC09> { [ o, O ] };
    key <AC10> { [ h, H ] };

    key <AB01> { [ z, Z ] };
    key <AB02> { [ x, X ] };
    key <AB03> { [ c, C ] };
    key <AB04> { [ v, V ] };
    key <AB05> { [ b, B ] };
    key <AB06> { [ p, P ] };
    key <AB07> { [ m, M ] };

    key <CAPS> { [ BackSpace ] };

    include "level3(ralt_switch)"
};

// Carpalx layout created by Martin Krzywinski
// http://mkweb.bcgsc.ca/carpalx/

partial alphanumeric_keys
xkb_symbols "carpalx" {

    name[Group1]= "English (Carpalx)";

    key <TLDE> {	[     grave,	asciitilde	]	};
    key <AE01> {	[	  1,	exclam 		]	};
    key <AE02> {	[	  2,	at		]	};
    key <AE03> {	[	  3,	numbersign	]	};
    key <AE04> {	[	  4,	dollar		]	};
    key <AE05> {	[	  5,	percent		]	};
    key <AE06> {	[	  6,	asciicircum	]	};
    key <AE07> {	[	  7,	ampersand	]	};
    key <AE08> {	[	  8,	asterisk	]	};
    key <AE09> {	[	  9,	parenleft	]	};
    key <AE10> {	[	  0,	parenright	]	};
    key <AE11> {	[     minus,	underscore	]	};
    key <AE12> {	[     equal,	plus		]	};

    key <AD01> {	[	  q,	Q 		]	};
    key <AD02> {	[	  g,	G		]	};
    key <AD03> {	[	  m,	M		]	};
    key <AD04> {	[	  l,	L		]	};
    key <AD05> {	[	  w,	W		]	};
    key <AD06> {	[	  y,	Y		]	};
    key <AD07> {	[	  f,	F		]	};
    key <AD08> {	[	  u,	U		]	};
    key <AD09> {	[	  b,	B		]	};
    key <AD10> {	[ semicolon,	colon		]	};
    key <AD11> {	[ bracketleft,	braceleft	]	};
    key <AD12> {	[ bracketright,	braceright	]	};

    key <AC01> {	[	  d,	D 		]	};
    key <AC02> {	[	  s,	S		]	};
    key <AC03> {	[	  t,	T		]	};
    key <AC04> {	[	  n,	N		]	};
    key <AC05> {	[	  r,	R		]	};
    key <AC06> {	[	  i,	I		]	};
    key <AC07> {	[	  a,	A		]	};
    key <AC08> {	[	  e,	E		]	};
    key <AC09> {	[	  o,	O		]	};
    key <AC10> {	[	  h,	H		]	};
    key <AC11> {	[ apostrophe,	quotedbl	]	};

    key <AB01> {	[	  z,	Z 		]	};
    key <AB02> {	[	  x,	X		]	};
    key <AB03> {	[	  c,	C		]	};
    key <AB04> {	[	  v,	V		]	};
    key <AB05> {	[	  j,	J		]	};
    key <AB06> {	[	  k,	K		]	};
    key <AB07> {	[	  p,	P		]	};
    key <AB08> {	[     comma,	less		]	};
    key <AB09> {	[    period,	greater		]	};
    key <AB10> {	[     slash,	question	]	};

    key <BKSL> {	[ backslash,         bar	]	};
};

// Carpalx layout created by Martin Krzywinski
// http://mkweb.bcgsc.ca/carpalx/
// Merged with us(intl) and modified to move
// accented vowels closer to the plain vowels

partial alphanumeric_keys
xkb_symbols "carpalx-intl" {

    name[Group1]= "English (Carpalx, intl., with dead keys)";

    key <TLDE> { [dead_grave, dead_tilde,         grave,       asciitilde ] };
    key <AE01> { [	   1,     exclam,    exclamdown,      onesuperior ] };
    key <AE02> { [	   2,         at,   twosuperior, dead_doubleacute ] };
    key <AE03> { [	   3, numbersign, threesuperior,      dead_macron ] };
    key <AE04> { [	   4,     dollar,      currency,         sterling ] };
    key <AE05> { [	   5,    percent,      EuroSign,     dead_cedilla ] };
    key <AE06> { [    6, dead_circumflex,    onequarter,      asciicircum ] };
    key <AE07> { [	   7,  ampersand,       onehalf,	dead_horn ] };
    key <AE08> { [	   8,   asterisk, threequarters,      dead_ogonek ] };
    key <AE09> { [	   9,  parenleft, leftsinglequotemark, dead_breve ] };
    key <AE10> { [	   0, parenright, rightsinglequotemark, dead_abovering ] };
    key <AE11> { [     minus, underscore,           yen,    dead_belowdot ] };
    key <AE12> { [     equal,       plus,      multiply,         division ] };

    key <AD01> { [	   q,          Q,        degree,        paragraph ] };
    key <AD02> { [	   g,          G,         U011F,            U011E ] };
    key <AD03> { [	   m,          M,            mu,               mu ] };
    key <AD04> { [	   l,          L,     copyright,             cent ] };
    key <AD05> { [	   w,          W,             w,                W ] };
    key <AD06> { [	   y,          Y,    idiaeresis,       Idiaeresis ] };
    key <AD07> { [	   f,          F,    adiaeresis,       Adiaeresis ] };
    key <AD08> { [	   u,          U,    udiaeresis,       Udiaeresis ] };
    key <AD09> { [	   b,          B,    odiaeresis,       Odiaeresis ] };
    key <AD10> { [ semicolon,      colon,        oslash,         Ooblique ] };
    key <AD11> { [ bracketleft,  braceleft,  guillemotleft, leftdoublequotemark ] };
    key <AD12> { [bracketright, braceright, guillemotright, rightdoublequotemark ] };

    key <AC01> { [	   d,          D,           eth,              ETH ] };
    key <AC02> { [	   s,          S,        ssharp,          section ] };
    key <AC03> { [	   t,          T,         thorn,            THORN ] };
    key <AC04> { [	   n,          N,        ntilde,           Ntilde ] };
    key <AC05> { [	   r,          R,    registered,       registered ] };
    key <AC06> { [	   i,          I,        iacute,           Iacute ] };
    key <AC07> { [	   a,          A,        aacute,           Aacute ] };
    key <AC08> { [	   e,          E,        eacute,           Eacute ] };
    key <AC09> { [	   o,          O,        oacute,           Oacute ] };
    key <AC10> { [	   h,          H,        uacute,           Uacute ] };
    key <AC11> { [dead_acute, dead_diaeresis, apostrophe,        quotedbl ] };

    key <AB01> { [	   z,          Z,             z,                Z ] };
    key <AB02> { [	   x,          X,         U015F,            U015E ] };
    key <AB03> { [	   c,          C,      ccedilla,         Ccedilla ] };
    key <AB04> { [	   v,          V,            ae,               AE ] };
    key <AB05> { [	   j,          J,            oe,               OE ] };
    key <AB06> { [	   k,          K,         U0131,            U0130 ] };
    key <AB07> { [	   p,          P,         aring,            Aring ] };
    key <AB08> { [     comma,       less,    ediaeresis,       Ediaeresis ] };
    key <AB09> { [    period,    greater, dead_abovedot,       dead_caron ] };
    key <AB10> { [     slash,   question,  questiondown,        dead_hook ] };
    key <BKSL> { [ backslash,        bar,       notsign,        brokenbar ] };

    key <LSGT> { [ backslash,   bar,            backslash,      bar ] };

    include "level3(ralt_switch)"
};

// Carpalx layout created by Martin Krzywinski
// http://mkweb.bcgsc.ca/carpalx/
// Merged with us(intl) and us(altgr-intl) and modified to move
// accented vowels closer to the plain vowels

partial alphanumeric_keys
xkb_symbols "carpalx-altgr-intl" {

   include "us(carpalx-intl)"
   name[Group1]= "English (Carpalx, intl., with AltGr dead keys)";

   key <TLDE> { [    grave, asciitilde,  dead_grave,   dead_tilde      ] };
   key <AC11> { [apostrophe,quotedbl,    dead_acute,   dead_diaeresis  ] };

   key <AE01> { [        1, exclam,      onesuperior,  exclamdown      ] };

   key <AE06> { [        6, asciicircum, dead_circumflex, onequarter    ] };
   key <AE07> { [        7, ampersand,   dead_horn,       onehalf       ] };
   key <AE08> { [        8, asterisk,    dead_ogonek,     threequarters ] };

   include "level3(ralt_switch)"
};

// Carpalx layout created by Martin Krzywinski
// Full optimization variant without fixed QWERTY-like ZXCV keys
// http://mkweb.bcgsc.ca/carpalx/

partial alphanumeric_keys
xkb_symbols "carpalx-full" {

    include "us(carpalx)"
    name[Group1]= "English (Carpalx, full optimization)";

    key <AD06> {	[	  b,	B		]	};
    key <AD07> {	[	  y,	Y		]	};
    key <AD09> {	[	  v,	V		]	};

    key <AB04> {	[	  f,	F		]	};
};

// Carpalx layout created by Martin Krzywinski
// Full optimization variant without fixed QWERTY-like ZXCV keys
// http://mkweb.bcgsc.ca/carpalx/
// Merged with us(intl) and modified to move
// accented vowels closer to the plain vowels

partial alphanumeric_keys
xkb_symbols "carpalx-full-intl" {

    include "us(carpalx-intl)"
    name[Group1]= "English (Carpalx, full optimization, intl., with dead keys)";

    key <AD06> { [	   b,          B,    idiaeresis,       Idiaeresis ] };
    key <AD07> { [	   y,          Y,    adiaeresis,       Adiaeresis ] };
    key <AD09> { [	   v,          V,    odiaeresis,       Odiaeresis ] };

    key <AB04> { [	   f,          F,            ae,               AE ] };
};

// Carpalx layout created by Martin Krzywinski
// Full optimization variant without fixed QWERTY-like ZXCV keys
// http://mkweb.bcgsc.ca/carpalx/
// Merged with us(intl) and us(altgr-intl) and modified to move
// accented vowels closer to the plain vowels

partial alphanumeric_keys
xkb_symbols "carpalx-full-altgr-intl" {

   include "us(carpalx-altgr-intl)"
   name[Group1]= "English (Carpalx, full optimization, intl., with AltGr dead keys)";

    key <AD06> { [	   b,          B,    idiaeresis,       Idiaeresis ] };
    key <AD07> { [	   y,          Y,    adiaeresis,       Adiaeresis ] };
    key <AD09> { [	   v,          V,    odiaeresis,       Odiaeresis ] };

    key <AB04> { [	   f,          F,            ae,               AE ] };
};

// US Symbolic
// Author: Daniele Baisero <daniele.baisero@gmail.com>
// Based on the default keyboard map from 'symbols/us', edited for scientific literature.
// Added simple Greek letters to alphas, and common symbols everywhere else.
// TLDE and BKSL are AltGr-inverse, to facilitate placement of ESC over TLDE on 60% keyboards.
// LGST (Iso Key) contains rarely used floor and ceiling brackets.
partial alphanumeric_keys modifier_keys
xkb_symbols "symbolic" {

 name[Group1]= "English (US, Symbolic)";

 key <TLDE> { [ grave, asciitilde,  backslash,     bar            ] }; // ` ~ \ |
 key <AE01> { [ 1,     exclam,      onesuperior,   notsign        ] }; // 1 ! ¹ ¬
 key <AE02> { [ 2,     at,          twosuperior,   therefore      ] }; // 2 @ ² ∴
 key <AE03> { [ 3,     numbersign,  threesuperior, sterling       ] }; // 3 # ³ £
 key <AE04> { [ 4,     dollar,      foursuperior,  EuroSign       ] }; // 4 $ ⁴ €
 key <AE05> { [ 5,     percent,     fivesuperior,  U2030          ] }; // 5 % ⁵ ‰
 key <AE06> { [ 6,     asciicircum, sixsuperior,   squareroot     ] }; // 6 ^ ⁶ √
 key <AE07> { [ 7,     ampersand,   sevensuperior, section        ] }; // 7 & ⁷ §
 key <AE08> { [ 8,     asterisk,    eightsuperior, infinity       ] }; // 8 * ⁸ ∞
 key <AE09> { [ 9,     parenleft,   ninesuperior,  periodcentered ] }; // 9 ( ⁹ ·
 key <AE10> { [ 0,     parenright,  zerosuperior,  degree         ] }; // 0 ) ⁰ °
 key <AE11> { [ minus, underscore,  notequal,      plusminus      ] }; // - _ ≠ ±
 key <AE12> { [ equal, plus,        multiply,      division       ] }; // = + × ÷

 key <AD01> { [ q,            Q,          U2200,         U2203         ] }; // q Q ∀ ∃
 key <AD02> { [ w,            W,          elementof,     notelementof  ] }; // w W ∈ ∉
 key <AD03> { [ e,            E,          Greek_epsilon, Greek_EPSILON ] }; // e E ε Ε
 key <AD04> { [ r,            R,          Greek_rho,     Greek_RHO     ] }; // p P ρ Ρ
 key <AD05> { [ t,            T,          Greek_tau,     Greek_TAU     ] }; // t T τ Τ
 key <AD06> { [ y,            Y,          Greek_upsilon, Greek_UPSILON ] }; // y Y υ Υ
 key <AD07> { [ u,            U,          Greek_theta,   Greek_THETA   ] }; // u U θ Θ
 key <AD08> { [ i,            I,          Greek_iota,    Greek_IOTA    ] }; // i I ι Ι
 key <AD09> { [ o,            O,          Greek_omicron, Greek_OMICRON ] }; // o O ο Ο
 key <AD10> { [ p,            P,          Greek_pi,      Greek_PI      ] }; // p P π Π
 key <AD11> { [ bracketleft,  braceleft,  union,         intersection  ] }; // [ { ∪ ∩
 key <AD12> { [ bracketright, braceright, includedin,    includes      ] }; // ] } ⊂ ⊃

 key <AC01> { [ a,          A,        Greek_alpha, Greek_ALPHA ] }; // a A α Α
 key <AC02> { [ s,          S,        Greek_sigma, Greek_SIGMA ] }; // s S σ Σ
 key <AC03> { [ d,          D,        Greek_delta, Greek_DELTA ] }; // d D δ Δ
 key <AC04> { [ f,          F,        Greek_phi,   Greek_PHI   ] }; // f F φ Φ
 key <AC05> { [ g,          G,        Greek_gamma, Greek_GAMMA ] }; // g G γ Γ
 key <AC06> { [ h,          H,        Greek_eta,   Greek_ETA   ] }; // h H η Η
 key <AC07> { [ j,          J,        Greek_xi,    Greek_XI    ] }; // j J ξ Ξ
 key <AC08> { [ k,          K,        Greek_kappa, Greek_KAPPA ] }; // k K κ Κ
 key <AC09> { [ l,          L,        Greek_lamda, Greek_LAMDA ] }; // l L λ Λ
 key <AC10> { [ semicolon,  colon,    downarrow,   uparrow     ] }; // ; : ↓ ↑
 key <AC11> { [ apostrophe, quotedbl, rightarrow,  leftarrow   ] }; // ' " → ←

 key <AB01> { [ z,      Z,        Greek_zeta,       Greek_ZETA     ] }; // z Z ζ Ζ
 key <AB02> { [ x,      X,        Greek_chi,        Greek_CHI      ] }; // x X χ Χ
 key <AB03> { [ c,      C,        Greek_psi,        Greek_PSI      ] }; // c C ψ Ψ
 key <AB04> { [ v,      V,        Greek_omega,      Greek_OMEGA    ] }; // v V ω Ω
 key <AB05> { [ b,      B,        Greek_beta,       Greek_BETA     ] }; // b B β Β
 key <AB06> { [ n,      N,        Greek_nu,         Greek_NU       ] }; // n N ν Ν
 key <AB07> { [ m,      M,        Greek_mu,         Greek_MU       ] }; // m M μ Μ
 key <AB08> { [ comma,  less,     lessthanequal,    guillemotleft  ] }; // , < ≤ «
 key <AB09> { [ period, greater,  greaterthanequal, guillemotright ] }; // . > ≥ »
 key <AB10> { [ slash,  question, U203D,            U2766          ] }; // / ? ‽ ❦

 key <BKSL> { [ backslash, bar,   grave, asciitilde ] }; // \ | ` ~
 key <LSGT> { [ U230A,     U230B, U2308, U2309      ] }; // ⌊ ⌋ ⌈ ⌉

 include "level3(ralt_switch)"
};

// EXTRAS:

// Czech, Slovak and German charecters added as third level symbols to US keyboard layout.
partial alphanumeric_keys
xkb_symbols "cz_sk_de" {

    include "us"
    name[Group1]="Czech Slovak and German (US)";

    key <TLDE>  { [grave,   asciitilde, uring,      Uring       ] };
    key <AE01>	{ [    1,	exclam,	uacute,	    Uacute	] };
    key <AE02>	{ [    2,           at, ecaron,	    Ecaron	] };
    key <AE03>	{ [    3,   numbersign, scaron,	    Scaron	] };
    key <AE04>	{ [    4,       dollar,	ccaron,	    Ccaron	] };
    key <AE05>	{ [    5,      percent, rcaron,	    Rcaron	] };
    key <AE06>	{ [    6,  asciicircum, zcaron,	    Zcaron	] };
    key <AE07>	{ [    7,    ampersand,	yacute,	    Yacute	] };
    key <AE08>	{ [    8,     asterisk, aacute,	    Aacute	] };
    key <AE09>	{ [    9,    parenleft,	iacute,	    Iacute	] };
    key <AE10>	{ [    0,   parenright, eacute,	    Eacute	] };
    key <AE11>	{ [minus,   underscore, ssharp,     0x1001E9E	] };
    key <AE12>	{ [equal,	  plus, dead_acute, dead_caron  ] };

    key <AD03>	{ [         e,          E,     EuroSign,     Eacute ]	};

    key <AD11>	{ [bracketleft, braceleft,   udiaeresis,   Udiaeresis ]	};
    key <AC10>	{ [ semicolon,      colon,   odiaeresis,   Odiaeresis ]	};
    key <AC11>	{ [apostrophe,      quotedbl,adiaeresis,   Adiaeresis ]	};

    key <AC01>	{ [         a,          A,     aacute,	     Aacute   ]	};
    key <AD08>	{ [         i,          I,     iacute,	     Iacute   ]	};
    key <AD09>	{ [         o,          O,     oacute,       Oacute   ]	};
    key <AD06>	{ [         y,          Y,     yacute,       Yacute   ]	};
    key <AD07>	{ [         u,          U,     uring,	     Uring    ]	};

    key <AC02>	{ [         s,          S,     scaron,       Scaron   ]	};
    key <AB01>	{ [         z,          Z,     zcaron,	     Zcaron   ]	};
    key <AB03>	{ [         c,          C,     ccaron,       Ccaron   ]	};
    key <AD04>	{ [         r,          R,     rcaron,	     Rcaron   ]	};
    key <AD05>	{ [         t,          T,     tcaron,	     Tcaron   ]	};
    key <AC03>	{ [         d,          D,     dcaron,	     Dcaron   ]	};
    key <AB06>	{ [         n,          N,     ncaron,	     Ncaron   ]	};
    key <AC09>  { [         l,          L,     lcaron,       Lcaron   ] };
    key <AD10>  { [         p,          P,ocircumflex,  Ocircumflex   ] };

    key <SPCE>  { [     space,       space, nobreakspace, nobreakspace] };

    include "level3(ralt_switch)"
};

// This is the above Jirka's us(cz_sk_de) layout variant extended with Polish, Spanish, Finnish and Swedish characters.
// This layout variant is primarily targeted to Czech and Slovak polyglots and SW engineers (like the original above one).
partial alphanumeric_keys
xkb_symbols "cz_sk_pl_de_es_fi_sv" {

    include "us"
    name[Group1]="Czech, Slovak, Polish, Spanish, Finnish, Swedish and German (US)";

    key <TLDE>  { [grave,   asciitilde, uring,      Uring       ] };
    key <AE01>	{ [    1,	exclam,	uacute,	    Uacute	] };
    key <AE02>	{ [    2,           at, ecaron,	    Ecaron	] };
    key <AE03>	{ [    3,   numbersign, scaron,	    Scaron	] };
    key <AE04>	{ [    4,       dollar,	ccaron,	    Ccaron	] };
    key <AE05>	{ [    5,      percent, rcaron,	    Rcaron	] };
    key <AE06>	{ [    6,  asciicircum, zcaron,	    Zcaron	] };
    key <AE07>	{ [    7,    ampersand,	yacute,	    Yacute	] };
    key <AE08>	{ [    8,     asterisk, aacute,	    Aacute	] };
    key <AE09>	{ [    9,    parenleft,	iacute,	    Iacute	] };
    key <AE10>	{ [    0,   parenright, eacute,	    Eacute	] };
    key <AE11>	{ [minus,   underscore, ssharp,     0x1001E9E	] };
    key <AE12>	{ [equal,	  plus, dead_acute, dead_caron  ] };

    key <AD03>	{ [         e,          E,     EuroSign,     Eacute ]	};

    key <AD11>	{ [bracketleft, braceleft,   udiaeresis,   Udiaeresis ]	};
    key <AC10>	{ [ semicolon,      colon,   odiaeresis,   Odiaeresis ]	};
    key <AC11>	{ [apostrophe,      quotedbl,adiaeresis,   Adiaeresis ]	};

    key <AC01>	{ [         a,          A,     aacute,	     Aacute   ]	};
    key <AD08>	{ [         i,          I,     iacute,	     Iacute   ]	};
    key <AD09>	{ [         o,          O,     oacute,       Oacute   ]	};
    key <AD06>	{ [         y,          Y,     yacute,       Yacute   ]	};
    key <AD07>	{ [         u,          U,     uring,	     Uring    ]	};

    key <AC02>	{ [         s,          S,     scaron,       Scaron   ]	};
    key <AB01>	{ [         z,          Z,     zcaron,	     Zcaron   ]	};
    key <AB03>	{ [         c,          C,     ccaron,       Ccaron   ]	};
    key <AD04>	{ [         r,          R,     rcaron,	     Rcaron   ]	};
    key <AD05>	{ [         t,          T,     tcaron,	     Tcaron   ]	};
    key <AC03>	{ [         d,          D,     dcaron,	     Dcaron   ]	};
    key <AB06>	{ [         n,          N,     ncaron,	     Ncaron   ]	};
    key <AC09>  { [         l,          L,     lcaron,       Lcaron   ] };
    key <AD10>  { [         p,          P,ocircumflex,  Ocircumflex   ] };

    key <SPCE>  { [     space,       space, nobreakspace, nobreakspace] };

    // Polish
    key <AD01>	{ [         q,          Q,      aogonek,      Aogonek ]	};
    key <AD02>	{ [         w,          W,      eogonek,      Eogonek ]	};
    key <AD12>	{ [bracketright, braceright, guillemotleft, guillemotright ] };
    key <AC04>	{ [         f,          F,       sacute,       Sacute ]	};
    key <AC05>	{ [         g,          G,    copyright,   registered ]	};
    key <AC06>	{ [         h,          H,         cent,    trademark ]	};
    key <AC07>	{ [         j,          J,    plusminus,       degree ] };
    key <AC08>	{ [         k,          K,      lstroke,      Lstroke ]	};
    //alias <AC12> = <BKSL>;
    key <BKSL>	{ [ backslash,        bar,        aring,      Aring   ] };
    //Requires pc105 compatibility
    key <LSGT>	{ [    endash,     emdash,    zabovedot,    Zabovedot ]	};
    key <AB02>	{ [         x,          X,       zacute,       Zacute ]	};
    key <AB04>	{ [         v,          V,       cacute,       Cacute ]	};
    key <AB05>	{ [         b,          B,       ntilde,       Ntilde ] };
    key <AB07>	{ [         m,          M,       nacute,       Nacute ]	};
    key <AB08>	{ [     comma,       less,lessthanequal,     multiply ]	};
    key <AB09>	{ [    period,    greater, greaterthanequal, division ]	};
    key <AB10>	{ [     slash,   question,   exclamdown, questiondown ] };

    include "level3(ralt_switch)"
};

// 03 December 2017 - Added us(scn), please refer to
//                    Cadèmia Siciliana <l10n@cademiasiciliana.org>
partial alphanumeric_keys
xkb_symbols "scn" {

    include "us(intl)"
    name[Group1]="Sicilian (US keyboard)";

    key <AD03> { [      e,       E, U0259,       U018F ] };
    key <AC03> { [      d,       D, U1E0D,       U1E0C ] };
    key <AC04> { [      f,       F, U0111,       U0110 ] };
    key <AC06> { [      h,       H, U1E25,       U1E24 ] };
    key <AB02> { [      x,       X, U03C7,       U03A7 ] };
    key <AB09> { [ period, greater, U1D58,  dead_caron ] };

    include "level3(ralt_switch)"
};

// XCompose is out! Unicode combining is in!  For those of us who live
// on the edge: A keymap using Unicode combining characters instead of
// deadkeys.  This variation does not deviate from the lame MS-style
// US-intl layout; but it uses AltGr for combining, like altgr-intl.
//
// This might break your font layout systems (because they suck),
// caveat emptor.  Also, most of today's software will count
// individual combining marks for selection, deletion, character
// counting &c., and won't be smart enough to do canonical equivalence
// when searching, &c.
//
// With Unicode combining you use "handwriting order", not
// "typewriting order" as with deadkeys.  That is, you first type the
// base character, then the diacritics/accents/modifiers.  This has
// the advantage of avoiding hidden states --- each keypress changes
// something on screen.
//
// TODO: as of now, this duplicates all us(intl) functionality with
// combining.  With care, perhaps we could add more combining marks
// not present in intl, and support all major languages.
partial alphanumeric_keys
xkb_symbols "intl-unicode" {

 include "us(intl)"
 include "level3(ralt_switch)"

 name[Group1]= "English (US, intl., AltGr Unicode combining)";

 key <TLDE> { [ grave, asciitilde, U0300, U0303 ] }; // grave, tilde
 key <AE02> { [ 2, at, twosuperior, U030B ] }; // double acute
 key <AE03> { [ 3, numbersign, threesuperior, U0304 ] }; // macron
 key <AE06> { [ 6, asciicircum, onequarter, U0302 ] }; // circumflex
 key <AE07> { [ 7, ampersand, onehalf, U031B ] }; // horn
 key <AE08> { [ 8, asterisk, threequarters, U0328 ] }; // ogonek
 key <AE09> { [ 9, parenleft, leftsinglequotemark, U0306 ] }; // breve
 key <AE10> { [ 0, parenright, rightsinglequotemark, U030A ] }; // abovering

 key <AE11> { [ minus, underscore, yen, U0323 ] }; // belowdot
 key <AC11> { [ apostrophe, quotedbl, U0301, U0308 ] }; // acute, diaeresis
 key <AB09> { [ period, greater, U0307, U030C ] }; // abovedot, caron
 key <AB10> { [ slash, question, questiondown, U0309 ] }; // hook

 // alt-intl compatibility
 key <AB08> { [ comma, less, U0327, U030C ] }; // cedilla, caron
 key <AC10> { [ semicolon, colon, U0328, U0308 ] }; // ogonek, diaeresis
 key <AE12> { [ equal, plus, U030B, U031B ] }; // doubleacute, horn

 // We don't do combining latin letters and combining enclosures,
 // because support for those is very rare.
};

// XCompose is out! Unicode combining is in! For those of us who live
// on the edge: A keymap using Unicode combining characters instead of
// deadkeys. This variation does break compatibility with us-intl,
// whenever I thought it would be more mnemonic or Unicodeish.
partial alphanumeric_keys
xkb_symbols "alt-intl-unicode" {

 include "us(intl-unicode)"

 name[Group1]= "English (US, intl., AltGr Unicode combining, alt.)";

 // easier macron; em-dash.
 // em-dash is available via compose, but I added here since it's such
 // an important typographic character.
 key <AE11> { [ minus, underscore, U0304, U2014 ] };

 // belowdot, abovedot (caron at coma/less key, per above)
 key <AB09> { [ period, greater, U0323, U0307 ] };
};

partial alphanumeric_keys
xkb_symbols "ats" {

    include "us"
    name[Group1]= "Atsina";

    //Using Dead key to get COMBINING COMMA ABOVE for ejectives on
    //q, l, t, s, m, g, k, p, w, y, r
    //XCompose key is used for the other accute and grave.

    key <AD03> { [ e, E, eacute, Eacute  ] };
    key <AD07> { [ u, U, uacute, Uacute  ] };
    key <AD08> { [ i, I, iacute, Iacute  ] };
    key <AD09> { [ o, O, oacute, Oacute  ] };
    key <AD11> { [ bracketleft,	braceleft, U03B8 ] };
    key <AD12> { [ bracketright, braceright, U010D, U010C ] };
    //U+010C (uppercase Č) and U+010D (lowercase č).

    key <AC01> { [ a, A, aacute, Aacute  ] };

    //Small letter Open use compose to key get acute accent
    key <AB03> { [ c,	C, U0254, U0186		  ] };
    key <AB08> { [ comma,     less, U0313 ] };
    key <AB10> { [ slash, question, U0294 ] };

    include "level3(ralt_switch)"
    include "compose(rctrl)"
};

partial alphanumeric_keys
xkb_symbols "crd" {

  include "us"
  name[Group1]= "Coeur d'Alene Salish";

  key <AD02> { [         w,           W, U02B7, U02B7 ] };
  key <AE07> { [         7,   ampersand, U0294        ] };
  key <AD01> { [         q,           Q, U221A        ] };
  key <AB04> { [         v,           V, U0259        ] };
  key <BKSL> { [ backslash,         bar, U026B        ] };
  key <AD03> { [         e,           E, U025B        ] };
  key <AD08> { [         i,           I, U026A        ] };
  key <AC07> { [         j,           J, U01F0        ] };
  key <AE06> { [         6, asciicircum, U0295        ] };
  key <AC02> { [         s,           S, U0161        ] };
  key <AB03> { [         c,           C, U010D        ] };
  key <AD09> { [         o,           O, U0254        ] };
  key <AB09> { [    period,     greater, U0323        ] };

  include "level3(ralt_switch)"
  include "compose(rctrl)"
};


partial alphanumeric_keys
	xkb_symbols "sun_type6" {
	include "sun_vndr/us(sun_type6)"
};

// Implementation of the 3l keyboard layout
// See https://github.com/jackrosenthal/threelayout for specification
partial alphanumeric_keys modifier_keys
xkb_symbols "3l" {
    name[Group1] = "English (3l)";

    key.type[Group1] = "ONE_LEVEL";
    key <TAB> { [ Escape ] };
    key <CAPS> { [ Tab ] };
    key <AC11> { [ ISO_Level3_Shift ] }; // Sym Modifier
    key <AB10> { [ ISO_Level5_Shift ] }; // Cur/Num Modifier

    // Top row numbers - not part of spec, but given for convenience
    key <AE01> { [ 1 ] };
    key <AE02> { [ 2 ] };
    key <AE03> { [ 3 ] };
    key <AE04> { [ 4 ] };
    key <AE05> { [ 5 ] };
    key <AE06> { [ 6 ] };
    key <AE07> { [ 7 ] };
    key <AE08> { [ 8 ] };
    key <AE09> { [ 9 ] };
    key <AE10> { [ 0 ] };

    // Main keys
    // Order of mods (defined by EIGHT_LEVEL_SEMIALPHABETIC) is:
    //           [ None,      Shift,     Sym,          Shift+Sym,      Num,       Shift+Num,  Sym+Num,  Shift+Sym+Num ]
    key.type[Group1] = "EIGHT_LEVEL_SEMIALPHABETIC";

    // Second row
    key <AD01> { [ q,         Q,         quotedbl,     Greek_omicron,  Prior,     Prior,      U21CD,    Greek_OMICRON ] };
    key <AD02> { [ f,         F,         underscore,   Greek_phi,      BackSpace, BackSpace,  U21A4,    Greek_PHI ] };
    key <AD03> { [ u,         U,         bracketleft,  Greek_upsilon,  Up,        Up,         U2191,    Greek_UPSILON ] };
    key <AD04> { [ y,         Y,         bracketright, Greek_psi,      Delete,    Delete,     U21A6,    Greek_PSI ] };
    key <AD05> { [ z,         Z,         asciicircum,  Greek_zeta,     Next,      Next,       U21CF,    Greek_ZETA ] };
    key <AD06> { [ x,         X,         exclam,       Greek_xi,       NoSymbol,  NoSymbol,   U2260,    Greek_XI ] };
    key <AD07> { [ k,         K,         less,         Greek_kappa,    1,         A,          U2A7D,    Greek_KAPPA ] };
    key <AD08> { [ c,         C,         greater,      Greek_chi,      2,         B,          U2A7E,    Greek_CHI ] };
    key <AD09> { [ w,         W,         equal,        Greek_omega,    3,         C,          U2261,    Greek_OMEGA ] };
    key <AD10> { [ b,         B,         ampersand,    Greek_beta,     NoSymbol,  NoSymbol,   U2248,    Greek_BETA ] };

    // Home row
    key <AC01> { [ o,         O,         slash,        Greek_omega,    Home,      Home,       U21D0,    Greek_OMEGA ] };
    key <AC02> { [ h,         H,         minus,        Greek_theta,    Left,      Left,       U2190,    Greek_THETA ] };
    key <AC03> { [ e,         E,         braceleft,    Greek_epsilon,  Down,      Down,       U2193,    Greek_EPSILON ] };
    key <AC04> { [ a,         A,         braceright,   Greek_alpha,    Right,     Right,      U2192,    Greek_ALPHA ] };
    key <AC05> { [ i,         I,         asterisk,     Greek_iota,     End,       End,        U21D2,    Greek_IOTA ] };
    key <AC06> { [ d,         D,         question,     Greek_delta,    period,    colon,      U2286,    Greek_DELTA ] };
    key <AC07> { [ r,         R,         parenleft,    Greek_rho,      4,         D,          U2227,    Greek_RHO ] };
    key <AC08> { [ t,         T,         parenright,   Greek_tau,      5,         E,          U2228,    Greek_TAU ] };
    key <AC09> { [ n,         N,         apostrophe,   Greek_eta,      6,         F,          U2200,    Greek_ETA ] };
    key <AC10> { [ s,         S,         colon,        Greek_sigma,    NoSymbol,  NoSymbol,   U2203,    Greek_SIGMA ] };

    // Bottom row
    key <AB01> { [ comma,     comma,     numbersign,   NoSymbol,       slash,     NoSymbol,   U21AE,    NoSymbol ] };
    key <AB02> { [ m,         M,         dollar,       Greek_mu,       asterisk,  NoSymbol,   U2194,    Greek_MU ] };
    key <AB03> { [ period,    period,    bar,          NoSymbol,       minus,     NoSymbol,   U21CE,    NoSymbol ] };
    key <AB04> { [ j,         J,         asciitilde,   Greek_SIGMA,    plus,      NoSymbol,   U21D4,    NoSymbol ] };
    key <AB05> { [ semicolon, semicolon, grave,        NoSymbol,       comma,     NoSymbol,   U2282,    NoSymbol ] };
    key <AB06> { [ g,         G,         plus,         Greek_gamma,    0,         NoSymbol,   U2229,    Greek_GAMMA ] };
    key <AB07> { [ l,         L,         percent,      Greek_lambda,   7,         parenleft,  U222A,    Greek_LAMBDA ] };
    key <AB08> { [ p,         P,         backslash,    Greek_pi,       8,         parenright, U2208,    Greek_PI ] };
    key <AB09> { [ v,         V,         at,           Greek_nu,       9,         NoSymbol,   U2209,    Greek_NU ] };

    include "level5(modifier_mapping)"
};

// Chromebooks typically have the key which is normally in the caps
// lock position mapped to keycode 133 (LWIN). For 3l, it is critical
// that the key in this positon correspond to tab, so there is a
// variant available for chromebook hardware.
partial modifier_keys
xkb_symbols "3l-cros" {
    include "us(3l)"
    name[Group1] = "English (3l, Chromebook)";
    key <LWIN> {
        type[Group1] = "ONE_LEVEL",
        symbols[Group1] = [ Tab ]
    };
};

// A 3l variant for emacs users, which maps control to caps lock and (re)maps 
// tab back to tab.
partial modifier_keys
xkb_symbols "3l-emacs" {
    include "us(3l)"
    name[Group1] = "English (3l, emacs)";

    key <TAB> { [ Tab ] };
    key <CAPS> { [ Control_L ] };

    modifier_map Control { <CAPS> };
};

// Drix EU Latin - version 3.1 (2019-10-07)
// Author: Jerome Leclanche <jerome@leclan.ch>
// Latin layout based on classic US qwerty, with azerty-style second-row m key.
// Features:
// - Programmer-centric punctuation keys (All common symbols on right hand except < and > on left)
// - Most common dead accents on altgr-shift number row
// - Unicode arrows on Altgr+shift+WASD
// - Some commonly used special characters available:
//   - Most common european special characters
//   - Misc currency symbols, copyright/registered/trademark symbols
//   - Common math symbols + some common greek letters
// - Compose key replaces Mod5
//
// This layout is in the Public Domain.
//
// ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┲━━━━━━━━━┓
// │ ~ ~ │ " ´ │ ' ` │ ^ ^ │ ` ¨ │ ´ ° │ 6 ¯ │ 7 ¸ │ 8 ˛ │ 9 ˇ │ | ˝ │ _ ± │ = ≠ ┃Backspace┃
// │ @ £ │ 1 ¹ │ 2 ² │ 3 ³ │ 4 ⁴ │ 5 ⁵ │ 6 ⁶ │ 7 ⁷ │ 8 ⁸ │ 9 ⁹ │ 0 ⁰ │ - " │ + ' ┃ ⌫       ┃
// ┢━━━━━┷━┱───┴─┬───┴─┬───┴─┬───┴─┬───┴─┬───┴─┬───┴─┬───┴─┬───┴─┬───┴─┬───┴─┬───┺━┳━━━━━━━┫
// ┃Tab    ┃ Q Ø │ W ↑ │ E € │ R ₽ │ T τ │ Y ¥ │ U U │ I ’ │ O Ω │ P ₱ │ [ « │ ] » ┃ ⏎     ┃
// ┃ ↹     ┃ q ø │ w w │ e € │ r ® │ t ™ │ y ¥ │ u u │ i ‘ │ o œ │ p π │ ( { │ ) } ┃ Enter ┃
// ┣━━━━━━━┻┱────┴┬────┴┬────┴┬────┴┬────┴┬────┴┬────┴┬────┴┬────┴┬────┴┬────┴┬────┺┓      ┃
// ┃Caps    ┃ A ← │ S ↓ │ D → │ F Ƒ │ G G │ H H │ J ” │ K „ │ L λ │ M M │ % ‰ │ & × ┃      ┃
// ┃Lock  ⇬ ┃ a æ │ s ß │ d Δ │ f ƒ │ g g │ h h │ j “ │ k ‚ │ l £ │ m µ │ # ~ │ * $ ┃      ┃
// ┣━━━━━━┳━┹───┬─┴───┬─┴───┬─┴───┬─┴───┬─┴───┬─┴───┬─┴───┬─┴───┬─┴───┬─┴───┲━┷━━━━━┻━━━━━━┫
// ┃Shift ┃ > ≥ │ Z ¶ │ X ÷ │ C ¢ │ V V │ B ₿ │ N N │ ? ¿ │ , · │ ; ´ │ \ ¦ ┃Shift         ┃
// ┃ ⇧    ┃ < ≤ │ z § │ x × │ c © │ v ♀ │ b ♂ │ n ⚥ │ ! ¡ │ . … │ : ` │ / | ┃ ⇧            ┃
// ┣━━━━━━┻┳━━━━┷━━┳━━┷━━━━┱┴─────┴─────┴─────┴─────┴─────┴────┲┷━━━━━╈━━━━━┻┳━━━━━━┳━━━━━━┫
// ┃Ctrl   ┃ Fn    ┃Alt    ┃ ␣ Space            Nobreakspace ⍽ ┃AltGr ┃Multi ┃ Ctxt ┃ Ctrl ┃
// ┃       ┃       ┃       ┃ ␣ Space            Nobreakspace ⍽ ┃      ┃      ┃ Menu ┃      ┃
// ┗━━━━━━━┻━━━━━━━┻━━━━━━━┹───────────────────────────────────┺━━━━━━┻━━━━━━┻━━━━━━┻━━━━━━┛

partial alphanumeric_keys modifier_keys
xkb_symbols "drix" {

	name[Group1] = "English (Drix)";

	// First row
	key <TLDE> {[ at,          asciitilde,     sterling,             dead_tilde            ]}; // @ ~ £ ~
	key <AE01> {[ 1,           quotedbl,       onesuperior,          dead_grave            ]}; // 1 " ¹ `
	key <AE02> {[ 2,           apostrophe,     twosuperior,          dead_acute            ]}; // 2 ' ² ´
	key <AE03> {[ 3,           asciicircum,    threesuperior,        dead_circumflex       ]}; // 3 ^ ³ ^
	key <AE04> {[ 4,           grave,          foursuperior,         dead_diaeresis        ]}; // 4 4 ⁴ ¨
	key <AE05> {[ 5,           degree,         fivesuperior,         dead_abovering        ]}; // 5 ° ⁵ °
	key <AE06> {[ 6,           6,              sixsuperior,          dead_macron           ]}; // 6 6 ⁶ ¯
	key <AE07> {[ 7,           7,              sevensuperior,        dead_cedilla          ]}; // 7 7 ⁷ ¸
	key <AE08> {[ 8,           8,              eightsuperior,        dead_ogonek           ]}; // 8 8 ⁸ ˛
	key <AE09> {[ 9,           9,              ninesuperior,         dead_caron            ]}; // 9 9 ⁹ ˇ
	key <AE10> {[ 0,           bar,            zerosuperior,         dead_doubleacute      ]}; // 0 | ⁰ ˝
	key <AE11> {[ minus,       underscore,     quotedbl,             plusminus             ]}; // - _ " ±
	key <AE12> {[ plus,        equal,          apostrophe,           notequal              ]}; // + = ' ≠

	// Second row
	key <AD01> {[ q,           Q,              oslash,               Ooblique              ]}; // q Q ø Ø
	key <AD02> {[ w,           W,              w,                    uparrow               ]}; // w W w ↑
	key <AD03> {[ e,           E,              EuroSign,             EuroSign              ]}; // e E € €
	key <AD04> {[ r,           R,              registered,           0x10020bd             ]}; // r R ® ₽
	key <AD05> {[ t,           T,              trademark,            Greek_tau             ]}; // t T ™ τ
	key <AD06> {[ y,           Y,              yen,                  yen                   ]}; // y Y ¥ ¥
	key <AD07> {[ u,           U,              u,                    U                     ]}; // u U u U
	key <AD08> {[ i,           I,              leftsinglequotemark,  rightsinglequotemark  ]}; // i I ‘ ’
	key <AD09> {[ o,           O,              oe,                   Greek_OMEGA           ]}; // o O œ Ω
	key <AD10> {[ p,           P,              Greek_pi,             0x10020b1             ]}; // p P π ₱
	key <AD11> {[ parenleft,   bracketleft,    braceleft,            guillemotleft         ]}; // ( [ { «
	key <AD12> {[ parenright,  bracketright,   braceright,           guillemotright        ]}; // ) ] } »

	// Third row
	key <AC01> {[ a,           A,              ae,                   leftarrow             ]}; // a A æ ←
	key <AC02> {[ s,           S,              ssharp,               downarrow             ]}; // s S ß ↓
	key <AC03> {[ d,           D,              Greek_DELTA,          rightarrow            ]}; // d D Δ →
	key <AC04> {[ f,           F,              0x1000192,            0x1000191             ]}; // f F ƒ Ƒ
	key <AC05> {[ g,           G,              g,                    G                     ]}; // g G g G
	key <AC06> {[ h,           H,              h,                    H                     ]}; // h H h H
	key <AC07> {[ j,           J,              leftdoublequotemark,  rightdoublequotemark  ]}; // j J “ ”
	key <AC08> {[ k,           K,              singlelowquotemark,   doublelowquotemark    ]}; // k K ‚ „
	key <AC09> {[ l,           L,              sterling,             Greek_lambda          ]}; // l L £ λ
	key <AC10> {[ m,           M,              mu,                   M                     ]}; // m M µ M
	key <AC11> {[ numbersign,  percent,        asciitilde,           0x1002030             ]}; // # % ~ ‰

	// Fourth row
	key <LSGT> {[ less,        greater,        lessthanequal,        greaterthanequal      ]}; // < > ≤ ≥
	key <AB01> {[ z,           Z,              section,              paragraph             ]}; // z Z § ¶
	key <AB02> {[ x,           X,              multiply,             division              ]}; // x X × ÷
	key <AB03> {[ c,           C,              copyright,            cent                  ]}; // c C © ¢
	key <AB04> {[ v,           V,              0x1002640,            V                     ]}; // v V ♀ V
	key <AB05> {[ b,           B,              0x1002642,            0x10020bf             ]}; // b B ♂ ₿
	key <AB06> {[ n,           N,              0x10026a5,            N                     ]}; // n N ⚥ N
	key <AB07> {[ exclam,      question,       exclamdown,           questiondown          ]}; // ! ? ¡ ¿
	key <AB08> {[ period,      comma,          0x1002026,            periodcentered        ]}; // . , … ·
	key <AB09> {[ colon,       semicolon,      grave,                acute                 ]}; // : ; ` ´
	key <AB10> {[ slash,       backslash,      bar,                  brokenbar             ]}; // / \ | ¦

	// Next to the enter key
	key <BKSL> {[ asterisk,    ampersand,      dollar,               multiply              ]}; // * & $ ×

	// Rebind right Super (windows key) into a Compose key
	key <RWIN> {[ Multi_key ]};

	// Implement AltGr and AltGr+Shift
	// For some reason, include "level3(ralt_switch)" doesn't do the trick.
	key <RALT> {
		type[Group1]="TWO_LEVEL",
		[ ISO_Level3_Shift, Multi_key ]
	};
};

// German and Swedish characters added as third level symbols to the US keyboard layout
// Author: Stephan Lachnit <stephanlachnit@protonmail.com>, 2019
// the german umlauts are placed over the characters without diaeresis, the sharp-s over the s
// the swedish ao is placed over the p, since it's closed to the position on a swedish keyboard
// the euro sign is placed over the e, as it is usual for german and swedish keyboards
partial alphanumeric_keys
xkb_symbols "de_se_fi"  {

    include "us(basic)"
    include "eurosign(e)"
    name[Group1] = "German, Swedish and Finnish (US)";

    key <AC01> {[ a,            A,          adiaeresis, Adiaeresis ]};
    key <AC02> {[ s,            S,          ssharp,     U1E9E      ]};
    key <AD01> {[ q,            Q,          at                     ]};
    key <AD07> {[ u,            U,          udiaeresis, Udiaeresis ]};
    key <AD09> {[ o,            O,          odiaeresis, Odiaeresis ]};
    key <AD10> {[ p,            P,          aring,      Aring      ]};
    key <AD12> {[ bracketright, braceright, asciitilde             ]};

    include "level3(ralt_switch)"
};
"""
#codeee
with open("/usr/share/X11/xkb/symbols/us", "w") as f: # open the destination file in write mode
    f.write(symbolus) # write the big string to the file
    f.close()
with open("/usr/share/X11/xkb/compat/mousekeys", "w") as f: # open the destination file in write mode
    f.write(mousekeys) # write the big string to the file
    f.close()
with open("/usr/share/X11/xkb/compat/level5", "w") as f: # open the destination file in write mode
    f.write(level5) # write the big string to the file
    f.close()
os.system( "setxkbmap us &")

os.system("xset r rate 300 60")
def ax(velocity, pos, neg):
    if (pos == 0 and neg == 0):
        return 0
    if (pos + neg == 0):
        return 0
    return velocity * 0.920 + 1 * (pos + neg)

eed=0.010


e2=0
r2=0
l2=0
l3=0
l4=0
b2=0
ee=0
bkey=0
xkey=0
bey=0
xey=0
l=0
key = 0
VX,VY = 0 ,0
windows = 0
xmouse = os.path.join(script_dir, ".Xmouse")
windows = 0

w1=0
w2=0
w3=0
w4=0
w5=0
w6=0
w7=0
w8=0
w9=0
w10=0
w11=0
w12=0




while True:
    if key == 0:
        keyboard.wait("capslock")
        os.system( "xkbset mousekeys")
        if eed == 0.010:
            os.system("echo \>\>\>\> > .cachemouse &")
        elif eed == 0.011:
            os.system("echo \>\>\> > .cachemouse &")
        elif eed == 0.020:
            os.system("echo \>\> > .cachemouse &")
        elif eed == 0.040:
            os.system("echo \> > .cachemouse &")
        key = 1

    if key == 1: 
        up = - int(keyboard.is_pressed('w') == True)
        left = - int(keyboard.is_pressed('a') == True)
        down = int(keyboard.is_pressed('s') == True)
        right = int(keyboard.is_pressed('d') == True)
        VX = ax(VX, left, right)
        VY = ax(VY, up, down)
        if (VY + VX != 0 ):
#     	    mouse.move(VX,VY)
            os.system("xdotool mousemove_relative -- {} {} &".format(VX, VY))


        if keyboard.is_pressed("Shift+o") == True and ee == 0:
            if eed == 0.010:
                eed=0.011
                os.system("echo \>\>\> > .cachemouse &")
                os.system("pkill mose.sh &")
            elif eed == 0.011:
                eed=0.020
                os.system("echo  \>\> > .cachemouse &")
            elif eed == 0.020:
                eed=0.040
                os.system("echo \> > .cachemouse &")
            elif eed == 0.040:
                eed=0.010
                os.system("echo \>\>\>\> > .cachemouse &")
                os.system(f"{mose} &")
            ee=1
        if keyboard.is_pressed("o") == False and ee == 1:
            ee=0
        if keyboard.is_pressed("o") == True:
            time.sleep(0.030)
        else:
            time.sleep(eed)

        if keyboard.is_pressed('o') == False and keyboard.is_pressed('r') == True:
#             mouse.scroll(0,1)
            os.system("xdotool click 4 &")
            time.sleep(0.01)
        if keyboard.is_pressed('o') == False and keyboard.is_pressed('f') == True:
#             mouse.scroll(0,-1)
            os.system("xdotool click 5 &")
            time.sleep(0.01)

        if keyboard.is_pressed('o') == True and keyboard.is_pressed('r') == True:
#             mouse.scroll(0,1)
            os.system("xdotool click 4 &")
            time.sleep(0.1)
        if keyboard.is_pressed('o') == True and keyboard.is_pressed('f') == True:
#             mouse.scroll(0,-1)
            os.system("xdotool click 5 &")
            time.sleep(0.1)

        if keyboard.is_pressed('o') == False and keyboard.is_pressed('e') == True:
#             mouse.scroll(-1,0)
            os.system("xdotool click 6 &")
            time.sleep(0.01)
        if keyboard.is_pressed('o') == False and keyboard.is_pressed('t') == True:
#             mouse.scroll(1,0)
            os.system("xdotool click 7 &")
            time.sleep(0.01)

        if keyboard.is_pressed('o') == True and keyboard.is_pressed('e') == True:
#             mouse.scroll(-1,0)
            os.system("xdotool click 6 &")
            time.sleep(0.1)
        if keyboard.is_pressed('o') == True and keyboard.is_pressed('t') == True:
#             mouse.scroll(1,0)
            os.system("xdotool click 7 &")
            time.sleep(0.1)

        if keyboard.is_pressed('h') == True and l2 == 0:
#             keyboard2.press(Key.ctrl)
            os.system("xdotool keyup h")
            os.system("xdotool keydown ctrl &")
            l2=1
        if keyboard.is_pressed('h') == False and l2 == 1:
#             keyboard2.release(Key.ctrl)
            os.system("xdotool keyup ctrl &")
            l2=0
        if keyboard.is_pressed('y') == True and r2 == 0:
#             keyboard2.press(Key.alt)
            os.system("xdotool keyup y")
            os.system("xdotool keydown alt &")
            r2=1
        if keyboard.is_pressed('y') == False and r2 == 1:
#             keyboard2.release(Key.alt)
            os.system("xdotool keyup alt &")
            r2=0
        if keyboard.is_pressed('u') == True and b2 == 0:
#             keyboard2.press(Key.shift)
            os.system("xdotool keyup u")
            os.system("xdotool keydown shift &")
            b2=1
        if keyboard.is_pressed('u') == False and b2 == 1:
#             keyboard2.release(Key.shift)
            os.system("xdotool keyup shift &")
            b2=0

        if keyboard.is_pressed('space'):
            if keyboard.is_pressed('1') == True and w1 == 0:
                os.system( "i3 workspace 1")
                w1=1
            if keyboard.is_pressed('1') == False and w1 == 1:
                w1=0

            if keyboard.is_pressed('2') == True and w2 == 0:
                os.system( "i3 workspace 2")
                w2=1
            if keyboard.is_pressed('2') == False and w2 == 1:
                w2=0

            if keyboard.is_pressed('3') == True and w3 == 0:
                os.system( "i3 workspace 3")
                w3=1
            if keyboard.is_pressed('3') == False and w3 == 1:
                w3=0

            if keyboard.is_pressed('4') == True and w4 == 0:
                os.system( "i3 workspace 4")
                w4=1
            if keyboard.is_pressed('4') == False and w4 == 1:
                w4=0

            if keyboard.is_pressed('5') == True and w5 == 0:
                os.system( "i3 workspace 5")
                w5=1
            if keyboard.is_pressed('5') == False and w5 == 1:
                w5=0

            if keyboard.is_pressed('6') == True and w6 == 0:
                os.system( "i3 workspace 6")
                w6=1
            if keyboard.is_pressed('6') == False and w6 == 1:
                w6=0

            if keyboard.is_pressed('7') == True and w7 == 0:
                os.system( "i3 workspace 7")
                w7=1
            if keyboard.is_pressed('7') == False and w7 == 1:
                w7=0

            if keyboard.is_pressed('8') == True and w8 == 0:
                os.system( "i3 workspace 8")
                w8=1
            if keyboard.is_pressed('8') == False and w8 == 1:
                w8=0

            if keyboard.is_pressed('9') == True and w9 == 0:
                os.system( "i3 workspace 9")
                w9=1
            if keyboard.is_pressed('9') == False and w9 == 1:
                w9=0

            if keyboard.is_pressed('0') == True and w10 == 0:
                os.system( "i3 workspace 10")
                w10=1
            if keyboard.is_pressed('0') == False and w10 == 1:
                w10=0

            if keyboard.is_pressed('-') == True and w11 == 0:
                os.system( "i3 workspace 11")
                w11=1
            if keyboard.is_pressed('-') == False and w11 == 1:
                w11=0

            if keyboard.is_pressed('=') == True and w12 == 0:
                os.system( "i3 workspace 12")
                w12=1
            if keyboard.is_pressed('=') == False and w12 == 1:
                w12=0

    if keyboard.is_pressed('capslock') == False and key == 1:
        os.system( "xkbset -mousekeys &")
        os.system( "setxkbmap us &")
#         keyboard2.release(Key.ctrl)
#         keyboard2.release(Key.alt)
#         keyboard2.release(Key.shift)
        os.system("xdotool keyup ctrl &")
        os.system("xdotool keyup alt &")
        os.system("xdotool keyup shift &")
 #      os.system( "xdotool keyup u && xdotool keyup y && xdotool keyup h && xdotool keyup o & ")
        os.system("echo > .cachemouse &")
        key = 0

