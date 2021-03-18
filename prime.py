psf=[1,2,3] # Primes So Far
i=0 # Iterations

while True:
    i=i+1;
    np=psf[len(psf)-1]+2; # Next Prime
    # Is this one a multiple of a previous prime
    for j in range(2,len(psf)):
        print(np,psf[j],j,np%psf[j])
        if np%psf[j]!=0 :
            print(np) 
            continue
    
    if(i>=100): break;