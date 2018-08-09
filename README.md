# backend-draft-cms

## Create virtual enviroment.
1. Download and install [virtualenv](https://virtualenv.pypa.io/).
```bash
	$ sudo pip install virtualenv
	$ sudp pip install https://github.com/pypa/virtualenv/tarball/master
	$ curl -O https://files.pythonhosted.org/packages/b1/72/2d70c5a1de409ceb3a27ff2ec007ecdd5cc52239e7c74990e32af57affe9/virtualenv-15.2.0.tar.gz
	$ tar xvfz virtualenv-15.2.0.tar.gz 
	$ cd virtualenv-15.2.0
	$ sudo python setup.py install
```  
2. Create a the virtual enviroment using Python 3.X.X using 
```bash
virtualenv -p python3 backend-draft-cms/
```  
3. Install the required packages stored inside requirements.txt using pip.
```bash
pip install -r requirements.txt
```  
4. Activate the virtual enviroment.
```bash
source bin/activate.fish
```  



