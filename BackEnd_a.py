import tkinter as tk, time
from tkinter import ttk

X,Y= 0,1

class Slider(tk.Scale):
    def __init__(self):
        pass

class Shape(tk.Canvas):
    def __init__(self, info, **kwargs):
        div, shape, psn, size, clr, purp, bg= info
        self.W, self.H= size        
        super().__init__(div, width=self.W, height=self.H, bg=bg, bd=0, **kwargs)
        self.place(relx= psn[X], rely= psn[Y])
        self.purp= purp; self.psn= psn; self.clr = clr
        self.shape= {'rect':self.rect}[shape]; self.shape()

    def rect(self):
        self.create_rectangle([0,0], [self.W,self.H], fill=self.clr, outline="", tags=self.purp)

    def show(self):
        self.place(relx= self.psn[X], rely=self.psn[Y])

class ProgBar(ttk.Progressbar):
    def __init__(self, info):
        div, size, psn, orntn, purp, style, lvl, clr, ver= info
        o, tl= 0, 1        
        self.purp = purp; self.ver= ver; self.psn= psn
        orntns = {'v':('Vertical',(0,1)), 'h':('Horizontal',(1,0))}
        self.orntn= orntns[orntn][o]
        self.W, self.H= size[orntns[orntn][tl][0]], size[orntns[orntn][tl][1]]        
        self.relx, self.rely= psn[X], psn[Y]                
        self.div= div
        self.style_name = f"{self.purp}.{self.orntn}.TProgressbar"
        self.style = ttk.Style(self.div)
        self.style.theme_use(style)# alt, clam        
        self.style.configure(self.style_name, thickness=size[0], troughcolor=clr, bordercolor='green', borderwidth=1)

        super().__init__(self.div, orient=orntn, length=size[1], style=self.style_name, mode='determinate')
        self['maximum'] = 100
        
        self.place(relx=self.relx, rely=self.rely, width=self.W, height=self.H)
        self.lvl= lvl
        self.update()

    def clrMap(self):
        if self.lvl<50:
            r, g, b= {'r':[0, 250-2*self.lvl, 250-5*self.lvl],'n':[250-5*self.lvl, 50+2*self.lvl, 0]}[self.ver]            
        else:
            r, g, b= {'n':[0, 50+2*self.lvl, (self.lvl-50)*5],'r':[(self.lvl-50)*5, 250-2*self.lvl, 0]}[self.ver]        
        return '#{0:02X}{1:02X}{2:02X}'.format(r, g, b)

    def update(self):
        self['value'] = self.lvl        
        self.clr = self.clrMap()        
        self.style.configure(self.style_name, background=self.clr)        

    def show(self):
        self.place(relx= self.psn[X], rely=self.psn[Y], width= self.W, height= self.H)

class Label(tk.Label):
    def __init__(self, info):
        div, txt, clr, psn, fontsize, purp= info
        self.txt= txt; self.purp= purp; self.psn= psn
        super().__init__(div, text=self.txt, fg=clr, bg=div.bg, font=('LCD', int(fontsize), 'bold')) #News Gothic MT
        self.place(relx=psn[X], rely=psn[Y])        

    def update(self):
        self.configure(text= self.txt)        

    def show(self):
        self.place(relx= self.psn[X], rely=self.psn[Y])

class Image(tk.Label):
    def __init__(self, info):
        div, path, psn, bg, purp= info
        self.purp= purp; self.psn= psn
        self.img = tk.PhotoImage(file=path)
        super().__init__(div, image=self.img, bg=bg)
        self.place(relx=psn[X], rely=psn[Y])

    def show(self):
        self.place(relx= self.psn[X], rely=self.psn[Y])
        
class Div(tk.Canvas):
    def __init__(self, dash, ind, width, height, bg, border_color, sw, **kwargs):
        self.H, self.W= width, height
        self.bg= bg
        super().__init__(dash, width=width, height=height, bg=bg, highlightbackground=border_color, highlightthickness=1, **kwargs)
        if {'x':False, 'v':True}[sw]:
            self.sw= tk.Button(self, text='SW', command= self.switch)
            self.sw.place(relx= 0, rely= 0)
        self.cur= 0

    def switch(self):
        for s in range(len(self.wdts)):
            for wdt in self.wdts[s]:
                wdt.place_forget()
            if s==self.cur:
                for wdt in self.wdts[s]:
                    wdt.show()
        self.cur+=1
        if self.cur== self.mds:
            self.cur=0

    def create(self, wdts_data):
        self.wdts= [[] for i in range(len(wdts_data))]        
        i= 0
        for switch in wdts_data:            
            for wdt_data in switch:                
                new_wdt= wdt_data['wdt'](wdt_data['info'])
                self.wdts[i].append(new_wdt) 
            i+=1 
        self.mds= len(self.wdts)   
        self.switch()    

class Main(tk.Tk):
    def __init__(self, color, size, title, **kwargs):
        super().__init__(**kwargs)
        self.configure(bg=color)
        self.divs= []; self.ind=0
        self.geometry(size)
        self.title(title)                

    def create(self, divs_data):
        clr, w, h, psn, bg, sw= 0, 1, 2, 3, 4, 5
        for div_data in divs_data:
            div = Div(self, self.ind, div_data[w], div_data[h], div_data[clr], div_data[bg], div_data[sw])
            div.place(relx=div_data[psn][X], rely=div_data[psn][Y])    
            self.divs.append(div); self.ind+=1            
