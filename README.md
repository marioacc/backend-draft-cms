# backend-draft-cms

## Create virtual environment.
1. Download and install [virtualenv](https://virtualenv.pypa.io/)
```bash
$ curl -O https://files.pythonhosted.org/packages/b1/72/2d70c5a1de409ceb3a27ff2ec007ecdd5cc52239e7c74990e32af57affe9/virtualenv-15.2.0.tar.gz
$ tar xvfz virtualenv-15.2.0.tar.gz
$ cd virtualenv-15.2.0
$ sudo python setup.py install
``` 
2. Clone this repository somewhere in your machine
```bash
$ git clone https://github.com/marioacc/backend-draft-cms.git
```
3. Go into the repository folder
```bash
$ cd backend-draft-cms
```
4. Create a the virtual environment using Python 3.X.X using 
```bash
$ virtualenv -p python3 .
```  
5. Activate the virtual environment.
```bash
$ source bin/activate
```  
6. Install the required packages stored inside requirements.txt using pip.
```bash
$ pip install -r requirements.txt
```  



