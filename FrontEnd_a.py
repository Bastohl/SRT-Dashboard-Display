from BackEnd_a import Main,Image,Label,ProgBar,Shape

W,H = 160,128
bg_clr= ['#101010',"#d9d9d9"][0]

Dash= Main('grey','480x320','Dashboard')
divs_swtch= [(bg_clr,W,H/4,[0,0],'grey','x'),(bg_clr,W,H,[0,0.1],'grey','x'),(bg_clr,W,H/4,[0,0.5],'grey','v'),(bg_clr,W,H,[0,0.6],'grey','v'),
            (bg_clr,W,H,[2/3,0],'grey','x'),(bg_clr,W,H/4,[2/3,0.4],'grey','x'),(bg_clr,W,H/4,[2/3,0.5],'grey','v'),(bg_clr,W,H,[2/3,0.6],'grey','v'),
            (bg_clr,W,H*0.3125,[1/3,0],'grey','x'),(bg_clr,W,H*1.5625,[1/3,0.125],'grey','x'),(bg_clr,W,H*0.625,[1/3,0.75],'grey','x')]
Dash.create(divs_swtch)
divs= Dash.divs

#Left Top~ ind 0
Btt_Lbl= {'wdt':Label,'info':(divs[0],'BATTERY','#00aeb4',(0.15,0.05),20,'Btt_Lbl','f')}

#Left 2nd~ ind 1
LV_Prg= {'wdt':ProgBar,'info':(divs[1],(50,90),(0.1,0.25),'v','LV_Prg','clam',35,bg_clr,'n',(0,100))}
HV_Prg= {'wdt':ProgBar,'info':(divs[1],(50,90),(0.6,0.25),'v','HV_Prg','clam',70,bg_clr,'n',(0,100))}
LV_Lbl= {'wdt':Label,'info':(divs[1],'LV',"#d1733c",(0.15,0.02),16,'LV_Lbl','f')}
HV_Lbl= {'wdt':Label,'info':(divs[1],'HV','#d1733c',(0.65,0.02),16,'HV_Lbl','f')}
Splt_lvhv= {'wdt':Shape,'info':(divs[1],'rect',(0.49,0.1),(0,106),'grey','splt_lvhv',bg_clr)}

#Left 3rd~ ind 2
Bspd= {'wdt':Label,'info':(divs[2],'BSPD','#1ab876',(0.25,0.05),18,'Bspd','f')}

#Center Top~ ind 8
Time_Lbl= {'wdt':Label,'info':(divs[8],'Time: ','grey',(0.03,0.08),20,'Time_Lbl','f')}
Time= {'wdt':Label,'info':(divs[8],'00:00','grey',(0.43,0.08),20,'Time','u')}

#Center Middle~ ind 9
Spd= {'wdt':Label,'info':(divs[9],'81.4','#d1733c',(0.08,0.02),60,'Spd','u')}
Spd_Lbl= {'wdt':Label,'info':(divs[9],'km/h','#00aeb4',(0.3,0.4),20,'Spd_Lbl','f')}
Rpm= {'wdt':Label,'info':(divs[9],'2056','#d1733c',(0.16,0.55),40,'Rpm','u')}
Rpm_Lbl= {'wdt':Label,'info':(divs[9],'RPM','#00aeb4',(0.35,0.8),20,'Rpm_Lbl','f')}

#Center Bottom~ ind 10
Gear= {'wdt':Label,'info':(divs[10],'N','#00aeb4',(0.08,0.02),55,'Gear','u')}
SRT= {'wdt':Image,'info':(divs[10],r"C:\Users\titus\Downloads\SRT.png",(0.45,0.02),bg_clr,'SRT')}

#Right Top~ ind 4
Dist_Lbl= {'wdt':Label,'info':(divs[4],'Distance','#00aeb4',(0.08,0.02),27,'Dist_Lbl','f')}
Dist= {'wdt':Label,'info':(divs[4],'0.34','#d1733c',(0.23,0.33),32,'Dist','u')}
Dist_Unt= {'wdt':Label,'info':(divs[4],'km','#00aeb4',(0.35,0.67),23,'Dist_Unt','f')}

#Right 2nd~ ind 5
Mode= {'wdt':Label,'info':(divs[5],'Lenana','#00aeb4',(0.1,0.05),18,'Mode','f')}

#______________BOTTOM_RIGHT_____________________________________________________________________________________________________________________

#Right 3rd A~ ind 6
TPS= {'wdt':Label,'info':(divs[6],'TPS','#00aeb4',(0.35,0.05),18,'TPS','f')}

#Right 3rd B~ ind 6
Btt_Tmp_Ttl= {'wdt':Label,'info':(divs[6],'Battery Temp','#00aeb4',(0.05,0.05),18,'Btt_Temp','f')}

#Right 3rd C~ ind 6
TPM= {'wdt':Label,'info':(divs[6],'Tire Pressures','#00aeb4',(0.05,0.05),16,'TPM','f')}

