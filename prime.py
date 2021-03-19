# Prime, print prime numbers up to a limit

psf=[1,2,3] # Primes So Far
i=0 # Iterations
nc=5 # Next Candidate
limit=10000

while True:
    i=i+1;
    nc=nc+2; # Next Prime

    # Is this one a multiple of a previous prime
    for j in range(1,len(psf)):
        #print(nc,psf[j],j,nc%psf[j],len(psf))
        if nc%psf[j]==0 :break
            
    if nc%psf[j]!=0 :
        psf.append(nc)
    else: continue
    
    if(i>=limit): break;
        
print(psf)