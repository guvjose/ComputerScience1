# Jose Guvenilir
# guvenj
# lab 1 checkpoint 3

jupDiam = 88846.0
jupToSun = 483632000.0
earthDiam = 7926.0
earthToSun = 92957100.0
speedOfLight = 186000

jupEarthSunRatio = jupToSun / earthToSun
jupEarthVolumeRatio = ((jupDiam / 2) ** 3) / ((earthDiam / 2) ** 3)
minsToEarth = (earthToSun / speedOfLight) / 60
secsToEarth = (earthToSun / speedOfLight) % 60
minsToJup = (jupToSun / speedOfLight) / 60
secsToJup = (jupToSun / speedOfLight) % 60

print 'Jupiter is', jupEarthSunRatio, 'times farther from the Sun than Earth is.'
print 'Jupiter is', jupEarthVolumeRatio, 'times more voluminous than Earth is.'
print 'It takes light %d minutes and %d seconds to reach Earth.' % (minsToEarth, secsToEarth)
print 'It takes light %d minutes and %d seconds to reach Jupiter.' % (minsToJup, secsToJup)
