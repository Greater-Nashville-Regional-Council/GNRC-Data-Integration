#dictionaries of geographies and formatting for GEO_IDs/FIPS etc.
#this dict has the Census Bureau default naming convention as the key, and the value we want to see in our docs as the value
censustocommon = {'Williamson County, Tennessee': 'Williamson County',
                  'Wilson County, Tennessee': 'Wilson County',
                  'Houston County, Tennessee': 'Houston County',
                  'Humphreys County, Tennessee': 'Humphreys County',
                  'Macon County, Tennessee': 'Macon County',
                  'Maury County, Tennessee': 'Maury County',
                  'Montgomery County, Tennessee': 'Montgomery County',
                  'Rutherford County, Tennessee': 'Rutherford County',
                  'Robertson County, Tennessee': 'Robertson County',
                  'Stewart County, Tennessee': 'Stewart County',
                  'Sumner County, Tennessee': 'Sumner County',
                  'Trousdale County, Tennessee': 'Trousdale County',
                  'Cheatham County, Tennessee': 'Cheatham County',
                  'Davidson County, Tennessee': 'Davidson County',
                  'Dickson County, Tennessee': 'Dickson County',
                  'Simpson County, Kentucky': 'Simpson County, KY',
                  'Allen County, Kentucky': 'Allen County, KY',
                  'Nolensville town, Tennessee': 'Nolensville',
                  'Adams city, Tennessee': 'Adams',
                  'Ashland City town, Tennessee': 'Ashland City',
                  'Belle Meade city, Tennessee': 'Belle Meade',
                  'Oak Hill city, Tennessee': 'Oak Hill',
                  'Pegram town, Tennessee': 'Pegram',
                  'Portland city, Tennessee': 'Portland',
                  'Pleasant View city, Tennessee': 'Pleasant View',
                  'Ridgetop city, Tennessee': 'Ridgetop',
                  'Berry Hill city, Tennessee': 'Berry Hill',
                  'Brentwood city, Tennessee': 'Brentwood',
                  'Burns town, Tennessee': 'Burns',
                  'Hendersonville city, Tennessee': 'Hendersonville',
                  'Kingston Springs town, Tennessee': 'Kingston Springs',
                  'Lafayette city, Tennessee': 'Lafayette',
                  'La Vergne city, Tennessee': 'La Vergne',
                  'Lebanon city, Tennessee': 'Lebanon',
                  'McEwen city, Tennessee': 'McEwen',
                  'Millersville city, Tennessee': 'Millersville',
                  'Mitchellville city, Tennessee': 'Mitchellville',
                  'Mount Juliet city, Tennessee': 'Mount Juliet',
                  'Mount Pleasant city, Tennessee': 'Mount Pleasant',
                  'Murfreesboro city, Tennessee': 'Murfreesboro',
                  'Nashville-Davidson metropolitan government (balance), Tennessee': 'Nashville',
                  'New Johnsonville city, Tennessee': 'New Johnsonville',
                  'Vanleer town, Tennessee': 'Vanleer',
                  'Watertown city, Tennessee': 'Watertown',
                  'Waverly city, Tennessee': 'Waverly',
                  'Westmoreland town, Tennessee': 'Westmoreland',
                  'White Bluff town, Tennessee': 'White Bluff',
                  'White House city, Tennessee': 'White House',
                  'Eagleville city, Tennessee': 'Eagleville',
                  'Erin city, Tennessee': 'Erin',
                  'Fairview city, Tennessee': 'Fairview',
                  'Forest Hills city, Tennessee': 'Forest Hills',
                  'Franklin city, Tennessee': 'Franklin',
                  'Gallatin city, Tennessee': 'Gallatin',
                  'Goodlettsville city, Tennessee': 'Goodlettsville',
                  'Greenbrier town, Tennessee': 'Greenbrier',
                  'Cedar Hill city, Tennessee': 'Cedar Hill',
                  'Charlotte town, Tennessee': 'Charlotte',
                  'Clarksville city, Tennessee': 'Clarksville',
                  'Coopertown town, Tennessee': 'Coopertown',
                  'Columbia city, Tennessee': 'Columbia',
                  'Cumberland City town, Tennessee': 'Cumberland City',
                  'Cross Plains city, Tennessee': 'Cross Plains',
                  'Dover city, Tennessee': 'Dover',
                  'Smyrna town, Tennessee': 'Smyrna',
                  'Slayden town, Tennessee': 'Slayden',
                  'Springfield city, Tennessee': 'Springfield',
                  'Spring Hill city, Tennessee': 'Spring Hill',
                  'Tennessee Ridge town, Tennessee': 'Tennessee Ridge',
                  "Thompson's Station town, Tennessee": "Thompson's Station",
                  'Dickson city, Tennessee': 'Dickson',
                  'Franklin city, Kentucky': 'Franklin',
                  'Scottsville city, Kentucky': 'Scottsville',
                  'Tennessee': 'Tennessee',
                  'United States': 'US'
}
#this dict has the common use name to the full geoid
commontogeoid = {'Williamson County': '0500000US47187',
                 'Wilson County': '0500000US47189',
                 'Houston County': '0500000US47083',
                 'Humphreys County': '0500000US47085',
                 'Macon County': '0500000US47111',
                 'Maury County': '0500000US47119',
                 'Montgomery County': '0500000US47125',
                 'Rutherford County': '0500000US47149',
                 'Robertson County': '0500000US47147',
                 'Stewart County': '0500000US47161',
                 'Sumner County': '0500000US47165',
                 'Trousdale County': '0500000US47169',
                 'Cheatham County': '0500000US47021',
                 'Davidson County': '0500000US47037',
                 'Dickson County': '0500000US47043',
                 'Simpson County, KY': '0500000US21213',
                 'Allen County, KY': '0500000US21003',
                 'Nolensville': '1600000US4753460',
                 'Adams': '1600000US4700200',
                 'Ashland City': '1600000US4702180',
                 'Belle Meade': '1600000US4704620',
                 'Oak Hill': '1600000US4754780',
                 'Pegram': '1600000US4757480',
                 'Portland': '1600000US4760280',
                 'Pleasant View': '1600000US4759560',
                 'Ridgetop': '1600000US4763140',
                 'Berry Hill': '1600000US4705140',
                 'Brentwood': '1600000US4708280',
                 'Burns': '1600000US4709880',
                 'Hendersonville': '1600000US4733280',
                 'Kingston Springs': '1600000US4739660',
                 'Lafayette': '1600000US4740160',
                 'La Vergne': '1600000US4741200',
                 'Lebanon': '1600000US4741520',
                 'McEwen': '1600000US4744840',
                 'Millersville': '1600000US4748980',
                 'Mitchellville': '1600000US4749460',
                 'Mount Juliet': '1600000US4750780',
                 'Mount Pleasant': '1600000US4751080',
                 'Murfreesboro': '1600000US4751560',
                 'Nashville': '1600000US4752006',
                 'New Johnsonville': '1600000US4752820',
                 'Vanleer': '1600000US4776860',
                 'Watertown': '1600000US4778320',
                 'Waverly': '1600000US4778560',
                 'Westmoreland': '1600000US4779420',
                 'White Bluff': '1600000US4779980',
                 'White House': '1600000US4780200',
                 'Eagleville': '1600000US4722360',
                 'Erin': '1600000US4724320',
                 'Fairview': '1600000US4725440',
                 'Forest Hills': '1600000US4727020',
                 'Franklin': '1600000US4727740',
                 'Gallatin': '1600000US4728540',
                 'Goodlettsville': '1600000US4729920',
                 'Greenbrier': '1600000US4730960',
                 'Cedar Hill': '1600000US4711980',
                 'Charlotte': '1600000US4713080',
                 'Clarksville': '1600000US4715160',
                 'Coopertown': '1600000US4716980',
                 'Columbia': '1600000US4716540',
                 'Cumberland City': '1600000US4718820',
                 'Cross Plains': '1600000US4718420',
                 'Dover': '1600000US4721400',
                 'Smyrna': '1600000US4769420',
                 'Slayden': '1600000US4769080',
                 'Springfield': '1600000US4770500',
                 'Spring Hill': '1600000US4770580',
                 'Tennessee Ridge': '1600000US4773460',
                 "Thompson's Station": '1600000US4773900',
                 'Dickson': '1600000US4720620',
                 'Franklin': '1600000US2128918',
                 'Scottsville': '1600000US2169114',
                 'Tennessee': '0400000US47',
                 'US': '0100000US'
}