#Right 3rd D~ ind 6
BrTM= {'wdt':Label,'info':(divs[6],'Brake Temps','#00aeb4',(0.08,0.05),18,'BTM','f')}

#Right Bottom A~ ind 7
Thrt= {'wdt':ProgBar,'info':(divs[7],(35,85),(0.25,0.25),'v','Thrt','clam',80,bg_clr,'n',(0,100))}
Brk= {'wdt':ProgBar,'info':(divs[7],(35,85),(0.55,0.25),'v','Brk','clam',20,bg_clr,'n',(0,100))}
Thrt_Lbl= {'wdt':Label,'info':(divs[7],'TH','#d1733c',(0.25,0.02),16,'Thrt_Lbl','f')}
Brk_Lbl= {'wdt':Label,'info':(divs[7],'BR','#d1733c',(0.55,0.02),16,'Brk_Lbl','f')}

#Right Bottom B~ ind 7
Btt_Tmp= {'wdt':ProgBar,'info':(divs[7],(50,130),(0.1,0.5),'h','Btt_Tmp','clam',95,bg_clr,'r',(15,40))}
Btt_Tmp_Val= {'wdt':Label,'info':(divs[7],'65.10','#d1733c',(0.12,0.02),20,'Btt_Tmp_Val','u')}
Btt_Tmp_Lbl= {'wdt':Label,'info':(divs[7],'°C','#00aeb4',(0.2,0.22),20,'Btt_Tmp_Lbl','f')}
Btt_Tmp_Wrng= {'wdt':Image,'info':(divs[7],r"C:\Users\titus\Downloads\WarningTriangle.png",(0.6,0.1),bg_clr,'Btt_Tmp_Wrng')}

#Right Bottom C~ ind 7
FL= {'wdt':ProgBar,'info':(divs[7],(15,50),(0.3,0.05),'v','FL','clam',90,bg_clr,'r',(15,25))}
FR= {'wdt':ProgBar,'info':(divs[7],(15,50),(0.55,0.05),'v','FR','clam',35,bg_clr,'r',(15,25))}
RL= {'wdt':ProgBar,'info':(divs[7],(15,50),(0.3,0.55),'v','RL','clam',70,bg_clr,'r',(15,25))}
RR= {'wdt':ProgBar,'info':(divs[7],(15,50),(0.55,0.55),'v','RR','clam',20,bg_clr,'r',(15,25))}
FL_Lbl= {'wdt':Label,'info':(divs[7],'25','#d1733c',(0.07,0.02),16,'FL_Lbl','u')}
FL_Lbl_Unt= {'wdt':Label,'info':(divs[7],'Psi','#00aeb4',(0.07,0.22),16,'FL_Lbl_Unt','f')}
FR_Lbl= {'wdt':Label,'info':(divs[7],'31','#d1733c',(0.67,0.02),16,'FR_Lbl','u')}
FR_Lbl_Unt= {'wdt':Label,'info':(divs[7],'Psi','#00aeb4',(0.67,0.22),16,'FR_Lbl_Unt','f')}
RL_Lbl= {'wdt':Label,'info':(divs[7],'30','#d1733c',(0.07,0.55),16,'RL_Lbl','u')}
RL_Lbl_Unt= {'wdt':Label,'info':(divs[7],'Psi','#00aeb4',(0.07,0.75),16,'RL_Lbl_Unt','f')}
RR_Lbl= {'wdt':Label,'info':(divs[7],'27','#d1733c',(0.67,0.55),16,'RR_Lbl','u')}
RR_Lbl_Unt= {'wdt':Label,'info':(divs[7],'Psi','#00aeb4',(0.67,0.75),16,'RR_Lbl_Unt','f')}

#Right Bottom D~ ind 7
FL_Br= {'wdt':ProgBar,'info':(divs[7],(15,50),(0.32,0.05),'v','FL_Br','clam',70,bg_clr,'r',(65,270))}
FR_Br= {'wdt':ProgBar,'info':(divs[7],(15,50),(0.55,0.05),'v','FR_Br','clam',25,bg_clr,'r',(65,270))}
RL_Br= {'wdt':ProgBar,'info':(divs[7],(15,50),(0.32,0.55),'v','RL_Br','clam',90,bg_clr,'r',(65,270))}
RR_Br= {'wdt':ProgBar,'info':(divs[7],(15,50),(0.55,0.55),'v','RR_Br','clam',40,bg_clr,'r',(65,270))}
FL_Br_Lbl= {'wdt':Label,'info':(divs[7],'55','#d1733c',(0.07,0.02),16,'FL_Br_Lbl','u')}
FR_Br_Lbl= {'wdt':Label,'info':(divs[7],'61','#d1733c',(0.67,0.02),16,'FR_Br_Lbl','u')}
RL_Br_Lbl= {'wdt':Label,'info':(divs[7],'60','#d1733c',(0.07,0.55),16,'RL_Br_Lbl','u')}
RR_Br_Lbl= {'wdt':Label,'info':(divs[7],'57',"#d1733c",(0.67,0.55),16,'RR_Br_Lbl','u')}
FL_Br_Lbl_Unt= {'wdt':Label,'info':(divs[7],'°C','#00aeb4',(0.07,0.22),16,'FL_Br_Lbl_Unt','f')}
FR_Br_Lbl_Unt= {'wdt':Label,'info':(divs[7],'°C','#00aeb4',(0.67,0.22),16,'FR_Br_Lbl_Unt','f')}
RL_Br_Lbl_Unt= {'wdt':Label,'info':(divs[7],'°C','#00aeb4',(0.07,0.75),16,'RL_Br_Lbl_Unt','f')}
RR_Br_Lbl_Unt= {'wdt':Label,'info':(divs[7],'°C','#00aeb4',(0.67,0.75),16,'RR_Br_Lbl_Unt','f')}

