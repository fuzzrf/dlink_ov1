D-Link Dir-2150 stack overflow

Built-in web service 'anweb' contains stack overflow in /check_browser request handler.

Basically, it takes two arguments from query string and calls  
```
sprintf(buf,"%s/browser_check/build/%s/%s.html","/srv/anweb",v1,v2), where the size of 'buf' is  512 bytes.
```

```
$ cat /VERSION 
NAME:           DIR_2150_MT7621D
VERSION:        4.0.0
DATAMODEL:      2.40.0
SYSBUILDTIME:   Fri Jun  5 18:21:26 MSK 2020
VENDOR:         D-Link Russia
BUGS:           <support@dlink.ru>
SUMMARY:        Root filesystem image for DIR_2150_MT7621D
```

Debug session:

```
(gdb) target remote 192.168.0.1:4142
Remote debugging using 192.168.0.1:4142
warning: No executable has been specified and target does not support
determining executable automatically.  Try using the "file" command.
0x773c7f84 in ?? ()
(gdb) c
Continuing.

Thread 4 received signal SIGSEGV, Segmentation fault.
[Switching to Thread 6390.6393]
0x31313131 in ?? ()
(gdb) i r
          zero       at       v0       v1       a0       a1       a2       a3
 R0   00000000 76ceb963 00000001 00000000 00000000 00000000 00000000 00000001 
            t0       t1       t2       t3       t4       t5       t6       t7
 R8   00000000 00000001 8553c2a8 0000fb00 00000001 6c69460a 00000000 6c69460a 
            s0       s1       s2       s3       s4       s5       s6       s7
 R16  31313131 31313131 31313131 31313131 31313131 31313131 31313131 31313131 
            t8       t9       k0       k1       gp       sp       s8       ra
 R24  00000003 77414e64 00004000 00000000 775625e0 76cefdc0 00444498 31313131 
        status       lo       hi badvaddr    cause       pc
      0100fc13 dd2fdd8c 0000dec4 31313130 50800008 31313131 
          fcsr      fir      hi1      lo1      hi2      lo2      hi3      lo3
      00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 
        dspctl  restart
      00000000 00000000 
(gdb) 
```

