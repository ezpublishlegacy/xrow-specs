Name: xrow-repo
Summary: The repository of the xrow GmbH
Version: 7.0
Release: 4
License: GPL
Group: Applications/Webservice
URL: https://github.com/xrowgmbh/xrow-specs
Distribution: Linux
Vendor: xrow GmbH
Packager: Bjoern Dieding / xrow GmbH <bjoern@xrow.de>
Requires: yum
Requires: yum-utils

BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch

%description
The RPM repository of the xrow GmbH

%build

%install

install -dm 755 $RPM_BUILD_ROOT/etc/yum.repos.d

cat <<EOL > $RPM_BUILD_ROOT/etc/yum.repos.d/xrow.repo
[xrow]
name=xrow GmbH
baseurl=https://s3.amazonaws.com/xrow-files/repo/CentOS/7/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-XROW

[varnish]
name=Varnish for Enterprise Linux
baseurl=http://repo.varnish-cache.org/redhat/varnish-4.0/el6/\$basearch
gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-VARNISH

#[jenkins]
#name=Jenkins-stable
#baseurl=http://pkg.jenkins-ci.org/redhat-stable
#gpgcheck=1
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-JENKINS

[s3tools]
name=Tools for managing Amazon S3 - Simple Storage Service (RHEL_6)
type=rpm-md
baseurl=http://s3tools.org/repo/RHEL_6/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-S3TOOLS
enabled=1

[virtualbox]
name=Oracle Linux / RHEL / CentOS-\$releasever / \$basearch - VirtualBox
baseurl=http://download.virtualbox.org/virtualbox/rpm/el/\$releasever/\$basearch
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ORACLE

EOL

install -dm 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg

cat <<EOL > $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-XROW
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.5 (GNU/Linux)

mQENBE2A44cBCAC+VR8yd5i1wclSta2avRJxOyRYV2GwflFSafJoWB36ZJBSEfcV
S9vvd8GnHHd9xMyVGV1lmSam+n6DXgwr00/nwIDYTuIgriq6Mv3Lfyce8hs3xEaJ
AMXpFiWLQoMV4/SvrT4NdFkY9pVE3FmNdekN0Ikve0bqNmNZhVNuJ33D49w0gClW
JWvmI8/MflUjbT3D67f4yFAxY0BtcPnBtR2Gu3WtXP869FJ2pPLPyv9bJtGT1rqU
IvMU8XqYT0ROas12MXM6HlBdzpOF8vv/OjlZcipU8C8bMIAJ4sVltQiKp1LVAoWk
Jh58W7ESPkW8IfpsDavxwk975OEoSm+n56X/ABEBAAG0MXhyb3cgR21iSCAoaHR0
cDovL3d3dy54cm93LmNvbSkgPHNlcnZpY2VAeHJvdy5kZT6JATYEEwECACAFAk2A
44cCGwMGCwkIBwMCBBUCCAMEFgIDAQIeAQIXgAAKCRDkNaa0NUsiPac5CACc5pKT
Ur4gQowvgZRR6t9ryeUFcXQo0QJtnlZ9C62mJ7V4gx+MUJydRjM3PVX0SrhNMwSq
XruNK5qPHynMt43p40A3IkGAdqD3Cpq4P2L0BVE1wAO/7JW27hGvOwbBjZ9UR34A
ER/CpCYLrGSm2ggM0F0cTEBsLhZH+PowkfuPnb2R31bSa/VBZ2gcRx61ayahDGLK
OzAMFCId2/QIxNJl4uKsX6aOvs/ZR3jslefEzu4Km/wbth6xFuPzgFav/uF8K7Xc
UJh/2fDF4rvzitHkcqkwxX6fFy3wVOnPnhKMX5+zwIWlDCZFtYlvR1inOsAHrjmV
11iQ6L/bJfwsU2v2
=R3aw
-----END PGP PUBLIC KEY BLOCK-----
EOL

cat <<EOL > $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-JENKINS
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.9 (GNU/Linux)

