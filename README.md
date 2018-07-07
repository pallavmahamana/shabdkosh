![https://raw.githubusercontent.com/pallavmahamana/shabdkosh/master/gif/shabdkosh.gif](https://raw.githubusercontent.com/pallavmahamana/shabdkosh/master/gif/shabdkosh.gif)


# shabdkosh
a nifty little Python script to improve your vocabulary.



# How to Setup ?
1. Move this script to your /usr/bin/ ,  $ sudo mv shabdkosh.py /usr/bin/shabdkosh
2. Give it super powers , $ sudo chmod +x /usr/bin/shabdkosh
3. Create a empty .shabdkosh.json file for storing history. $ sudo echo '{}'>/usr/bin/.shabdkosh.json && sudo chmod +777 /usr/bin/.shabdkosh.json
4. Start playing with it by 
    * $ shabdkosh 
    
        *to get defination of random word*
        
    * $ shabdkosh <some_word> 
    
        *to get defination of some word.*
        
    * $ shabdkosh --history
    
        *to get defination of word from your history.*





# ^^ This method is Boring, I need one line script to install shabdkosh !!!

>sudo bash -c 'wget https://raw.githubusercontent.com/pallavmahamana/shabdkosh/master/shabdkosh.py -O /usr/bin/shabdkosh && wget https://raw.githubusercontent.com/pallavmahamana/shabdkosh/master/shabdbash.py -O /usr/bin/shabdbash && echo '{}'>>/usr/bin/.shabdkosh.json && chmod +x /usr/bin/shabdkosh && chmod +x /usr/bin/shabdbash && chmod +777 /usr/bin/.shabdkosh.json && echo 'shabdbash'>>~/.bashrc && echo 'shabdbash'>>~/.zshrc && shabdkosh welcome'
