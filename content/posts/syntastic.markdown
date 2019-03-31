title: Syntastic and closure-compiler: no checkers available for Javascript
slug: syntastic-closure-compiler
category: posts 
date: 2019-03-15
modified: 2019-03-31


While trying to get the Vim Syntastic 
syntax checker to work for Javascript
I came across the following errors 
(the numbers are not specific to the errors): 

```text
syntastic: 9.418609: CacheErrors: Checker javascript/closurecompiler is not available
syntastic: 9.418964: CacheErrors: no checkers available for javascript
```
<br/>

At first I tried to use the Google closure-compiler 
by unzipping the .jar file and setting the
corresponding settings in my .vimrc like so:


```vim
let g:syntastic_javascript_checkers = ["closurecompiler"]
let g:syntastic_javascript_closurecompiler_path = $HOME . '/.vim/linters/js/closure-compiler/closure-compiler-v20190301.jar'
```
<br/>

As it turns out though, you also need to
have Java installed to make it run. In
Bash, type "java" to see whether you have it
installed. The following did the trick 
(always run update first):

```bash
sudo apt-get update
sudo apt-get install default-jre
```
<br/>

The closure-compiler is a .jar (Java ARchive)
file.

<br/>

But, in the end, I'll probably go with Vim ALE 
and ESLint. Because:

* ALE is asynchronous (!)
* Java seems heavy and slow (but ESLint still needs Node)
* ESLint should also work with html files
* ESLint is more popular
* Closure-compiler doesn't seem to be available for ALE anyways.