mQGiBEmFQG0RBACXScOxb6BTV6rQE/tcJopAEWsdvmE0jNIRWjDDzB7HovX6Anrq
n7+Vq4spAReSFbBVaYiiOx2cGDymj2dyx2i9NAI/9/cQXJOU+RPdDzHVlO1Edksp
5rKn0cGPWY5sLxRf8s/tO5oyKgwCVgTaB5a8gBHaoGms3nNC4YYf+lqlpwCgjbti
3u1iMIx6Rs+dG0+xw1oi5FUD/2tLJMx7vCUQHhPRupeYFPoD8vWpcbGb5nHfHi4U
8/x4qZspAIwvXtGw0UBHildGpqe9onp22Syadn/7JgMWhHoFw5Ke/rTMlxREL7pa
TiXuagD2G84tjJ66oJP1FigslJzrnG61y85V7THL61OFqDg6IOP4onbsdqHby4VD
zZj9A/9uQxIn5250AGLNpARStAcNPJNJbHOQuv0iF3vnG8uO7/oscB0TYb8/juxr
hs9GdSN0U0BxENR+8KWy5lttpqLMKlKRknQYy34UstQiyFgAQ9Epncu9uIbVDgWt
y7utnqXN033EyYkcWx5EhLAgHkC7wSzeSWABV3JSXN7CeeOif7QiS29oc3VrZSBL
YXdhZ3VjaGkgPGtrQGtvaHN1a2Uub3JnPohjBBMRAgAjAhsDBgsJCAcDAgQVAggD
BBYCAwECHgECF4AFAko/7vYCGQEACgkQm30y8tUFguabhgCgi54IQR4rpJZ/uUHe
ZB879zUWTQwAniQDBO+Zly7Fsvm0Mcvqvl02UzxCtC1Lb2hzdWtlIEthd2FndWNo
aSA8a29oc3VrZS5rYXdhZ3VjaGlAc3VuLmNvbT6IYAQTEQIAIAUCSj/qbQIbAwYL
CQgHAwIEFQIIAwQWAgMBAh4BAheAAAoJEJt9MvLVBYLm38gAoIGR2+TQeJaCeEa8
CQhZYzDoiJkQAJ0cpmD+0VA+leOAr5LEccNVd70Z/dHNy83JARAAAQEAAAAAAAAA
AAAAAAD/2P/gABBKRklGAAEBAQBgAGAAAP/hAGBFeGlmAABJSSoACAAAAAQAMQEC
ABkAAAA+AAAAEFEBAAEAAAABQ5AAEVEEAAEAAAASCwAAElEEAAEAAAASCwAAAAAA
AE1hY3JvbWVkaWEgRmlyZXdvcmtzIDQuMAAA/9sAQwAIBgYHBgUIBwcHCQkICgwU
DQwLCwwZEhMPFB0aHx4dGhwcICQuJyAiLCMcHCg3KSwwMTQ0NB8nOT04MjwuMzQy
/9sAQwEJCQkMCwwYDQ0YMiEcITIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIy
MjIyMjIyMjIyMjIyMjIyMjIyMjIy/8AAEQgArgCWAwEiAAIRAQMRAf/EAB8AAAEF
AQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQEC
AwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkq
NDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqS
k5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk
5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkK
C//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGx
wQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFla
Y2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2
t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQAC
EQMRAD8A9wEj/wB9vzpfMf8Avt+dRinCpGSeY398/nS72/vH86YKBQBJvb+8fzpd
7f3j+dMFLQA/e394/nS7j6n86ZSimA7cfU07cfU1HnFOFADtx9aXJ9TTKUUxD8n1
pc+9Mp1AC5ozSUtAC0maKKADNFJ2ooAoCnCmilzWZQ6lFJSimAopaQUtAC54rOvN
dsLCTZPPGrdwXAry/wCKHxXfRppND0Mq16Bie5PIi9lHdv5V8/X+rXt/O8tzcyyy
MclnYkk0avYdl1PqPxT8VtH8NwqwzdXEuSkaHoB61wjftCXhlzHosBjHZpSCa8PW
O7uhuAkcDueaaYbhOqMMe1L5lcvWx9U+FPjJ4f8AEU0dpdhtLvXOFWdgY3PoH6fg
cV6MrZGa+EklIOJOPqK9i+G3xem0TytI8QSSXGnHCQXJO57f2Pqn6indrclq+x9G
5pwNVoLiO4hSaGRZIpFDKynIYHuKmBqyB+aWmg0uaAFopKKAFoozRQBQFLSUorMo
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
=cjdq
-----END PGP PUBLIC KEY BLOCK-----
EOL

cat <<EOL > $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-GOOGLE
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.2.2 (GNU/Linux)

