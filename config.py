settings_dict = {
    'url' : 'http://sfbay.craigslist.org/apa/',
    'period' : 60,
    'neighborhoods' : [
        'north beach', 
        'telegraph hill', 
        'nob hill', 
        'marina', 
        'cow hollow', 
        'russian hill', 
        'soma'
    ],
    'max_rent' : 1700
}

class Settings(object):
    pass

settings = Settings()
for k,v in settings_dict.items():
    setattr(settings, k, v)
