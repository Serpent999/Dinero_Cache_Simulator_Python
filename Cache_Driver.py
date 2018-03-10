"""
Project : Dinero Based Cache Simulator
Engineer : Nikhil.P.Lokhande
email: nikhil.l.1@aol.com

Note: Some of the simulation if blocks are redundant and may be combined together with similar blocks.
However, due to time constraints leaving it as it is.

"""


from cache_libv0_1 import *
import sys, os, string, re;

M = 0
A = 0
H =0

def replace(rpol):
        if(rpol=='f'):
                pass
        
                
                
def dosim(Infile,Csize=1,Bsize=1,A=1,rpol="r",walloc="n"):
        cache_data =[]
        a=0
        h=0
        m=0
        
        
        with open(Infile) as C_file:
                full_data=(C_file.readlines())

        for i in range(0,len(full_data)):
                if( (len(full_data[i].split())) >1):
                         mode =  full_data[i].split()[0]
                         Address = full_data[i].split()[1]
                         
                         
                         
                        
                        
               
                
                cache_data.append( (int(mode),(int(Address,16))) )

                
                
        #print(len(full_data))
                         
        C_file.close()
        #Populate the cache data user input size
        c = Cache(Csize,Bsize,A,rpol,walloc)
        
        for i in cache_data:
                a+=1
                mode=(i[0])
                Addr=(i[1])
                NumCL= c.get_NumCL()
                Tag = int(Addr/(NumCL*Bsize))
                Baddr = int(Addr/Bsize)
                CLi = int( (Baddr)%(NumCL) )
                hit_found=False
                
                
                if(A<=1):
                        if( (mode == 0 or mode ==2) and ((c[CLi][0].get_Vflag()==0) or (c[CLi][0].get_Tval()!= Tag)) ) :
                                c[CLi][0].set_Vflag(1) #A =1 direct mapped testing
                                c[CLi][0].set_Tval(Tag)
                                m+=1
                     
                                #print("Miss")

        
            
                        elif( c[CLi][0].get_Vflag()==1 and (c[CLi][0].get_Tval()== Tag)):
                            h+=1
                            #print("Hit")
                        elif( (mode ==1 ) and( (c[CLi][0].get_Vflag()==0) or (c[CLi][0].get_Tval()!= Tag)) and (walloc=="n") ):     #No allocate 
                                m+=1

                        elif( (mode ==1 ) and( (c[CLi][0].get_Vflag()==0) or (c[CLi][0].get_Tval()!= Tag)) and (walloc=="a") ):#Always allocate
                                c[CLi][0].set_Vflag(1) #A =1 direct mapped testing
                                c[CLi][0].set_Tval(Tag)
                                m+=1
                else:
                        
                        if( (mode == 0 or mode ==2)  and (rpol=="f") and (walloc=="n") ) : #A >1  Replace block FIFO

                                for i in range(A):
                                        if( (c[CLi][i].get_Vflag()==1) and (c[CLi][i].get_Tval()== Tag) ):
                                                h+=1
                                                hit_found=True
                                                break
                                if( (hit_found) is False ):
                                        tempi=c[CLi].get_FIFOi()
                                        c[CLi][tempi].set_Vflag(1) 
                                        c[CLi][tempi].set_Tval(Tag)
                                        c[CLi].FIFO_inc()
                                        #print(tempi)
                                        m+=1
                                                         
                                        
                                                

                        elif( (mode ==1 ) and (rpol=="f")and (walloc=="n") ): #A >1  Replace block FIFO, no allocate
                                tempi=c[CLi].get_FIFOi()
                                for i in range(A):
                                        if( (c[CLi][i].get_Vflag()==1) and (c[CLi][i].get_Tval()== Tag) ):
                                                h+=1
                                                hit_found=True
                                                break
                                
                                if( (hit_found) is False ):
                                        m+=1


                                        

                        if( (mode == 0 or mode ==2)  and (rpol=="f") and (walloc=="a") ) : #A >1  Replace block FIFO, always allocate

                                for i in range(A):
                                        if( (c[CLi][i].get_Vflag()==1) and (c[CLi][i].get_Tval()== Tag) ):
                                                h+=1
                                                hit_found=True
                                                break
                                if( (hit_found) is False ):
                                        tempi=c[CLi].get_FIFOi()
                                        c[CLi][tempi].set_Vflag(1) 
                                        c[CLi][tempi].set_Tval(Tag)
                                        c[CLi].FIFO_inc()
                                        #print(tempi)
                                        m+=1
                                                         
                                        
                                                

                        elif( (mode ==1 ) and (rpol=="f")and (walloc=="a") ): #A >1  Replace block FIFO, always allocate
                                tempi=c[CLi].get_FIFOi()
                                for i in range(A):
                                        if( (c[CLi][i].get_Vflag()==1) and (c[CLi][i].get_Tval()== Tag) ):
                                                h+=1
                                                hit_found=True
                                                break
                                
                                if( (hit_found) is False ):
                                        tempi=c[CLi].get_FIFOi()
                                        c[CLi][tempi].set_Vflag(1) 
                                        c[CLi][tempi].set_Tval(Tag)
                                        c[CLi].FIFO_inc()
                                        #print(tempi)
                                        m+=1

                                        
                        if( (mode == 0 or mode ==2) and (rpol=="l") and (walloc=="n") ) : #A >1  Replace block LRU,no allocate
                                for i in range(A):
                                        if( (c[CLi][i].get_Vflag()==1) and (c[CLi][i].get_Tval()== Tag) ):
                                                h+=1
                                                hit_found=True
                                                c[CLi][i].set_BUi(0)
                                                c[CLi].BUi_Update_all()
                                                
                                                
                                                break
                                if((hit_found) is False):
                                        LRUi=c[CLi].get_LRUi()
                                        c[CLi][LRUi].set_Vflag(1) 
                                        c[CLi][LRUi].set_Tval(Tag)
                                        c[CLi][LRUi].set_BUi(0)
                                        c[CLi].BUi_Update_all()
                                        
                                        m+=1
                                                
                                                
                                
                        elif( (mode ==1 ) and (rpol=="l")and (walloc=="n") ): #A >1  Replace block LRU, no allocate
                                #LRUi=c[CLi].get_LRUi()
                                for i in range(A):
                                        if( (c[CLi][i].get_Vflag()==1) and (c[CLi][i].get_Tval()== Tag) ):
                                                h+=1
                                                hit_found=True
                                                c[CLi][i].set_BUi(0)
                                                c[CLi].BUi_Update_all()
                                                
                                                break
                                
                                if( (hit_found) is False ):
                                        m+=1



                        if( (mode == 0 or mode ==2) and (rpol=="l") and (walloc=="a") ) : #A >1  Replace block LRU,  always allocate
                                for i in range(A):
                                        if( (c[CLi][i].get_Vflag()==1) and (c[CLi][i].get_Tval()== Tag) ):
                                                h+=1
                                                hit_found=True
                                                c[CLi][i].set_BUi(0)
                                                c[CLi].BUi_Update_all()
                                                
                                                
                                                break
                                if((hit_found) is False):
                                        LRUi=c[CLi].get_LRUi()
                                        c[CLi][LRUi].set_Vflag(1) 
                                        c[CLi][LRUi].set_Tval(Tag)
                                        c[CLi][LRUi].set_BUi(0)
                                        c[CLi].BUi_Update_all()
                                        
                                        m+=1
                                                
                                                
                                
                        elif( (mode ==1 ) and (rpol=="l")and (walloc=="a") ): #A >1  Replace block LRU, always allocate
                                #LRUi=c[CLi].get_LRUi()
                                for i in range(A):
                                        if( (c[CLi][i].get_Vflag()==1) and (c[CLi][i].get_Tval()== Tag) ):
                                                h+=1
                                                hit_found=True
                                                c[CLi][i].set_BUi(0)
                                                c[CLi].BUi_Update_all()
                                                
                                                break
                                
                                if( (hit_found) is False ):
                                        LRUi=c[CLi].get_LRUi()
                                        c[CLi][LRUi].set_Vflag(1) 
                                        c[CLi][LRUi].set_Tval(Tag)
                                        c[CLi][LRUi].set_BUi(0)
                                        c[CLi].BUi_Update_all()
                                        m+=1                




                                        
                                        

                                        


                                        
                                
                                        
                                                
                                        
                                                
                                
                                

                                
                                    
                                
                        
                                        
                                
                               
    
                                
                                                
                                                
                                                 

                

                
        out=[]
        out.append(a)
        out.append(h)
        out.append(m)
        return out          
                    
           
                
        

        
               
        
#Read and store cache input file data

print("Welcome to Dinero based cache simulator in Python")
fname =(raw_input("Enter the path filename of the .din or similar trace file with respect to the driver eg folder \ file.din or enter D for demo file:"))
if( (fname == 'D') or (fname == 'd') ):
        fname="Demo.din"
usize=int(input("Enter cache size (positive integer):"))
ubsize=int(input("Enter cache block size (positive integer):"))
uassoc=int(input("Enter cache associativity (positive integer):"))
if( (usize<=0)or (ubsize<=0) or (uassoc<=0) ):
        print("Please enter positive values only")
        sys.exit()
urepl=(raw_input("Enter the cache replacement policy l= (Least Recently Used) , f = (FIFO) , other key for no policy:"))

uwalloc=(raw_input("Enter the cache write allocation policy a= (Always Allocate) , n = (Never Allocate) , other key for no policy:"))

#Test
#out=dosim(fname,1024,32,4,'l','n')
   
out=dosim(fname,usize,ubsize,uassoc,urepl,uwalloc)
A=out[0]
H=out[1]
M=out[2]




        


print ("Access:"+ str(A),"Hits:" +str(H), "Misses:"+ str(M))
 




