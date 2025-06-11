from BackEnd_a import Main, Image, Label, ProgBar, Shape

W, H = 160, 128
bg_clr= ['#101010','#e0e0e0'][0]

Dash= Main('grey', '480x320', 'Dashboard')
divs_swtch= [(bg_clr,W,H/4,[0, 0],'grey'),(bg_clr,W,H,[0, 0.1],'grey'),(bg_clr,W,H/4,[0, 0.5],'grey'),(bg_clr,W,H,[0, 0.6],'grey'),
            (bg_clr,W,H,[2/3, 0],'grey'),(bg_clr,W,H/4,[2/3, 0.4],'grey'),(bg_clr,W,H/4,[2/3, 0.5],'grey'),(bg_clr,W,H,[2/3, 0.6],'grey'),
            (bg_clr,W,H*0.3125,[1/3, 0],'grey'),(bg_clr,W,H*1.5625,[1/3, 0.125],'grey'),(bg_clr,W,H*0.625,[1/3, 0.75],'grey')]
Dash.create(divs_swtch)
divs= Dash.divs

#Left Top~ ind 0
Btt_Lbl= {'wdt':Label, 'info':(divs[0], 'BATTERY', '#00aeb4', (0.15,0.05), 20, 'Btt_Lbl')}

#Left 2nd~ ind 1
LV_Prg= {'wdt':ProgBar, 'info':(divs[1], (50,90), (0.1,0.25), 'v', 'LV_Prg', 'clam', 35, bg_clr, 'n')}
HV_Prg= {'wdt':ProgBar, 'info':(divs[1], (50,90), (0.6,0.25), 'v', 'HV_Prg', 'clam', 70, bg_clr, 'n')}
LV_Lbl= {'wdt':Label, 'info':(divs[1], 'LV', '#d49e2a', (0.15,0.02), 16, 'LV_Lbl')}
HV_Lbl= {'wdt':Label, 'info':(divs[1], 'HV', '#d49e2a', (0.65,0.02), 16, 'HV_Lbl')}
Splt_lvhv= {'wdt':Shape, 'info':(divs[1], 'rect', (0.49,0.1), (0,106), 'grey', 'splt_lvhv', bg_clr)}

#Left 3rd~ ind 2
Bspd= {'wdt':Label, 'info':(divs[2], 'BSPD', '#1ab876', (0.25,0.05), 18, 'Bspd')}

#Center Top~ ind 8
Time= {'wdt':Label, 'info':(divs[8], 'Time: 00:00', 'grey', (0.08,0.08), 20, 'Time')}

#Center Middle~ ind 9
Spd= {'wdt':Label, 'info':(divs[9], '81.4', '#d49e2a', (0.12,0.02), 60, 'Spd')}
Spd_Lbl= {'wdt':Label, 'info':(divs[9], 'km/h', '#00aeb4', (0.3,0.4), 20, 'Spd_Lbl')}
Rpm= {'wdt':Label, 'info':(divs[9], '2056', '#d49e2a', (0.16,0.55), 40, 'Rpm')}
Rpm_Lbl= {'wdt':Label, 'info':(divs[9], 'RPM', '#00aeb4', (0.35,0.8), 20, 'Rpm_Lbl')}

#Center Bottom~ ind 10
Gear= {'wdt':Label, 'info':(divs[10], 'N', '#00aeb4', (0.08,0.02), 55, 'Gear')}
SRT= {'wdt':Image, 'info':(divs[10], r"C:\Users\titus\Downloads\SRT.png", (0.45, 0.02), bg_clr, 'SRT')}

#Right Top~ ind 4
Dist_Lbl= {'wdt':Label, 'info':(divs[4], 'Distance', '#00aeb4', (0.08,0.02), 27, 'Dist_Lbl')}
Dist= {'wdt':Label, 'info':(divs[4], '0.34', '#d49e2a', (0.23,0.33), 32, 'Dist')}
Dist_Unt= {'wdt':Label, 'info':(divs[4], 'km', '#00aeb4', (0.35,0.67), 23, 'Dist_Unt')}

