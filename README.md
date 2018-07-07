![https://raw.githubusercontent.com/pallavmahamana/shabdkosh/master/gif/shabdkosh.gif](https://raw.githubusercontent.com/pallavmahamana/shabdkosh/master/gif/shabdkosh.gif)


# shabdkosh
a nifty little Python script to improve your vocabulary.



# How to Setup ?
0. Install dependencies by 
   $ pip install -r requirements.txt

1. Move this script to your /usr/bin/ ,  $ sudo mv shabdkosh.py /usr/bin/shabdkosh
2. Give it super powers , $ sudo chmod +x /usr/bin/shabdkosh
3. Create a empty .shabdkosh.json file for storing history. $ sudo echo '{}'>/usr/bin/.shabdkosh.json && sudo chmod +777 /usr/bin/.shabdkosh.json
4. Start playing with it by 
    * $ shabdkosh 
    
        *to get definition of random word*
        
    * $ shabdkosh <some_word> 
    
        *to get definition of some word.*
        
    * $ shabdkosh --history
    
        *to get definition of word from your history.*





# ^^ This method is Boring, I need one line script to install shabdkosh !!!

This one big bash line will setup shabdkosh for you and will even make it show you one random word from history when you start up a terminal session.


```
sudo bash -c 'wget https://raw.githubusercontent.com/pallavmahamana/shabdkosh/master/shabdkosh.py -O /usr/bin/shabdkosh && wget https://raw.githubusercontent.com/pallavmahamana/shabdkosh/master/shabdbash.py -O /usr/bin/shabdbash && echo '{}'>>/usr/bin/.shabdkosh.json && chmod +x /usr/bin/shabdkosh && chmod +x /usr/bin/shabdbash && chmod +777 /usr/bin/.shabdkosh.json && echo ''>>~/.bashrc && echo ''>>~/.zshrc && echo 'shabdbash'>>~/.bashrc && echo 'shabdbash'>>~/.zshrc && shabdkosh welcome'

```
