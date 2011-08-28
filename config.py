settings_dict = {
    'url' : 'http://sfbay.craigslist.org/apa/',
    'period' : 60,
    'neighborhoods' : [
        'north beach', 
        'telegraph hill', 
        'marina', 
        'cow hollow', 
        'russian hill', 
        'soma',
	'downtown'
    ],
    'badhoods' : [
        'oakland',
        'san jose'
    ],
    'max_rent' : 1700
}

class Settings(object):
    pass

settings = Settings()
for k,v in settings_dict.items():
    setattr(settings, k, v)
