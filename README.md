# This is a very basic library that encrypts and decrypts the text. No matter whatever the text is !!!


<p align="center">
  <img width="200" src="https://webdesigngalore.com/wp-content/uploads/2013/11/lock-icon-ssl-certificates-geo-trust-comodo-thawte-symantec.gif" alt="Encrypt The Text">
</p>

1. It uses no external libraries. So, Your text is secure with this library.
1. Plus, The letter encrypted here is never the same as the result of any previous encrypted value.
1. Plus, It encrypts and decrypts all the keys included the `Rupee` symbol with all the keywords present on the regular keyboards. If some Don't work, create an issue asking for the `letter` to be added in the library via [GitHub](https://github.com/jainamoswal/secureme/issues/new). We will soon improve it and deploy it in the new version.

 >#### How Can this happen?
      
This encrypts and decrypts the text as per your text length.

This means if `Cat` is encrypted, The result will be like `6>G`.

And if `Cake` is encrypted, Instead of `6>gp` the result will be different like `2:An`

So, decrypting the text without this library is difficult, But not impossible. Developers are on this issue and will soon improve this after `ver 0.1.5`

>#### But how to use it ??

### How to install the library ?? :-
This is for installing on windows OS,
For other systems, You can [Google](https://www.google.com/search?sxsrf=ALeKk02qopUdAGhnqeM5giRDxjmNYMKefg%3A1608048571827&source=hp&ei=u9_YX57RL8LE4-EP_eiGmAY&q=Install+Python+packages+on+Ubuntu&oq=Install+Python+packages+on+Ubuntu&gs_lcp=CgZwc3ktYWIQAzIHCCMQyQMQJzIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHlDdBljdBmDLC2gAcAB4AIABeIgBeJIBAzAuMZgBAKABAqABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjempzfr9DtAhVC4jgGHX20AWMQ4dUDCAc&uact=5) it or even visit [Pypi.org](https://packaging.python.org/tutorials/installing-packages/) for detailed documentation.

>#### 1. To install this library:-
>`pip install secureme`

>#### 2. To update this library:-
>` pip install secureme --upgrade`

### How to use the library ?? :- 

First, you will have to import this in your Python files by `import secureme`. 

You can also import a single function from the library by `from secureme import <Function Name Here>`. 

>#### 1. To Encrypt the text :-
>`secureme.encrypt(<Any Text Here>)`

>#### 2. To Decrypt the Encrypted value :-
>`secureme.decrypt(<Encrypted Text Here>)`

>#### 3. To check that this libary works for your text or not, Use :-
>`secureme.decrypt(secureme.encrypt(<Your Text Goes Here>))`



### Then you can do whatever you want to do with the Encrypted text or with Decrypted text.
This can also be used for decrypting the passwords which are saved on the [Google Sheets](https://docs.google.com/spreadsheets/) or [Excel Sheet](https://www.microsoft.com/en-in/microsoft-365/excel). The decrypted Passwords can be retrieved by a Telegram Bot or any other service you prefer.

#### For more information you can contact me on Social Media via [Telegram](https://t.me/jainamoswal) or [E-Mail](mailto:jainamoswal4@gmail.com)
Contributers |   1   | 2 | 3 | 4 
--- | --- | --- | --- |--- 
Names | [Jainam](https://www.github.com/jainamoswal) | [Shivam](https://www.github.com/shivamsn97) | Ayesha | This is reserved only for you. | 

---------------------------------------------------

---------------------------------------------------
## Note:- 
From later versions after `0.1.5` the Encrypted text with versions below `0.1.5` won’t be Decrypted after the up-gradation of this library, you will need to Save all the encrypted text in the normal Text and then Re-Encrypt it. This is done for giving better security to your text. If you don't want to update, Don't. It's your wish. Upgrading gives extra security to prevent anyone to break the Encrypted text. As the version levels up, the security also levels up. So, it is advised to keep this library up-to-date !!
