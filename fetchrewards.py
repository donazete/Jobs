def getEmailID(emailaddy): # extracts emailId from full email address
    i = 0
    j = 0

    while i < len(emailaddy):
        if (emailaddy[i] == '@'):
            j = i
        i += 1
    res = removeDot(emailaddy[0 : j]) + emailaddy[j : ]
    return res


def removeDot(emailId): #removes dot from any part of the emailID
    result = emailId.replace('.', '')
    return result

def extractId(emailList): #extracts the id without the plus sign
    x = 0
    y = 0
    z = 0
    count = emailList.count('+')

    if count > 0:
        while x < len(emailList):
            if (emailList[x] == '+'):
                y = x
            if (emailList[x] == '@'):
                z = x
            x += 1
        res = removeDot(emailList[0 : y]) + emailList[z : ]
    else:
        res = getEmailID(emailList)
    return res

#x = 'abc.edc+edu@xyz.com'
#print(x)
#y = removeDot(x)
#print(y)
#z = extractId(x)
#print(z)

def compareEmail(emailList):
    index = 0
    ind = 1 
    unique = []
    val = extractId(emailList[index])
    #print(val)
    unique.append(val)

    while index < len(emailList) - 1:
        
        while ind < len(emailList):
            val1 = extractId(emailList[index])
            val2 = extractId(emailList[ind])
            #print('ind '+ str(ind)+': ' + emailList[ind])
            #print('index '+ str(index)+': ' + emailList[index])
            #print(val1 +' - '+ val2)
            if val1 != val2:
                if unique.count(val2) == 0:
                    unique.append(val2)
            ind += 1
        
        ind = 1
        """print('Index before: '+str(index))
        print('Value1 : '+ emailList[index])
        print('Value2 : '+ emailList[ind-1])"""
        index += 1
        
    return len(unique)


#Test data
"""email = ['donoye@gmail.com', 'don.oye@gmail.com', 'donoye+123@gmail.com', 'don.oye@yahoo.com', 'brandolph@abc.com', 'b.randolph@abc.com', 'b.randolph+guy@abc.com', 'b.randolph@xyz.com', 'dun@ths.org', 'set@yth.com','set+@yth.com']
out = compareEmail(email)
print(out)
print(len(email))"""