#Right 2nd~ ind 5
Mode= {'wdt':Label, 'info':(divs[5], 'Lenana', '#00aeb4', (0.1,0.05), 18, 'Mode')}

#______________BOTTOM_RIGHT_____________________________________________________________________________________________________________________

#Right 3rd A~ ind 6
TPS= {'wdt':Label, 'info':(divs[6], 'TPS', '#00aeb4', (0.35,0.05), 18, 'TPS')}

#Right 3rd B~ ind 6
Btt_Tmp_Ttl= {'wdt':Label, 'info':(divs[6], 'Battery Temp', '#00aeb4', (0.05,0.05), 18, 'Btt_Temp')}

#Right 3rd C~ ind 6
TPM= {'wdt':Label, 'info':(divs[6], 'Tire Pressures', '#00aeb4', (0.05,0.05), 16, 'TPM')}

#Right 3rd D~ ind 6
BrTM= {'wdt':Label, 'info':(divs[6], 'Brake Temps', '#00aeb4', (0.08,0.05), 18, 'BTM')}

#Right Bottom A~ ind 7
Thrt= {'wdt':ProgBar, 'info':(divs[7], (35,85), (0.25,0.25), 'v', 'Thrt', 'clam', 80, bg_clr, 'n')}
Brk= {'wdt':ProgBar, 'info':(divs[7], (35,85), (0.55,0.25), 'v', 'Brk', 'clam', 20, bg_clr, 'n')}
Thrt_Lbl= {'wdt':Label, 'info':(divs[7], 'TH', '#d49e2a', (0.25,0.02), 16, 'Thrt_Lbl')}
Brk_Lbl= {'wdt':Label, 'info':(divs[7], 'BR', '#d49e2a', (0.55,0.02), 16, 'Brk_Lbl')}

#Right Bottom B~ ind 7
Btt_Tmp= {'wdt':ProgBar, 'info':(divs[7], (50,130), (0.1,0.5), 'h', 'Btt_Tmp', 'clam', 95, bg_clr, 'r')}
Btt_Tmp_Val= {'wdt':Label, 'info':(divs[7], '65.10', '#d49e2a', (0.12,0.02), 20, 'Btt_Tmp_Val')}
Btt_Tmp_Lbl= {'wdt':Label, 'info':(divs[7], '°C', '#00aeb4', (0.2,0.22), 20, 'Btt_Tmp_Lbl')}
Btt_Tmp_Wrng= {'wdt':Image, 'info':(divs[7], r"C:\Users\titus\Downloads\WarningTriangle.png", (0.6, 0.1), bg_clr, 'Btt_Tmp_Wrng')}

#Right Bottom C~ ind 7
FL= {'wdt':ProgBar, 'info':(divs[7], (15,50), (0.3,0.05), 'v', 'FL', 'clam', 90, bg_clr, 'r')}
FR= {'wdt':ProgBar, 'info':(divs[7], (15,50), (0.55,0.05), 'v', 'FR', 'clam', 35, bg_clr, 'r')}
RL= {'wdt':ProgBar, 'info':(divs[7], (15,50), (0.3,0.55), 'v', 'RL', 'clam', 70, bg_clr, 'r')}
RR= {'wdt':ProgBar, 'info':(divs[7], (15,50), (0.55,0.55), 'v', 'RR', 'clam', 20, bg_clr, 'r')}
FL_Lbl= {'wdt':Label, 'info':(divs[7], '25\nPsi', '#d49e2a', (0.07,0.02), 16, 'FL_Lbl')}
FR_Lbl= {'wdt':Label, 'info':(divs[7], '31\nPsi', '#d49e2a', (0.67,0.02), 16, 'FR_Lbl')}
RL_Lbl= {'wdt':Label, 'info':(divs[7], '30\nPsi', '#d49e2a', (0.07,0.55), 16, 'RL_Lbl')}
RR_Lbl= {'wdt':Label, 'info':(divs[7], '27\nPsi', '#d49e2a', (0.67,0.55), 16, 'RR_Lbl')}