#____________________________________________________________________________________________________________________________________

wdts_swtch0= [[Btt_Lbl]] #Left Top~ ind 0
wdts_swtch1= [[LV_Prg,HV_Prg,LV_Lbl,HV_Lbl,Splt_lvhv]] #Left 2nd~ ind 1
wdts_swtch2= [[]] #Left 3rd~ ind 2
wdts_swtch3= [[]] #Left Bottom~ ind 3
wdts_swtch4= [[Dist_Lbl,Dist,Dist_Unt]] #Right Top~ ind 4
wdts_swtch5= [[Mode]] #Right 2nd~ ind 5
wdts_swtch6= [[TPS],[Btt_Tmp_Ttl],[TPM],[BrTM]] #Right 3rd~ ind 6
wdts_swtch7= [[Thrt,Brk,Thrt_Lbl,Brk_Lbl],[Btt_Tmp,Btt_Tmp_Val,Btt_Tmp_Lbl,Btt_Tmp_Wrng],
              [FL,FR,RL,RR,FL_Lbl,FR_Lbl,RL_Lbl,RR_Lbl,FL_Lbl_Unt,FR_Lbl_Unt,RL_Lbl_Unt,RR_Lbl_Unt],[FL_Br,FR_Br,RL_Br,RR_Br,FL_Br_Lbl,FR_Br_Lbl,RL_Br_Lbl,RR_Br_Lbl,FL_Br_Lbl_Unt,FR_Br_Lbl_Unt,RL_Br_Lbl_Unt,RR_Br_Lbl_Unt]] #Right Bottom~ ind 7
wdts_swtch8= [[Time,Time_Lbl]] #Center Top~ ind 8
wdts_swtch9= [[Spd,Spd_Lbl,Rpm,Rpm_Lbl]] #Center Middle~ ind 9
wdts_swtch10= [[Gear,SRT]] #Center Bottom~ ind 10

divs_crt= [(divs[0],wdts_swtch0),(divs[1],wdts_swtch1),(divs[2],wdts_swtch2),(divs[3],wdts_swtch3),(divs[4],wdts_swtch4),(divs[5],wdts_swtch5),
           (divs[6],wdts_swtch6),(divs[7],wdts_swtch7),(divs[8],wdts_swtch8),(divs[9],wdts_swtch9),(divs[10],wdts_swtch10)]

def collect_data():
    sample_data= {'LV_Prg': 60,'HV_Prg': 20,'Dist': 17.51,'Thrt': 15,'Brk': 90,'Btt_Tmp': 30,
                  'FL': 18,'FR': 17,'RL': 21,'RR': 22,
                  'FL_Br': 228,'FR_Br': 217,'RL_Br': 198,'RR_Br': 205,                  
                  'Time': '1:07:45','Spd': 57.80,'Rpm': 1964,'Gear': 'D'}
    
    progbars= ['FL','FR','RL','RR','FL_Br','FR_Br','RL_Br','RR_Br','Btt_Tmp']
    labels= ['FL_Lbl','FR_Lbl','RL_Lbl','RR_Lbl','FL_Br_Lbl','FR_Br_Lbl','RL_Br_Lbl','RR_Br_Lbl','Btt_Tmp_Val']
    prg_n_lbl= dict(zip(progbars,labels))
    for prg in prg_n_lbl:
        sample_data[prg_n_lbl[prg]]= sample_data[prg]
    data= sample_data
    return data

widgets= {}
for div,wdts in divs_crt:
    div.create(wdts)
    for switch in div.wdts:
        for wdt in switch:
            if wdt.updble:
                widgets[wdt.purp]= wdt

def update():
    data= collect_data()
    for wdt in widgets:
        widgets[wdt].txt= data[wdt]
        widgets[wdt].update()
    Dash.after(500,update)

update()
Dash.mainloop()
