mQGiBEXwb0YRBADQva2NLpYXxgjNkbuP0LnPoEXruGmvi3XMIxjEUFuGNCP4Rj/a
kv2E5VixBP1vcQFDRJ+p1puh8NU0XERlhpyZrVMzzS/RdWdyXf7E5S8oqNXsoD1z
fvmI+i9b2EhHAA19Kgw7ifV8vMa4tkwslEmcTiwiw8lyUl28Wh4Et8SxzwCggDcA
feGqtn3PP5YAdD0km4S4XeMEAJjlrqPoPv2Gf//tfznY2UyS9PUqFCPLHgFLe80u
QhI2U5jt6jUKN4fHauvR6z3seSAsh1YyzyZCKxJFEKXCCqnrFSoh4WSJsbFNc4PN
b0V0SqiTCkWADZyLT5wll8sWuQ5ylTf3z1ENoHf+G3um3/wk/+xmEHvj9HCTBEXP
78X0A/0Tqlhc2RBnEf+AqxWvM8sk8LzJI/XGjwBvKfXe+l3rnSR2kEAvGzj5Sg0X
4XmfTg4Jl8BNjWyvm2Wmjfet41LPmYJKsux3g0b8yzQxeOA4pQKKAU3Z4+rgzGmf
HdwCG5MNT2A5XxD/eDd+L4fRx0HbFkIQoAi1J3YWQSiTk15fw7RMR29vZ2xlLCBJ
bmMuIExpbnV4IFBhY2thZ2UgU2lnbmluZyBLZXkgPGxpbnV4LXBhY2thZ2VzLWtl
eW1hc3RlckBnb29nbGUuY29tPohjBBMRAgAjAhsDBgsJCAcDAgQVAggDBBYCAwEC
HgECF4AFAkYVdn8CGQEACgkQoECDD3+sWZHKSgCfdq3HtNYJLv+XZleb6HN4zOcF
AJEAniSFbuv8V5FSHxeRimHx25671az+uQINBEXwb0sQCACuA8HT2nr+FM5y/kzI
A51ZcC46KFtIDgjQJ31Q3OrkYP8LbxOpKMRIzvOZrsjOlFmDVqitiVc7qj3lYp6U
rgNVaFv6Qu4bo2/ctjNHDDBdv6nufmusJUWq/9TwieepM/cwnXd+HMxu1XBKRVk9
XyAZ9SvfcW4EtxVgysI+XlptKFa5JCqFM3qJllVohMmr7lMwO8+sxTWTXqxsptJo
pZeKz+UBEEqPyw7CUIVYGC9ENEtIMFvAvPqnhj1GS96REMpry+5s9WKuLEaclWpd
K3krttbDlY1NaeQUCRvBYZ8iAG9YSLHUHMTuI2oea07Rh4dtIAqPwAX8xn36JAYG
2vgLAAMFB/wKqaycjWAZwIe98Yt0qHsdkpmIbarD9fGiA6kfkK/UxjL/k7tmS4Vm
CljrrDZkPSQ/19mpdRcGXtb0NI9+nyM5trweTvtPw+HPkDiJlTaiCcx+izg79Fj9
KcofuNb3lPdXZb9tzf5oDnmm/B+4vkeTuEZJ//IFty8cmvCpzvY+DAz1Vo9rA+Zn
cpWY1n6z6oSS9AsyT/IFlWWBZZ17SpMHu+h4Bxy62+AbPHKGSujEGQhWq8ZRoJAT
G0KSObnmZ7FwFWu1e9XFoUCt0bSjiJWTIyaObMrWu/LvJ3e9I87HseSJStfw6fki
5og9qFEkMrIrBCp3QGuQWBq/rTdMuwNFiEkEGBECAAkFAkXwb0sCGwwACgkQoECD
D3+sWZF/WACfeNAu1/1hwZtUo1bR+MWiCjpvHtwAnA1R3IHqFLQ2X3xJ40XPuAyY
/FJG
=Quqp
-----END PGP PUBLIC KEY BLOCK-----
EOL

cat <<EOL > $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-S3TOOLS
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.5 (GNU/Linux)

mQGiBEeWWZURBACMTragRr0MoLS3Pfy+0ilKxfsmFIHSoXDE4vZTkAjTG0HCpmIA
hrDfw6cl+mKzeG9zlBHEXPpFx/L9A42fsuG2p/9lV5IMCcMCZW71xWSgDINCD68z
28mnHBRRcRn3GzKQuktlzHrYMaQUaA3J+K7Lgcgr31pZsCmf0qD9nTvQxwCgjKqV
GKvQRl7mkJ1uYn/A6u8V89kD/j+BeD+wPHkxwQVCsbtlP6K89bscA4y3VJNsZv7I
8ZrFtO7eY6lpmMnmCk9c+yeW+3aCexch3qy+iwN5s4V/ZeFjT3e0Gt9iuO/z96ZA
Mips+kEyjXzptGLlwgcYQpK0CsNCY1fMPYfnhg8LTVrQINal7RlLBxZSftp5Dzis
BYcMA/wI2WNX5x72sv4SJlunGpFtxcEu0VAhXmn9Gt44aHpsgVVNmHLTN/ETtIxT
rfe7MDU0RRupobj0k8W/TFFpVJmYVAcrdqgzUaRdi9nI5k9cPb9FIJiOH3ticGfz
BsOj77yLMs3Q85Cruc2HSiu5mkEH2JS+3ZvFv1CZNKYpkPYld7Q6aG9tZTptbHVk
dmlnIE9CUyBQcm9qZWN0IDxob21lOm1sdWR2aWdAYnVpbGQub3BlbnN1c2Uub3Jn
PohmBBMRAgAmBQJHllmVAhsDBQkEHrAABgsJCAcDAgQVAggDBBYCAwECHgECF4AA
CgkQn31JTeYSsifhqwCfXLEYFCYAXudF1y6pM8nd/sF3utYAnAvUZwV6dApYjxH7
TcG9A+zruy6/iEYEExECAAYFAkeWWZUACgkQOzARt2udZSNOmACfbZmtq1Ur/3Ho
4IQnKepS2qDTiAEAn2skWiI52FOd3nmgsU9k0UNPG8jC
=sLB6
-----END PGP PUBLIC KEY BLOCK-----
EOL