#Right Bottom D~ ind 7
FL_Br= {'wdt':ProgBar, 'info':(divs[7], (15,50), (0.3,0.05), 'v', 'FL_Br', 'clam', 70, bg_clr, 'r')}
FR_Br= {'wdt':ProgBar, 'info':(divs[7], (15,50), (0.55,0.05), 'v', 'FR_Br', 'clam', 25, bg_clr, 'r')}
RL_Br= {'wdt':ProgBar, 'info':(divs[7], (15,50), (0.3,0.55), 'v', 'RL_Br', 'clam', 90, bg_clr, 'r')}
RR_Br= {'wdt':ProgBar, 'info':(divs[7], (15,50), (0.55,0.55), 'v', 'RR_Br', 'clam', 40, bg_clr, 'r')}
FL_Br_Lbl= {'wdt':Label, 'info':(divs[7], '55\n°C', '#d49e2a', (0.07,0.02), 16, 'FL_Br_Lbl')}
FR_Br_Lbl= {'wdt':Label, 'info':(divs[7], '61\n°C', '#d49e2a', (0.67,0.02), 16, 'FR_Br_Lbl')}
RL_Br_Lbl= {'wdt':Label, 'info':(divs[7], '60\n°C', '#d49e2a', (0.07,0.55), 16, 'RL_Br_Lbl')}
RR_Br_Lbl= {'wdt':Label, 'info':(divs[7], '57\n°C', '#d49e2a', (0.67,0.55), 16, 'RR_Br_Lbl')}

#____________________________________________________________________________________________________________________________________

wdts_swtch0= [[Btt_Lbl]] #Left Top~ ind 0
wdts_swtch1= [[LV_Prg, HV_Prg, LV_Lbl, HV_Lbl, Splt_lvhv]] #Left 2nd~ ind 1
wdts_swtch2= [[]] #Left 3rd~ ind 2
wdts_swtch3= [[]] #Left Bottom~ ind 3
wdts_swtch4= [[Dist_Lbl, Dist, Dist_Unt]] #Right Top~ ind 4
wdts_swtch5= [[Mode]] #Right 2nd~ ind 5
wdts_swtch6= [[TPS],[Btt_Tmp_Ttl],[TPM],[BrTM]] #Right 3rd~ ind 6
wdts_swtch7= [[Thrt, Brk, Thrt_Lbl, Brk_Lbl],[Btt_Tmp, Btt_Tmp_Val, Btt_Tmp_Lbl, Btt_Tmp_Wrng],
              [FL, FR, RL, RR, FL_Lbl, FR_Lbl, RL_Lbl, RR_Lbl],[FL_Br, FR_Br, RL_Br, RR_Br, FL_Br_Lbl, FR_Br_Lbl, RL_Br_Lbl, RR_Br_Lbl]] #Right Bottom~ ind 7
wdts_swtch8= [[Time]] #Center Top~ ind 8
wdts_swtch9= [[Spd, Spd_Lbl, Rpm, Rpm_Lbl]] #Center Middle~ ind 9
wdts_swtch10= [[Gear, SRT]] #Center Bottom~ ind 10

divs_crt= [(divs[0],wdts_swtch0),(divs[1],wdts_swtch1),(divs[2],wdts_swtch2),(divs[3],wdts_swtch3),(divs[4],wdts_swtch4),(divs[5],wdts_swtch5),
           (divs[6],wdts_swtch6),(divs[7],wdts_swtch7),(divs[8],wdts_swtch8),(divs[9],wdts_swtch9),(divs[10],wdts_swtch10)]

widgets= {}
for div, wdts in divs_crt:
    div.create(wdts)
    for switch in div.wdts:
        for wdt in switch:
            widgets[wdt.purp]= wdt

test_switch, test_value= [6,7], 0
for div in test_switch:
    divs[div].sw= test_value

Dash.mainloop()
















