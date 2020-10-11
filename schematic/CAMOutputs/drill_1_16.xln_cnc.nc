(G-CODE GENERATED BY FLATCAM v8.993 - www.flatcam.org - Version Date: 2020/06/05)

(Name: drill_1_16.xln_cnc)
(Type: G-code from Excellon)
(Units: MM)

(Created on Saturday, 10 October 2020 at 19:59)

(This preprocessor is used with a motion controller loaded with GRBL firmware.)
(It is configured to be compatible with almost any version of GRBL firmware.)


(TOOLS DIAMETER: )
(Tool: 2 -> Dia: 0.813)
(Tool: 1 -> Dia: 1.016)

(FEEDRATE Z: )
(Tool: 2 -> Feedrate: 50.0)
(Tool: 1 -> Feedrate: 50.0)

(FEEDRATE RAPIDS: )
(Tool: 2 -> Feedrate Rapids: 1500)
(Tool: 1 -> Feedrate Rapids: 1500)

(Z_CUT: )
(Tool: 2 -> Z_Cut: -1.8)
(Tool: 1 -> Z_Cut: -1.8)

(Tools Offset: )
(Tool: 2 -> Offset Z: -0.0)
(Tool: 1 -> Offset Z: -0.0)

(Z_MOVE: )
(Tool: 2 -> Z_Move: 1.0)
(Tool: 1 -> Z_Move: 1.0)

(Z Start: None mm)
(Z End: 2.0 mm)
(Steps per circle: 64)
(Preprocessor Excellon: grbl_11)

(X range:  -29.7180 ...   -5.9435  mm)
(Y range:    3.4035 ...   23.2665  mm)

(Spindle Speed: 1000.0 RPM)
G21
G90
G17
G94




G00 Z1.0000

G01 F50.00
M03 S1000
G4 P1.5
G00 X-8.8900 Y17.7800
G01 Z-1.8000
G00 Z1.0000
G00 X-6.3500 Y17.7800
G01 Z-1.8000
G00 Z1.0000
G00 X-15.2400 Y17.7800
G01 Z-1.8000
G00 Z1.0000
G00 X-15.2400 Y15.2400
G01 Z-1.8000
G00 Z1.0000
G00 X-15.2400 Y12.7000
G01 Z-1.8000
G00 Z1.0000
G00 X-15.2400 Y10.1600
G01 Z-1.8000
G00 Z1.0000
G00 X-15.2400 Y7.6200
G01 Z-1.8000
G00 Z1.0000
G00 X-16.5100 Y3.8100
G01 Z-1.8000
G00 Z1.0000
G00 X-19.0500 Y3.8100
G01 Z-1.8000
G00 Z1.0000
G00 X-21.5900 Y3.8100
G01 Z-1.8000
G00 Z1.0000
G00 X-22.8600 Y7.6200
G01 Z-1.8000
G00 Z1.0000
G00 X-22.8600 Y10.1600
G01 Z-1.8000
G00 Z1.0000
G00 X-22.8600 Y12.7000
G01 Z-1.8000
G00 Z1.0000
G00 X-22.8600 Y15.2400
G01 Z-1.8000
G00 Z1.0000
G00 X-22.8600 Y17.7800
G01 Z-1.8000
G00 Z1.0000
G00 X-22.8600 Y20.3200
G01 Z-1.8000
G00 Z1.0000
G00 X-22.8600 Y22.8600
G01 Z-1.8000
G00 Z1.0000
G00 X-15.2400 Y22.8600
G01 Z-1.8000
G00 Z1.0000
G00 X-15.2400 Y20.3200
G01 Z-1.8000
G00 Z1.0000
G01 F50.00
M03 S1000
G4 P1.5
G00 X-29.2100 Y12.7000
G01 Z-1.8000
G00 Z1.0000
G00 X-29.2100 Y15.2400
G01 Z-1.8000
G00 Z1.0000
M05
G00 Z2.00

