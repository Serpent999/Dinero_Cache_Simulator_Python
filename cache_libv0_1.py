"""
Project : Dinero Based Cache Simulator
Engineer : Nikhil.P.Lokhande
email: nikhil.l.1@aol.com

"""

class Cache_Block:

    def __init__(self,Flag=0,Tag=0):
        self._V_Flag =Flag
        self._T_Value=Tag
        self._BUi= 0


    def get_Vflag(self):
        return(self._V_Flag)

    def get_Tval(self):
        return(self._T_Value)
    
    def set_Vflag(self,val):
        self._V_Flag=val

    def set_Tval(self,val):
        self._T_Value=val

    def get_BUi(self):
        return self._BUi

    def set_BUi(self,val):
        self._BUi = val
        

        



class Cache_Line:

    def __init__(self,Csize=1,Bsize=1,A=0):
        if( (A)<=0 ):       #A =0 => 1 CL, 0 BL, A=1 => CL>1 && BL =1
            self._NumCB=0
        else:
            self._NumCB = A  
            
        self._Array =[]
        
    
        for i in range(self._NumCB):
            temp = Cache_Block()
            self._Array.append(temp)

        self._FIFOi =0    

            

    def __getitem__(self, key):
        return  (self._Array[key])
    
    def __len__(self):
        return  (self._NumCB)
        
            

    def get_Cline(self):
        return(self._Array)

    def BUi_Update_all(self):
        for i in self._Array:
            tempv=i.get_BUi()+1
            i.set_BUi(tempv)
                #if(i.get_BUi()>0):
                    

    def FIFO_inc(self):
        self._FIFOi+=1
        self._FIFOi%=self._NumCB

    def get_FIFOi(self):
        return (self._FIFOi)

    def get_LRUi(self):
        Ui=[]
        
        for i in range(self._NumCB):
            Ui.append(self._Array[i].get_BUi())
        for i in range(self._NumCB):
            if(self._Array[i].get_BUi()==max(Ui)):
                out=i
                
        #print(self._Array[3].get_BUi(),Ui,i,max(Ui))        
        return out       
            
        
            
        

    

    
        
                    
                
                
            

    

class Cache:

    def __init__(self,Csize=1,Bsize=1,A=1,rpol=0,walloc=0):

        self._Csize = Csize
        self._Bsize = Bsize
        self._asso= A
        if( (A*Bsize) <=0):
            self._NumCL = 1
        elif(Bsize <=0):
            self._Bsize=1

        else:
            self._Bsize = Bsize
            self._NumCL = int(Csize/(A*Bsize))
            
        
        self._Array=[]
        for i in range(self._NumCL):
            temp = Cache_Line(Csize,Bsize,A)
            self._Array.append(temp)

    def __getitem__(self, key):
        return  (self._Array[key])     

        
        
        
            
            

    def get_NumCL(self):
        return(self._NumCL)

    def get_Csize(self):
        return(self._Csize)

    def get_CL(self,CLi):
        return self.Array[CLi]
        
            

        
        

   
        
        

    

    

    


    


    
        
    


    











    

     

    
    
    

    
