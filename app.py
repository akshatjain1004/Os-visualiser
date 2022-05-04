from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def entry_point():
    
    return render_template('index.html')

@app.route('/form1', methods=['GET','POST'])
def form1():
    
    return render_template('form1.html')

@app.route('/form2', methods=['GET','POST'])
def form2():
    
    return render_template('form2.html')

@app.route('/form3', methods=['GET','POST'])
def form3():
    
    return render_template('form3.html')

@app.route('/fifo', methods=['GET','POST'])
def fifo():
    status=[]
    
    Frame=[]
    mat=[]
    if(request.method=='POST'):
        
        s= request.form['input_string']
        frames= request.form['frames']
        s= list(str(s).split(','))
        
        frames= int(frames)
        
        for i in range(frames):
            Frame.append(" ")
        count=0
        for i in s:
            temp= True
            for j in Frame:
                if(j==i):
                    status.append('hit')
                    temp= False
            if(temp):
                status.append('fault')
                Frame[count]=i
                count= (count+1)%frames
            print(Frame)
            a= Frame
            mat.append(tuple(a))
            print(mat)
        print(mat)
        return render_template('table1.html',matr=mat, status=status, frames= Frame)
    return render_template('table1.html',matr=mat, status=status, frames= Frame)

@app.route('/lru', methods=['GET','POST'])
def lru():
    status=[]
    
    Frame=[]
    mat=[]
    if(request.method=='POST'):
        
        s= request.form['input_string']
        frames= request.form['frames']
        s= list(str(s).split(','))
        
        frames= int(frames)
        
        for i in range(frames):
            Frame.append(" ")
        count=0
        for i in range(len(s)):
            temp= True
            for j in Frame:
                if(j==s[i]):
                    status.append('hit')
                    temp= False
            if(temp):
                st= True
                status.append('fault')
                for j in range(len(Frame)):
                    if(Frame[j]==" "):
                        Frame[j]=s[i]
                        st= False
                        break
                if(st):
                    lru= 0
                    dist=0
                    for j in range(len(Frame)):
                        d=0
                        for k in range(i):
                            if(s[i-k]==Frame[j]):
                                break
                            else:
                                d+=1
                        if(d>=dist):
                            dist=d
                            lru=j
                    Frame[lru]=s[i]
            print(Frame)
            a= Frame
            mat.append(tuple(a))
            print(mat)
        print(mat)
        return render_template('table1.html',matr=mat, status=status, frames= Frame)
    return render_template('table1.html',matr=mat, status=status, frames= Frame)

@app.route('/optimum', methods=['GET','POST'])
def optimum():
    status=[]
    
    Frame=[]
    mat=[]
    if(request.method=='POST'):
        
        s= request.form['input_string']
        frames= request.form['frames']
        s= list(str(s).split(','))
        
        frames= int(frames)
        
        for i in range(frames):
            Frame.append(" ")
        count=0
        for i in range(len(s)):
            temp= True
            for j in Frame:
                if(j==s[i]):
                    status.append('hit')
                    temp= False
            if(temp):
                st= True
                status.append('fault')
                for j in range(len(Frame)):
                    if(Frame[j]==" "):
                        Frame[j]=s[i]
                        st= False
                        break
                if(st):
                    lru= 0
                    dist=0
                    for j in range(len(Frame)):
                        d=0
                        for k in range(i+1,len(s)):
                            if(s[k]==Frame[j]):
                                break
                            else:
                                d+=1
                        if(d>dist):
                            dist=d
                            lru=j
                    Frame[lru]=s[i]
            print(Frame)
            a= Frame
            mat.append(tuple(a))
            print(mat)
        print(mat)
        return render_template('table1.html',matr=mat, status=status, frames= Frame)
    return render_template('table1.html',matr=mat, status=status, frames= Frame)

if __name__ == '__main__':
    app.run(debug=True,port=8000)