#list of FIPS codes
GNRC = ['111', #Macon
       '161', #Stewart
       '125', #Montgomery
       '083', #Houston
       '085', #Humphreys
       '043', #Dickson
       '021', #Cheatham
       '147', #Robertson
       '165', #Sumner
       '037', #Davidson
       '189', #Wilson
       '169', #Trousdale
       '187', #Williamson
       '149', #Rutherford
       '119'] #Maury
KY = ['003', #Allen
      '213'] #Simpson
censusplaces = ['1600000US4700200', #Adams city, Tennessee: Robertson
          '1600000US4702180', #Ashland City town, Tennessee: Cheatham
          '1600000US4704620', #Belle Meade city, Tennessee: Davidson
          '1600000US4705140', #Berry Hill city, Tennessee: Davidson
          '1600000US4708280', #Brentwood city, Tennessee: Williamson
          '1600000US4709880', #Burns town, Tennessee: Dickson
          '1600000US4711980', #Cedar Hill city, Tennessee: Robertson
          '1600000US4713080', #Charlotte town, Tennessee: Dickson
          '1600000US4715160', #Clarksville city, Tennessee: Montgomery
          '1600000US4716540', #Columbia city, Tennessee: Maury
          '1600000US4716980', #Coopertown town, Tennessee: Robertson
          '1600000US4718420', #Cross Plains city, Tennessee: Robertson
          '1600000US4718820', #Cumberland City town, Tennessee: Stewart
          '1600000US4720620', #Dickson city, Tennessee: Dickson
          '1600000US4721400', #Dover city, Tennessee: Stewart
          '1600000US4722360', #Eagleville city, Tennessee: Rutherford
          '1600000US4724320', #Erin city, Tennessee: Houston
          '1600000US4725440', #Fairview city, Tennessee: Williamson
          '1600000US4727020', #Forest Hills city, Tennessee: Davidson
          '1600000US4727740', #Franklin city, Tennessee: Williamson
          '1600000US4728540', #Gallatin city, Tennessee: Sumner
          '1600000US4729920', #Goodlettsville city, Tennessee: Davidson/Sumner
          '1600000US4730960', #Greenbrier town, Tennessee: Robertson
          '1600000US4733280', #Hendersonville city, Tennessee: Sumner
          '1600000US4739660', #Kingston Springs town, Tennessee: Cheatham
          '1600000US4741200', #La Vergne city, Tennessee: Rutherford
          '1600000US4740160', #La Vergne city, Tennessee: Macon
          '1600000US4741520', #Lebanon city, Tennessee: Wilson
          '1600000US4744840', #McEwen city, Tennessee: Humphreys
          '1600000US4748980', #Millersville city, Tennessee: Robertson/Sumner
          '1600000US4749460', #Mitchellville city, Tennessee: Sumner
          '1600000US4750780', #Mount Juliet city, Tennessee: Wilson
          '1600000US4751080', #Mount Pleasant city, Tennessee: Maury
          '1600000US4751560', #Murfreesboro city, Tennessee: Rutherford
          '1600000US4752006', #Nashville-Davidson metropolitan government (balance): Davidson
          '1600000US4752820', #New Johnsonville city, Tennessee: Humphreys
          '1600000US4753460', #Nolensville town, Tennessee: Williamson
          '1600000US4754780', #Oak Hill city, Tennessee: Davidson
          '1600000US4757480', #Pegram town, Tennessee: Cheatham
          '1600000US4759560', #Pleasant View city, Tennessee: Cheatham
          '1600000US4760280', #Portland city, Tennessee: Robertson/Sumner
          '1600000US4763140', #Ridgetop city, Tennessee: Davidson/Robertson
          '1600000US4769080', #Slayden town, Tennessee: Dickson
          '1600000US4769420', #Smyrna town, Tennessee: Rutherford
          '1600000US4770580', #Spring Hill city, Tennessee: Maury/Williamson
          '1600000US4770500', #Springfield city, Tennessee: Robertson
          '1600000US4773460', #Tennessee Ridge town, Tennessee: Houston/Stewart
          '1600000US4773900', #Thompson's Station town, Tennessee: Williamson
          '1600000US4776860', #Vanleer town, Tennessee: Dickson
          '1600000US4778320', #Watertown city, Tennessee: Wilson
          '1600000US4778560', #Waverly city, Tennessee: Humphreys
          '1600000US4779420', #Westmoreland town, Tennessee: Sumner
          '1600000US4779980', #White Bluff town, Tennessee: Dickson
          '1600000US4780200', #White House city, Tennessee: Robertson/Sumner
          '1600000US2128918', #Franklin city, Kentucky:
          '1600000US2169114'] #Scottsville city, Kentucky
