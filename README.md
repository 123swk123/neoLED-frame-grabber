Addressable LED frame grabber and LED virtual display

# neoLED Frame Grabber

This Hardware is made using PIC12F18325 and uses CLC to reconstruct SPI CLK signal and CS signal from LED data signal there by creating SPI Mode 3 type signals which is then fed to internal SPI module. 
this way we compose LED data bits to single byte which is read on SPI interrupt and then pushed to PC(USB 2 UART) though **UART @ 2MHz** baud rate. At End Of Frame we push '0D 0A'.

### neoLED Grabber block diagram
![neoLED Grabber block diagram](analysis/neoLED_Grabber_HW.png)

[Schematic](schematic/neoLED2SPI.PDF)

Python + Qt QML based PC neoLED Viewer software, which reads the UART and renders them on the fly.
- Many types of LED support
- Any layout size and 4 types of LED layout arrangement
    - Snake Left 2 Right
    - Snake Top 2 Bottom
    - ZigZag Left 2 Right
    - ZigZag Top 2 Bottom
- New Layout shape can be easily added, currently supports Rectangle shape
- Records and Dumps data for offline play back (WIP)
- Refresh Rate monitoring

### Software Picture 32x32 Snake Layout Left 2 Right
![Software Picture 32x32 Snake Layout Left 2 Right](analysis/neoLED_Viewer_32x32_SnakeL2R.png)