cat <<EOL > $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-ORACLE
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.9 (GNU/Linux)

mQGiBEvy0LARBACPBH1AUv6krDseyvbL63CWS9fw43iReZ+NmgmDp4/sPsYHLduQ
rxKSqiK7fgFFE+fas/7DCaZXIQW6hnqeD3CgnX0w1+gYiyqEuPY1LQH9okBR5o92
/s2FLm7oUN4RNGv6vWoNSH1ZiRHknL5D0pKSGTKU+pG6cBYWJytAuJZHfwCguS55
aPZuXfhjaWsXG8TF6GH0K8ED/RY3KbirJ7rueK/7KL7ziwqn4CdhQSLOhbZ/R2E0
bknJQDo+vWJciRRRpTe+AG59ctgDF7lEXpjvCms0atyKtE8hObNaMJ5p48l/sgFL
LEujqiq4tByAn2hDOf0s7YrfruIY+HHkBSI9XbwH9nPlsQq8WNsTWTzPrw+ZlQ7v
AEuuA/9cJ/4qYUOq1pg3i/GqH+2dbRHOFH6idXr5YrdB3cYW8jORagOcwdQHeV/0
CaTZVMyMhTVjtIiUt+UR/96CHKxedg0giHwD61GidpUVBUYSaDhjOKE3jwf6/jo5
714e4+ZfL3y1Q2N4HzfK/gEkvPZby/o8WX2N7vUcxfztQ8yq6bRJT3JhY2xlIENv
cnBvcmF0aW9uIChWaXJ0dWFsQm94IGFyY2hpdmUgc2lnbmluZyBrZXkpIDxpbmZv
QHZpcnR1YWxib3gub3JnPohgBBMRAgAgBQJL8tCwAhsDBgsJCAcDAgQVAggDBBYC
AwECHgECF4AACgkQVEIqS5irUTmlvwCeIjsPZ0I9HhLmlS9dLjk397Y5rncAn3kB
XUPRIWb83FMxRwqS85rTCZyouQINBEvy0LAQCAC/pkqDW6H99qQdyW8zvQL5xj6C
UcvlTpL5VkaIRDVwRNbiFoWsVMv2jdhmlJEoh5N+aXYcAzLv0HaiZBSDmTO6fqMM
uPRHyIioQQUFNW4hRI7sdMkYvd2oZcxnzRCLdzG+s42EmzxE4F29eT/FA7o/QBj2
nDbomVqM9jCXKB5/jSJ0W3Uf7I8b7go0AawJT9vVARRMFjz4A7h6QfjeSO9sPHSC
1Dx5Fmd3u4y08W+o6w2kxXRYT9wfMFuGl4MWVJ+f6KPyRhqRCEaa/mz7lXhQdfeG
qW8psDHKmoNnpPEq5Rl4aDIJOppwYJhnDELv+k8JJ6R1JM9hJUWTG8zv9sLzAAMF
CAC6pagGYEK8Dh+3SV6dXjBLNghmj5qnx6GoCXwCDTEFXeWUnszZrqM7PTKLyrfK
ZjOhluydpQSGY7TqDBJJ6emLyNNJV92IQ21eN/h9i0wB97pu8jwvi7RjD0vSkDHh
OpSr9vJm9EeESU1Z+mEKOjz2AONjRLplbBNt9kbXmSWpIP8XMFkU+1KTuNbfi+h4
muOJWKkAGcT7bMUlqbZQjZ2O0RtwDjThxHvw8NhRkxPDYHVxE4uRRobhPquq4NsC
QkMc7LlRilXZCS5mrabHw5+edullNWaQtGuKGlQXGfM4kEhGt7b/XIiyhI5bsh60
o8Mz0KuFpClp9B7c78+QBzTbiEkEGBECAAkFAkvy0LACGwwACgkQVEIqS5irUTnq
qACgtXuTbe2b72sgKdc6gGRKPhLDoEMAmgLwGVN3a4CqewQL+03bqfcKczNH
=19g1
-----END PGP PUBLIC KEY BLOCK-----
EOL

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%post
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-JENKINS
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-XROW
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-ZEND
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-GOOGLE
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-S3TOOLS
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-ORACLE

%clean
rm -rf $RPM_BUILD_ROOT
