facebook = False
twitter = True
instagram = True

if facebook and twitter == True:
    print('Your are a good influencer!')
elif facebook and instagram == True:
    print('Your are a good influencer!')
elif twitter and instagram == True:
    print('Your are a good influencer!')
elif twitter and instagram and facebook == True:
    print('Your are a good influencer!')
else:
    print('Your are a bad influencer!')